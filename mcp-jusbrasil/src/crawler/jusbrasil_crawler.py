"""Jusbrasil jurisprudence crawler.

Fetches only real, verifiable decisions. Never generates synthetic content.
Discards any item with missing or ambiguous metadata.
"""

import re
import time
from datetime import date
from typing import Iterator
from urllib.parse import urlencode, urljoin

import requests
from bs4 import BeautifulSoup

from ..models.jurisprudencia import Jurisprudencia, TipoDecisao, Favorabilidade
from ..utils.logger import AuditLogger
from ..utils.validators import (
    validar_tribunal,
    validar_data_julgamento,
    validar_numero_processo,
    validar_ementa,
    validar_link,
    parsear_data,
)

_BASE = "https://www.jusbrasil.com.br"
_SEARCH_URL = f"{_BASE}/jurisprudencia/busca"
_DELAY_BETWEEN_REQUESTS = 2.0  # segundos — respeita rate limit

# Termos objetivos de resultado favorável (configuráveis)
_TERMOS_FAVORAVEIS = frozenset({
    "provimento", "procedente", "procedência", "deferido",
    "acolhido", "acolhida", "favorável", "reconhecimento do direito",
    "condenação da parte ré", "condenada a pagar",
})
_TERMOS_DESFAVORAVEIS = frozenset({
    "improvimento", "improcedente", "improcedência", "indeferido",
    "negado provimento", "não provimento", "desprovido",
})


class CaptchaDetectado(Exception):
    pass


class CrawlerError(Exception):
    pass


def _get_soup(session: requests.Session, url: str, logger: AuditLogger) -> BeautifulSoup:
    logger.registrar_url(url)
    try:
        resp = session.get(url, timeout=30, allow_redirects=True)
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise CrawlerError(f"Falha ao acessar {url}: {exc}") from exc

    if "captcha" in resp.url.lower() or "captcha" in resp.text.lower():
        raise CaptchaDetectado(f"Captcha detectado em {url}")

    return BeautifulSoup(resp.text, "html.parser")


def _classificar_favorabilidade(ementa: str) -> Favorabilidade:
    """Classify strictly by objective terms; ambiguity → NAO_CLASSIFICADA."""
    lower = ementa.lower()
    tem_favoravel = any(t in lower for t in _TERMOS_FAVORAVEIS)
    tem_desfavoravel = any(t in lower for t in _TERMOS_DESFAVORAVEIS)

    if tem_favoravel and not tem_desfavoravel:
        return Favorabilidade.FAVORAVEL
    if tem_desfavoravel and not tem_favoravel:
        return Favorabilidade.DESFAVORAVEL
    if tem_favoravel and tem_desfavoravel:
        return Favorabilidade.NEUTRA
    return Favorabilidade.NAO_CLASSIFICADA


def _extrair_ementa_da_pagina(
    session: requests.Session,
    url: str,
    logger: AuditLogger,
) -> str | None:
    """Navigate to decision page and extract the literal ementa text."""
    try:
        soup = _get_soup(session, url, logger)
        time.sleep(_DELAY_BETWEEN_REQUESTS)
    except (CrawlerError, CaptchaDetectado) as exc:
        logger.warning(f"Não foi possível acessar página da decisão: {exc}")
        return None

    # Priority selector list — most specific first
    selectors = [
        "[data-testid='decision-ementa']",
        ".ementa",
        ".decision-ementa",
        "#ementa",
        ".ementario",
        "[class*='ementa']",
        "[id*='ementa']",
        "section.ementa",
        "div.ementa",
    ]
    for sel in selectors:
        el = soup.select_one(sel)
        if el:
            text = el.get_text(separator=" ", strip=True)
            if len(text) >= 80:
                return text

    # Fallback: look for "EMENTA" heading pattern
    for el in soup.find_all(["p", "div", "span", "section"]):
        text = el.get_text(separator=" ", strip=True)
        if re.match(r"EMENTA\s*[:\-]?", text, re.IGNORECASE) and len(text) >= 80:
            return text

    return None


def _parsear_card(
    card: BeautifulSoup,
    session: requests.Session,
    logger: AuditLogger,
) -> Jurisprudencia | None:
    """Parse a single result card; return None if any required field is missing."""

    # --- Link ---
    a = card.select_one("a[href*='/jurisprudencia/']") or card.select_one("a[href]")
    if not a or not a.get("href"):
        logger.registrar_descarte("card_sem_link", "link ausente")
        return None

    href = a["href"]
    link = href if href.startswith("https://") else urljoin(_BASE, href)

    if not validar_link(link):
        logger.registrar_descarte(link, "link inválido ou não-Jusbrasil")
        return None

    # --- Tribunal ---
    tribunal_el = (
        card.select_one("[data-testid='tribunal']")
        or card.select_one(".tribunal")
        or card.select_one("[class*='tribunal']")
        or card.select_one("[class*='court']")
    )
    tribunal_raw = tribunal_el.get_text(strip=True) if tribunal_el else ""

    # Also try to extract from the title or metadata
    if not tribunal_raw:
        title_el = card.select_one("h2, h3, [class*='title']")
        if title_el:
            m = re.search(r"\b(STF|STJ|TRF\d?|TJ[A-Z]{2})\b", title_el.get_text())
            if m:
                tribunal_raw = m.group(1)

    if not tribunal_raw or not validar_tribunal(tribunal_raw):
        logger.registrar_descarte(link, f"tribunal ausente ou inválido: {tribunal_raw!r}")
        return None

    # Normalise tribunal to sigla
    m = re.search(r"\b(STF|STJ|TRF\d?|TJ[A-Z]{2})\b", tribunal_raw.upper())
    tribunal = m.group(1) if m else tribunal_raw.upper()

    # --- Número do processo ---
    proc_el = (
        card.select_one("[data-testid='numero-processo']")
        or card.select_one(".numero-processo")
        or card.select_one("[class*='process']")
    )
    numero_raw = proc_el.get_text(strip=True) if proc_el else ""

    if not numero_raw:
        # Search all text in card
        full_text = card.get_text(" ")
        m_proc = re.search(
            r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}"
            r"|\d[\d\.\-/]{10,}\d",
            full_text,
        )
        numero_raw = m_proc.group(0) if m_proc else ""

    if not validar_numero_processo(numero_raw):
        logger.registrar_descarte(link, f"número de processo ausente ou inválido: {numero_raw!r}")
        return None

    # --- Data de julgamento ---
    data_el = (
        card.select_one("[data-testid='data-julgamento']")
        or card.select_one(".data-julgamento")
        or card.select_one("[class*='date']")
        or card.select_one("time")
    )
    data_raw = ""
    if data_el:
        data_raw = data_el.get("datetime", "") or data_el.get_text(strip=True)

    if not data_raw:
        m_data = re.search(r"\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}", card.get_text(" "))
        if m_data:
            data_raw = m_data.group(0)

    data_julgamento = parsear_data(data_raw) if data_raw else None
    if not data_julgamento:
        logger.registrar_descarte(numero_raw, "data de julgamento ausente ou inválida")
        return None

    ok, motivo = validar_data_julgamento(data_julgamento)
    if not ok:
        logger.registrar_descarte(numero_raw, f"data fora da janela temporal: {motivo}")
        return None

    # --- Ementa ---
    ementa_el = (
        card.select_one("[data-testid='ementa']")
        or card.select_one(".ementa")
        or card.select_one("[class*='ementa']")
        or card.select_one("[class*='summary']")
    )
    ementa_raw = ementa_el.get_text(separator=" ", strip=True) if ementa_el else ""

    # If ementa is truncated in the card, fetch the full page
    if len(ementa_raw) < 200:
        ementa_completa = _extrair_ementa_da_pagina(session, link, logger)
        if ementa_completa:
            ementa_raw = ementa_completa

    ok, motivo = validar_ementa(ementa_raw)
    if not ok:
        logger.registrar_descarte(numero_raw, f"ementa inválida: {motivo}")
        return None

    # --- Tipo da decisão ---
    tipo = TipoDecisao.ACORDAO
    texto_tipo = card.get_text(" ").lower()
    if "monocrática" in texto_tipo or "monocratica" in texto_tipo:
        tipo = TipoDecisao.DECISAO_MONOCRATICA
    elif "despacho" in texto_tipo:
        tipo = TipoDecisao.DESPACHO

    # --- Relator (opcional) ---
    relator_el = card.select_one("[class*='relator']") or card.select_one("[class*='judge']")
    relator = relator_el.get_text(strip=True) if relator_el else None

    favorabilidade = _classificar_favorabilidade(ementa_raw)

    return Jurisprudencia(
        numero_processo=numero_raw.strip(),
        tribunal=tribunal,
        data_julgamento=data_julgamento,
        link=link,
        ementa=ementa_raw.strip(),
        favorabilidade=favorabilidade,
        relator=relator,
        tipo=tipo,
        fonte_url_verificada=True,
    )


def _deduplicate(items: list[Jurisprudencia]) -> list[Jurisprudencia]:
    """Remove duplicates by processo number; prefer acórdãos."""
    seen: dict[str, Jurisprudencia] = {}
    for item in items:
        key = re.sub(r"\D", "", item.numero_processo)
        if key not in seen:
            seen[key] = item
        else:
            # Replace if current item is acórdão and existing isn't
            if (
                item.tipo == TipoDecisao.ACORDAO
                and seen[key].tipo != TipoDecisao.ACORDAO
            ):
                seen[key] = item
    return list(seen.values())


def coletar(
    session: requests.Session,
    tema: str,
    limite: int,
    logger: AuditLogger,
) -> tuple[list[Jurisprudencia], int]:
    """Collect jurisprudence from Jusbrasil for the given tema.

    Returns (valid_items, total_found_count).
    Raises CrawlerError on unrecoverable errors.
    """
    logger.info(f"Iniciando coleta — tema: {tema!r}, limite: {limite}")

    params = {
        "q": tema,
        "categoria": "jurisprudencia",
    }
    search_url = f"{_SEARCH_URL}?{urlencode(params)}"

    resultados_brutos: list[Jurisprudencia] = []
    pagina = 1
    total_encontrado = 0

    while len(resultados_brutos) < limite * 3:  # extra margin for filtering
        url = f"{search_url}&pagina={pagina}" if pagina > 1 else search_url
        logger.info(f"Buscando página {pagina}: {url}")

        try:
            soup = _get_soup(session, url, logger)
        except CaptchaDetectado as exc:
            raise CrawlerError(str(exc)) from exc
        except CrawlerError:
            if pagina == 1:
                raise
            break  # partial results are acceptable after page 1

        time.sleep(_DELAY_BETWEEN_REQUESTS)

        # Detect result cards using multiple strategies
        cards = (
            soup.select("[data-testid='jurisprudencia-card']")
            or soup.select(".jurisprudencia-card")
            or soup.select("[class*='JurisprudenciaCard']")
            or soup.select("article[class*='result']")
            or soup.select(".result-item")
            or soup.select("li[class*='result']")
        )

        if not cards:
            logger.warning(f"Nenhum card encontrado na página {pagina}")
            break

        total_encontrado += len(cards)
        logger.info(f"Cards encontrados na página {pagina}: {len(cards)}")

        for card in cards:
            if len(resultados_brutos) >= limite * 2:
                break
            jurisprudencia = _parsear_card(card, session, logger)
            if jurisprudencia:
                resultados_brutos.append(jurisprudencia)

        # Check if there's a next page
        next_btn = (
            soup.select_one("a[rel='next']")
            or soup.select_one("[aria-label='Próxima página']")
            or soup.select_one("[class*='next-page']")
        )
        if not next_btn:
            break

        pagina += 1

    # Deduplicate and sort: acórdãos first, then by date descending
    unicos = _deduplicate(resultados_brutos)
    unicos.sort(
        key=lambda j: (
            j.tipo != TipoDecisao.ACORDAO,  # False < True → acórdãos first
            -(j.data_julgamento.toordinal()),
        )
    )

    validos = unicos[:limite]
    logger.info(f"Após deduplicação e ordenação: {len(validos)} itens válidos")
    return validos, total_encontrado

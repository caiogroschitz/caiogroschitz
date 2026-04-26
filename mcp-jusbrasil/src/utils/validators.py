"""Strict validators — discard on any ambiguity."""

import re
from datetime import date, datetime, timedelta

TRIBUNAIS_ACEITOS = frozenset({
    "STF", "STJ",
    "TRF1", "TRF2", "TRF3", "TRF4", "TRF5", "TRF6",
    "TJAC", "TJAL", "TJAM", "TJAP", "TJBA", "TJCE", "TJDF",
    "TJES", "TJGO", "TJMA", "TJMG", "TJMS", "TJMT", "TJPA",
    "TJPB", "TJPE", "TJPI", "TJPR", "TJRJ", "TJRN", "TJRO",
    "TJRR", "TJRS", "TJSC", "TJSE", "TJSP", "TJTO",
})

_JANELA_ANOS = 3
_EMENTA_MIN_CHARS = 80
_PROCESS_PATTERN = re.compile(
    r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}"  # CNJ: 0000000-00.0000.0.00.0000
    r"|\d{7}-\d{2}\.\d{4}\.[0-9A-Z]\.\d{2}\.\d{4}"
    r"|\d[\d\.\-/]+\d",  # formatos legados
)


def validar_tribunal(tribunal: str) -> bool:
    sigla = tribunal.strip().upper()
    return any(sigla.startswith(t) for t in TRIBUNAIS_ACEITOS)


def validar_data_julgamento(data: date) -> tuple[bool, str]:
    hoje = date.today()
    limite = hoje - timedelta(days=_JANELA_ANOS * 365)
    if data > hoje:
        return False, f"data futura: {data}"
    if data < limite:
        return False, f"fora da janela de {_JANELA_ANOS} anos: {data}"
    return True, ""


def validar_numero_processo(numero: str) -> bool:
    return bool(numero and _PROCESS_PATTERN.search(numero.strip()))


def validar_ementa(ementa: str) -> tuple[bool, str]:
    if not ementa or not ementa.strip():
        return False, "ementa ausente"
    texto = ementa.strip()
    if len(texto) < _EMENTA_MIN_CHARS:
        return False, f"ementa muito curta ({len(texto)} chars)"
    suspeitos = [
        "lorem ipsum", "exemplo de ementa", "[ementa não disponível]",
        "sem ementa", "ementa não localizada", "não há ementa",
    ]
    lower = texto.lower()
    for s in suspeitos:
        if s in lower:
            return False, f"ementa com marcador suspeito: {s!r}"
    return True, ""


def validar_link(link: str) -> bool:
    return bool(
        link
        and link.startswith("https://")
        and "jusbrasil" in link
    )


def parsear_data(raw: str) -> date | None:
    raw = raw.strip()
    formatos = [
        "%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y",
        "%d/%m/%y", "%d.%m.%Y",
    ]
    for fmt in formatos:
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    # Tenta extrair data por regex
    m = re.search(r"(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{2,4})", raw)
    if m:
        d, mo, a = m.groups()
        if len(a) == 2:
            a = "20" + a
        try:
            return datetime(int(a), int(mo), int(d)).date()
        except ValueError:
            return None
    return None

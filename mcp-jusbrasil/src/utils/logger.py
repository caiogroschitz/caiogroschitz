"""Audit logger — never records credentials or sensitive cookies."""

import logging
import os
from datetime import datetime
from pathlib import Path

_SENSITIVE_KEYS = frozenset({
    "password", "senha", "secret", "token", "cookie",
    "session", "authorization", "auth", "credential",
    "jusbrasil_password", "jusbrasil_email",
})


def _sanitize(msg: str) -> str:
    """Strip any value that looks like a credential assignment."""
    import re
    return re.sub(
        r"(password|senha|token|session[_-]?id|authorization)\s*[=:]\s*\S+",
        r"\1=[REDACTED]",
        msg,
        flags=re.IGNORECASE,
    )


class AuditLogger:
    def __init__(self, nome_tema: str, log_dir: str = "logs"):
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        slug = nome_tema[:50].replace(" ", "_").replace("/", "-")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = Path(log_dir) / f"auditoria_{slug}_{ts}.log"

        self._logger = logging.getLogger(f"mcp_jusbrasil.{ts}")
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = False

        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        fh.setFormatter(fmt)
        self._logger.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(fmt)
        self._logger.addHandler(sh)

        self.log_path = str(log_path)
        self._urls_acessadas: list[str] = []
        self._itens_descartados: list[dict] = []

        self.info(f"Sessão iniciada — tema: {nome_tema!r}")

    def info(self, msg: str) -> None:
        self._logger.info(_sanitize(msg))

    def warning(self, msg: str) -> None:
        self._logger.warning(_sanitize(msg))

    def error(self, msg: str) -> None:
        self._logger.error(_sanitize(msg))

    def debug(self, msg: str) -> None:
        self._logger.debug(_sanitize(msg))

    def registrar_url(self, url: str) -> None:
        self._urls_acessadas.append(url)
        self.debug(f"URL acessada: {url}")

    def registrar_descarte(self, identificador: str, motivo: str) -> None:
        self._itens_descartados.append({"id": identificador, "motivo": motivo})
        self.info(f"DESCARTADO [{identificador}] — {motivo}")

    def resumo_final(
        self,
        total_encontrado: int,
        total_valido: int,
        caminho_arquivo: str | None = None,
    ) -> None:
        self.info("=== RESUMO FINAL ===")
        self.info(f"URLs acessadas: {len(self._urls_acessadas)}")
        self.info(f"Itens encontrados: {total_encontrado}")
        self.info(f"Itens válidos: {total_valido}")
        self.info(f"Itens descartados: {len(self._itens_descartados)}")
        if caminho_arquivo:
            self.info(f"Arquivo gerado: {caminho_arquivo}")

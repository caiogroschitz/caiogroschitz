"""Isolated authentication module for Jusbrasil.

Credentials are read exclusively from environment variables.
They are never logged, printed or stored in plain text beyond the session object.
"""

import os
import re
import time
import pickle
from pathlib import Path
from typing import Optional

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

_SESSION_CACHE = Path(".jusbrasil_session.pkl")
_LOGIN_URL = "https://www.jusbrasil.com.br/autenticacao/login"
_HOME_URL = "https://www.jusbrasil.com.br"
_SESSION_TTL = 3600  # segundos

_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


class AuthenticationError(Exception):
    """Raised when authentication fails; execution must stop."""


def _build_session() -> Session:
    session = requests.Session()
    session.headers.update(_HEADERS)
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def _load_cached_session() -> Optional[tuple[Session, float]]:
    if not _SESSION_CACHE.exists():
        return None
    try:
        with _SESSION_CACHE.open("rb") as f:
            data = pickle.load(f)
        session: Session = data["session"]
        created_at: float = data["created_at"]
        if time.time() - created_at > _SESSION_TTL:
            _SESSION_CACHE.unlink(missing_ok=True)
            return None
        return session, created_at
    except Exception:
        _SESSION_CACHE.unlink(missing_ok=True)
        return None


def _persist_session(session: Session) -> None:
    try:
        with _SESSION_CACHE.open("wb") as f:
            pickle.dump({"session": session, "created_at": time.time()}, f)
        # Restrict read access to owner only
        _SESSION_CACHE.chmod(0o600)
    except Exception:
        pass  # Cache falhou; continua sem persistência


def _extract_csrf(session: Session) -> Optional[str]:
    """Retrieve CSRF token from the login page."""
    from bs4 import BeautifulSoup

    resp = session.get(_LOGIN_URL, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    for attr in ["csrf-token", "csrf_token", "_csrf_token"]:
        tag = soup.find("meta", attrs={"name": attr})
        if tag and tag.get("content"):
            return tag["content"]

    inp = soup.find("input", attrs={"name": re.compile(r"csrf|token", re.I)})
    if inp and inp.get("value"):
        return inp["value"]

    return None


def _verify_authenticated(session: Session) -> bool:
    """Return True only if the session is genuinely authenticated."""
    try:
        resp = session.get(
            "https://www.jusbrasil.com.br/perfil/",
            timeout=15,
            allow_redirects=True,
        )
        # If redirected to login, session is not authenticated
        if "autenticacao" in resp.url or "login" in resp.url:
            return False
        return resp.status_code == 200
    except Exception:
        return False


def autenticar() -> Session:
    """Return an authenticated requests.Session.

    Reads credentials from JUSBRASIL_EMAIL and JUSBRASIL_PASSWORD environment
    variables only. Raises AuthenticationError on any failure — callers must
    not proceed without a valid session.
    """
    email = os.environ.get("JUSBRASIL_EMAIL", "").strip()
    password = os.environ.get("JUSBRASIL_PASSWORD", "").strip()

    if not email:
        raise AuthenticationError(
            "JUSBRASIL_EMAIL não definida. "
            "Defina a variável de ambiente antes de executar."
        )
    if not password:
        raise AuthenticationError(
            "JUSBRASIL_PASSWORD não definida. "
            "Defina a variável de ambiente antes de executar."
        )

    # Try to reuse cached session
    cached = _load_cached_session()
    if cached:
        session, _ = cached
        if _verify_authenticated(session):
            return session

    session = _build_session()

    try:
        csrf = _extract_csrf(session)
    except requests.RequestException as exc:
        raise AuthenticationError(f"Falha ao acessar página de login: {exc}") from exc

    payload: dict = {"email": email, "password": password}
    if csrf:
        payload["_token"] = csrf
        payload["authenticity_token"] = csrf

    try:
        resp = session.post(
            _LOGIN_URL,
            data=payload,
            timeout=30,
            allow_redirects=True,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": _LOGIN_URL,
                "Origin": _HOME_URL,
            },
        )
    except requests.RequestException as exc:
        raise AuthenticationError(f"Erro de rede durante login: {exc}") from exc
    finally:
        # Immediately wipe credentials from local scope
        del email, password
        if "password" in payload:
            del payload["password"]

    if resp.status_code not in (200, 302):
        raise AuthenticationError(
            f"Login retornou status inesperado: {resp.status_code}"
        )

    if not _verify_authenticated(session):
        raise AuthenticationError(
            "Autenticação falhou: sessão não válida após POST. "
            "Verifique e-mail/senha nas variáveis de ambiente."
        )

    _persist_session(session)
    return session

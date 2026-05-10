"""Memory Manager — gerencia memória contextual persistente do sistema editorial."""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


MEMORY_DIR = Path("memory")
MEMORY_FILES = {
    "main": MEMORY_DIR / "memory.json",
    "headlines": MEMORY_DIR / "headlines_used.json",
    "topics": MEMORY_DIR / "topics_covered.json",
    "hooks": MEMORY_DIR / "hooks_used.json",
    "ctas": MEMORY_DIR / "ctas_approved.json",
    "styles": MEMORY_DIR / "styles_approved.json",
}


class MemoryManager:
    """Gerencia a memória contextual persistente do sistema editorial."""

    def __init__(self, dedup_window_days: int = 30):
        self.dedup_window = dedup_window_days
        self._ensure_files()

    def _ensure_files(self):
        MEMORY_DIR.mkdir(exist_ok=True)
        defaults = {
            "main": {
                "sistema": "Sistema Editorial Jurídico",
                "criado_em": datetime.now().isoformat(),
                "ultima_atualizacao": datetime.now().isoformat(),
                "ciclos_executados": 0,
                "temas_recentes": [],
                "formatos_performance": {},
                "estilos_aprovados": [],
                "padroes_linguagem": [],
            },
            "headlines": {"headlines": [], "total": 0},
            "topics": {"topics": [], "total": 0},
            "hooks": {"hooks": [], "total": 0},
            "ctas": {"ctas": [], "total": 0},
            "styles": {
                "aberturas_aprovadas": [],
                "estruturas_funcionais": [],
                "cadencias_aprovadas": [],
            },
        }
        for key, path in MEMORY_FILES.items():
            if not path.exists():
                path.write_text(
                    json.dumps(defaults[key], ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )

    def _load(self, key: str) -> dict:
        path = MEMORY_FILES[key]
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save(self, key: str, data: dict):
        MEMORY_FILES[key].write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _is_recent(self, timestamp_str: str) -> bool:
        try:
            dt = datetime.fromisoformat(timestamp_str)
            return datetime.now() - dt < timedelta(days=self.dedup_window)
        except (ValueError, TypeError):
            return False

    def get_context(self) -> dict:
        """Retorna contexto completo da memória para injeção nos agentes."""
        main = self._load("main")
        headlines = self._load("headlines")
        topics = self._load("topics")
        hooks = self._load("hooks")

        cutoff = datetime.now() - timedelta(days=self.dedup_window)

        recent_headlines = [
            h["headline"] for h in headlines.get("headlines", [])
            if self._is_recent(h.get("data", ""))
        ]
        recent_topics = [
            t["tema"] for t in topics.get("topics", [])
            if self._is_recent(t.get("data", ""))
        ]
        recent_hooks = [
            h["hook"] for h in hooks.get("hooks", [])
            if self._is_recent(h.get("data", ""))
        ]

        return {
            "temas_recentes": recent_topics,
            "headlines_recentes": recent_headlines,
            "hooks_recentes": recent_hooks,
            "formatos_performance": main.get("formatos_performance", {}),
            "estilos_aprovados": main.get("estilos_aprovados", []),
            "padroes_linguagem": main.get("padroes_linguagem", []),
            "ciclos_executados": main.get("ciclos_executados", 0),
        }

    def register_headline(self, headline: str, tema: str, performance: str = ""):
        """Registra headline utilizada."""
        data = self._load("headlines")
        headlines = data.get("headlines", [])
        headlines.append({
            "headline": headline,
            "tema": tema,
            "data": datetime.now().isoformat(),
            "performance": performance,
        })
        if len(headlines) > 500:
            headlines = headlines[-500:]
        data["headlines"] = headlines
        data["total"] = len(headlines)
        self._save("headlines", data)

    def register_topic(self, tema: str, formato: str, score: int = 0):
        """Registra tema coberto."""
        data = self._load("topics")
        topics = data.get("topics", [])
        topics.append({
            "tema": tema,
            "formato": formato,
            "score": score,
            "data": datetime.now().isoformat(),
        })
        if len(topics) > 300:
            topics = topics[-300:]
        data["topics"] = topics
        data["total"] = len(topics)
        self._save("topics", data)

    def register_hook(self, hook: str, tema: str, formato: str):
        """Registra hook utilizado."""
        data = self._load("hooks")
        hooks = data.get("hooks", [])
        hooks.append({
            "hook": hook,
            "tema": tema,
            "formato": formato,
            "data": datetime.now().isoformat(),
        })
        if len(hooks) > 200:
            hooks = hooks[-200:]
        data["hooks"] = hooks
        data["total"] = len(hooks)
        self._save("hooks", data)

    def register_approved_cta(self, cta: str, formato: str):
        """Registra CTA aprovado."""
        data = self._load("ctas")
        ctas = data.get("ctas", [])
        if not any(c["cta"] == cta for c in ctas):
            ctas.append({
                "cta": cta,
                "formato": formato,
                "data": datetime.now().isoformat(),
                "aprovado": True,
            })
        data["ctas"] = ctas
        data["total"] = len(ctas)
        self._save("ctas", data)

    def update_format_performance(self, formato: str, engajamento: str):
        """Atualiza performance de formato para priorização futura."""
        main = self._load("main")
        perf = main.get("formatos_performance", {})
        if formato not in perf:
            perf[formato] = {"usos": 0, "alto_engajamento": 0, "medio": 0, "baixo": 0}
        perf[formato]["usos"] += 1
        perf[formato][engajamento] = perf[formato].get(engajamento, 0) + 1
        main["formatos_performance"] = perf
        main["ultima_atualizacao"] = datetime.now().isoformat()
        self._save("main", main)

    def increment_cycle(self):
        """Incrementa o contador de ciclos executados."""
        main = self._load("main")
        main["ciclos_executados"] = main.get("ciclos_executados", 0) + 1
        main["ultima_atualizacao"] = datetime.now().isoformat()
        self._save("main", main)

    def is_topic_recent(self, tema: str) -> bool:
        """Verifica se um tema foi coberto recentemente."""
        data = self._load("topics")
        for topic in data.get("topics", []):
            if tema.lower() in topic.get("tema", "").lower():
                if self._is_recent(topic.get("data", "")):
                    return True
        return False

    def is_headline_used(self, headline: str) -> bool:
        """Verifica se uma headline foi usada recentemente (similaridade básica)."""
        data = self._load("headlines")
        headline_words = set(headline.lower().split())
        for h in data.get("headlines", []):
            if not self._is_recent(h.get("data", "")):
                continue
            stored_words = set(h.get("headline", "").lower().split())
            if len(headline_words & stored_words) / max(len(headline_words), 1) > 0.7:
                return True
        return False

    def get_approved_ctas(self, formato: str = "") -> list:
        """Retorna CTAs aprovados historicamente."""
        data = self._load("ctas")
        ctas = data.get("ctas", [])
        if formato:
            return [c["cta"] for c in ctas if c.get("formato") == formato]
        return [c["cta"] for c in ctas]

    def save_cycle_output(self, cycle_data: dict):
        """Salva dados do ciclo atual na memória principal."""
        main = self._load("main")
        main["ultimo_ciclo"] = {
            "data": datetime.now().isoformat(),
            "pautas_geradas": cycle_data.get("total_pautas", 0),
            "conteudos_gerados": cycle_data.get("total_conteudos", 0),
            "top_tema": cycle_data.get("top_tema", ""),
        }
        self._save("main", main)
        self.increment_cycle()

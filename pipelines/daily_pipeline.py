"""Daily Pipeline — orquestra o ciclo editorial completo de forma paralela."""

import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import (
    TrendHunterAgent,
    JurisprudenciaAgent,
    SocialPainAgent,
    ContentStrategistAgent,
    LegalRiskAgent,
    CarouselWriterAgent,
    ReelsScriptAgent,
    SeoBlogAgent,
    AuthorityLinkedInAgent,
    EditorialChiefAgent,
)
from memory import MemoryManager
from ranking import ScoringEngine


class DailyPipeline:
    """
    Orquestrador do pipeline editorial diário.

    FLUXO:
    FASE 1 (Paralela): TrendHunter + Jurisprudência + SocialPain
    FASE 2 (Sequencial): ContentStrategist (usa saída da fase 1)
    FASE 3 (Paralela): LegalRisk + Scoring (usa estratégia da fase 2)
    FASE 4 (Paralela): Carousel + Reels + SEO + LinkedIn (conteúdo aprovado)
    FASE 5 (Sequencial): EditorialChief (consolida tudo)
    """

    def __init__(self, config: dict):
        self.config = config
        self.memory = MemoryManager(
            dedup_window_days=config.get("memoria", {}).get("janela_deduplicacao_dias", 30)
        )
        self.scoring = ScoringEngine(config)
        self.results = {}
        self.start_time = datetime.now()

    def run(self) -> dict:
        """Executa o pipeline completo."""
        print(f"\n{'='*60}")
        print(f"PIPELINE EDITORIAL JURÍDICO — {self.start_time.strftime('%d/%m/%Y %H:%M')}")
        print(f"{'='*60}\n")

        memoria_contexto = self.memory.get_context()

        print("▶ FASE 1: Pesquisa paralela (Tendências + Jurisprudência + Dores)")
        fase1 = self._run_fase1(memoria_contexto)
        self.results.update(fase1)

        trends_data = fase1.get("trends", {}).get("data", {})
        tendencias = trends_data.get("tendencias", []) if isinstance(trends_data, dict) else []

        print("\n▶ FASE 2: Estratégia editorial")
        fase2_context = {
            "tendencias": tendencias,
            "dores": fase1.get("social_pain", {}).get("data", {}).get("json_index", {}),
            "jurisprudencia_resumo": fase1.get("jurisprudencia", {}).get("data", {}).get("conteudo_md", "")[:2000],
            "memoria": memoria_contexto,
        }
        fase2 = self._run_fase2(fase2_context)
        self.results.update(fase2)

        print("\n▶ FASE 3: Scoring e auditoria jurídica")
        pautas = fase2.get("strategy", {}).get("data", {}).get("pautas", []) if isinstance(
            fase2.get("strategy", {}).get("data"), dict) else []
        pautas_ranked = self.scoring.rank_pautas(pautas)
        self.scoring.save_report(pautas_ranked)

        fase3 = self._run_fase3(pautas_ranked)
        self.results.update(fase3)

        pautas_aprovadas = self._filter_approved(pautas_ranked, fase3.get("audit", {}))

        print("\n▶ FASE 4: Produção de conteúdo (paralela)")
        fase4_context = {
            "pautas_aprovadas": pautas_aprovadas,
            "dores": fase1.get("social_pain", {}).get("data", {}).get("json_index", {}),
            "data": {
                "jurisprudencia": fase1.get("jurisprudencia", {}),
            },
        }
        fase4 = self._run_fase4(fase4_context)
        self.results.update(fase4)

        print("\n▶ FASE 5: Editorial Chief — consolidação")
        fase5_context = {
            "data": {
                "trends": trends_data,
                "strategy": fase2.get("strategy", {}).get("data", {}),
                "audit": fase3.get("audit", {}).get("data", {}).get("relatorio_json", {}),
                "carousels": fase4.get("carousels", {}).get("data", {}),
                "reels": fase4.get("reels", {}).get("data", {}),
                "seo": fase4.get("seo", {}).get("data", {}),
                "linkedin": fase4.get("linkedin", {}).get("data", {}),
            }
        }
        fase5 = self._run_fase5(fase5_context)
        self.results.update(fase5)

        self._update_memory(pautas_aprovadas)

        duration = (datetime.now() - self.start_time).seconds
        print(f"\n{'='*60}")
        print(f"✅ PIPELINE CONCLUÍDO em {duration}s")
        print(f"{'='*60}\n")

        return self._build_final_report()

    def _run_fase1(self, memoria_contexto: dict) -> dict:
        """Fase 1: Pesquisa em paralelo."""
        agents = {
            "trends": TrendHunterAgent(self.config, self.memory),
            "jurisprudencia": JurisprudenciaAgent(self.config, self.memory),
            "social_pain": SocialPainAgent(self.config, self.memory),
        }
        results = {}
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = {
                executor.submit(agent.run, {"memoria": memoria_contexto}): name
                for name, agent in agents.items()
            }
            for future in as_completed(futures):
                name = futures[future]
                try:
                    result = future.result(timeout=120)
                    results[name] = result
                    print(f"  ✓ {name}: {result.get('summary', 'concluído')}")
                except Exception as e:
                    print(f"  ✗ {name}: ERRO — {e}")
                    results[name] = {"status": "error", "error": str(e), "data": {}}
        return results

    def _run_fase2(self, context: dict) -> dict:
        """Fase 2: Estratégia editorial (sequencial, depende da fase 1)."""
        agent = ContentStrategistAgent(self.config, self.memory)
        try:
            result = agent.run(context)
            print(f"  ✓ strategy: {result.get('summary', 'concluído')}")
            return {"strategy": result}
        except Exception as e:
            print(f"  ✗ strategy: ERRO — {e}")
            return {"strategy": {"status": "error", "error": str(e), "data": {}}}

    def _run_fase3(self, pautas_ranked: list) -> dict:
        """Fase 3: Auditoria ética."""
        agent = LegalRiskAgent(self.config, self.memory)
        try:
            result = agent.run({"pautas": pautas_ranked[:10]})
            print(f"  ✓ audit: {result.get('summary', 'concluído')}")
            return {"audit": result}
        except Exception as e:
            print(f"  ✗ audit: ERRO — {e}")
            return {"audit": {"status": "error", "data": {}}}

    def _run_fase4(self, context: dict) -> dict:
        """Fase 4: Produção de conteúdo em paralelo."""
        agents = {
            "carousels": CarouselWriterAgent(self.config, self.memory),
            "reels": ReelsScriptAgent(self.config, self.memory),
            "seo": SeoBlogAgent(self.config, self.memory),
            "linkedin": AuthorityLinkedInAgent(self.config, self.memory),
        }
        results = {}
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = {
                executor.submit(agent.run, context): name
                for name, agent in agents.items()
            }
            for future in as_completed(futures):
                name = futures[future]
                try:
                    result = future.result(timeout=180)
                    results[name] = result
                    print(f"  ✓ {name}: {result.get('summary', 'concluído')}")
                except Exception as e:
                    print(f"  ✗ {name}: ERRO — {e}")
                    results[name] = {"status": "error", "error": str(e), "data": {}}
        return results

    def _run_fase5(self, context: dict) -> dict:
        """Fase 5: Editorial Chief consolida."""
        agent = EditorialChiefAgent(self.config, self.memory)
        try:
            result = agent.run(context)
            print(f"  ✓ editorial-chief: {result.get('summary', 'concluído')}")
            return {"editorial_chief": result}
        except Exception as e:
            print(f"  ✗ editorial-chief: ERRO — {e}")
            return {"editorial_chief": {"status": "error", "data": {}}}

    def _filter_approved(self, pautas: list, audit_result: dict) -> list:
        """Filtra apenas pautas aprovadas pela auditoria ética."""
        if not audit_result or audit_result.get("status") == "error":
            return pautas[:5]

        audit_data = audit_result.get("data", {}).get("relatorio_json", {})
        itens_auditoria = audit_data.get("itens_auditoria", [])

        bloqueados = {
            item.get("item", "").lower()
            for item in itens_auditoria
            if not item.get("liberado_publicacao", True)
        }

        aprovadas = [
            p for p in pautas
            if p.get("tema", "").lower() not in bloqueados and p.get("publicar", True)
        ]

        return aprovadas[:8] if aprovadas else pautas[:5]

    def _update_memory(self, pautas_aprovadas: list):
        """Atualiza a memória com os dados do ciclo atual."""
        for pauta in pautas_aprovadas:
            tema = pauta.get("tema", "")
            formato = pauta.get("formato_ideal", "carrossel")
            score = pauta.get("score_final", 0)
            headline = pauta.get("headline_sugerida", "")
            hook = pauta.get("hook_sugerido", "")

            if tema:
                self.memory.register_topic(tema, formato, score)
            if headline:
                self.memory.register_headline(headline, tema)
            if hook:
                self.memory.register_hook(hook, tema, formato)

        self.memory.save_cycle_output({
            "total_pautas": len(pautas_aprovadas),
            "total_conteudos": 4,
            "top_tema": pautas_aprovadas[0].get("tema", "") if pautas_aprovadas else "",
        })

    def _build_final_report(self) -> dict:
        """Constrói relatório final do pipeline."""
        duration = (datetime.now() - self.start_time).seconds
        return {
            "status": "success",
            "data": datetime.now().strftime("%d/%m/%Y"),
            "hora": self.start_time.strftime("%H:%M"),
            "duracao_segundos": duration,
            "fases_executadas": 5,
            "resultados": {k: v.get("status", "unknown") for k, v in self.results.items()},
            "output_dir": str(Path("output/daily") / datetime.now().strftime("%Y-%m-%d")),
        }

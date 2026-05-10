#!/usr/bin/env python3
"""
Pipeline Runner — ponto de entrada principal do Sistema Editorial Jurídico.

Uso:
    python pipeline_runner.py                    # Pipeline completo
    python pipeline_runner.py --mode=full        # Pipeline completo
    python pipeline_runner.py --mode=research    # Apenas pesquisa
    python pipeline_runner.py --mode=content     # Apenas conteúdo
    python pipeline_runner.py --agent=trend-hunter  # Agente específico
    python pipeline_runner.py --report           # Relatório do último ciclo
    python pipeline_runner.py --score "tema"     # Score de um tema específico
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def load_config() -> dict:
    config_path = Path("config.json")
    if not config_path.exists():
        print("ERRO: config.json não encontrado. Execute do diretório raiz do projeto.")
        sys.exit(1)
    return json.loads(config_path.read_text(encoding="utf-8"))


def check_env():
    """Verifica variáveis de ambiente obrigatórias."""
    missing = []
    if not os.environ.get("ANTHROPIC_API_KEY"):
        missing.append("ANTHROPIC_API_KEY")
    if missing:
        print(f"ERRO: Variáveis de ambiente ausentes: {', '.join(missing)}")
        print("Configure no .env ou exporte antes de executar.")
        sys.exit(1)


def load_dotenv():
    """Carrega variáveis do .env se existir."""
    env_path = Path(".env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())


def run_full_pipeline(config: dict):
    """Executa o pipeline editorial completo."""
    from pipelines import DailyPipeline
    pipeline = DailyPipeline(config)
    result = pipeline.run()
    print(f"\nOutput salvo em: {result.get('output_dir')}")
    return result


def run_single_agent(agent_name: str, config: dict):
    """Executa um agente específico."""
    agent_map = {
        "trend-hunter": ("agents", "TrendHunterAgent"),
        "jurisprudencia": ("agents", "JurisprudenciaAgent"),
        "social-pain": ("agents", "SocialPainAgent"),
        "content-strategist": ("agents", "ContentStrategistAgent"),
        "legal-risk": ("agents", "LegalRiskAgent"),
        "carousel-writer": ("agents", "CarouselWriterAgent"),
        "reels-script": ("agents", "ReelsScriptAgent"),
        "seo-blog": ("agents", "SeoBlogAgent"),
        "linkedin": ("agents", "AuthorityLinkedInAgent"),
        "editorial-chief": ("agents", "EditorialChiefAgent"),
    }

    if agent_name not in agent_map:
        print(f"Agente '{agent_name}' não encontrado.")
        print(f"Agentes disponíveis: {', '.join(agent_map.keys())}")
        sys.exit(1)

    module_name, class_name = agent_map[agent_name]
    module = __import__(module_name, fromlist=[class_name])
    AgentClass = getattr(module, class_name)

    print(f"Executando: {agent_name}")
    agent = AgentClass(config)
    result = agent.run({})
    print(f"Status: {result.get('status')}")
    print(f"Resumo: {result.get('summary')}")
    print(f"Output: {result.get('output_path')}")
    return result


def show_last_report():
    """Exibe o relatório do último ciclo."""
    output_dir = Path("output/daily")
    if not output_dir.exists():
        print("Nenhum ciclo executado ainda.")
        return

    dates = sorted([d for d in output_dir.iterdir() if d.is_dir()], reverse=True)
    if not dates:
        print("Nenhum output encontrado.")
        return

    last_dir = dates[0]
    report_files = list(last_dir.glob("*relatorio_executivo*.md"))

    if report_files:
        print(f"\n=== RELATÓRIO: {last_dir.name} ===\n")
        print(report_files[0].read_text(encoding="utf-8"))
    else:
        print(f"Outputs de {last_dir.name}:")
        for f in sorted(last_dir.iterdir()):
            print(f"  - {f.name}")


def score_tema(tema: str):
    """Calcula score de conversão para um tema."""
    from skills import score_topic, calculate_trend_score

    conversion = score_topic(tema)
    trend = calculate_trend_score(tema)

    print(f"\n=== SCORE: {tema} ===")
    print(f"Score de Conversão: {conversion['score_total']}/100 — {conversion['classificacao']}")
    print(f"Score de Tendência: {trend['score_final']}/100 — {trend['classificacao']}")
    print(f"Publicar: {'✅ Sim' if conversion['publicar'] else '❌ Não'}")
    print(f"Recomendação: {conversion['recomendacao']}")


def main():
    load_dotenv()
    check_env()
    config = load_config()

    parser = argparse.ArgumentParser(description="Sistema Editorial Jurídico — Pipeline Runner")
    parser.add_argument("--mode", choices=["full", "research", "content"], default="full")
    parser.add_argument("--agent", type=str, help="Executar agente específico")
    parser.add_argument("--report", action="store_true", help="Ver relatório do último ciclo")
    parser.add_argument("--score", type=str, help="Calcular score de um tema")
    args = parser.parse_args()

    if args.report:
        show_last_report()
        return

    if args.score:
        score_tema(args.score)
        return

    if args.agent:
        run_single_agent(args.agent, config)
        return

    if args.mode == "full":
        run_full_pipeline(config)
    else:
        print(f"Modo '{args.mode}' ainda não implementado. Use --mode=full")


if __name__ == "__main__":
    main()

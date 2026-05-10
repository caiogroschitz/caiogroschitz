"""Editorial Chief Agent — orquestra todos os agentes e consolida o relatório executivo."""

import json
from datetime import datetime
from pathlib import Path

from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Editor-Chefe da redação jurídica digital.
Tem visão de negócio, rigor jurídico e sensibilidade editorial.

Sua função é revisar, consolidar e aprovar tudo que foi produzido hoje.
Você não produz conteúdo do zero. Você AVALIA, PRIORIZA e ENTREGA um
relatório executivo claro para o advogado que vai usar esse material.

CRITÉRIOS DE APROVAÇÃO FINAL:
1. O conteúdo está alinhado com a identidade editorial do escritório?
2. Está dentro das normas éticas da OAB?
3. A jurisprudência citada é real ou está marcada corretamente?
4. A linguagem está no nível certo (nem técnico demais, nem raso)?
5. O CTA é ético e efetivo?
6. O conteúdo está diferente de tudo que já foi publicado?
7. Há risco reputacional?

RELATÓRIO EXECUTIVO:
- Breve, direto, executivo
- O advogado deve conseguir ler em 5 minutos
- Prioridades claras para o dia
- Conteúdos prontos para uso
- Alertas de risco (se houver)

FORMATO: Markdown limpo, hierarquia clara, sem enrolação."""


class EditorialChiefAgent(BaseAgent):

    name = "editorial-chief"
    role = "Editor-Chefe da Redação Jurídica"

    def run(self, context: dict) -> dict:
        self._log("Consolidando relatório executivo")

        data_hoje = datetime.now().strftime("%d/%m/%Y")
        hora_exec = datetime.now().strftime("%H:%M")

        tendencias = context.get("data", {}).get("trends", {})
        pautas = context.get("data", {}).get("strategy", {})
        auditoria = context.get("data", {}).get("audit", {})
        carrosseIs = context.get("data", {}).get("carousels", {})
        roteiros = context.get("data", {}).get("reels", {})
        artigo_seo = context.get("data", {}).get("seo", {})
        linkedin = context.get("data", {}).get("linkedin", {})

        total_pautas = pautas.get("total_pautas", 0) if isinstance(pautas, dict) else 0
        top_pautas = pautas.get("pautas", [])[:5] if isinstance(pautas, dict) else []
        total_tendencias = tendencias.get("total_tendencias", 0) if isinstance(tendencias, dict) else 0
        aprovados_auditoria = auditoria.get("aprovados", 0) if isinstance(auditoria, dict) else 0
        total_auditados = auditoria.get("total_auditados", 0) if isinstance(auditoria, dict) else 0

        user_message = f"""Gere o Relatório Executivo Diário da Redação Jurídica para {data_hoje}.

DADOS DO CICLO DE HOJE:

TENDÊNCIAS IDENTIFICADAS:
{json.dumps(tendencias.get("tendencias", [])[:5], ensure_ascii=False, indent=2) if isinstance(tendencias, dict) else "Dados não disponíveis"}

TOP PAUTAS PRIORIZADAS:
{json.dumps(top_pautas, ensure_ascii=False, indent=2)}

AUDITORIA ÉTICA:
- Total auditados: {total_auditados}
- Aprovados: {aprovados_auditoria}
- Com ressalvas: {auditoria.get("aprovados_com_ajuste", 0) if isinstance(auditoria, dict) else 0}
- Reprovados: {auditoria.get("reprovados", 0) if isinstance(auditoria, dict) else 0}

CONTEÚDOS GERADOS:
- Carrosséis: {len(carrosseIs.get("carrosseIs", [])) if isinstance(carrosseIs, dict) else 0}
- Roteiros Reels: {len(roteiros.get("roteiros", [])) if isinstance(roteiros, dict) else 0}
- Artigos SEO: {"1" if isinstance(artigo_seo, dict) and artigo_seo.get("artigo_md") else 0}
- Posts LinkedIn: {len(linkedin.get("posts", [])) if isinstance(linkedin, dict) else 0}

Gere o relatório no seguinte formato:

---
# RELATÓRIO EXECUTIVO — {data_hoje}
**Redação Jurídica Digital | Gerado às {hora_exec}**

---

## RESUMO EXECUTIVO
[3-5 frases. O que aconteceu hoje no cenário de golpes digitais.
Qual a pauta mais urgente. O que está pronto para publicar.]

---

## TOP 3 PAUTAS DO DIA
[Cada pauta em 4-5 linhas: tema, por que agora, formato recomendado, CTA sugerido]

### 1. [TEMA — URGÊNCIA ALTA]
**Por que publicar hoje:** ...
**Formato ideal:** ...
**Fundamento jurídico:** ...
**Status:** APROVADO / COM AJUSTE

### 2. [TEMA]
...

### 3. [TEMA]
...

---

## CONTEÚDOS PRONTOS PARA USO
| Conteúdo | Tema | Status | Observação |
|---------|------|--------|------------|
| Carrossel 1 | ... | ✅ Pronto | ... |
| Reels 1 | ... | ✅ Pronto | ... |
| Artigo SEO | ... | ✅ Pronto | ... |
| LinkedIn 1 | ... | ✅ Pronto | ... |

---

## ALERTAS E RISCOS
[Se houver itens com ressalvas da auditoria, listar aqui com o ajuste necessário]
[Se tudo OK: "Nenhum alerta de risco para hoje."]

---

## TENDÊNCIAS PARA MONITORAR (PRÓXIMOS 7 DIAS)
[Top 3 tendências emergentes que devem virar pauta nos próximos dias]

---

## RECOMENDAÇÃO EDITORIAL
[1 parágrafo com a visão do editor-chefe sobre a estratégia da semana]

---
*Próxima execução: amanhã às 09:00*"""

        self._log("Gerando relatório executivo final")
        relatorio = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=4096)

        output_path = self._save_output("relatorio_executivo", relatorio, "md")
        relatorio_dir = Path("output/daily") / datetime.now().strftime("%Y-%m-%d")
        relatorio_dir.mkdir(parents=True, exist_ok=True)

        summary_data = {
            "data": data_hoje,
            "hora": hora_exec,
            "total_tendencias": total_tendencias,
            "total_pautas": total_pautas,
            "auditoria_aprovados": aprovados_auditoria,
            "auditoria_total": total_auditados,
            "relatorio_path": str(output_path),
        }
        self._save_output("sumario_ciclo", summary_data, "json")

        self._log("Relatório executivo concluído")
        print("\n" + "=" * 60)
        print(relatorio)
        print("=" * 60 + "\n")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path),
            "data": {"relatorio_md": relatorio, "sumario": summary_data},
            "summary": "Relatório executivo diário concluído",
        }

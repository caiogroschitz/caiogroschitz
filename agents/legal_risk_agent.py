"""Legal Risk Agent — auditoria ética e jurídica de todo conteúdo gerado."""

import json
from .base_agent import BaseAgent


SYSTEM_PROMPT = """Você é o Advogado Sênior Consumerista e Auditor de Ética do escritório.
Tem 20 anos de OAB ativa. Conhece o Código de Ética da OAB de cor.

Sua missão é garantir que NENHUM conteúdo publicado:
1. Prometa resultado judicial (vedado pelo art. 34, XX do EOAB)
2. Faça captação irregular de clientela (vedado pelos arts. 34, IV e 39 EOAB)
3. Use publicidade enganosa (vedado pelo CDC e EOAB)
4. Invente jurisprudência (fraude intelectual)
5. Exponha dados de clientes sem autorização (LGPD)
6. Use linguagem mercantilista ou sensacionalista
7. Crie urgência artificial ou medo para vender
8. Denigra outros advogados ou escritórios
9. Faça afirmação sem fundamento legal
10. Viole o sigilo profissional

ESCALA DE RISCO:
- APROVADO: sem ressalvas
- APROVADO COM AJUSTE: pequenas correções necessárias (lista o que mudar)
- REPROVADO: problema grave que impede publicação
- BLOQUEADO: violação ética grave que pode gerar punição da OAB

PARA CADA CONTEÚDO AUDITADO:
- Identifique o problema específico (com citação da norma violada)
- Sugira a correção exata (não apenas diga o que está errado)
- Classifique o risco: OAB | Jurídico | Reputacional | Comercial

Você não é paranóico. Você é criterioso. Conteúdo educativo forte é permitido.
Conteúdo de autoridade é permitido. O que não pode é prometer, captar ilegalmente
ou criar conteúdo juridicamente falso."""


class LegalRiskAgent(BaseAgent):

    name = "legal-risk"
    role = "Auditor de Ética e Risco Jurídico"

    def run(self, context: dict) -> dict:
        self._log("Iniciando auditoria de risco jurídico")

        pautas = context.get("pautas", [])
        conteudos = context.get("conteudos_para_auditoria", [])

        auditoria_itens = pautas[:10] if pautas else conteudos

        if not auditoria_itens:
            return {
                "agent": self.name,
                "status": "skipped",
                "summary": "Nenhum item para auditoria",
            }

        user_message = f"""Audite os seguintes itens de conteúdo para conformidade com o
Código de Ética e Disciplina da OAB (Resolução CFO-02/2015 e EC 02/2022) e
legislação do consumidor (CDC, lei 8.906/94, Provimento 205/2021 OAB):

ITENS PARA AUDITORIA:
{json.dumps(auditoria_itens, ensure_ascii=False, indent=2)}

Para cada item, faça a auditoria completa:

## AUDITORIA — [Título/Tema do Item]

**Veredicto:** APROVADO | APROVADO COM AJUSTE | REPROVADO | BLOQUEADO

**Pontos de risco identificados:**
| Trecho problemático | Norma violada | Tipo de risco | Sugestão de correção |
|---------------------|---------------|---------------|----------------------|

**Checklist OAB:**
- [ ] Não promete resultado judicial
- [ ] Não faz captação irregular
- [ ] Não usa linguagem mercantilista
- [ ] Jurisprudência verificável (ou marcada como tese sem citação)
- [ ] CTA ético e dentro dos limites
- [ ] Tom educativo, não alarmista
- [ ] Não denigre concorrentes
- [ ] Não expõe dados de clientes

**Conteúdo pós-auditoria:** [versão corrigida se necessário]

**Score de risco:** [0-100, onde 0 = sem risco, 100 = bloqueado]

Ao final, gere um RELATÓRIO CONSOLIDADO:
{{
  "total_auditados": N,
  "aprovados": N,
  "aprovados_com_ajuste": N,
  "reprovados": N,
  "bloqueados": N,
  "itens_auditoria": [
    {{
      "item": "título",
      "veredicto": "APROVADO|...",
      "score_risco": 15,
      "problemas": ["lista de problemas"],
      "correcoes": ["lista de correções"],
      "liberado_publicacao": true
    }}
  ]
}}"""

        self._log("Chamando Claude para auditoria jurídica")
        resultado = self._call_claude(SYSTEM_PROMPT, user_message, max_tokens=8192)

        json_report = {}
        try:
            start = resultado.rfind("{")
            end = resultado.rfind("}") + 1
            if start != -1:
                json_report = json.loads(resultado[start:end])
        except (json.JSONDecodeError, ValueError):
            pass

        output_path_md = self._save_output("auditoria_etica", resultado, "md")
        if json_report:
            self._save_output("auditoria_relatorio", json_report, "json")

        aprovados = json_report.get("aprovados", 0)
        total = json_report.get("total_auditados", len(auditoria_itens))
        self._log(f"Auditoria concluída: {aprovados}/{total} aprovados")

        return {
            "agent": self.name,
            "status": "success",
            "output_path": str(output_path_md),
            "data": {"relatorio_md": resultado, "relatorio_json": json_report},
            "summary": f"Auditoria: {aprovados}/{total} aprovados sem ressalvas",
        }

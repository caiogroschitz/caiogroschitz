"""MCP server — Jusbrasil jurisprudence collector.

Exposes a single tool: `coletar_jurisprudencia`.

Environment variables required at runtime:
    JUSBRASIL_EMAIL     — registered e-mail on Jusbrasil
    JUSBRASIL_PASSWORD  — account password

Never set these in code or config files.
"""

import json
from datetime import datetime
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server import Server

from .auth.jusbrasil_client import autenticar, AuthenticationError
from .crawler.jusbrasil_crawler import coletar, CrawlerError
from .formatter.docx_formatter import gerar_docx
from .models.jurisprudencia import ResultadoColeta
from .utils.logger import AuditLogger

_MIN_EMENTAS_VALIDAS = 3

app = Server("mcp-jusbrasil")


@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="coletar_jurisprudencia",
            description=(
                "Autentica no Jusbrasil com credenciais do usuário (via variáveis de "
                "ambiente), busca jurisprudências reais sobre o tema informado, valida "
                "rigorosamente cada item e gera um arquivo .docx local com as ementas "
                "literais. Nunca inventa ou modifica conteúdo jurídico."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tema": {
                        "type": "string",
                        "description": "Tema jurídico a pesquisar (texto livre)",
                        "minLength": 3,
                    },
                    "limite": {
                        "type": "integer",
                        "description": "Número máximo de resultados válidos (padrão: 15)",
                        "default": 15,
                        "minimum": 1,
                        "maximum": 50,
                    },
                },
                "required": ["tema"],
            },
        )
    ]


@app.call_tool()
async def call_tool(
    name: str,
    arguments: dict[str, Any],
) -> list[types.TextContent]:
    if name != "coletar_jurisprudencia":
        raise ValueError(f"Ferramenta desconhecida: {name!r}")

    tema: str = arguments.get("tema", "").strip()
    if not tema:
        return [types.TextContent(type="text", text="Erro: 'tema' é obrigatório.")]

    limite: int = int(arguments.get("limite", 15))
    limite = max(1, min(limite, 50))

    logger = AuditLogger(tema)
    logger.info(f"Ferramenta chamada — tema={tema!r} limite={limite}")

    # ── 1. Autenticação ──────────────────────────────────────────────────────
    try:
        session = autenticar()
        logger.info("Autenticação realizada com sucesso")
    except AuthenticationError as exc:
        logger.error(f"Falha de autenticação: {exc}")
        return [
            types.TextContent(
                type="text",
                text=(
                    f"ERRO DE AUTENTICAÇÃO — execução interrompida.\n"
                    f"Detalhe: {exc}\n\n"
                    "Configure as variáveis de ambiente JUSBRASIL_EMAIL e "
                    "JUSBRASIL_PASSWORD antes de executar."
                ),
            )
        ]

    # ── 2. Coleta ────────────────────────────────────────────────────────────
    try:
        itens_validos, total_encontrado = coletar(session, tema, limite, logger)
    except CrawlerError as exc:
        logger.error(f"Erro no crawler: {exc}")
        return [
            types.TextContent(
                type="text",
                text=f"ERRO DE COLETA — {exc}",
            )
        ]

    total_descartado = total_encontrado - len(itens_validos)

    # ── 3. Verificação de suficiência ────────────────────────────────────────
    if len(itens_validos) < _MIN_EMENTAS_VALIDAS:
        msg = (
            f"INSUFICIÊNCIA DE DADOS: apenas {len(itens_validos)} "
            f"ementas válidas encontradas (mínimo: {_MIN_EMENTAS_VALIDAS}).\n"
            "Possíveis causas: tema muito específico, mudança no DOM do Jusbrasil, "
            "captcha ou período sem decisões nos últimos 3 anos.\n"
            f"Log de auditoria: {logger.log_path}"
        )
        logger.warning(msg)
        logger.resumo_final(total_encontrado, len(itens_validos))
        return [types.TextContent(type="text", text=msg)]

    # ── 4. Geração do documento ──────────────────────────────────────────────
    resultado = ResultadoColeta(
        tema=tema,
        total_encontrado=total_encontrado,
        total_valido=len(itens_validos),
        total_descartado=total_descartado,
        itens=itens_validos,
        descartados=logger._itens_descartados,
    )

    try:
        caminho = gerar_docx(resultado)
        resultado.caminho_arquivo = caminho
        logger.resumo_final(total_encontrado, len(itens_validos), caminho)
    except Exception as exc:
        logger.error(f"Erro ao gerar .docx: {exc}")
        return [
            types.TextContent(
                type="text",
                text=f"ERRO AO GERAR DOCUMENTO — {exc}",
            )
        ]

    # ── 5. Resposta estruturada ──────────────────────────────────────────────
    linhas = [
        f"Coleta concluída com sucesso.",
        f"Tema: {tema}",
        f"Itens válidos: {len(itens_validos)} / {total_encontrado} encontrados",
        f"Itens descartados: {total_descartado}",
        f"Arquivo gerado: {caminho}",
        f"Log de auditoria: {logger.log_path}",
        "",
        "=== RESUMO DOS RESULTADOS ===",
    ]
    for idx, item in enumerate(itens_validos, 1):
        linhas.append(
            f"\n[{idx}] {item.tribunal} — {item.numero_processo}"
            f"\n    Data: {item.data_julgamento.strftime('%d/%m/%Y')}"
            f"\n    Tipo: {item.tipo.value}"
            f"\n    Favorabilidade: {item.favorabilidade.value}"
            f"\n    Link: {item.link}"
            f"\n    Ementa (primeiros 300 chars): {item.ementa[:300]}..."
        )

    return [types.TextContent(type="text", text="\n".join(linhas))]


def main() -> None:
    import asyncio

    async def _run() -> None:
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                app.create_initialization_options(),
            )

    asyncio.run(_run())


if __name__ == "__main__":
    main()

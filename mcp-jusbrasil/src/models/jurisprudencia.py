"""Data models for jurisprudence collection."""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from enum import Enum


class Favorabilidade(Enum):
    FAVORAVEL = "FAVORÁVEL"
    DESFAVORAVEL = "DESFAVORÁVEL"
    NEUTRA = "NEUTRA"
    NAO_CLASSIFICADA = "NÃO CLASSIFICADA"


class TipoDecisao(Enum):
    ACORDAO = "ACÓRDÃO"
    DECISAO_MONOCRATICA = "DECISÃO MONOCRÁTICA"
    DESPACHO = "DESPACHO"
    DESCONHECIDO = "DESCONHECIDO"


@dataclass
class Jurisprudencia:
    numero_processo: str
    tribunal: str
    data_julgamento: date
    link: str
    ementa: str
    favorabilidade: Favorabilidade = Favorabilidade.NAO_CLASSIFICADA
    relator: Optional[str] = None
    tipo: TipoDecisao = TipoDecisao.ACORDAO
    fonte_url_verificada: bool = False

    def __post_init__(self):
        if not self.numero_processo.strip():
            raise ValueError("Número do processo não pode ser vazio")
        if not self.tribunal.strip():
            raise ValueError("Tribunal não pode ser vazio")
        if not self.link.strip():
            raise ValueError("Link não pode ser vazio")
        if not self.ementa.strip():
            raise ValueError("Ementa não pode ser vazia")


@dataclass
class ResultadoColeta:
    tema: str
    total_encontrado: int
    total_valido: int
    total_descartado: int
    itens: list = field(default_factory=list)
    descartados: list = field(default_factory=list)
    caminho_arquivo: Optional[str] = None
    erro: Optional[str] = None

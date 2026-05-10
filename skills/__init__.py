"""Legal Editorial System — Skills package."""

from .detect_high_conversion_topic import score_topic, batch_score
from .anti_ai_writing import analyze as analyze_ai_writing, clean as clean_ai_writing
from .hook_generator import generate as generate_hook, generate_bank as generate_hook_bank
from .ethical_cta import generate as generate_cta, validate as validate_cta
from .trend_score import calculate as calculate_trend_score, batch_calculate as batch_trend_score
from .jurisprudencia_summarizer import summarize as summarize_jurisprudencia, build_legal_brief
from .emotional_pain_mapper import get_profile as get_pain_profile, map_content_to_pain
from .fake_jurisprudence_validator import validate_citation, validate_batch, get_tese_consolidada

__all__ = [
    "score_topic", "batch_score",
    "analyze_ai_writing", "clean_ai_writing",
    "generate_hook", "generate_hook_bank",
    "generate_cta", "validate_cta",
    "calculate_trend_score", "batch_trend_score",
    "summarize_jurisprudencia", "build_legal_brief",
    "get_pain_profile", "map_content_to_pain",
    "validate_citation", "validate_batch", "get_tese_consolidada",
]

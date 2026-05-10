"""Base class for all legal editorial agents."""

import json
import os
import time
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any

import anthropic


class BaseAgent(ABC):
    """Abstract base for all specialized agents in the legal editorial system."""

    name: str = "base"
    role: str = "Agente base"

    def __init__(self, config: dict, memory_manager=None):
        self.config = config
        self.memory = memory_manager
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        self.model = config.get("system", {}).get("model", "claude-opus-4-7")
        self.output_dir = Path("output/daily") / datetime.now().strftime("%Y-%m-%d")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._execution_log = []

    def _load_prompt(self, prompt_name: str) -> str:
        prompt_path = Path("prompts") / f"{prompt_name}.md"
        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8")
        return ""

    def _load_context(self, context_name: str) -> str:
        ctx_path = Path("contexts") / f"{context_name}.md"
        if ctx_path.exists():
            return ctx_path.read_text(encoding="utf-8")
        return ""

    def _call_claude(self, system_prompt: str, user_message: str, max_tokens: int = 4096) -> str:
        for attempt in range(3):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_message}],
                )
                return response.content[0].text
            except anthropic.RateLimitError:
                wait = 2 ** attempt * 5
                time.sleep(wait)
            except anthropic.APIError as e:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        return ""

    def _save_output(self, filename: str, content: Any, fmt: str = "md") -> Path:
        out_path = self.output_dir / f"{self.name}_{filename}.{fmt}"
        if fmt == "json":
            out_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
        else:
            if isinstance(content, dict):
                content = json.dumps(content, ensure_ascii=False, indent=2)
            out_path.write_text(str(content), encoding="utf-8")
        return out_path

    def _log(self, message: str, level: str = "INFO"):
        entry = {"timestamp": datetime.now().isoformat(), "agent": self.name, "level": level, "message": message}
        self._execution_log.append(entry)
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    @abstractmethod
    def run(self, context: dict) -> dict:
        """Execute the agent's main task. Returns structured output."""
        ...

    def get_execution_summary(self) -> dict:
        return {
            "agent": self.name,
            "role": self.role,
            "logs": self._execution_log,
            "timestamp": datetime.now().isoformat(),
        }

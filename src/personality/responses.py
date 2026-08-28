import random
from functools import lru_cache
from pathlib import Path

import yaml

PHRASES_DIR = Path(__file__).resolve().parent / "phrases"


@lru_cache()
def load_all_phrases() -> dict[str, list[str]]:
    merged: dict[str, list[str]] = {}

    for file in PHRASES_DIR.glob("*.yaml"):
        data = yaml.safe_load(file.read_text(encoding="utf-8")) or {}

        for key, templates in data.items():
            merged.setdefault(key, []).extend(templates)

    return merged


def get_response(key: str, **kwargs) -> str:
    phrases = load_all_phrases()

    pool = (
        phrases.get(key)
        or phrases.get("generic error")
        or ["Done"]
    )

    template = random.choice(pool)

    try:
        return template.format(**kwargs)
    except KeyError:
        return template

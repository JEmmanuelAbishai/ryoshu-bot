import pytest

from src.personality.responses import _load_all_phrases

@pytest.fixture(scope="session", autouse=True)
def clear_phrase_cache():
    _load_all_phrases.cache_clear()
    yield
    _load_all_phrases.cache_clear()
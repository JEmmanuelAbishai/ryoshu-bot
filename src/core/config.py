from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra = "ignore")

    discord_token: str
    command_prefix: str = "!"

    anthropic_key = str
    llm_model: str = "claude-v1.3"
    llm_max_tokens: int = 1000

    database_url: str = "sqlite+aiosqlite:///./database.db"

    default_personality : str = "ryoshu"
    max_context_messages : int = 20
    log_level : str = "INFO"

@lru_cache()
def get_settings() -> Settings:
    return Settings() 
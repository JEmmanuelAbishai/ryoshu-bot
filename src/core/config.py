from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra = "ignore")

    discord_token: str
    command_prefix: str = "r!"

    mod_log_channel_id: int
    giphy_api_key: str | None = None
    database_url: str = "sqlite+aiosqlite:///./database.db"
    log_level: str = "INFO"

@lru_cache()
def get_settings() -> Settings:
    return Settings() 
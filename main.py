import asyncio

from src.core.bot import build_bot
from src.core.config import get_settings
from src.utils.loggers import setup_logging

async def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)

    bot = build_bot(settings)
    await bot.start(settings.discord_token)

if __name__ == "__main__":
    asyncio.run(main())
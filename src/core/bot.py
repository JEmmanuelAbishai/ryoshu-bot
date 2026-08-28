from pathlib import Path

import discord
import discord.ext.commands as commands
from loguru import logger

from src.core.config import Settings
from src.database.connection import init_db

COGS_PACKAGE = "src.cogs"
COGS_DIR = Path(__file__).resolve().parent.parent / "cogs"

class Bot(commands.Bot):
    def __init__(self, settings: Settings, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=settings.command_prefix, intents=intents, **kwargs) 
        self.settings = settings

    async def setup_hook(self) -> None:
        await init_db(self.settings.database_url)
        await self.load_cogs()
        logger.info("Bot setup complete.")

    async def load_cogs(self) -> None:
        for file in COGS_DIR.glob("*.py"):
            if file.name.startswith("_"):
                continue
            extension = f"{COGS_PACKAGE}.{file.stem}"
            try:
                await self.load_extension(extension)
                logger.info(f"Loaded cog: {extension}")
            except Exception as exc:
                logger.error(f"Failed to load cog {extension}: {exc}")

    async def on_ready(self) -> None:
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

def build_bot(settings: Settings) -> Bot:
    bot = Bot(settings)
    return bot
import sys
from pathlib import Path

from loguru import logger

LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"


def setup_logging(level: str = "INFO") -> None:
    LOG_DIR.mkdir(exist_ok=True)

    logger.remove()  # drop default handler
    logger.add(sys.stderr, level=level, colorize=True)
    logger.add(
        LOG_DIR / "bot.log",
        level=level,
        rotation="10 MB",
        retention="14 days",
        compression="zip",
        enqueue=True,
    )
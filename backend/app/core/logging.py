import os
from loguru import logger
from app.core.config import settings

logger.remove()

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

LOG_FORMAT = (
    "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
)

# Resolve the WARNING level number ONCE at import time.
# Note: Loguru's built-in level name is "WARNING" (uppercase).
WARNING_NO = logger.level("WARNING").no

logger.add(
    sink=os.path.join(LOG_DIR, "debug.log"),
    format=LOG_FORMAT,
    level="DEBUG" if settings.ENVIRONMENT == "local" else "INFO",
    filter=lambda record: record["level"].no <= WARNING_NO,
    rotation="10MB",
    retention="30 days",
    compression="zip",
)

logger.add(
    sink=os.path.join(LOG_DIR, "error.log"),
    format=LOG_FORMAT,
    level="DEBUG",
    rotation="10MB",
    retention="30 days",
    compression="zip",
    backtrace=True,
    diagnose=True,
)

def get_logger():
    return logger
import logging
from app.core.config import settings

# Create a logger instance
logger = logging.getLogger(__name__)

def setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ) 
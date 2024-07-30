import logging

def setup_logger():
    """Set up the logger with desired configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

import logging
import os
import sys

DEFAULT_LOG_LEVEL = 'ERROR'
LOG_LEVEL = os.getenv('LOG_LEVEL', DEFAULT_LOG_LEVEL).upper()
LOG_LEVEL = getattr(logging, LOG_LEVEL, DEFAULT_LOG_LEVEL)

LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(name)s]: %(message)s'

# Configure root logger
logging.basicConfig(
    level=LOG_LEVEL,  # Change to INFO or WARNING in production
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout),  # Console logging
    ],
)


def get_logger(name: str) -> logging.Logger:
    """Returns a logger with the specified name."""
    return logging.getLogger(name)

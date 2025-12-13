# logger.py
import logging
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger("email_classifier")
logger.setLevel(logging.INFO)  # or DEBUG for more verbosity

# File handler with rotation
file_handler = RotatingFileHandler(
    "email_classifier.log", maxBytes=1_000_000, backupCount=5
)
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)

# Optional: also log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

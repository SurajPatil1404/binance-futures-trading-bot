import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'trading.log')


def configure_logging(level: int = logging.INFO) -> None:
	logger = logging.getLogger('trading')
	logger.setLevel(level)

	# Avoid adding handlers multiple times in interactive runs
	if logger.handlers:
		return

	fmt = '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
	formatter = logging.Formatter(fmt)

	# Console handler
	ch = logging.StreamHandler()
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	# Rotating file handler
	fh = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3)
	fh.setFormatter(formatter)
	logger.addHandler(fh)


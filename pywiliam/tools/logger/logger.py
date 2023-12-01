import logging

# Creqte and configure a logger
LOG_FORMAT = "%(levelname)s - %(asctime)s, %(lineno)d: %(message)s"

# Log to stdout
logging.basicConfig(format=LOG_FORMAT,
                    level=logging.INFO,
                    datefmt='%a, %d %b %Y %H:%M:%S')

log = logging.getLogger(__name__)

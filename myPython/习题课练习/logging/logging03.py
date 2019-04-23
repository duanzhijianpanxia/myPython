import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="mylogging.log")

logging.debug("This is a debug")
logging.info("This is a info")
logging.warning("This is a warning")
logging.error("This is a error")
logging.critical("This is a critical")
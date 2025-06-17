import logging

def setup_logging():
  logging.basicConfig(level=logging.INFO, format="%(asctime_s %(message)s")
  return logging.getLogger(__name__)

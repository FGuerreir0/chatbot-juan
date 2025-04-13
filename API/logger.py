import logging
import sys

def setup(name, level=logging.DEBUG):
   
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)

    # Create formatters and add them to the handlers
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(funcName)s: %(message)s')
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)

    # Stop propagation to avoid having duplicate logs
    logger.propagate = False

    return logger
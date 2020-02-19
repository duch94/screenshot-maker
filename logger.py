import logging.config


def get_logger(name="") -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(fmt="[%(asctime)s][%(name)s][%(levelname)s]: %(message)s")

    file_handler = logging.FileHandler(filename="app.log")
    file_handler.setFormatter(fmt=formatter)
    logger.addHandler(file_handler)
    logger.setLevel("DEBUG")

    return logger

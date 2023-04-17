import inspect
import logging


class cutomLoger:
    def get_logger(loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]

        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

        fh = logging.FileHandler(".\\Logs\\automation.log")

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        fh.setFormatter(formatter)

        logger.addHandler(fh)

        return logger


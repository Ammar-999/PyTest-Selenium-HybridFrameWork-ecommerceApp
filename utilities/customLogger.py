import logging


class LogGen:
    @staticmethod
    # Creating automation.log file in Logs directory and assigning format
    def loggen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='.\\Logs\\automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

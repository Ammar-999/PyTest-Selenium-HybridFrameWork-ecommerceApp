import logging


class LogGen:
    @staticmethod
    # Creating automation.log file in Logs directory and assigning format
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=".\\Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger



# logger = logging.getLogger()
# fhandler = logging.FileHandler(filename='mylog.log', mode='a')
# formatter = logging.Formatter(''%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# fhandler.setFormatter(formatter)
# logger.addHandler(fhandler)

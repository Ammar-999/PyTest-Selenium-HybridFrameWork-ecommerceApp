import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    # creating static method for all common variables in "config.ini" in Configuration folder
    @staticmethod
    def getApplicationURL():
        url = config.get('common variable', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common variable', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common variable', 'password')
        return password

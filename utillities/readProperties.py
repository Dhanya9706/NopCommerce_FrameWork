import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getEmailId():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getFirstName():
        firstname = config.get('common info', 'firstname')
        return firstname
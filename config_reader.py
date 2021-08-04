import configparser

class ConfigReader:   #read config.ini file
    def __init__(self):
        self.filename = 'config.ini'
    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)
        self.configuration=self.config['DEFAULT']
        # self.sender_email=self.configuration['SENDER_EMAIL']
        # self.password = self.configuration['PASSWORD']
        # self.email_body = self.configuration['EMAIL_BODY']
        # self.email_subject = self.configuration['EMAIL_SUBJECT']

        return self.configuration   # returns configuration which is a dictionary, key:value pair
    #emial_body:value....the values from config.ini is returned to sendemail.py


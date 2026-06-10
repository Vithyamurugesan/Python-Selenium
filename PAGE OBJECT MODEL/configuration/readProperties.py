from configparser import ConfigParser

config = ConfigParser()
config.read("configuration/config.ini")
class ReadConfig:
 
    def get_application_url():
        return config.get("common info", "baseURL")

    def get_email():
        return config.get("common info", "email")
 
    def get_password():
        return config.get("common info", "password")
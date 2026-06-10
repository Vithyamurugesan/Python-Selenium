from configparser import ConfigParser
import os

config = ConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.ini")
config.read(config_path)

class ReadConfig:
  
    def get_application_url():
        return config.get("common info", "baseURL")
 
    def get_email():
        return config.get("common info", "email")

    def get_password():
        return config.get("common info", "password")
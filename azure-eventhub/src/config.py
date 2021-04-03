########################################################################
# Owner: Anuj Singhal
# Description: configuration file setting variables from .ini file
########################################################################

from configparser import ConfigParser
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
:: %(message)s', level = logging.INFO)

logging.info("Setting Configurations from config.ini file")
#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the connection string
eventinfosend = config_object["EVENTINFOSEND"]
eventinforeceive = config_object["EVENTINFORECEIVE"]
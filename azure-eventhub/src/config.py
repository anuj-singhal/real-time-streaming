from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the connection string
eventinfosend = config_object["EVENTINFOSEND"]
eventinforeceive = config_object["EVENTINFORECEIVE"]
from configparser import ConfigParser


conf_obj = ConfigParser()
conf_obj.read('Config\config.ini')

try:
    config = conf_obj['DataBase']
    DRIVER = config.get('DRIVER')
    SERVER = config.get('SERVER')
    DATABASE = config.get('DATABASE')
    
    
    
except Exception as e:
    pass
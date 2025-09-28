from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config_file_path="C:/Users/Admin/PycharmProjects/PythonHybridFrameworkSelenium/configuration/config.ini"
    config.read(config_file_path)
    return config.get(category,key)
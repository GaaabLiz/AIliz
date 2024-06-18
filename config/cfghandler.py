
import configparser
import os

from config.cfglist import CfgList
from config.cfgsection import CfgSection
from config.literals import HOME_FOLDER_NAME, SETTING_FILE_NAME, MODELS_FOLDER_NAME
from util import osutils

dir_app = osutils.get_app_home_dir(HOME_FOLDER_NAME)
dir_app_setting = os.path.join(dir_app, SETTING_FILE_NAME)
dir_app_models = os.path.join(dir_app, MODELS_FOLDER_NAME)


def create_config(path):
    config = configparser.ConfigParser()

    section_general_text = CfgSection.GENERAL.value
    section_ai_text = CfgSection.AI.value

    config.add_section(section_general_text)
    config.set(section_general_text, CfgList.INIT.value, 'False')

    config.add_section(section_ai_text)
    config.set(section_ai_text, CfgList.OLLAMA_URL_SET.value, 'False')

    try:
        with open(path, 'w') as configfile:
            config.write(configfile)
        print("Configuration file created in: ", path)
    except Exception as e:
        print("Error while creating configuration file: ", e)


def read_config(section, key, is_bool=False):
    config = configparser.ConfigParser()
    config.read(dir_app_setting)
    if is_bool:
        return config.getboolean(section, key)
    return config.get(section, key)


def write_config(section, key, value):
    config = configparser.ConfigParser()
    config.read(dir_app_setting)
    config.set(section, key, value)
    with open(dir_app_setting, 'w') as configfile:
        config.write(configfile)


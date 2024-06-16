import os

from literals import HOME_FOLDER_NAME
from util import osutils
from rich import print


dir_app = osutils.get_app_home_dir(HOME_FOLDER_NAME)
dir_app_setting = os.path.join(dir_app, "settings.json")


def check_init():
    is_setting_file_ok = osutils.check_path(dir_app_setting)
    return is_setting_file_ok


def exec_init():
    if check_init():
        print("Application already initialized. \nTry [green]--help[/green] for command list.")
        return
    print("Initializing...")
    osutils.check_path(dir_app_setting, create_if_not=True)
    print("Configuration file created in: ", dir_app_setting)

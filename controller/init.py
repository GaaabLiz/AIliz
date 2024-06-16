import os

import typer

from config.cfghandler import *
from util import osutils
from rich import print


def check_init(called_from_init: bool = False):
    init = osutils.check_path(dir_app_setting)
    if init:
        if called_from_init:
            print("Application already initialized. \nTry [green]--help[/green] for command list.")
            raise typer.Exit()
    else:
        if not called_from_init:
            print("Application not initialized.")
            print("Rerun application with [green]init[/green] command to start.")
            raise typer.Exit()


def delete_init():
    try:
        os.remove(dir_app_setting)
        print("Configuration file deleted.")
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print("Error while deleting configuration file: ", e)


def exec_init():
    print("Initializing...")
    create_config(dir_app_setting)


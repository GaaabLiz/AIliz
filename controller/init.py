import os

import inquirer
import typer

from cli.asker import ask_ollama_location
from config.cfghandler import *
from util import osutils
from rich import print


def handle_not_initialized():
    print("Application not initialized.")
    print("Rerun application with [green]init[/green] command to start.")
    raise typer.Exit()


def check_init(called_from_init: bool = False):
    file_exist = osutils.check_path(dir_app_setting)
    if not file_exist:
        if not called_from_init:
            handle_not_initialized()
        else:
            return
    init = read_config(CfgSection.GENERAL.value, CfgList.INIT.value, True)
    if init:
        if called_from_init:
            print("Application already initialized. \nTry [green]--help[/green] for command list.")
            raise typer.Exit()
        else:
            return
    else:
        if called_from_init:
            return
        else:
            handle_not_initialized()


def delete_init():
    try:
        os.remove(dir_app_setting)
        print("Configuration file deleted.")
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print("Error while deleting configuration file: ", e)


def setup_ollama_location():
    url = ask_ollama_location()
    write_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value, url)


def exec_init():
    print("Initializing...")
    create_config(dir_app_setting)
    setup_ollama_location()


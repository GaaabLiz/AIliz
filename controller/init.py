import os

import inquirer
import typer

from ai.ollamaliz import check_ollama_status, check_ollama_status2
from cli.asker import ask_ollama_location, ask_ai_power
from config.cfghandler import *
from network.netrestype import NetResponseType
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
    status = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL_SET.value, True)
    if not status:
        url = ask_ollama_location()
        write_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value, url)
        write_config(CfgSection.AI.value, CfgList.OLLAMA_URL_SET.value, "True")
        print("Ollama url set to: ", url)
    else:
        print("Ollama url already set.")


def setup_ai_power():
    power = ask_ai_power()
    write_config(CfgSection.AI.value, CfgList.AI_POWER.value, power)
    pass


def setup_ollama_models():
    check_ollama()


def check_ollama():
    url_set = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL_SET.value, True)
    if url_set is False:
        print("Ollama url was not set. Please re-run the application with init command.")
        raise typer.Exit()
    print("Checking ollama server status...")
    url = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value)
    response = check_ollama_status2(url)
    if response.is_successful():
        print("Ollama server is running.")
    else:
        error = response.get_error()
        print("Ollama server is not running or some error occurred: " + "[red]" + error + "[/red]")
        print("Please check the server and try again.")
        raise typer.Exit()



def exec_init():
    print("Initializing...")
    create_config(dir_app_setting)
    setup_ai_power()
    setup_ollama_location()
    setup_ollama_models()
    write_config(CfgSection.GENERAL.value, CfgList.INIT.value, 'True')
    print("Initialization finished.")


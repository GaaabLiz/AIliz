import os

import inquirer
import typer

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
        handle_not_initialized()


def delete_init():
    try:
        os.remove(dir_app_setting)
        print("Configuration file deleted.")
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print("Error while deleting configuration file: ", e)


def ask_for_models_custom_path():
    questions = [
        inquirer.Path('custom_model_path',
                      message="Where models should be stored?",
                      path_type=inquirer.Path.DIRECTORY,
                      ),
    ]
    answers = inquirer.prompt(questions)
    write_config(CfgSection.AI.value, CfgList.AI_MODEL_CUSTOM_PATH.value, answers['custom_model_path'])
    write_config(CfgSection.AI.value, CfgList.USE_CUSTOM_PATH.value, 'True')


def ask_for_models_paths():
    questions = [
        inquirer.List('path_type',
                      message="Where do you want to store the models?",
                      choices=[dir_app_models, "Custom path"],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers['path_type'] == dir_app_models:
        write_config(CfgSection.AI.value, CfgList.USE_CUSTOM_PATH.value, 'False')
    else:
        ask_for_models_custom_path()


def ask_ollama_location():
    def_url = "http://localhost:11434"
    questions = [
        inquirer.List('ollama_location',
                      message="Where ollama server is running?",
                      choices=["On this machine (localhost)", "Remote server", "Nowhere"],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers['ollama_location'] == "Remote server":
        questions = [
            inquirer.Text('ollama_path',message="Enter the URL of the ollama server (ex http://xxx.xxx.xxx.xxx:11434):",),
        ]
        answers = inquirer.prompt(questions)
        def_url = answers['ollama_path']
    elif answers['ollama_location'] == "On this machine (localhost)":
        def_url = "http://localhost:11434"
    elif answers['ollama_location'] == "Nowhere":
        print("To run the application, you need to provide the location of the ollama server.")
        raise typer.Exit()
    else:
        def_url = ""
    write_config(CfgSection.GENERAL.value, CfgList.OLLAMA_URL.value, def_url)


def exec_init():
    print("Initializing...")
    create_config(dir_app_setting)
    ask_ollama_location()


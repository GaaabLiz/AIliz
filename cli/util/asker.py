import inquirer
import typer

from core.enum.ai_power import AiPower
from core.util.cfgutils import DEFAULT_NO_VALUE
from util.ai.ollamapi import OLLAMA_PORT, OLLAMA_HTTP_LOCALHOST_URL

QS_OLLAMA_LOC_NAME = "ollama_location"
QS_OLLAMA_LOC_CHOICES = ["On this machine (localhost)", "Remote server", "Nowhere"]
QS_OLLAMA_LOC_DEFAULT = "On this machine (localhost)"
QS_OLLAMA_LOC_MSG = "Where ollama server is running?"

QS_OLLAMA_URL_NAME = "ollama_url"
QS_OLLAMA_URL_MSG = f"Enter the URL of the ollama server (ex http://xxx.xxx.xxx.xxx:{OLLAMA_PORT}):"
QS_OLLAMA_URL_DEFAULT = OLLAMA_HTTP_LOCALHOST_URL

QS_AI_POWER_NAME = "ai_power"
QS_AI_POWER_CHOICES = [AiPower.LOW.value, AiPower.MEDIUM.value, AiPower.HIGH.value]
QS_AI_POWER_DEFAULT = AiPower.MEDIUM.value
QS_AI_POWER_MSG = "Select the size of the AI model to be used."


def ask_ollama_url():
    questions = [
        inquirer.Text(QS_OLLAMA_URL_NAME, message=QS_OLLAMA_URL_MSG, default=QS_OLLAMA_URL_DEFAULT),
    ]
    answers = inquirer.prompt(questions)
    return answers[QS_OLLAMA_URL_NAME]


def ask_ollama_location(last_inserted: str = DEFAULT_NO_VALUE):
    def_url = ""
    if last_inserted != DEFAULT_NO_VALUE:
        default = last_inserted
    else:
        default = QS_OLLAMA_LOC_DEFAULT
    questions = [
        inquirer.List(QS_OLLAMA_LOC_NAME, message=QS_OLLAMA_LOC_MSG, choices=QS_OLLAMA_LOC_CHOICES, default=default),
    ]
    answers = inquirer.prompt(questions)
    if answers[QS_OLLAMA_LOC_NAME] == QS_OLLAMA_LOC_CHOICES[1]:
        def_url = ask_ollama_url()
    elif answers[QS_OLLAMA_LOC_NAME] == QS_OLLAMA_LOC_CHOICES[0]:
        def_url = OLLAMA_HTTP_LOCALHOST_URL
    elif answers[QS_OLLAMA_LOC_NAME] == QS_OLLAMA_LOC_CHOICES[2]:
        print("To run the application, you need to provide the location of the ollama server.")
        raise typer.Exit()
    else:
        print("An error occurred while asking for the ollama location. Exiting...")
        raise typer.Exit()
    return def_url


def ask_ai_power():
    questions = [
        inquirer.List(QS_AI_POWER_NAME, message=QS_AI_POWER_MSG, choices=QS_AI_POWER_CHOICES, default=QS_AI_POWER_DEFAULT),
    ]
    answers = inquirer.prompt(questions)
    return answers[QS_AI_POWER_NAME]




# def ask_for_models_custom_path():
#     questions = [
#         inquirer.Path('custom_model_path',
#                       message="Where models should be stored?",
#                       path_type=inquirer.Path.DIRECTORY,
#                       ),
#     ]
#     answers = inquirer.prompt(questions)
#     write_config(CfgSection.AI.value, CfgList.AI_MODEL_CUSTOM_PATH.value, answers['custom_model_path'])
#     write_config(CfgSection.AI.value, CfgList.USE_CUSTOM_PATH.value, 'True')
#
#
# def ask_for_models_paths():
#     questions = [
#         inquirer.List('path_type',
#                       message="Where do you want to store the models?",
#                       choices=[dir_app_models, "Custom path"],
#                       ),
#     ]
#     answers = inquirer.prompt(questions)
#     if answers['path_type'] == dir_app_models:
#         write_config(CfgSection.AI.value, CfgList.USE_CUSTOM_PATH.value, 'False')
#     else:
#         ask_for_models_custom_path()

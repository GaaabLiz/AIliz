import json

import requests
import rich
import typer

from core.enum.ai_power import AiPower
from core.model.ollama_model import OllamaModel
from util.ai.ollamapi import check_ollama_status, get_installed_models
from core.util.cfgutils import read_config
from core.enum.cfglist import CfgList
from core.enum.cfgsection import CfgSection


def check_ollama():
    url_set = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL_SET.value, True)
    if url_set is False:
        print("Ollama url was not set. Please re-run the application with init command.")
        raise typer.Exit()
    print("Checking ollama server status...")
    url = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value)
    response = check_ollama_status(url)
    if response.is_successful():
        print("Ollama server is running.")
    else:
        error = response.get_error()
        rich.print("Ollama server is not running or some error occurred: " + "[red]" + error + "[/red]")
        print("Please check the server and try again.")
        raise typer.Exit()


def download_models_list(ollama_url: str) -> list[OllamaModel]:
    net_res = get_installed_models(ollama_url)
    if net_res.is_successful():
        data = json.loads(net_res.response.text)
        models = [OllamaModel(**model) for model in data['models']]
        return models
    else:
        error = net_res.get_error()
        print("Error while fetching models: " + "[red]" + error + "[/red]")
        raise typer.Exit()


def is_model_installed(model_name: str, actual_list: list[OllamaModel]) -> bool:
    for model in actual_list:
        if model.name == model_name:
            return True
    return False


def check_required_model(name: str):
    pass


def get_ai_power_model_list(ai_power: AiPower) -> list[str]:
    if ai_power == AiPower.HIGH.value:
        return ['llava:13b', 'llava:13b']
    elif ai_power == AiPower.MEDIUM.value:
        return ['llava:13b', 'llama3:latest']
    else:
        return ["llava:7b"]


def download_required_models(ai_power: AiPower, actual_list: list[OllamaModel]):
    required_models = get_ai_power_model_list(ai_power)
    for model in required_models:
        print("Checking if model " + model + " is installed in ollama...")
        if not is_model_installed(model, actual_list):
            print("Downloading model: ", model)
            # download_model(model)
        else:
            rich.print("Model [bold blue]" + model + "[/bold blue] is already installed.")


def download_model(ollama_url: str, model_name: str):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "name": model_name,
        "stream": True
    }

    response = requests.post(ollama_url, headers=headers, data=json.dumps(data), stream=True)

    total = None
    completed = 0

    for line in response.iter_lines():
        if line:
            status = json.loads(line.decode('utf-8'))
            if 'total' in status and 'completed' in status:
                total = status['total']
                completed = status['completed']
                percentage = (completed / total) * 100
                print(f"Downloading: {percentage:.2f}% complete")
            elif status.get("status") == "success":
                print("Download complete!")
                break
            else:
                print(f"Status: {status.get('status')}")

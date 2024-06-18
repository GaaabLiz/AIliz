import json

import typer

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
        print("Ollama server is not running or some error occurred: " + "[red]" + error + "[/red]")
        print("Please check the server and try again.")
        raise typer.Exit()


def download_models():
    ollama_url = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value)
    net_res = get_installed_models(ollama_url)
    if net_res.is_successful():
        data = json.loads(net_res.response.text)
        models = [OllamaModel(**model) for model in data['models']]
        for model in models:
            print(model)
    else:
        error = net_res.get_error()
        print("Error while fetching models: " + "[red]" + error + "[/red]")
        raise typer.Exit()
    pass

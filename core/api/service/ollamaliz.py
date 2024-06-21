import base64
import json

import requests
import rich
import typer

from core.api.dto.ollama_response import OllamaResponse
from core.enum.ai_power import AiPower
from core.api.dto.ollama_model import OllamaModel
from core.api.data.ollamapi import check_ollama_status, get_installed_models, llava_image
from core.model.ailiz_image import AilizImage
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


def scan_image_with_llava(
        file_path: str,
        power: AiPower,
) -> AilizImage | None:

    # Converting image to base64
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Reading prompt from resources
    with open("./resources/llava_prompt.txt", "r") as file:
        prompt = file.read()

    # Reading ollama url from config
    ollama_url = read_config(CfgSection.AI.value, CfgList.OLLAMA_URL.value)

    try:
        # Getting response from ollama
        response = llava_image(ollama_url, prompt, encoded_string, "llava:13b")

        # Checking ollama response and extracting data
        if response.is_successful():
            resp_text = response.text
            resp_text_json = json.loads(resp_text)
            resp_obj = OllamaResponse.from_json(resp_text_json)
            def_json = json.loads(resp_obj.response)
            print("Tags: ", def_json.get("tags", []))
            print("Description: ", def_json.get("description", ""))
            print("Text: ", def_json.get("text", ""))
            print("filename: ", def_json.get("filename", ""))
            elapsed_seconds = resp_obj.total_duration / 1_000_000_000
            rich.print("Elapsed time: " + "[bold blue]" + str(elapsed_seconds) + "[/bold blue]" + " seconds")
            image = AilizImage(file_path)
            image.set_ai_tags(def_json.get("tags", []))
            return image
        else:
            error = response.get_error()
            print("Error while connecting to ollama: " + "[red]" + error + "[/red]")
            return None
    except Exception as e:
        print("Error while analyzing current image: " + "[red]" + e + "[/red]")
        return None



from sys import exception

import requests

from network.netres import NetResponse
from network.netrestype import NetResponseType

OLLAMA_PORT = "11434"
OLLAMA_HTTP_LOCALHOST_URL = "http://localhost:" + OLLAMA_PORT


def check_ollama_status(url) -> NetResponse:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return NetResponse(response, NetResponseType.OK200)
        else:
            return NetResponse(response, NetResponseType.ERROR)
    except requests.ConnectionError as e:
        return NetResponse(None, NetResponseType.CONNECTION_ERROR, e)
    except requests.Timeout as e:
        return NetResponse(None, NetResponseType.TIMEOUT, e)
    except requests.RequestException as e:
        return NetResponse(None, NetResponseType.REQUEST_ERROR, e)


def check_ollama_status2(url) -> NetResponse:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return NetResponse(response, NetResponseType.OK200)
        else:
            return NetResponse(response, NetResponseType.ERROR)
    except Exception as e:
        return NetResponse(None, NetResponseType.CONNECTION_ERROR, e)

import requests

from util.network.netres import NetResponse
from util.network.netrestype import NetResponseType
from util.network.netutils import exec_net_call

OLLAMA_PORT = "11434"
OLLAMA_HTTP_LOCALHOST_URL = "http://localhost:" + OLLAMA_PORT


def check_ollama_status(url) -> NetResponse:
    return exec_net_call(url)


def get_installed_models(url):
    api_url = url + "/api/tags"
    return exec_net_call(api_url)


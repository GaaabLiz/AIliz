from util.network.netutils import exec_get

EAGLE_PORT = "41595"
EAGLE_URL = "http://localhost:" + EAGLE_PORT


def get_app_info():
    api_url = EAGLE_URL + "/api/application/info"
    return exec_get(api_url)

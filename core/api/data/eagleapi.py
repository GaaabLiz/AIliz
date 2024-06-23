from util.network.netutils import exec_get, exec_post

EAGLE_PORT = "41595"
EAGLE_URL = "http://localhost:" + EAGLE_PORT


def get_app_info():
    api_url = EAGLE_URL + "/api/application/info"
    return exec_get(api_url)


def add_image_from_path(
        path: str,
        name: str,
        tags: list[str],
        annotation: str,
        modification_time: float,
):
    api_url = EAGLE_URL + "/api/item/addFromPath"
    payload = {
        "path": path,
        "name": name,
        "tags": tags,
        "annotation": annotation,
        "modification_time": modification_time
    }
    return exec_post(api_url, payload, False)
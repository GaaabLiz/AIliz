import requests

from util.network.netres import NetResponse
from util.network.netrestype import NetResponseType


def exec_net_call(url: str,) -> NetResponse:
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

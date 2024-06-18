from requests import Response

from util.network.netrestype import NetResponseType


class NetResponse:

    def __init__(self, response: Response | None, response_type: NetResponseType, exception=None):
        self.response = response
        self.hasResponse = self.response is not None
        if self.hasResponse:
            self.code = self.response.status_code
        else:
            self.code = None
        self.type = response_type
        self.exception = exception

    def __str__(self):
        return ""

    def is_successful(self):
        return self.code == 200

    def is_error(self):
        return self.code != 200

    def get_error(self):
        if self.hasResponse:
            return "(" + str(self.code) + "): " + self.response.text
        else:
            pre = "(" + self.type.value + ") "
            if self.exception is not None:
                pre = pre + str(self.exception)
            return pre

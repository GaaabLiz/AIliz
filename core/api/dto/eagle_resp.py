
class EagleResp:

    def __init__(self, status, data):
        self.status = status
        self.data = data

    def is_successful(self):
        return self.status == "success"

    def __repr__(self):
        return f"EagleResp(status={self.status}, data={self.data})"

import json

import rich
import typer

from core.api.data import eagleapi
from core.api.dto.eagle_dto import EagleDto
from core.api.dto.eagle_status import EagleStatus


# def check_eagle() -> EagleStatus | None:
#     resp_obj = eagleapi.get_app_info()
#     if resp_obj.is_successful():
#         status = resp_obj.json.get("status")
#         if status == "success":
#             rich.print("Eagle instance is running.")
#             data_json = resp_obj.json.get("data")
#             eagle_obj = EagleStatus(
#                 version=data_json.get("version"),
#                 execPath=data_json.get("execPath", None),
#                 prereleaseVersion=data_json.get("prereleaseVersion"),
#                 buildVersion=data_json.get("buildVersion"),
#                 platform=data_json.get("platform")
#             )
#             # rich.print("Eagle running on path " + "[cyan]" + eagle_obj.execPath + "[/cyan].")
#             return eagle_obj
#         else:
#             rich.print("Eagle response status is not successful. Please check the eagle instance.")
#             return None
#     else:
#         error = resp_obj.get_error()
#         rich.print("Error while connecting to local eagle instance: " + "[red]" + error + "[/red]")
#         return None


def check_eagle() -> EagleDto | None:
    resp_obj = eagleapi.get_app_info()
    if resp_obj.is_successful():
        resp_json: str = resp_obj.json
        eagle_obj = EagleDto.from_dict(resp_json)
        if eagle_obj.status == "success":
            rich.print("Found Eagle instance version " + "[cyan]" + eagle_obj.data.version + "[/cyan].")
            rich.print("Eagle instance is running.")
            return eagle_obj
        else:
            rich.print("Eagle response status is not successful. Please check the eagle instance.")
            return None
    else:
        error = resp_obj.get_error()
        rich.print("Error while connecting to local eagle instance: " + "[red]" + error + "[/red]")
        return None

from typing import Any
from dataclasses import dataclass
import json


@dataclass
class Data:
    version: str
    prereleaseVersion: str
    buildVersion: str
    execPath: str
    platform: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        _version = str(obj.get("version"))
        _prereleaseVersion = str(obj.get("prereleaseVersion"))
        _buildVersion = str(obj.get("buildVersion"))
        _execPath = str(obj.get("execPath"))
        _platform = str(obj.get("platform"))
        return Data(_version, _prereleaseVersion, _buildVersion, _execPath, _platform)


@dataclass
class EagleDto:
    status: str
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'EagleDto':
        _status = str(obj.get("status"))
        _data = Data.from_dict(obj.get("data"))
        return EagleDto(_status, _data)
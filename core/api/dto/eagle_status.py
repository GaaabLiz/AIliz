
class EagleStatus:
    def __init__(self, version, prereleaseVersion, buildVersion, execPath, platform):
        self.version = version
        self.prereleaseVersion = prereleaseVersion
        self.buildVersion = buildVersion
        self.execPath = execPath
        self.platform = platform

    def __repr__(self):
        return (f"EagleData(version={self.version}, prereleaseVersion={self.prereleaseVersion}, "
                f"buildVersion={self.buildVersion}, execPath={self.execPath}, platform={self.platform})")
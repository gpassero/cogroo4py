import java.util
import typing



class ParonymList:
    def __init__(self): ...
    def getParonymsMap(self) -> java.util.Map[str, str]: ...
    def parseConfiguration(self) -> java.util.Map[str, str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.paronym")``.

    ParonymList: typing.Type[ParonymList]

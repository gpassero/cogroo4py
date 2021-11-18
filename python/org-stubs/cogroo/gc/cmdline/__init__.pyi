import java.util
import org.cogroo.gc.cmdline.dictionary
import org.cogroo.gc.cmdline.grammarchecker
import typing



class CLI:
    CMD: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def getToolNames() -> java.util.Set[str]: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class EndUserCLI:
    CMD: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def getToolNames() -> java.util.Set[str]: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.gc.cmdline")``.

    CLI: typing.Type[CLI]
    EndUserCLI: typing.Type[EndUserCLI]
    dictionary: org.cogroo.gc.cmdline.dictionary.__module_protocol__
    grammarchecker: org.cogroo.gc.cmdline.grammarchecker.__module_protocol__

import java.util
import org.cogroo.cmdline.dictionary
import org.cogroo.cmdline.featurizer
import typing



class CLI:
    CMD: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def getToolNames() -> java.util.Set[str]: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.cmdline")``.

    CLI: typing.Type[CLI]
    dictionary: org.cogroo.cmdline.dictionary.__module_protocol__
    featurizer: org.cogroo.cmdline.featurizer.__module_protocol__

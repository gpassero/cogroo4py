import opennlp.tools.cmdline
import typing



class AbbreviationDictionaryBuilderTool(opennlp.tools.cmdline.BasicCmdLineTool):
    def __init__(self): ...
    def getHelp(self) -> str: ...
    def getShortDescription(self) -> str: ...
    def run(self, stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.cmdline.dictionary")``.

    AbbreviationDictionaryBuilderTool: typing.Type[AbbreviationDictionaryBuilderTool]

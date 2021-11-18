import java.util
import org.cogroo.entities
import org.cogroo.tools.checker
import org.cogroo.tools.checker.rules.dictionary
import typing



class UIMAChecker(org.cogroo.tools.checker.AbstractTypedChecker):
    def __init__(self, cogrooTagDictionary: org.cogroo.tools.checker.rules.dictionary.CogrooTagDictionary): ...
    def check(self, sentence: org.cogroo.entities.Sentence) -> java.util.List[org.cogroo.entities.Mistake]: ...
    def getIdPrefix(self) -> str: ...
    def getPriority(self) -> int: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.ruta.checker")``.

    UIMAChecker: typing.Type[UIMAChecker]

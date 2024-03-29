import java.util
import org.cogroo.analyzer
import org.cogroo.entities
import org.cogroo.text.impl
import org.cogroo.tools.checker
import typing



class Categories:
    def __init__(self): ...
    @staticmethod
    def getCat(string: str) -> str: ...
    @staticmethod
    def getCategories() -> java.util.Set[str]: ...
    @staticmethod
    def getCategoryDescription(string: str) -> str: ...
    @staticmethod
    def getRules() -> java.util.Set[str]: ...
    @staticmethod
    def isCategoryImplemented(string: str) -> bool: ...
    @staticmethod
    def printCategoriesByRules() -> None: ...

class CheckAnalyzer:
    def analyze(self, checkDocument: 'CheckDocument') -> None: ...

class CheckDocument(org.cogroo.text.impl.DocumentImpl):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getMistakes(self) -> java.util.List[org.cogroo.entities.Mistake]: ...
    def getMistakesAsString(self) -> str: ...
    def getSentencesLegacy(self) -> java.util.List[org.cogroo.entities.Sentence]: ...
    def setMistakes(self, list: java.util.List[org.cogroo.entities.Mistake]) -> None: ...
    def setSentencesLegacy(self, list: java.util.List[org.cogroo.entities.Sentence]) -> None: ...
    def toString(self) -> str: ...

class GrammarChecker(CheckAnalyzer):
    @typing.overload
    def __init__(self, analyzer: org.cogroo.analyzer.Analyzer): ...
    @typing.overload
    def __init__(self, analyzer: org.cogroo.analyzer.Analyzer, boolean: bool, longArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, analyzer: org.cogroo.analyzer.Analyzer, string: str): ...
    @typing.overload
    def analyze(self, checkDocument: CheckDocument) -> None: ...
    @typing.overload
    def analyze(self, checkDocument: CheckDocument, boolean: bool) -> None: ...
    def getRuleDefinitions(self) -> java.util.Set[org.cogroo.tools.checker.RuleDefinition]: ...
    def ignoreRule(self, string: str) -> None: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def resetIgnoredRules(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.checker")``.

    Categories: typing.Type[Categories]
    CheckAnalyzer: typing.Type[CheckAnalyzer]
    CheckDocument: typing.Type[CheckDocument]
    GrammarChecker: typing.Type[GrammarChecker]

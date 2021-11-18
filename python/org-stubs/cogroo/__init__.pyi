import java.util
import opennlp.tools.chunker
import opennlp.tools.formats.ad
import opennlp.tools.namefind
import opennlp.tools.postag
import opennlp.tools.sentdetect
import opennlp.tools.tokenize
import org.cogroo.analyzer
import org.cogroo.checker
import org.cogroo.cmdline
import org.cogroo.config
import org.cogroo.dictionary
import org.cogroo.entities
import org.cogroo.errorreport
import org.cogroo.exceptions
import org.cogroo.formats
import org.cogroo.gc
import org.cogroo.interpreters
import org.cogroo.ruta
import org.cogroo.text
import org.cogroo.tools
import org.cogroo.util
import typing



class CLI:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class ContractionUtility(opennlp.tools.formats.ad.PortugueseContractionUtility):
    def __init__(self): ...
    @staticmethod
    def expand(string: str) -> typing.List[str]: ...
    @staticmethod
    def getContractionSet() -> java.util.Set[str]: ...

class LanguageLoader:
    def getChunker(self) -> opennlp.tools.chunker.Chunker: ...
    def getContractionFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getExpressionFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getPOSTagger(self) -> opennlp.tools.postag.POSTagger: ...
    def getProperNameFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getSentenceDetector(self) -> opennlp.tools.sentdetect.SentenceDetector: ...
    def getShallowParser(self) -> opennlp.tools.chunker.Chunker: ...
    def getTokenizer(self) -> opennlp.tools.tokenize.Tokenizer: ...

class RuntimeLanguageLoader(LanguageLoader):
    SENT: typing.ClassVar[str] = ...
    TOK: typing.ClassVar[str] = ...
    PROP: typing.ClassVar[str] = ...
    EXP: typing.ClassVar[str] = ...
    CON: typing.ClassVar[str] = ...
    POS: typing.ClassVar[str] = ...
    CHK: typing.ClassVar[str] = ...
    SP: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getChunker(self) -> opennlp.tools.chunker.Chunker: ...
    def getContractionFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getExpressionFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getPOSTagger(self) -> opennlp.tools.postag.POSTagger: ...
    def getProperNameFinder(self) -> opennlp.tools.namefind.TokenNameFinder: ...
    def getSentenceDetector(self) -> opennlp.tools.sentdetect.SentenceDetector: ...
    def getShallowParser(self) -> opennlp.tools.chunker.Chunker: ...
    def getTokenizer(self) -> opennlp.tools.tokenize.Tokenizer: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo")``.

    CLI: typing.Type[CLI]
    ContractionUtility: typing.Type[ContractionUtility]
    LanguageLoader: typing.Type[LanguageLoader]
    RuntimeLanguageLoader: typing.Type[RuntimeLanguageLoader]
    analyzer: org.cogroo.analyzer.__module_protocol__
    checker: org.cogroo.checker.__module_protocol__
    cmdline: org.cogroo.cmdline.__module_protocol__
    config: org.cogroo.config.__module_protocol__
    dictionary: org.cogroo.dictionary.__module_protocol__
    entities: org.cogroo.entities.__module_protocol__
    errorreport: org.cogroo.errorreport.__module_protocol__
    exceptions: org.cogroo.exceptions.__module_protocol__
    formats: org.cogroo.formats.__module_protocol__
    gc: org.cogroo.gc.__module_protocol__
    interpreters: org.cogroo.interpreters.__module_protocol__
    ruta: org.cogroo.ruta.__module_protocol__
    text: org.cogroo.text.__module_protocol__
    tools: org.cogroo.tools.__module_protocol__
    util: org.cogroo.util.__module_protocol__
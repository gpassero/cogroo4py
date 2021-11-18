import opennlp.tools.chunker
import opennlp.tools.util
import org.cogroo.tools.featurizer
import typing



class ShallowParserContextGenerator(opennlp.tools.chunker.ChunkerContextGenerator):
    def __init__(self): ...
    @typing.overload
    def getContext(self, int: int, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str], stringArray4: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str], objectArray: typing.List[typing.Any]) -> typing.List[str]: ...
    @staticmethod
    def phrasesAsSpanList(stringArray: typing.List[str]) -> typing.List[opennlp.tools.util.Span]: ...

class ShallowParserFactory(opennlp.tools.chunker.ChunkerFactory):
    def __init__(self): ...
    def getContextGenerator(self) -> opennlp.tools.chunker.ChunkerContextGenerator: ...
    def getSequenceValidator(self) -> opennlp.tools.util.SequenceValidator[opennlp.tools.util.TokenTag]: ...

class ShallowParserSequenceValidator(opennlp.tools.chunker.DefaultChunkerSequenceValidator):
    def __init__(self): ...
    @typing.overload
    def validSequence(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str], string2: str) -> bool: ...
    @typing.overload
    def validSequence(self, int: int, wordTagArray: typing.List[org.cogroo.tools.featurizer.WordTag], stringArray: typing.List[str], string2: str) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.shallowparser")``.

    ShallowParserContextGenerator: typing.Type[ShallowParserContextGenerator]
    ShallowParserFactory: typing.Type[ShallowParserFactory]
    ShallowParserSequenceValidator: typing.Type[ShallowParserSequenceValidator]
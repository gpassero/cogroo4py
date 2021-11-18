import opennlp.tools.chunker
import opennlp.tools.util
import typing



class HeadFinderContextGenerator(opennlp.tools.chunker.ChunkerContextGenerator):
    def __init__(self): ...
    @typing.overload
    def getContext(self, int: int, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str], stringArray4: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str]) -> typing.List[str]: ...
    @typing.overload
    def getContext(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str], objectArray: typing.List[typing.Any]) -> typing.List[str]: ...

class HeadFinderFactory(opennlp.tools.chunker.ChunkerFactory):
    def __init__(self): ...
    def getContextGenerator(self) -> opennlp.tools.chunker.ChunkerContextGenerator: ...
    def getSequenceValidator(self) -> opennlp.tools.util.SequenceValidator[opennlp.tools.util.TokenTag]: ...

class HeadFinderSequenceValidator(opennlp.tools.util.SequenceValidator[opennlp.tools.util.TokenTag]):
    def __init__(self): ...
    def validSequence(self, int: int, tokenTagArray: typing.List[opennlp.tools.util.TokenTag], stringArray: typing.List[str], string2: str) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.headfinder")``.

    HeadFinderContextGenerator: typing.Type[HeadFinderContextGenerator]
    HeadFinderFactory: typing.Type[HeadFinderFactory]
    HeadFinderSequenceValidator: typing.Type[HeadFinderSequenceValidator]

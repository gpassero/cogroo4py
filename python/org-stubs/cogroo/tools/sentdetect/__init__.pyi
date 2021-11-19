import java.lang
import java.util
import opennlp.tools.dictionary
import opennlp.tools.sentdetect
import typing



class PortuguesSentenceDetectorFactory(opennlp.tools.sentdetect.SentenceDetectorFactory):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool, dictionary: opennlp.tools.dictionary.Dictionary, charArray: typing.List[str]): ...
    def getSDContextGenerator(self) -> opennlp.tools.sentdetect.SDContextGenerator: ...

class PortugueseSDContextGenerator(opennlp.tools.sentdetect.SDContextGenerator):
    @typing.overload
    def __init__(self, charArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, set: java.util.Set[str], charArray: typing.List[str]): ...
    def getContext(self, charSequence: typing.Union[java.lang.CharSequence, str], int: int) -> typing.List[str]: ...
    def getSentenceContext(self, string: str, int: int) -> java.util.List[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.sentdetect")``.

    PortuguesSentenceDetectorFactory: typing.Type[PortuguesSentenceDetectorFactory]
    PortugueseSDContextGenerator: typing.Type[PortugueseSDContextGenerator]

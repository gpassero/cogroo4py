import java.util
import java.util.regex
import opennlp.tools.dictionary
import opennlp.tools.tokenize
import typing



class PortugueseTokenContextGenerator(opennlp.tools.tokenize.DefaultTokenContextGenerator):
    def __init__(self, set: java.util.Set[str]): ...

class PortugueseTokenizerFactory(opennlp.tools.tokenize.TokenizerFactory):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, dictionary: opennlp.tools.dictionary.Dictionary, boolean: bool, pattern: java.util.regex.Pattern): ...
    def getContextGenerator(self) -> opennlp.tools.tokenize.TokenContextGenerator: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.tokenizer")``.

    PortugueseTokenContextGenerator: typing.Type[PortugueseTokenContextGenerator]
    PortugueseTokenizerFactory: typing.Type[PortugueseTokenizerFactory]

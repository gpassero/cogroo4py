import java.util
import org.cogroo.entities.impl
import org.cogroo.interpreters
import org.cogroo.tools.checker.rules.model
import org.cogroo.util
import typing



class CogrooTagDictionary:
    def exists(self, string: str, boolean: bool) -> bool: ...
    def getInflectedPrimitive(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> typing.List[str]: ...
    @typing.overload
    def getPrimitive(self, string: str, morphologicalTag: org.cogroo.entities.impl.MorphologicalTag, boolean: bool) -> typing.List[str]: ...
    @typing.overload
    def getPrimitive(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> typing.List[str]: ...
    def getTagInterpreter(self) -> org.cogroo.interpreters.TagInterpreter: ...
    @typing.overload
    def getTags(self, string: str) -> typing.List[org.cogroo.entities.impl.MorphologicalTag]: ...
    @typing.overload
    def getTags(self, string: str, boolean: bool) -> typing.List[org.cogroo.entities.impl.MorphologicalTag]: ...
    def match(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> bool: ...

class LexicalDictionary:
    def getLemmasAndPosTagsForWord(self, string: str) -> java.util.List[org.cogroo.util.PairWordPOSTag]: ...
    def getPOSTagsForWord(self, string: str) -> java.util.List[str]: ...
    def getWordsAndPosTagsForLemma(self, string: str) -> java.util.List[org.cogroo.util.PairWordPOSTag]: ...
    def wordExists(self, string: str) -> bool: ...

class FSALexicalDictionary(LexicalDictionary):
    def __init__(self): ...
    def getLemmasAndPosTagsForWord(self, string: str) -> java.util.List[org.cogroo.util.PairWordPOSTag]: ...
    def getPOSTagsForWord(self, string: str) -> java.util.List[str]: ...
    def getWordsAndPosTagsForLemma(self, string: str) -> java.util.List[org.cogroo.util.PairWordPOSTag]: ...
    def wordExists(self, string: str) -> bool: ...

class TagDictionary(CogrooTagDictionary):
    def __init__(self, lexicalDictionary: LexicalDictionary, boolean: bool, tagInterpreter: org.cogroo.interpreters.TagInterpreter): ...
    def convertToTargetConvention(self, string: str) -> org.cogroo.entities.impl.MorphologicalTag: ...
    def exists(self, string: str, boolean: bool) -> bool: ...
    def getInflectedPrimitive(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> typing.List[str]: ...
    @typing.overload
    def getPrimitive(self, string: str, morphologicalTag: org.cogroo.entities.impl.MorphologicalTag, boolean: bool) -> typing.List[str]: ...
    @typing.overload
    def getPrimitive(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> typing.List[str]: ...
    def getTagInterpreter(self) -> org.cogroo.interpreters.TagInterpreter: ...
    @typing.overload
    def getTags(self, string: str) -> typing.List[org.cogroo.entities.impl.MorphologicalTag]: ...
    @typing.overload
    def getTags(self, string: str, boolean: bool) -> typing.List[org.cogroo.entities.impl.MorphologicalTag]: ...
    def match(self, string: str, tagMask: org.cogroo.tools.checker.rules.model.TagMask, boolean: bool) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.dictionary")``.

    CogrooTagDictionary: typing.Type[CogrooTagDictionary]
    FSALexicalDictionary: typing.Type[FSALexicalDictionary]
    LexicalDictionary: typing.Type[LexicalDictionary]
    TagDictionary: typing.Type[TagDictionary]

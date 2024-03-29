import java.lang
import java.util
import org.cogroo.entities
import org.cogroo.entities.impl
import org.cogroo.tools.checker.rules.model
import typing



class EqualsUtils:
    def __init__(self): ...
    @staticmethod
    def areBooleanEquals(boolean: bool, boolean2: bool) -> bool: ...
    @staticmethod
    def areCompositionEquals(composition: org.cogroo.tools.checker.rules.model.Composition, composition2: org.cogroo.tools.checker.rules.model.Composition) -> bool: ...
    @staticmethod
    def areElementEquals(element: org.cogroo.tools.checker.rules.model.Element, element2: org.cogroo.tools.checker.rules.model.Element) -> bool: ...
    @staticmethod
    def arePatternElementEquals(patternElement: org.cogroo.tools.checker.rules.model.PatternElement, patternElement2: org.cogroo.tools.checker.rules.model.PatternElement) -> bool: ...
    @staticmethod
    def areStringEquals(string: str, string2: str) -> bool: ...
    @staticmethod
    def areTagMaskEquals(tagMask: org.cogroo.tools.checker.rules.model.TagMask, tagMask2: org.cogroo.tools.checker.rules.model.TagMask) -> bool: ...

class MistakeComparator(java.util.Comparator[org.cogroo.entities.Mistake]):
    def __init__(self): ...
    def compare(self, mistake: org.cogroo.entities.Mistake, mistake2: org.cogroo.entities.Mistake) -> int: ...

class RuleUtils:
    def __init__(self): ...
    @staticmethod
    def completeMissingParts(tagMask: org.cogroo.tools.checker.rules.model.TagMask, morphologicalTag: org.cogroo.entities.impl.MorphologicalTag) -> None: ...
    @typing.overload
    @staticmethod
    def createTagMaskFromReference(reference: org.cogroo.tools.checker.rules.model.Reference, sentence: org.cogroo.entities.Sentence, int: int) -> org.cogroo.tools.checker.rules.model.TagMask: ...
    @typing.overload
    @staticmethod
    def createTagMaskFromReference(reference: org.cogroo.tools.checker.rules.model.Reference, morphologicalTag: org.cogroo.entities.impl.MorphologicalTag, chunkTag: org.cogroo.entities.impl.ChunkTag, syntacticTag: org.cogroo.entities.impl.SyntacticTag) -> org.cogroo.tools.checker.rules.model.TagMask: ...
    @staticmethod
    def createTagMaskFromReferenceSyntatic(reference: org.cogroo.tools.checker.rules.model.Reference, sentence: org.cogroo.entities.Sentence, int: int) -> org.cogroo.tools.checker.rules.model.TagMask: ...
    @staticmethod
    def getBoundariesAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getElementAsString(element: org.cogroo.tools.checker.rules.model.Element) -> str: ...
    @staticmethod
    def getGroupAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getMessageAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getMethodAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getPatternAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getPatternElementAsString(patternElement: org.cogroo.tools.checker.rules.model.PatternElement) -> str: ...
    @staticmethod
    def getRuleAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> java.util.Map['RuleUtils.RuleInfo', str]: ...
    @staticmethod
    def getShortMessageAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getSuggestionsAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def getTagMaskAsString(tagMask: org.cogroo.tools.checker.rules.model.TagMask) -> str: ...
    @staticmethod
    def getTagReferenceAsString(reference: org.cogroo.tools.checker.rules.model.Reference) -> str: ...
    @staticmethod
    def getTypeAsString(rule: org.cogroo.tools.checker.rules.model.Rule) -> str: ...
    @staticmethod
    def translate(string: str) -> str: ...
    @staticmethod
    def useCasedString(string: str, string2: str) -> str: ...
    class RuleInfo(java.lang.Enum['RuleUtils.RuleInfo']):
        METHOD: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        TYPE: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        GROUP: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        MESSAGE: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        SHORTMESSAGE: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        PATTERN: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        BOUNDARIES: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        SUGGESTIONS: typing.ClassVar['RuleUtils.RuleInfo'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'RuleUtils.RuleInfo': ...
        @staticmethod
        def values() -> typing.List['RuleUtils.RuleInfo']: ...

class RulesProperties:
    rootFolder: typing.ClassVar[str] = ...
    NUMBER_OF_TREES: typing.ClassVar[int] = ...
    GENERAL_TREE: typing.ClassVar[int] = ...
    PHRASE_LOCAL_TREE: typing.ClassVar[int] = ...
    SUBJECT_VERB_TREE: typing.ClassVar[int] = ...
    APPLY_LOCAL: typing.ClassVar[bool] = ...
    APPLY_PHRASE_LOCAL: typing.ClassVar[bool] = ...
    APPLY_SUBJECT_VERB: typing.ClassVar[bool] = ...
    PACKAGE: typing.ClassVar[str] = ...
    REREAD_FROM_SERIALIZED: typing.ClassVar[bool] = ...
    DATA_SOURCE: typing.ClassVar[str] = ...
    XML_FILE_ENCODING: typing.ClassVar[str] = ...
    CHECKERS: typing.ClassVar[typing.List[str]] = ...
    @staticmethod
    def getRulesFile() -> str: ...
    @staticmethod
    def getSchemaFile() -> str: ...
    @staticmethod
    def getSerializedTreesFile() -> str: ...
    @staticmethod
    def isReadFromSerialized() -> bool: ...
    @staticmethod
    def isRereadRules() -> bool: ...
    @staticmethod
    def setReadFromSerialized(boolean: bool) -> None: ...
    @staticmethod
    def setRereadRules(boolean: bool) -> None: ...
    @staticmethod
    def setRootFolder(string: str) -> None: ...
    @staticmethod
    def setRulesFile(string: str) -> None: ...
    @staticmethod
    def setSchemaFile(string: str) -> None: ...

class RulesTreesPrinter:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class RulesTreesSerializer:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    @staticmethod
    def serialize() -> None: ...
    @staticmethod
    def serializeIfAbsent() -> None: ...

class TagMaskUtils:
    def __init__(self): ...
    @staticmethod
    def clone(tagMask: org.cogroo.tools.checker.rules.model.TagMask) -> org.cogroo.tools.checker.rules.model.TagMask: ...
    @staticmethod
    def createTagMaskFromToken(token: org.cogroo.entities.Token, string: str) -> org.cogroo.tools.checker.rules.model.TagMask: ...
    @staticmethod
    def parse(string: str) -> org.cogroo.tools.checker.rules.model.TagMask: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.util")``.

    EqualsUtils: typing.Type[EqualsUtils]
    MistakeComparator: typing.Type[MistakeComparator]
    RuleUtils: typing.Type[RuleUtils]
    RulesProperties: typing.Type[RulesProperties]
    RulesTreesPrinter: typing.Type[RulesTreesPrinter]
    RulesTreesSerializer: typing.Type[RulesTreesSerializer]
    TagMaskUtils: typing.Type[TagMaskUtils]

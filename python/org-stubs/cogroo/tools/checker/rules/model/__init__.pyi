import java.io
import java.lang
import java.util
import javax.xml.datatype
import typing



class Boundaries(java.io.Serializable):
    def __init__(self): ...
    def getLower(self) -> int: ...
    def getUpper(self) -> int: ...
    def setLower(self, int: int) -> None: ...
    def setUpper(self, int: int) -> None: ...

class Composition(java.io.Serializable):
    def __init__(self): ...
    def getAnd(self) -> 'Operator': ...
    def getOr(self) -> 'Operator': ...
    def setAnd(self, operator: 'Operator') -> None: ...
    def setOr(self, operator: 'Operator') -> None: ...

class Element(java.io.Serializable):
    def __init__(self): ...
    def getMask(self) -> java.util.List['Mask']: ...
    def isNegated(self) -> bool: ...
    def setNegated(self, boolean: bool) -> None: ...

class Example(java.io.Serializable):
    def __init__(self): ...
    def getCorrect(self) -> str: ...
    def getIncorrect(self) -> str: ...
    def setCorrect(self, string: str) -> None: ...
    def setIncorrect(self, string: str) -> None: ...

class Mask(java.io.Serializable):
    def __init__(self): ...
    def getLexemeMask(self) -> str: ...
    def getOutOfBounds(self) -> str: ...
    def getPrimitiveMask(self) -> str: ...
    def getTagMask(self) -> 'TagMask': ...
    def getTagReference(self) -> 'Reference': ...
    def setLexemeMask(self, string: str) -> None: ...
    def setOutOfBounds(self, string: str) -> None: ...
    def setPrimitiveMask(self, string: str) -> None: ...
    def setTagMask(self, tagMask: 'TagMask') -> None: ...
    def setTagReference(self, reference: 'Reference') -> None: ...

class ModificationHistory(java.io.Serializable):
    def __init__(self): ...
    def getAuthor(self) -> str: ...
    def getComment(self) -> str: ...
    def getDate(self) -> javax.xml.datatype.XMLGregorianCalendar: ...
    def setAuthor(self, string: str) -> None: ...
    def setComment(self, string: str) -> None: ...
    def setDate(self, xMLGregorianCalendar: javax.xml.datatype.XMLGregorianCalendar) -> None: ...

class ObjectFactory:
    def __init__(self): ...
    def createBoundaries(self) -> Boundaries: ...
    def createComposition(self) -> Composition: ...
    def createElement(self) -> Element: ...
    def createExample(self) -> Example: ...
    def createMask(self) -> Mask: ...
    def createModificationHistory(self) -> ModificationHistory: ...
    def createOperator(self) -> 'Operator': ...
    def createPattern(self) -> 'Pattern': ...
    def createPatternElement(self) -> 'PatternElement': ...
    def createReference(self) -> 'Reference': ...
    def createRule(self) -> 'Rule': ...
    def createRules(self) -> 'Rules': ...
    def createSuggestion(self) -> 'Suggestion': ...
    def createSuggestionReplace(self) -> 'Suggestion.Replace': ...
    def createSuggestionReplaceMapping(self) -> 'Suggestion.ReplaceMapping': ...
    def createSuggestionSwap(self) -> 'Suggestion.Swap': ...
    def createTagMask(self) -> 'TagMask': ...
    def createTagReference(self) -> 'TagReference': ...

class Operator(java.io.Serializable):
    def __init__(self): ...
    def getPatternElement(self) -> java.util.List['PatternElement']: ...

class Pattern(java.io.Serializable):
    def __init__(self): ...
    def getPatternElement(self) -> java.util.List['PatternElement']: ...

class PatternElement(java.io.Serializable):
    def __init__(self): ...
    def getComposition(self) -> Composition: ...
    def getElement(self) -> Element: ...
    def isOptional(self) -> bool: ...
    def setComposition(self, composition: Composition) -> None: ...
    def setElement(self, element: Element) -> None: ...
    def setOptional(self, boolean: bool) -> None: ...

class Reference(java.io.Serializable):
    def __init__(self): ...
    def getIndex(self) -> int: ...
    def getProperty(self) -> java.util.List['Reference.Property']: ...
    def setIndex(self, long: int) -> None: ...
    class Property(java.lang.Enum['Reference.Property']):
        SYNTACTIC_FUNCTION: typing.ClassVar['Reference.Property'] = ...
        CHUNK_FUNCTION: typing.ClassVar['Reference.Property'] = ...
        CLASS: typing.ClassVar['Reference.Property'] = ...
        GENDER: typing.ClassVar['Reference.Property'] = ...
        NUMBER: typing.ClassVar['Reference.Property'] = ...
        CASE: typing.ClassVar['Reference.Property'] = ...
        PERSON: typing.ClassVar['Reference.Property'] = ...
        TENSE: typing.ClassVar['Reference.Property'] = ...
        MOOD: typing.ClassVar['Reference.Property'] = ...
        FINITENESS: typing.ClassVar['Reference.Property'] = ...
        PUNCTUATION: typing.ClassVar['Reference.Property'] = ...
        @staticmethod
        def fromValue(string: str) -> 'Reference.Property': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Reference.Property': ...
        @staticmethod
        def values() -> typing.List['Reference.Property']: ...

class Rule(java.io.Serializable):
    def __init__(self): ...
    def getBoundaries(self) -> Boundaries: ...
    def getExample(self) -> java.util.List[Example]: ...
    def getGroup(self) -> str: ...
    def getId(self) -> int: ...
    def getMessage(self) -> str: ...
    def getMethod(self) -> 'Rule.Method': ...
    def getModificationHistory(self) -> java.util.List[ModificationHistory]: ...
    def getPattern(self) -> Pattern: ...
    def getPriority(self) -> int: ...
    def getShortMessage(self) -> str: ...
    def getSuggestion(self) -> java.util.List['Suggestion']: ...
    def getType(self) -> str: ...
    def isActive(self) -> bool: ...
    def setActive(self, boolean: bool) -> None: ...
    def setBoundaries(self, boundaries: Boundaries) -> None: ...
    def setGroup(self, string: str) -> None: ...
    def setId(self, long: int) -> None: ...
    def setMessage(self, string: str) -> None: ...
    def setMethod(self, method: 'Rule.Method') -> None: ...
    def setPattern(self, pattern: Pattern) -> None: ...
    def setPriority(self, long: int) -> None: ...
    def setShortMessage(self, string: str) -> None: ...
    def setType(self, string: str) -> None: ...
    class Method(java.lang.Enum['Rule.Method']):
        GENERAL: typing.ClassVar['Rule.Method'] = ...
        PHRASE_LOCAL: typing.ClassVar['Rule.Method'] = ...
        SUBJECT_VERB: typing.ClassVar['Rule.Method'] = ...
        @staticmethod
        def fromValue(string: str) -> 'Rule.Method': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Rule.Method': ...
        @staticmethod
        def values() -> typing.List['Rule.Method']: ...

class Rules(java.io.Serializable):
    def __init__(self): ...
    def getRule(self) -> java.util.List[Rule]: ...

class Suggestion(java.io.Serializable):
    def __init__(self): ...
    def getReplace(self) -> java.util.List['Suggestion.Replace']: ...
    def getReplaceMapping(self) -> java.util.List['Suggestion.ReplaceMapping']: ...
    def getSuggestionAsString(self) -> str: ...
    def getSwap(self) -> java.util.List['Suggestion.Swap']: ...
    def setSuggestionAsString(self, string: str) -> None: ...
    class Replace(java.io.Serializable):
        def __init__(self): ...
        def getIndex(self) -> int: ...
        def getLexeme(self) -> str: ...
        def getReference(self) -> Reference: ...
        def getTagReference(self) -> 'TagReference': ...
        def setIndex(self, long: int) -> None: ...
        def setLexeme(self, string: str) -> None: ...
        def setReference(self, reference: Reference) -> None: ...
        def setTagReference(self, tagReference: 'TagReference') -> None: ...
    class ReplaceMapping(java.io.Serializable):
        def __init__(self): ...
        def getIndex(self) -> int: ...
        def getKey(self) -> str: ...
        def getValue(self) -> str: ...
        def setIndex(self, long: int) -> None: ...
        def setKey(self, string: str) -> None: ...
        def setValue(self, string: str) -> None: ...
    class Swap(java.io.Serializable):
        def __init__(self): ...
        def getA(self) -> int: ...
        def getB(self) -> int: ...
        def setA(self, long: int) -> None: ...
        def setB(self, long: int) -> None: ...

class TagMask(java.io.Serializable):
    def __init__(self): ...
    def getCase(self) -> 'TagMask.Case': ...
    def getChunkFunction(self) -> 'TagMask.ChunkFunction': ...
    def getClazz(self) -> 'TagMask.Class': ...
    def getGender(self) -> 'TagMask.Gender': ...
    def getMood(self) -> 'TagMask.Mood': ...
    def getNumber(self) -> 'TagMask.Number': ...
    def getPerson(self) -> 'TagMask.Person': ...
    def getPunctuation(self) -> 'TagMask.Punctuation': ...
    def getSyntacticFunction(self) -> 'TagMask.SyntacticFunction': ...
    def getTense(self) -> 'TagMask.Tense': ...
    def setCase(self, case: 'TagMask.Case') -> None: ...
    def setChunkFunction(self, chunkFunction: 'TagMask.ChunkFunction') -> None: ...
    def setClazz(self, class_: 'TagMask.Class') -> None: ...
    def setGender(self, gender: 'TagMask.Gender') -> None: ...
    def setMood(self, mood: 'TagMask.Mood') -> None: ...
    def setNumber(self, number: 'TagMask.Number') -> None: ...
    def setPerson(self, person: 'TagMask.Person') -> None: ...
    def setPunctuation(self, punctuation: 'TagMask.Punctuation') -> None: ...
    def setSyntacticFunction(self, syntacticFunction: 'TagMask.SyntacticFunction') -> None: ...
    def setTense(self, tense: 'TagMask.Tense') -> None: ...
    class Case(java.lang.Enum['TagMask.Case']):
        NOMINATIVE: typing.ClassVar['TagMask.Case'] = ...
        ACCUSATIVE: typing.ClassVar['TagMask.Case'] = ...
        DATIVE: typing.ClassVar['TagMask.Case'] = ...
        PREPOSITIVE: typing.ClassVar['TagMask.Case'] = ...
        ACCUSATIVE_DATIVE: typing.ClassVar['TagMask.Case'] = ...
        NOMINATIVE_PREPOSITIVE: typing.ClassVar['TagMask.Case'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Case': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Case': ...
        @staticmethod
        def values() -> typing.List['TagMask.Case']: ...
    class ChunkFunction(java.lang.Enum['TagMask.ChunkFunction']):
        BOUNDARY_NOUN_PHRASE: typing.ClassVar['TagMask.ChunkFunction'] = ...
        BOUNDARY_NOUN_PHRASE_MAIN: typing.ClassVar['TagMask.ChunkFunction'] = ...
        BOUNDARY_VERB_PHRASE_MAIN: typing.ClassVar['TagMask.ChunkFunction'] = ...
        INTERMEDIARY_NOUN_PHRASE: typing.ClassVar['TagMask.ChunkFunction'] = ...
        INTERMEDIARY_NOUN_PHRASE_MAIN: typing.ClassVar['TagMask.ChunkFunction'] = ...
        INTERMEDIARY_VERB_PHRASE: typing.ClassVar['TagMask.ChunkFunction'] = ...
        OTHER: typing.ClassVar['TagMask.ChunkFunction'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.ChunkFunction': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.ChunkFunction': ...
        @staticmethod
        def values() -> typing.List['TagMask.ChunkFunction']: ...
    class Class(java.lang.Enum['TagMask.Class']):
        NOUN: typing.ClassVar['TagMask.Class'] = ...
        NOUN_ADJECTIVE: typing.ClassVar['TagMask.Class'] = ...
        PROPER_NOUN: typing.ClassVar['TagMask.Class'] = ...
        PERSONAL_PRONOUN: typing.ClassVar['TagMask.Class'] = ...
        PRONOUN: typing.ClassVar['TagMask.Class'] = ...
        ARTICLE: typing.ClassVar['TagMask.Class'] = ...
        ADJECTIVE: typing.ClassVar['TagMask.Class'] = ...
        ADVERB: typing.ClassVar['TagMask.Class'] = ...
        INFINITIVE_VERB: typing.ClassVar['TagMask.Class'] = ...
        NUMERAL: typing.ClassVar['TagMask.Class'] = ...
        SUBORDINATING_CONJUNCTION: typing.ClassVar['TagMask.Class'] = ...
        COORDINATING_CONJUNCTION: typing.ClassVar['TagMask.Class'] = ...
        INTERJECTION: typing.ClassVar['TagMask.Class'] = ...
        PREFIX: typing.ClassVar['TagMask.Class'] = ...
        PREPOSITION: typing.ClassVar['TagMask.Class'] = ...
        PUNCTUATION_MARK: typing.ClassVar['TagMask.Class'] = ...
        FINITIVE_VERB: typing.ClassVar['TagMask.Class'] = ...
        PARTICIPLE_VERB: typing.ClassVar['TagMask.Class'] = ...
        GERUND_VERB: typing.ClassVar['TagMask.Class'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Class': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Class': ...
        @staticmethod
        def values() -> typing.List['TagMask.Class']: ...
    class Gender(java.lang.Enum['TagMask.Gender']):
        MALE: typing.ClassVar['TagMask.Gender'] = ...
        FEMALE: typing.ClassVar['TagMask.Gender'] = ...
        NEUTRAL: typing.ClassVar['TagMask.Gender'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Gender': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Gender': ...
        @staticmethod
        def values() -> typing.List['TagMask.Gender']: ...
    class Mood(java.lang.Enum['TagMask.Mood']):
        INDICATIVE: typing.ClassVar['TagMask.Mood'] = ...
        SUBJUNCTIVE: typing.ClassVar['TagMask.Mood'] = ...
        IMPERATIVE: typing.ClassVar['TagMask.Mood'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Mood': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Mood': ...
        @staticmethod
        def values() -> typing.List['TagMask.Mood']: ...
    class Number(java.lang.Enum['TagMask.Number']):
        SINGULAR: typing.ClassVar['TagMask.Number'] = ...
        PLURAL: typing.ClassVar['TagMask.Number'] = ...
        NEUTRAL: typing.ClassVar['TagMask.Number'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Number': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Number': ...
        @staticmethod
        def values() -> typing.List['TagMask.Number']: ...
    class Person(java.lang.Enum['TagMask.Person']):
        FIRST: typing.ClassVar['TagMask.Person'] = ...
        SECOND: typing.ClassVar['TagMask.Person'] = ...
        THIRD: typing.ClassVar['TagMask.Person'] = ...
        FIRST_THIRD: typing.ClassVar['TagMask.Person'] = ...
        NONE_FIRST_THIRD: typing.ClassVar['TagMask.Person'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Person': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Person': ...
        @staticmethod
        def values() -> typing.List['TagMask.Person']: ...
    class Punctuation(java.lang.Enum['TagMask.Punctuation']):
        ABS: typing.ClassVar['TagMask.Punctuation'] = ...
        NSEP: typing.ClassVar['TagMask.Punctuation'] = ...
        BIN: typing.ClassVar['TagMask.Punctuation'] = ...
        REL: typing.ClassVar['TagMask.Punctuation'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Punctuation': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Punctuation': ...
        @staticmethod
        def values() -> typing.List['TagMask.Punctuation']: ...
    class SyntacticFunction(java.lang.Enum['TagMask.SyntacticFunction']):
        SUBJECT: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        VERB: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        INDIRECT_OBJECT: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        DIRECT_OBJECT: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        SUBJECT_PREDICATIVE: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        IDENTIFYING_APPOSITION: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        ADVERBIAL_ADJUNCT: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        NONE: typing.ClassVar['TagMask.SyntacticFunction'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.SyntacticFunction': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.SyntacticFunction': ...
        @staticmethod
        def values() -> typing.List['TagMask.SyntacticFunction']: ...
    class Tense(java.lang.Enum['TagMask.Tense']):
        PRESENT: typing.ClassVar['TagMask.Tense'] = ...
        PRETERITO_IMPERFEITO: typing.ClassVar['TagMask.Tense'] = ...
        PRETERITO_PERFEITO: typing.ClassVar['TagMask.Tense'] = ...
        PRETERITO_MAIS_QUE_PERFEITO: typing.ClassVar['TagMask.Tense'] = ...
        FUTURE: typing.ClassVar['TagMask.Tense'] = ...
        CONDITIONAL: typing.ClassVar['TagMask.Tense'] = ...
        PRETERITO_PERFEITO_MAIS_QUE_PERFEITO: typing.ClassVar['TagMask.Tense'] = ...
        @staticmethod
        def fromValue(string: str) -> 'TagMask.Tense': ...
        def value(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'TagMask.Tense': ...
        @staticmethod
        def values() -> typing.List['TagMask.Tense']: ...

class TagReference(java.io.Serializable):
    def __init__(self): ...
    def getIndex(self) -> int: ...
    def getTagMask(self) -> TagMask: ...
    def setIndex(self, long: int) -> None: ...
    def setTagMask(self, tagMask: TagMask) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.model")``.

    Boundaries: typing.Type[Boundaries]
    Composition: typing.Type[Composition]
    Element: typing.Type[Element]
    Example: typing.Type[Example]
    Mask: typing.Type[Mask]
    ModificationHistory: typing.Type[ModificationHistory]
    ObjectFactory: typing.Type[ObjectFactory]
    Operator: typing.Type[Operator]
    Pattern: typing.Type[Pattern]
    PatternElement: typing.Type[PatternElement]
    Reference: typing.Type[Reference]
    Rule: typing.Type[Rule]
    Rules: typing.Type[Rules]
    Suggestion: typing.Type[Suggestion]
    TagMask: typing.Type[TagMask]
    TagReference: typing.Type[TagReference]

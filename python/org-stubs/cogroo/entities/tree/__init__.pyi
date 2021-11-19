import java.io
import org.cogroo.entities
import typing



class OldStyleModel:
    def __init__(self): ...
    @staticmethod
    def createTree(sentence: org.cogroo.entities.Sentence) -> 'Node': ...

class TreeElement:
    def __init__(self): ...
    def getLevel(self) -> int: ...
    def getMorphologicalTag(self) -> str: ...
    def getSyntacticTag(self) -> str: ...
    def setLevel(self, int: int) -> None: ...
    def setMorphologicalTag(self, string: str) -> None: ...
    def setSyntacticTag(self, string: str) -> None: ...
    def toSyntaxTree(self) -> str: ...

class Leaf(TreeElement):
    def __init__(self): ...
    def getFeatures(self) -> str: ...
    def getLemma(self) -> typing.List[str]: ...
    def getLexeme(self) -> str: ...
    def setFeatures(self, string: str) -> None: ...
    def setIsChunkHead(self, boolean: bool) -> None: ...
    def setLemma(self, stringArray: typing.List[str]) -> None: ...
    def setLexeme(self, string: str) -> None: ...
    def toString(self) -> str: ...
    def toSyntaxTree(self) -> str: ...

class Node(TreeElement, java.io.Serializable):
    def __init__(self): ...
    def addElement(self, treeElement: TreeElement) -> None: ...
    def getElements(self) -> typing.List[TreeElement]: ...
    def toString(self) -> str: ...
    def toSyntaxTree(self) -> str: ...

class TextModel:
    SPAN: typing.ClassVar[str] = ...
    SYNTACTIC_FUNCTION: typing.ClassVar[str] = ...
    CHUNK_FUNCTION: typing.ClassVar[str] = ...
    MORPH_FUNCTION: typing.ClassVar[str] = ...
    def __init__(self, sentence: org.cogroo.entities.Sentence): ...
    def getRoot(self) -> Node: ...
    class Chunk(Node):
        def __init__(self, textModel: 'TextModel'): ...
    class Sentence(Node):
        def __init__(self, textModel: 'TextModel'): ...
        def getSyntacticTag(self) -> str: ...
    class Text(Node):
        def __init__(self, textModel: 'TextModel'): ...
    class Token(Leaf):
        def __init__(self, textModel: 'TextModel'): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.entities.tree")``.

    Leaf: typing.Type[Leaf]
    Node: typing.Type[Node]
    OldStyleModel: typing.Type[OldStyleModel]
    TextModel: typing.Type[TextModel]
    TreeElement: typing.Type[TreeElement]

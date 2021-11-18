import java.util
import org.cogroo.entities
import org.cogroo.text
import typing



class RulePostValidator:
    def isValid(self, mistake: org.cogroo.entities.Mistake, document: org.cogroo.text.Document) -> bool: ...

class RuleValidatorUtil:
    def __init__(self): ...
    @staticmethod
    def getMistakeCoveredTokens(sentence: org.cogroo.text.Sentence, mistake: org.cogroo.entities.Mistake) -> java.util.List[org.cogroo.text.Token]: ...
    @staticmethod
    def getMistakeStartSentence(document: org.cogroo.text.Document, mistake: org.cogroo.entities.Mistake) -> org.cogroo.text.Sentence: ...

class Rule124Validator(RulePostValidator):
    def __init__(self): ...
    def isValid(self, mistake: org.cogroo.entities.Mistake, document: org.cogroo.text.Document) -> bool: ...

class RulePostValidatorProvider(RulePostValidator):
    def __init__(self): ...
    def isValid(self, mistake: org.cogroo.entities.Mistake, document: org.cogroo.text.Document) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.validator")``.

    Rule124Validator: typing.Type[Rule124Validator]
    RulePostValidator: typing.Type[RulePostValidator]
    RulePostValidatorProvider: typing.Type[RulePostValidatorProvider]
    RuleValidatorUtil: typing.Type[RuleValidatorUtil]

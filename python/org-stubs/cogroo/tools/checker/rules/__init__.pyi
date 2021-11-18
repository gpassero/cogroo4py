import java.io
import java.util
import jpype.protocol
import org.cogroo.checker
import org.cogroo.text
import org.cogroo.tools.checker.rules.applier
import org.cogroo.tools.checker.rules.dictionary
import org.cogroo.tools.checker.rules.exception
import org.cogroo.tools.checker.rules.model
import org.cogroo.tools.checker.rules.paronym
import org.cogroo.tools.checker.rules.util
import org.cogroo.tools.checker.rules.validator
import org.cogroo.tools.checker.rules.verbs
import typing



class CogrooHtml:
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], grammarChecker: org.cogroo.checker.GrammarChecker): ...
    def evaluate(self) -> None: ...
    def getAnalysisAsTable(self, sentence: org.cogroo.text.Sentence) -> java.util.List[java.util.List[str]]: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules")``.

    CogrooHtml: typing.Type[CogrooHtml]
    applier: org.cogroo.tools.checker.rules.applier.__module_protocol__
    dictionary: org.cogroo.tools.checker.rules.dictionary.__module_protocol__
    exception: org.cogroo.tools.checker.rules.exception.__module_protocol__
    model: org.cogroo.tools.checker.rules.model.__module_protocol__
    paronym: org.cogroo.tools.checker.rules.paronym.__module_protocol__
    util: org.cogroo.tools.checker.rules.util.__module_protocol__
    validator: org.cogroo.tools.checker.rules.validator.__module_protocol__
    verbs: org.cogroo.tools.checker.rules.verbs.__module_protocol__

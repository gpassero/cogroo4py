import java.nio.file
import java.util
import jpype.protocol
import org.cogroo.tools.checker
import typing



class RuleParser:
    @typing.overload
    @staticmethod
    def getRuleDefinitionList(string: str) -> java.util.Set[org.cogroo.tools.checker.RuleDefinition]: ...
    @typing.overload
    @staticmethod
    def getRuleDefinitionList(path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath]) -> java.util.Set[org.cogroo.tools.checker.RuleDefinition]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.ruta.tools")``.

    RuleParser: typing.Type[RuleParser]

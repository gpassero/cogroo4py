import java.lang
import typing



class RulesException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.tools.checker.rules.exception")``.

    RulesException: typing.Type[RulesException]

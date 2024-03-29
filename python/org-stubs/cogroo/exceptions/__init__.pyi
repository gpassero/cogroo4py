import java.lang
import java.util
import typing



class CommunityExceptionMessages:
    INTERNAL_ERROR: typing.ClassVar[str] = ...
    INVALID_USER: typing.ClassVar[str] = ...
    def __init__(self): ...

class ExceptionMessages:
    MODEL_FILE_NOT_FOUND: typing.ClassVar[str] = ...
    def __init__(self): ...

class InternationalizedException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getArguments(self) -> typing.List[typing.Any]: ...
    def getCause(self) -> java.lang.Throwable: ...
    @typing.overload
    def getLocalizedMessage(self) -> str: ...
    @typing.overload
    def getLocalizedMessage(self, locale: java.util.Locale) -> str: ...
    def getMessage(self) -> str: ...
    def getMessageKey(self) -> str: ...
    def getResourceBundleName(self) -> str: ...
    def hasMessageKey(self, string: str) -> bool: ...
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...

class InternationalizedRuntimeException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getArguments(self) -> typing.List[typing.Any]: ...
    def getCause(self) -> java.lang.Throwable: ...
    @typing.overload
    def getLocalizedMessage(self) -> str: ...
    @typing.overload
    def getLocalizedMessage(self, locale: java.util.Locale) -> str: ...
    def getMessage(self) -> str: ...
    def getMessageKey(self) -> str: ...
    def getResourceBundleName(self) -> str: ...
    def initCause(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...

class CogrooException(InternationalizedException):
    STANDARD_MESSAGE_CATALOG: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CogrooRuntimeException(InternationalizedRuntimeException):
    STANDARD_MESSAGE_CATALOG: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, string2: str, objectArray: typing.List[typing.Any], throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.exceptions")``.

    CogrooException: typing.Type[CogrooException]
    CogrooRuntimeException: typing.Type[CogrooRuntimeException]
    CommunityExceptionMessages: typing.Type[CommunityExceptionMessages]
    ExceptionMessages: typing.Type[ExceptionMessages]
    InternationalizedException: typing.Type[InternationalizedException]
    InternationalizedRuntimeException: typing.Type[InternationalizedRuntimeException]

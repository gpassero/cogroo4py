import java.io
import java.lang
import java.net
import jpype.protocol
import org.apache.log4j
import org.apache.log4j.spi
import typing



class SimpleSocketServer:
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class SocketAppender(org.apache.log4j.AppenderSkeleton):
    DEFAULT_PORT: typing.ClassVar[int] = ...
    ZONE: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @typing.overload
    def __init__(self, inetAddress: java.net.InetAddress, int: int): ...
    def activateOptions(self) -> None: ...
    def append(self, loggingEvent: org.apache.log4j.spi.LoggingEvent) -> None: ...
    def cleanUp(self) -> None: ...
    def close(self) -> None: ...
    def getApplication(self) -> str: ...
    def getLocationInfo(self) -> bool: ...
    def getPort(self) -> int: ...
    def getReconnectionDelay(self) -> int: ...
    def getRemoteHost(self) -> str: ...
    def isAdvertiseViaMulticastDNS(self) -> bool: ...
    def requiresLayout(self) -> bool: ...
    def setAdvertiseViaMulticastDNS(self, boolean: bool) -> None: ...
    def setApplication(self, string: str) -> None: ...
    def setLocationInfo(self, boolean: bool) -> None: ...
    def setPort(self, int: int) -> None: ...
    def setReconnectionDelay(self, int: int) -> None: ...
    def setRemoteHost(self, string: str) -> None: ...

class SocketHubAppender(org.apache.log4j.AppenderSkeleton):
    ZONE: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def activateOptions(self) -> None: ...
    def append(self, loggingEvent: org.apache.log4j.spi.LoggingEvent) -> None: ...
    def cleanUp(self) -> None: ...
    def close(self) -> None: ...
    def getApplication(self) -> str: ...
    def getBufferSize(self) -> int: ...
    def getLocationInfo(self) -> bool: ...
    def getPort(self) -> int: ...
    def isAdvertiseViaMulticastDNS(self) -> bool: ...
    def requiresLayout(self) -> bool: ...
    def setAdvertiseViaMulticastDNS(self, boolean: bool) -> None: ...
    def setApplication(self, string: str) -> None: ...
    def setBufferSize(self, int: int) -> None: ...
    def setLocationInfo(self, boolean: bool) -> None: ...
    def setPort(self, int: int) -> None: ...

class SocketNode(java.lang.Runnable):
    def __init__(self, socket: java.net.Socket, loggerRepository: org.apache.log4j.spi.LoggerRepository): ...
    def run(self) -> None: ...

class SocketServer:
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class SyslogAppender(org.apache.log4j.AppenderSkeleton):
    LOG_KERN: typing.ClassVar[int] = ...
    LOG_USER: typing.ClassVar[int] = ...
    LOG_MAIL: typing.ClassVar[int] = ...
    LOG_DAEMON: typing.ClassVar[int] = ...
    LOG_AUTH: typing.ClassVar[int] = ...
    LOG_SYSLOG: typing.ClassVar[int] = ...
    LOG_LPR: typing.ClassVar[int] = ...
    LOG_NEWS: typing.ClassVar[int] = ...
    LOG_UUCP: typing.ClassVar[int] = ...
    LOG_CRON: typing.ClassVar[int] = ...
    LOG_AUTHPRIV: typing.ClassVar[int] = ...
    LOG_FTP: typing.ClassVar[int] = ...
    LOG_LOCAL0: typing.ClassVar[int] = ...
    LOG_LOCAL1: typing.ClassVar[int] = ...
    LOG_LOCAL2: typing.ClassVar[int] = ...
    LOG_LOCAL3: typing.ClassVar[int] = ...
    LOG_LOCAL4: typing.ClassVar[int] = ...
    LOG_LOCAL5: typing.ClassVar[int] = ...
    LOG_LOCAL6: typing.ClassVar[int] = ...
    LOG_LOCAL7: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, layout: org.apache.log4j.Layout, int: int): ...
    @typing.overload
    def __init__(self, layout: org.apache.log4j.Layout, string: str, int: int): ...
    def activateOptions(self) -> None: ...
    def append(self, loggingEvent: org.apache.log4j.spi.LoggingEvent) -> None: ...
    def close(self) -> None: ...
    @typing.overload
    def getFacility(self) -> str: ...
    @typing.overload
    @staticmethod
    def getFacility(string: str) -> int: ...
    def getFacilityPrinting(self) -> bool: ...
    @staticmethod
    def getFacilityString(int: int) -> str: ...
    def getHeader(self) -> bool: ...
    def getSyslogHost(self) -> str: ...
    def requiresLayout(self) -> bool: ...
    def setFacility(self, string: str) -> None: ...
    def setFacilityPrinting(self, boolean: bool) -> None: ...
    def setHeader(self, boolean: bool) -> None: ...
    def setSyslogHost(self, string: str) -> None: ...

class TelnetAppender(org.apache.log4j.AppenderSkeleton):
    def __init__(self): ...
    def activateOptions(self) -> None: ...
    def close(self) -> None: ...
    def getPort(self) -> int: ...
    def requiresLayout(self) -> bool: ...
    def setPort(self, int: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.apache.log4j.net")``.

    SimpleSocketServer: typing.Type[SimpleSocketServer]
    SocketAppender: typing.Type[SocketAppender]
    SocketHubAppender: typing.Type[SocketHubAppender]
    SocketNode: typing.Type[SocketNode]
    SocketServer: typing.Type[SocketServer]
    SyslogAppender: typing.Type[SyslogAppender]
    TelnetAppender: typing.Type[TelnetAppender]
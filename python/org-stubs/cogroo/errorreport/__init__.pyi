import java.io
import org.cogroo.tools.errorreport.model
import typing



class ErrorReportAccess:
    def __init__(self): ...
    def getErrorReport(self, reader: java.io.Reader) -> org.cogroo.tools.errorreport.model.ErrorReport: ...
    @staticmethod
    def serialize(errorReport: org.cogroo.tools.errorreport.model.ErrorReport) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.errorreport")``.

    ErrorReportAccess: typing.Type[ErrorReportAccess]

import javax.swing
import typing



class Main(javax.swing.JFrame):
    PORT_PROP_NAME: typing.ClassVar[str] = ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.apache.log4j.chainsaw")``.

    Main: typing.Type[Main]

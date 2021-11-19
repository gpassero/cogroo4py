import java.io
import opennlp.tools.util.model
import typing



class ByteArraySerializer(opennlp.tools.util.model.ArtifactSerializer[typing.List[int]]):
    def __init__(self): ...
    def create(self, inputStream: java.io.InputStream) -> typing.List[int]: ...
    def serialize(self, byteArray: typing.List[int], outputStream: java.io.OutputStream) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.util.serializers")``.

    ByteArraySerializer: typing.Type[ByteArraySerializer]

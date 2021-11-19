import opennlp.tools.formats
import opennlp.tools.util
import org.cogroo.formats.ad
import org.cogroo.tools.featurizer
import typing



class FeatureSampleStreamFactory(opennlp.tools.formats.AbstractSampleStreamFactory[org.cogroo.tools.featurizer.FeatureSample]):
    def create(self, stringArray: typing.List[str]) -> opennlp.tools.util.ObjectStream[org.cogroo.tools.featurizer.FeatureSample]: ...
    @staticmethod
    def registerFactory() -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.formats")``.

    FeatureSampleStreamFactory: typing.Type[FeatureSampleStreamFactory]
    ad: org.cogroo.formats.ad.__module_protocol__

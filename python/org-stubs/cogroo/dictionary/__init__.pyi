import org.cogroo.dictionary.impl
import typing



class FeatureDictionary:
    def getFeatures(self, string: str, string2: str) -> typing.List[str]: ...

class LemmaDictionary:
    def getLemmas(self, string: str, string2: str) -> typing.List[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.cogroo.dictionary")``.

    FeatureDictionary: typing.Type[FeatureDictionary]
    LemmaDictionary: typing.Type[LemmaDictionary]
    impl: org.cogroo.dictionary.impl.__module_protocol__

import cogroo4py.jpype_config

import jpype.imports  # noqa
import java.util  # noqa
import org.cogroo  # noqa
import org.apache.log4j  # noqa

import stubgenj
stubgenj.generateJavaStubs([java.util, org.cogroo, org.apache.log4j], useStubsSuffix=True, outputDir='..')

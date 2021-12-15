import cogroo4py.jpype_config  # noqa

import jpype.imports  # noqa
import java.util  # noqa
import org.cogroo  # noqa

import stubgenj

current_path = cogroo4py.jpype_config.current_path


def generate_stubs(output_dir: str = current_path+'/..'):
    stubgenj.generateJavaStubs([java.util, org.cogroo], useStubsSuffix=True, outputDir=output_dir)


if __name__ == '__main__':
    generate_stubs()

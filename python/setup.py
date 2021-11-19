import os
from setuptools import setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


java_stubs_paths = package_files('java-stubs') + ['../py.typed']
jpype_stubs_paths = package_files('jpype-stubs') + ['../py.typed']
org_stubs_paths = package_files('org-stubs') + ['../py.typed']

setup(name='cogroo4py',
      version='0.4.1',
      description='Interface for accessing CoGrOO from Python scripts using jpype',
      author='Guilherme Passero',
      author_email='guilherme.passero0@gmail.com',
      url='https://github.com/kevencarneiro/cogroo4py',
      include_package_data=True,
      packages=['cogroo_interface', 'cogroo4py', 'java-stubs', 'jpype-stubs', 'org-stubs'],
      package_dir={
          'cogroo_interface': 'cogroo_interface',
          'cogroo4py': 'cogroo4py',
          'java-stubs': 'java-stubs',
          'jpype-stubs': 'jpype-stubs',
          'org-stubs': 'org-stubs'
      },
      
      package_data={
          'cogroo4py': ['jars/*.jar', '../../README.md'],
          'java-stubs': java_stubs_paths,
          'jpype-stubs': jpype_stubs_paths,
          'org-stubs': org_stubs_paths
      },
      install_requires=['JPype1==1.3.0', 'Deprecated==1.2.13'],
      extras_require={
          'dev': ['stubgenj==0.2.5']
      },
      keywords=['cogroo'],
      classifiers=[
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Natural Language :: Portuguese (Brazilian)',
          'Operating System :: OS Independent',
          'Topic :: Text Processing'
      ])

from setuptools import setup

setup(name='cogroo4py',
      version='0.4.0',
      description='Interface for accessing CoGrOO from Python scripts using py4j',
      author='Guilherme Passero',
      author_email='guilherme.passero0@gmail.com',
      url='https://github.com/kevencarneiro/cogroo4py',
      include_package_data=True,
      packages=['cogroo_interface', 'cogroo4py'],
      package_dir={'cogroo_interface': 'cogroo_interface'},
      package_data={'cogroo_interface': ['cogroo4py.jar'], 'cogroo4py': ['jars/*.jar']},
      # py_modules=['cogroo_interface'],
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

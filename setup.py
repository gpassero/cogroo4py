from setuptools import setup

setup(name='cogroo_interface',
      version='0.3.5',
      description='Interface for accessing CoGrOO from Python scripts using py4j',
      author='Guilherme Passero',
      author_email='guilherme.passero0@gmail.com',
      url='https://github.com/kevencarneiro/cogroo4py',
      include_package_data=True,
      packages=['cogroo_interface'],
      package_dir={'cogroo_interface': 'cogroo_interface'},
      package_data={'cogroo_interface': ['cogroo4py.jar']},
      py_modules=['cogroo_interface'],
      install_requires=['py4j', 'retry'],
      keywords=['cogroo'],
      classifiers=[
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Natural Language :: Portuguese (Brazilian)',
          'Operating System :: OS Independent',
          'Topic :: Text Processing'
      ])

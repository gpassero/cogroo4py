from distutils.core import setup
setup(name='cogroo_interface',
      version='0.3',      
	  description='An interface to use CoGrOO (a grammar checker for the Portuguese language) with Python using py4j',
	  author='Guilherme Passero',
	  author_email='guilherme.passero0@gmail.com',
	  url='https://github.com/gpassero/cogroo4py',
	  py_modules=['cogroo_interface'],
	  install_requires=['py4j'],
)
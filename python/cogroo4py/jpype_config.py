import os

import jpype
import jpype.imports
from jpype.types import *

current_path = os.path.dirname(os.path.realpath(__file__))
jars_path = os.path.join(current_path, 'jars', '*')

jpype.startJVM(classpath=[jars_path], convertStrings=True)

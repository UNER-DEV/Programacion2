import os
import sys

rutaUtils = os.path.abspath(__file__)           # Programacion2\TPX\modules\utils.py
rutaModules = os.path.dirname(rutaUtils)        # Programacion2\TPX\modules
rutaTP = os.path.dirname(rutaModules)           # Programacion2\TPX
rutaProgramacion2 = os.path.dirname(rutaTP)     # Programacion2
sys.path.append(rutaProgramacion2)              # Modifica la ruta actual

from utils.console import *
from utils.strings import *
from utils.numbers import *
from utils.list import *
from utils.calendar import *
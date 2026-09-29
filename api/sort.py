import sys
import os

# Agrega el directorio backend al sistema de rutas de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app # type: ignore
import sys
import os

# Agregamos la carpeta backend al PATH del sistema
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app import app # type: ignore
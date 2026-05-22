# esto es para que pytest encuentre el codigo que esta en la carpeta src
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from openpyxl import load_workbook
from pathlib import Path

class Exportador:

    def __init__(self):

        self.ruta = None
        self.libro = None
        self.hoja = None
        self.fila_actual = None
        self.abierto = False
    
    def abrir_excel(self, ruta):

        self.ruta = ruta

        self.libro = load_workbook(ruta)

        self.hoja = self.libro.active

        self.fila_actual = self.hoja.max_row + 1

        return True

    def crear_excel(self, ruta):
        self.ruta = ruta

    def guardar_resultado(
        self,
        trazabilidad,
        resultado,
        referencia,
        caja
    ):
        pass

import pandas as pd


class GestorExcel:

    def __init__(self):
        self.trazabilidades = set()

    def cargar_excel(self, ruta):

        df = pd.read_excel(ruta)

        self.trazabilidades = set(
            df.iloc[:, 0]
            .astype(str)
            .str.strip()
        )

        return len(self.trazabilidades)
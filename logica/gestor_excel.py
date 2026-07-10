import pandas as pd


class GestorExcel:

    def __init__(self):
        self.base_datos = set()

    def cargar_excel(self, ruta_archivo):

        df = pd.read_excel(ruta_archivo)

        self.base_datos = set(
            df.iloc[:,0]
            .astype(str)
            .str.strip()
    )

    return len(self.base_datos)
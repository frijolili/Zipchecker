class Comprobador:

    def __init__(self, base):

        self.base = base
        self.escaneadas = set()

    def comprobar(self, codigo):

        codigo = codigo.strip()
        if not codigo:
            return "VACIO"
            
        if codigo in self.escaneadas:
            return "DUPLICADA"

        if codigo in self.base:
            return "MALA"

        self.escaneadas.add(codigo)

        return "BUENA"
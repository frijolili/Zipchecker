from vista.ventana_principal import VentanaPrincipal
from logica.comprobador import Comprobador


base = {
    "111",
    "222",
    "333"
}


comprobador = Comprobador(base)

print(comprobador.comprobar("444"))
print(comprobador.comprobar("444"))
print(comprobador.comprobar("222"))
print(comprobador.comprobar("555"))


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
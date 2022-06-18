from model.Cuenta import Cuenta

class Venta:

    def __init__(self) -> None:
        super().__init__()
        self.ventas = []

    #funcion creada para agregar cosas al arreglo cuenta
    def agregar_venta(self, factura):
        self.ventas.append(factura)

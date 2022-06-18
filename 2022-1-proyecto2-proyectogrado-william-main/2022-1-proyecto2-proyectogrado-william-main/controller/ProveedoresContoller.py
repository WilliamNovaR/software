from model.Cuenta import Cuenta

class Provedores:

    def __init__(self) -> None:
        super().__init__()
        self.proveedores = []

    #funcion creada para agregar cosas al arreglo cuenta
    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def listaProveedores(self):
        return self.proveedores

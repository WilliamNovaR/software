#clase Acciones esta clase es la encargada de controlar las opciones e iconos del menu dependiendo del rol del usuario

class Keys:
    #se crean los dos atributos en los cuales es estableceran las acciones y los iconos del menus
    def __init__(self) -> None:
        super().__init__()
        self.crearCuenta = [0, 1, 2]
        self.agregarProducto = [0, 1, 2, 3, 4]
        self.consultar = [0, 1, 2, ""]
        self.compra = [0, 1, 2, "", "factura0", "cobro0", 3, 4, 5]
        self.configCaja = [0, 1, 2, 3, 4, 5, False]
        self.proveedores = 0


    def copraAumento(self):
        self.compra[0] += 6
        self.compra[1] += 6
        self.compra[2] += 6
        self.compra[6] += 6
        self.compra[7] += 6
        self.compra[8] += 6



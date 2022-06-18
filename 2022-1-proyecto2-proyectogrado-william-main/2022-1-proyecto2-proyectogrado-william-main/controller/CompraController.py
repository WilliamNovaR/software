#clase Acciones esta clase es la encargada de controlar las opciones e iconos del menu dependiendo del rol del usuario

class Factura:
    #se crean los dos atributos en los cuales es estableceran las acciones y los iconos del menus
    def __init__(self) -> None:
        super().__init__()
        self.items = []
        self.total = None
        self.hora = None

    def agregar_compra(self, obj):
        self.items.append(obj)

    def comprobarStock(self, seleccion, codigo, codigoBarras, ProductoController, cantidad):
        for buscar in self.items:
            if seleccion == buscar.nombre or codigo == buscar.codigo or codigoBarras == buscar.codigoBarras:
                for produc in ProductoController.productos:
                    if buscar.nombre == produc.nombre and buscar.cantidad + cantidad > produc.cantidad:
                        return 1
        return 0

    def aumentarCantidad(self, nuevoItem, cantidad):
        for k in self.items:
            if nuevoItem.nombre == k.nombre:
                k.cantidad += cantidad
                k.costo = k.cantidad * k.precio
                return 1
        return 0
    def reiniciarValores(self):
        self.items = []
        self.total = None
        self.hora = None

    def actualizarStock(self, ProductoController):
        for i in self.items:
            for j in ProductoController.productos:
                if i.nombre == j.nombre:
                    j.cantidad -= i.cantidad





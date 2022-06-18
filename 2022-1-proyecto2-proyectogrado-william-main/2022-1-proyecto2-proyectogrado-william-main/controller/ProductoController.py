import json
from model.Cuenta import Cuenta

#esta clase sirve para guardar las cuentas dentro de un arreglo de manera ordenada y hacer todos los calculos referentes a las Actas en el backend


class Productos:

    def __init__(self) -> None:
        super().__init__()
        self.productos = []


    #funcion creada para agregar cosas al arreglo cuenta
    def agregar_producto(self, acta_obj):
        self.productos.append(acta_obj)

    def comprobarExistencia(self, producto):
        for i in self.productos:
            if producto.nombre == i.nombre:
                return 1
            elif producto.codigo == i.codigo:
                return 2
            elif producto.codigoBarras == i.codigoBarras:
                return 3
        return 0

    def nombreProductosSistema(self):
        nombre = [""]
        for i in self.productos:
            nombre.append(i.nombre)
        return nombre

    def nombreProductosExistencia(self):
        nombre = [""]
        for i in self.productos:
            if i.cantidad > 0:
                nombre.append(i.nombre)
        return nombre

    def nombreProductosAgotados(self):
        nombre = [""]
        for i in self.productos:
            if i.cantidad == 0:
                nombre.append(i.nombre)
        return nombre

    def buscarProducto(self, seleccion, codigo, codigoBarras):
        for i in self.productos:
            if seleccion == i.nombre or codigo == i.codigo or codigoBarras == i.codigoBarras:
                return i
        return None

    def comprobarStock(self, seleccion, codigo, codigoBarras, cantidad):
        for product in self.productos:
            if (seleccion == product.nombre or codigo == product.codigo or codigoBarras == product.codigoBarras) and cantidad > product.cantidad:
                return 1
        return 0

    def agregarProducto(self, nuevoItem):
        for j in self.productos:
            if nuevoItem.nombre == j.nombre:
                nuevoItem.codigo = j.codigo
                nuevoItem.codigoBarras = j.codigoBarras
                nuevoItem.precio = j.precio

    def buscarIndexProducto(self, seleccion, codigo, codigoBarras):
        for i in range(len(self.productos)):
            if seleccion == self.productos[i].nombre or codigo == self.productos[i].codigo or codigoBarras == self.productos[i].codigoBarras:
                return i
        return -1

    def verificarDatos(self, seleccion, codigo, codigoBarras, index):
        for i in range(len(self.productos)):
            if i == index:
                continue
            if seleccion == self.productos[i].nombre or codigo == self.productos[i].codigo or codigoBarras == self.productos[i].codigoBarras:
                return 0
        return 1

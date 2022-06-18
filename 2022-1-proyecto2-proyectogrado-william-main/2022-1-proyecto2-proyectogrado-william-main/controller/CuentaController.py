import json
from model.Cuenta import Cuenta

#esta clase sirve para guardar las cuentas dentro de un arreglo de manera ordenada y hacer todos los calculos referentes a las Actas en el backend


class Cuentas:

    def __init__(self) -> None:
        super().__init__()
        self.cuentas = []
        dueno = Cuenta()
        dueno.tipo = "Dueño"
        dueno.usuario = "1"
        dueno.contrasena = "1"
        self.cuentas.append(dueno)

    #funcion creada para agregar cosas al arreglo cuenta
    def agregar_cuenta(self, acta_obj):
        self.cuentas.append(acta_obj)

    def comprobarExistencia(self, st, nueva_cuenta):
        for i in self.cuentas:
            if nueva_cuenta.usuario == i.usuario:
                st.error( "esta cuenta ya existe" )
                return True
        return False
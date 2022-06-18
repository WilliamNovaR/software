#clase Acciones esta clase es la encargada de controlar las opciones e iconos del menu dependiendo del rol del usuario

class Horarios:
    #se crean los dos atributos en los cuales es estableceran las acciones y los iconos del menus
    def __init__(self) -> None:
        super().__init__()
        self.horaApertura = "06"
        self.minutoApertura = "00"
        self.horaCierre = "22"
        self.minutoCierre = "00"
        self.dineroCaja = None
        self.baseDia = None
        self.estado = "Cerrado"
        self.registro = []
        self.registroPagos = []
        self.index = len(self.registro) - 1

    def validarDatos(self, hora, minutos, horaCierre, minutosCierre):
        horasAbiles = []
        minutosAbiles = []
        for i in range(24):
            horasAbiles.append(i)
        for j in range(60):
            minutosAbiles.append(j)
        for k in horasAbiles:
            if k == int(hora):
                break
            if str(k) == "23" and hora != "23":
                return 0
        for l in minutosAbiles:
            if l == int(minutos):
                break
            if str(l) == "59" and minutos != "59":
                return 0
        for n in horasAbiles:
            if n == int(horaCierre):
                break
            if str(n) == "23" and horaCierre != "23":
                return 0
        for m in minutosAbiles:
            if m == int(minutosCierre):
                break
            if str(m) == "59" and minutosCierre != "59":
                return 0
        return 1

    def agustarHoras(self, valor):
        if int(valor) < 10:
            for i in range(10):
                if valor == str(i):
                    return "0" + str(i)
        return valor

    def agregarRegistro(self, info):
        self.registro.append(info)

    def agregarRegistroPagos(self, pago):
        self.registroPagos.append(pago)


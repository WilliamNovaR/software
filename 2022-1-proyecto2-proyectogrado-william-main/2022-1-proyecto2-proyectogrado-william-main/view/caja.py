from model.DatosAbrirCerrar import DatoAbrirCerrar
from datetime import datetime


def configurarInicioCierreCaja(st, keyController, aperturaCierreController):
    st.header("Configurar inicio y cierres de caja")
    st.write(" ")
    st.subheader("Configurar inicio de caja")
    st.write(" ")
    st.write("Escribe la hora y el minuto en el que quieres que se pueda iniciar y/o cerrar caja en un formato de 24 horas")
    col1, col2 = st.columns([1, 1])
    with col1:
        hour = st.empty()
        hora = hour.text_input("Hora de inicio de caja", key=keyController.configCaja[0], value = aperturaCierreController.horaApertura)

    with col2:
        minutes = st.empty()
        minutos = minutes.text_input("Minuto de inicio de cada", key=keyController.configCaja[1], value = aperturaCierreController.minutoApertura)

    st.write("--------------------------------------------------")
    st.subheader("Configurar cierre de caja")
    col3, col4 = st.columns([1, 1])
    with col3:
        hourClose = st.empty()
        horaCierre = hourClose.text_input("Hora de cierre de caja", key=keyController.configCaja[2], value = aperturaCierreController.horaCierre)
    with col4:
        minutesClose = st.empty()
        minutosCierre = minutesClose.text_input("Minuto de cierre de cada", key=keyController.configCaja[3], value = aperturaCierreController.minutoCierre)
    st.write(" ")
    dayOpen = st.empty()
    diasAbrir = dayOpen.multiselect("Que dias quieres abrir?", ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"), key=keyController.configCaja[4])
    establecer = st.button("Establecer Horario")
    if establecer:
        if aperturaCierreController.validarDatos(hora, minutos, horaCierre, minutosCierre) == 0 or diasAbrir == []:
            st.error("Los campos no han sido llenados de manera correcta")
            return
        diasApertura = []
        for i in diasAbrir:
            if i == "Lunes":
                diasApertura.append("Monday")
            elif i == "Martes":
                diasApertura.append("Tuesday")
            elif i == "Miercoles":
                diasApertura.append("Wednesday")
            elif i == "Jueves":
                diasApertura.append("Thursday")
            elif i == "Viernes":
                diasApertura.append("Friday")
            elif i == "Sabado":
                diasApertura.append("Saturday")
            elif i == "Domindo":
                diasApertura.append("Sunday")

        aperturaCierreController.horaApertura = aperturaCierreController.agustarHoras(hora)
        aperturaCierreController.minutoApertura = aperturaCierreController.agustarHoras(minutos)
        aperturaCierreController.horaCierre = aperturaCierreController.agustarHoras(horaCierre)
        aperturaCierreController.minutoCierre = aperturaCierreController.agustarHoras(minutosCierre)
        aperturaCierreController.diasAbrir = diasApertura

        keyController.configCaja[0] += 6
        keyController.configCaja[1] += 6
        keyController.configCaja[2] += 6
        keyController.configCaja[3] += 6
        keyController.configCaja[4] += 6
        hour.text_input("Hora de inicio de caja", key=keyController.configCaja[0], value = aperturaCierreController.horaApertura)
        minutes.text_input("Minuto de inicio de cada", key=keyController.configCaja[1], value = aperturaCierreController.minutoApertura)
        hourClose.text_input("Hora de cierre de caja", key=keyController.configCaja[2],
                             value=aperturaCierreController.horaCierre)
        minutesClose.text_input("Minuto de cierre de cada", key=keyController.configCaja[3],
                                value=aperturaCierreController.minutoCierre)
        dayOpen.multiselect("Que dias quieres abrir?",
                            ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"), key=keyController.configCaja[4])
        st.success("Hora configurada exitosamente")
    if keyController.configCaja[6] == False:
        st.write("--------------------------------------------------------------")
        st.subheader("Establecer base caja")
        base = st.empty()
        baseCaja = base.number_input("Cual va a ser la base inicial de la caja:", min_value=0,
                                     key=keyController.configCaja[5])
        boton_baseCaja = st.button("Establecer base")
        if boton_baseCaja:
            aperturaCierreController.dineroCaja = baseCaja
            keyController.configCaja[6] = True
            st.success("Base de caja establecida")

def CerrarOAbrir(st, aperturaCierreController, cuentasController):
    if aperturaCierreController.estado == "Cerrado":
        iniciarCaja(st, aperturaCierreController, cuentasController)
    elif aperturaCierreController.estado == "Abierto":
        cerrarCaja(st, aperturaCierreController, cuentasController)

def iniciarCaja(st, aperturaCierreController, cuentasController):
    st.header("Iniciar caja")
    st.write(" ")
    st.write("El iniciar caja sirve para inicializar el sistema y poder empezar a usarlo y llevar registro de todas las ventas en el dia y poder hacer arqueo al final de la jornada laboral")
    nuevosDatos = DatoAbrirCerrar()
    user = st.empty()
    password = st.empty()
    usuario = user.text_input("Usuario:", key=23)
    contrasena = password.text_input("Contraseña:", type="password", key=7)
    flag = 0
    for i in cuentasController.cuentas:  # recorre el arreglo para saber si los datos digitados concuerdan con alguna cuenta creada
        if usuario == i.usuario and contrasena == i.contrasena:  # comprueba que el usuario y contraseña coicidan y esten creados
            flag = 1
            if st.button("Iniciar caja"):
                aperturaCierreController.estado = "Abierto"
                aperturaCierreController.baseDia = aperturaCierreController.dineroCaja
                nuevosDatos.pagos = 0
                nuevosDatos.basedia = aperturaCierreController.baseDia
                nuevosDatos.usuario = usuario
                nuevosDatos.tipo = i.tipo
                nuevosDatos.accion = "Abrir"
                fechaHora = datetime.now()
                nuevosDatos.fechaAbrir = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
                user.text_input("Usuario:", key=24)
                contrasena = password.text_input("Contraseña:", type="password", key=8)
                aperturaCierreController.agregarRegistro(nuevosDatos)
                continuarBotton = st.button("Continuar")
                st.success("Caja iniciada")


    if flag == 0:
        st.error("Datos no validos")  # en caso que la sesion no exista o no coicidan los datos muestra el error
        return

def cerrarCaja(st, aperturaCierreController, cuentasController):
    now = datetime.now()
    horaAceptada = -1
    minutoAceptado = 0
    if now.hour == int(aperturaCierreController.horaCierre):
        horaAceptada = 0
    elif now.hour > int(aperturaCierreController.horaCierre):
        horaAceptada = 1
        minutoAceptado = 1
    if horaAceptada == 0:
        if now.minute >= int(aperturaCierreController.minutoCierre):
            minutoAceptado = 1
    st.header("Cerrar caja")
    st.write(" ")
    st.write(
        "El iniciar caja sirve para inicializar el sistema y poder empezar a usarlo y llevar registro de todas las ventas en el dia y poder hacer arqueo al final de la jornada laboral")
    if minutoAceptado != 1:
        st.error("Todavia no es hora de cierre")
        return
    user = st.empty()
    password = st.empty()
    usuario = user.text_input("Usuario:", key=23)
    contrasena = password.text_input("Contraseña:", type="password", key=7)
    flag = 0
    for i in cuentasController.cuentas:  # recorre el arreglo para saber si los datos digitados concuerdan con alguna cuenta creada
        if usuario == i.usuario and contrasena == i.contrasena:  # comprueba que el usuario y contraseña coicidan y esten creados
            flag = 1
            cerrarCajaBoton = st.button("Cerrar caja")
            if cerrarCajaBoton:
                aperturaCierreController.estado = "Cerrado"
                aperturaCierreController.baseDia = aperturaCierreController.dineroCaja
                aperturaCierreController.registro[aperturaCierreController.index].usuarioCierre = i.usuario
                aperturaCierreController.registro[aperturaCierreController.index].tipoCierre = i.tipo
                aperturaCierreController.registro[aperturaCierreController.index].accion = "Cerrar"
                fechaHora = datetime.now()
                aperturaCierreController.registro[aperturaCierreController.index].fechaCerrar = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
                aperturaCierreController.registro[aperturaCierreController.index].ventasDia = aperturaCierreController.dineroCaja - aperturaCierreController.baseDia
                st.subheader("Ventas del día:")
                st.write("{0:.2f}".format(aperturaCierreController.registro[aperturaCierreController.index].ventasDia))
                st.subheader("Pagos del día:")
                st.write("{0:.2f}".format(aperturaCierreController.registro[aperturaCierreController.index].pagos))
                st.subheader("Dinero en caja:")
                st.write("{0:.2f}".format(aperturaCierreController.dineroCaja))

                continuarBoton = st.button("Continuar")
                st.success("Caja Cerrada")
                user.text_input("Usuario:", key=24, value="")
                contrasena = password.text_input("Contraseña:", type="password", key=8, value = "")

    if flag == 0:
        st.error("Datos no validos")  # en caso que la sesion no exista o no coicidan los datos muestra el error
        return

def pagoFacturas(st, aperturaCierreController, provedoresController):
    st.header("Registro de pago de facturas")
    if aperturaCierreController.estado == "Cerrado":
        st.error("Para pagar facturas primero debes iniciar la caja")
        return
    listaProveedores = provedoresController.listaProveedores()
    datosPago = {"Provedor": None, "Pago": None, "Foto factura": None, "Fecha": None}
    provedor = st.empty()
    pay = st.empty()
    img = st.empty()
    nombreProveedor = provedor.selectbox("Proveedor", listaProveedores)
    pago = pay.number_input("Valor a pagar", min_value= 0)
    fotoFactura = img.file_uploader("carga imagen de factura")
    pagarBoton = st.button("Pagar")
    if pagarBoton:
        aperturaCierreController.dineroCaja -= pago
        aperturaCierreController.registro[aperturaCierreController.index].pagos += pago
        datosPago["Provedor"] = nombreProveedor
        datosPago["Pago"] = pago
        datosPago["Foto factura"] = fotoFactura
        fechaHora = datetime.now()
        datosPago["Fecha"] = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
        aperturaCierreController.agregarRegistroPagos(datosPago)
        st.success("Pago de factura exitoso")
        provedor.selectbox("Proveedor", (1, 2), key = 2131)
        pay.number_input("Valor a pagar", min_value=0,  key = 213231)

from model.Cuenta import Cuenta

def iniciar_sesion( st, cuentasController, accionesController):
    st.header("Iniciar sesion")
    #se leen los datos para iniciar sesion
    usuario = st.text_input( "Usuario:", key = 23 )
    contrasena = st.text_input( "Contraseña:", type="password"  , key = 7 )
    flag = 0
    col1, col2 = st.columns([0.2, 1]) #se crean columnas para que ambos botones queden juntos
    for i in cuentasController.cuentas: #recorre el arreglo para saber si los datos digitados concuerdan con alguna cuenta creada
        if usuario == i.usuario and contrasena == i.contrasena: #comprueba que el usuario y contraseña coicidan y esten creados
            flag = 1
            with col1:
                if st.button( "Iniciar sesion" ):
                    accionesController.menu_acciones(i.tipo)  # establece segun el tipo de cuenta que acciones se dentran disponibles en el menu
                    with col2:
                        if st.button( "Entrar" ):
                            return
    if flag == 0:
        st.error("Datos no validos")  # en caso que la sesion no exista o no coicidan los datos muestra el error
        return

def crear_cuenta(st, cuentaController, keyController):
    st.header( "Crear cuenta" )
    nueva_cuenta = Cuenta()
    user = st.empty()
    password = st.empty()
    type = st.empty()
    #se leen los datos que va a tener la cuenta y se guardan dentro de nueva_cuenta
    nueva_cuenta.usuario = user.text_input( "Usuario:", value = '', key = keyController.crearCuenta[0] )
    nueva_cuenta.contrasena = password.text_input( "Contraseña:", value= '', key = keyController.crearCuenta[1]  )
    tipo = type.selectbox( "Que tipo de cuenta quieres crear?", ('Dueño', 'Administrador', 'Trabajador'), key = keyController.crearCuenta[2] )
    crear = st.button( "Crear" )
    if crear:
        #comprueba que no se creen cuentas con usuarios ya creados
        existencia = cuentaController.comprobarExistencia(st, nueva_cuenta)
        if existencia == 1:
            return
        #se guarda la cuenta dentro de cuentaController y se carga la cuenta en el .json
        nueva_cuenta.tipo = tipo
        cuentaController.agregar_cuenta( nueva_cuenta )
        st.success( "Cuenta creada" )
        keyController.crearCuenta[0] += 3
        keyController.crearCuenta[1] += 3
        keyController.crearCuenta[2] += 3
        user.text_input("Usuario:", value='', key=keyController.crearCuenta[0])
        password.text_input("Contraseña:", value='', key=keyController.crearCuenta[1])
        type.selectbox("Que tipo de cuenta quieres crear?", ('Dueño', 'Administrador', 'Trabajador'), key = keyController.crearCuenta[2] )

def crear_cuenta_usuarios(st, cuentaController, keyController):
    st.header( "Crear cuenta" )
    nueva_cuenta = Cuenta()
    user = st.empty()
    password = st.empty()
    #se leen los datos que va a tener la cuenta y se guardan dentro de nueva_cuenta
    nueva_cuenta.usuario = user.text_input( "Usuario:", value = '', key = keyController.crearCuenta[0] )
    nueva_cuenta.contrasena = password.text_input( "Contraseña:", value= '', key = keyController.crearCuenta[1]  )
    crear = st.button( "Crear" )
    if crear:
        #comprueba que no se creen cuentas con usuarios ya creados
        existencia = cuentaController.comprobarExistencia(st, nueva_cuenta)
        if existencia == 1:
            return
        #se guarda la cuenta dentro de cuentaController y se carga la cuenta en el .json
        nueva_cuenta.tipo = "Cliente"
        cuentaController.agregar_cuenta( nueva_cuenta )
        st.success( "Cuenta creada" )
        keyController.crearCuenta[0] += 3
        keyController.crearCuenta[1] += 3
        user.text_input("Usuario:", value='', key=keyController.crearCuenta[0])
        password.text_input("Contraseña:", value='', key=keyController.crearCuenta[1])

def cerrar_sesion(st, accionesController):
    st.subheader( "Cerrar sesion" )
    col1, col2 = st.columns([0.2, 1]) #culumans para tener los botones de Cerrar sison y Salir juntos
    with col1:
        logout = st.button("Cerrar sesion")
        if logout:
            accionesController.acciones = ['sesion', 'Contacto Soporte'] #se guardan las opciones de menu que se tienen cuando no se esta logueado
            accionesController.iconos = [ 'person-check'] #se guardan los iconos de estas opciones de menu
            with col2:
                st.button("Salir")
                return












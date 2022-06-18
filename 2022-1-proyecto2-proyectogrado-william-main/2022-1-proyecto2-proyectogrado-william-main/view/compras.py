from model.Compra import Compra
from datetime import datetime

def registrarCompra( st, ProductoController, keyController, CompraController, VentaController, aperturaCierreController ):
    st.header("Registrar Compra")
    if aperturaCierreController.estado == "Cerrado":
        st.error("Para registrar compras primero debes iniciar la caja")
        return
    col1, col2, col3 = st.columns([1, 0.1, 1])
    lista = ProductoController.nombreProductosExistencia()
    productoEncontrado = 0
    productoEnCarrito = 0
    clickBorrar = 0
    cancelarCompra = None
    checkearStock = 0

    with col1:
        st.subheader( "Registrar Producto" )
        name = st.empty()
        code = st.empty()
        codeBarr = st.empty()
        seleccion = name.selectbox( "Nombre producto:", lista, key = keyController.compra[0] )
        codigo = code.text_input( "Codigo Producto:", key = keyController.compra[1] )
        codigoBarras = codeBarr.text_input( "Codigo de barras Producto:", key = keyController.compra[2] )

        if seleccion != "" and keyController.compra[3] != "s":
            keyController.compra[1] += 6
            keyController.compra[2] += 6
            codigo = code.text_input("Codigo Producto:",
                                      key=keyController.compra[1], value="")
            codigoBarras = codeBarr.text_input("Codigo de barras Producto:",
                                                key=keyController.compra[2], value="")
            keyController.compra[3] = "s"
        if codigo != "" and keyController.compra[3] != "c":
            keyController.compra[0] += 6
            keyController.compra[2] += 6
            seleccion = name.selectbox('Nombre producto:', lista,
                                        key=keyController.compra[0], index=0)
            codigoBarras = codeBarr.text_input("Codigo de barras Producto:",
                                                key=keyController.compra[2], value="")
            keyController.compra[3] = "c"
        if codigoBarras != "" and keyController.compra[3] != "cb":
            keyController.compra[0] += 6
            keyController.compra[1] += 6
            seleccion = name.selectbox('Nombre producto:', lista,
                                        key=keyController.compra[0], index=0)
            codigo = code.text_input("Codigo Producto:",
                                     key=keyController.compra[1], value="")
            keyController.compra[3] = "cb"

    with col2:
        for i in range(9):
            st.write("|")

    with col3:
        st.subheader("Información producto")
        datosProducto = ProductoController.buscarProducto(seleccion, codigo, codigoBarras)
        if datosProducto != None:
            productoEncontrado = 1
            st.write(" ")
            st.write(" ")
            st.subheader("Nombre: %s" % (datosProducto.nombre))
            st.subheader("codigo: %s" % (datosProducto.codigo))
            st.subheader("codigo de barras: %s" % (datosProducto.codigoBarras))
            st.subheader("Precio: %i $" % (datosProducto.precio))
            productoEncontrado = 1

    if productoEncontrado:
        st.write("--------------------------------------------------")
        col1, col2, col3 = st.columns([1.8, 1.3, 1.3])

        with col1:
            st.write(' ')

        with col2:
            if keyController.compra[4] == "factura1":
                limpiar = st.button("Cancelar Compra")
                if limpiar:
                    cancelarCompra = 1

        with col3:
            st.write('  ')

        if cancelarCompra:
            keyController.compra[4] = "factura0"
            CompraController.items = []
            keyController.compra[0] += 6
            keyController.compra[1] += 6
            keyController.compra[2] += 6
            seleccion = name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
            codigo = code.text_input("Codigo Producto:", key=keyController.compra[1])
            codigoBarras = codeBarr.text_input("Codigo de barras Producto:", key=keyController.compra[2])
            keyController.compra[3] = ""
            return

        colAgregar, colEspacio ,colBorrar =st.columns([1, 0.1, 1])

        with colAgregar:
            cuantity = st.empty()
            cantidad = cuantity.number_input("Cantidad producto:", min_value= 0.01, key = keyController.compra[6])
            checkearStock = CompraController.comprobarStock(seleccion, codigo, codigoBarras, ProductoController, cantidad)

            if checkearStock == 1:
                st.error("No hay suficiente producto")

            if checkearStock == 0:
                checkearStock = ProductoController.comprobarStock(seleccion, codigo, codigoBarras, cantidad)
                if checkearStock == 1:
                    st.error("No hay suficiente producto")

            if checkearStock == 0:
                agregar = st.button("Agregar")

        with colEspacio:
            for linea in range(4):
                st.write("|")

        if checkearStock == 0:
            if agregar:
                keyController.compra[6] += 6
                cuantity.number_input("Cantidad producto:", min_value=0.01, key=keyController.compra[6])
                keyController.compra[4] = "factura1"
                nuevoItem = Compra()
                nuevoItem.nombre = seleccion
                ProductoController.agregarProducto(nuevoItem)
                productoEnCarrito = CompraController.aumentarCantidad(nuevoItem, cantidad)
                if productoEnCarrito == 0:
                    nuevoItem.cantidad = cantidad
                    nuevoItem.costo = nuevoItem.cantidad * nuevoItem.precio
                    CompraController.agregar_compra( nuevoItem )
                    print(len(CompraController.items))

        with colBorrar:
            if len(CompraController.items) > 0:
                clean = st.empty()
                quitar = clean.number_input("Escribe el numero del producto que quieras eliminar:", key = keyController.compra[7] )
                borrar = st.button("Borrar")
                if borrar:
                    clickBorrar = 1
                    keyController.compra[7] += 6
                    clean.number_input("Escribe el numero del producto que quieras eliminar:", key =keyController.compra[7] )

        st.write("--------------------------------------------------")

        if keyController.compra[4] == "factura1":
            total = 0
            if clickBorrar and quitar > 0 and quitar <= len(CompraController.items):
                CompraController.items.pop(int(quitar - 1))
                if len(CompraController.items) == 0:
                    keyController.compra[4] = "factura0"
                    keyController.compra[0] += 6
                    keyController.compra[1] += 6
                    keyController.compra[2] += 6
                    seleccion = name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
                    codigo = code.text_input("Codigo Producto:", key=keyController.compra[1])
                    codigoBarras = codeBarr.text_input("Codigo de barras Producto:", key=keyController.compra[2])
                    keyController.compra[3] = ""
                    return
            colNumero, colNombre, colCodigo, colPrecioUnidad, colCantidad, colCosto = st.columns(
                [0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
            with colNumero:
                st.write("Numero")

            with colNombre:
                st.write("Nombre")

            with colCodigo:
                st.write("Codigo")

            with colPrecioUnidad:
                st.write("Precio Unidad")

            with colCantidad:
                st.write("Cantidad")

            with colCosto:
                st.write("Costo")
            index = 0
            borrar = None
            for l in CompraController.items:

                total += l.costo

                with colNumero:
                    st.write("%i." % (index + 1))

                with colNombre:
                    st.write(l.nombre)

                with colCodigo:
                    st.write(l.codigo)

                with colPrecioUnidad:
                    st.write(str(l.precio))

                with colCantidad:
                    st.write(str(round(l.cantidad, 2)))

                with colCosto:
                    st.write(str(l.costo))

                index += 1
            st.subheader("Precio total: %s" % str(round(total, 2)))
            cobrar = st.button("Cobrar")

            if cobrar:
                keyController.compra[5] = "cobrar1"

            if keyController.compra[5] == "cobrar1":
                money = st.empty()
                dinero = money.number_input("Con cuanto paga el cliente:", key = keyController.compra[8])
                if dinero < total:
                    st.error("Valor menor al total")
                    return

                finalizarCompra = st.button("Finalizar Compra")

                if finalizarCompra:
                    aperturaCierreController.dineroCaja += total
                    st.write("El cambio es de: " + "{0:.2f}".format(dinero - total))
                    st.success("Compra realizada exitosamente")
                    keyController.compra[4] = "factura0"
                    keyController.copraAumento()
                    name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
                    code.text_input("Codigo Producto:", key=keyController.compra[1])
                    codeBarr.text_input("Codigo de barras Producto:", key=keyController.compra[2])
                    cuantity.number_input("Cantidad producto:", min_value=0.01, key=keyController.compra[6])
                    clean.number_input("Escribe el numero del producto que quieras eliminar:",
                                       key=keyController.compra[7])
                    money.number_input("Con cuanto paga el cliente:", key = keyController.compra[8])
                    keyController.compra[3] = ""
                    fechaHora = datetime.now()
                    momentoCompra = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
                    CompraController.total = total
                    CompraController.hora = momentoCompra
                    VentaController.agregar_venta(CompraController)
                    CompraController.actualizarStock(ProductoController)
                    CompraController.reiniciarValores()
                    st.button("Continuar Facturando")
                    st.write(momentoCompra)
            return
    else:
        st.error("No se a encontrado ningun producto con estos datos")
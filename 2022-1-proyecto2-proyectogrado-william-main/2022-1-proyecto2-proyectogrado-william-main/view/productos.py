from model.Producto import Producto

def agregarProducto(st, ProductoController, keyController):
    if keyController.agregarProducto[0] > 100 and keyController.agregarProducto[1] > 100 and keyController.agregarProducto[2] > 100 and keyController.agregarProducto[3] > 100 and keyController.agregarProducto[4] > 100:
        keyController.agregarProducto[0] = 0
        keyController.agregarProducto[1] = 0
        keyController.agregarProducto[2] = 0
        keyController.agregarProducto[3] = 0
        keyController.agregarProducto[4] = 0
    st.header( "Agregar nuevo producto al sistema e inventario" )
    nuevoProducto = Producto()
    name = st.empty()
    code = st.empty()
    codeBarr = st.empty()
    price = st.empty()
    total = st.empty()
    nuevoProducto.nombre = name.text_input( "Nombre del producto", key = keyController.agregarProducto[0] )
    nuevoProducto.codigo = code.text_input( "Codigo del producto", key = keyController.agregarProducto[1] )
    nuevoProducto.codigoBarras = codeBarr.text_input( "Codigo de Barras", key = keyController.agregarProducto[2] )
    nuevoProducto.precio = price.number_input( "Precio del producto", key = keyController.agregarProducto[3] )
    nuevoProducto.cantidad = total.number_input( "Cantidad de unidades de este producto:", key = keyController.agregarProducto[4] )
    crearProducto = st.button( "Crear Producto" )
    if crearProducto :
        existencia = ProductoController.comprobarExistencia(nuevoProducto)
        if existencia == 1:
            st.error("Ya existe un producto con este nombre")
        elif existencia == 2:
            st.error("Ya existe un producto con este codigo")
        elif existencia == 3:
            st.error("Ya existe un producto con este codigo de barras")
        else:
            ProductoController.agregar_producto(nuevoProducto)
            st.success("Prouducto agregado exitosamente")
            keyController.agregarProducto[0] += 5
            keyController.agregarProducto[1] += 5
            keyController.agregarProducto[2] += 5
            keyController.agregarProducto[3] += 5
            keyController.agregarProducto[4] += 5
            name.text_input("Nombre del producto", key=keyController.agregarProducto[0])
            code.text_input("Codigo del producto", key=keyController.agregarProducto[1])
            codeBarr.text_input("Codigo de Barras", key=keyController.agregarProducto[2])
            price.number_input("Precio del producto", key=keyController.agregarProducto[3])
            total.number_input("Cantidad de unidades de este producto:",
                                                        key=keyController.agregarProducto[4])


def seleccionarListado(st, ProductoController):
    st.header( "Inventario" )
    listar = st.selectbox( "Que quieres ver del inventario", ("Todos los productos", "Productos en existencia", "Productos agotados" ) )
    if listar == "Todos los productos":
        productosSistema(st, ProductoController)
    elif listar == "Productos en existencia":
        productosExistencia(st, ProductoController)
    elif listar == "Productos agotados":
        productoAgotados(st, ProductoController)

def productosSistema(st, ProductoController):
    nombreProductos = ProductoController.nombreProductosSistema()
    print(nombreProductos)
    seleccion = st.selectbox( "seleccionar producto para ver informacion:", nombreProductos )
    for i in ProductoController.productos:
        if seleccion == i.nombre:
            st.subheader( "Codigo:" )
            st.write( i.codigo )
            st.subheader("Codigo de barras:")
            st.write(i.codigoBarras)
            st.subheader("Precio:")
            st.write(str(i.precio))
            st.subheader("Cantidad unidades:")
            st.write(str(i.cantidad))

def productosExistencia(st, ProductoController):
    nombreProductos = ProductoController.nombreProductosExistencia()
    seleccion = st.selectbox("seleccionar producto para ver informacion:", nombreProductos)
    for i in ProductoController.productos:
        if seleccion == i.nombre and i.cantidad > 0:
            st.subheader("Codigo:")
            st.write(i.codigo)
            st.subheader("Codigo de barras:")
            st.write(i.codigoBarras)
            st.subheader("Precio:")
            st.write(str(i.precio))
            st.subheader("Cantidad unidades:")
            st.write(str(i.cantidad))

def productoAgotados(st, ProductoController):
    nombreProductos = ProductoController.nombreProductosAgotados()
    seleccion = st.selectbox("seleccionar producto para ver informacion:", nombreProductos)
    for i in ProductoController.productos:
        if seleccion == i.nombre and i.cantidad == 0:
            st.subheader("Codigo:")
            st.write(i.codigo)
            st.subheader("Codigo de barras:")
            st.write(i.codigoBarras)
            st.subheader("Precio:")
            st.write(str(i.precio))

def consultarProducto(st, ProductoController, keyController):
    mostrar = None
    st.header("Consultar informacion de producto")
    st.write("Puedes buscar la informacion de un producto por medio de su nombre buscandolo o escribiendolo en el primer recuadro, o por su codigo escribiendolo en el segundo recuadro, o por su codigo de barras en el tercer recuadro, recuerda que solo podras buscar mediante un metodo ya que al escribir en cualquier recuadro los otros dos se borraran")
    if keyController.consultar[0] > 100 and keyController.consultar[1] > 100 and keyController.consultar[2] > 100:
        keyController.consultar[0] = 0
        keyController.consultar[1] = 0
        keyController.consultar[2] = 0
    listaProductos = ProductoController.nombreProductosSistema()
    listaProductos.insert(0, "")
    lista = st.empty()
    codes = st.empty()
    codesBarr = st.empty()
    seleccion = lista.selectbox('Selecciona o busca el nombre del producto', listaProductos, key = keyController.consultar[0], index=0)
    codigo = codes.text_input( "Escribe el codigo del producto que quieres buscar:", key = keyController.consultar[1] )
    codigoBarras = codesBarr.text_input( "Codigo de barras del producto que quieres buscar:", key = keyController.consultar[2] )
    if seleccion != "" and keyController.consultar[3] != "s" :
        keyController.consultar[1] += 3
        keyController.consultar[2] +=3
        codigo = codes.text_input( "Escribe el codigo del producto que quieres buscar:", key = keyController.consultar[1], value="" )
        codigoBarras = codesBarr.text_input("Codigo de barras del producto que quieres buscar:", key=keyController.consultar[2], value = "")
        keyController.consultar[3] = "s"
    if codigo != "" and keyController.consultar[3] != "c":
        keyController.consultar[0] += 3
        keyController.consultar[2] += 3
        seleccion = lista.selectbox('Selecciona o busca el nombre del producto', listaProductos, key = keyController.consultar[0], index=0)
        codigoBarras = codesBarr.text_input("Codigo de barras del producto que quieres buscar:", key= keyController.consultar[2], value = "")
        keyController.consultar[3] = "c"
    if codigoBarras != "" and keyController.consultar[3] != "cb":
        keyController.consultar[0] += 3
        keyController.consultar[1] += 3
        seleccion = lista.selectbox('Selecciona o busca el nombre del producto', listaProductos, key=keyController.consultar[0], index=0)
        codigo = codes.text_input("Escribe el codigo del producto que quieres buscar:", key=keyController.consultar[1], value="")
        keyController.consultar[3] = "cb"
    col1, col2 = st.columns([0.2, 1.7])
    if seleccion != "" or codigo != "" or codigoBarras != "":
        with col1:
            buscar = st.button("Buscar")
        with col2:
            limpiar = st.button("Limpiar")
        if buscar:
            mostrar = 1
        if limpiar:
            mostrar = 0
        if mostrar == 1:
            if seleccion != "" and codigo == "" and codigoBarras == "":
                for i in ProductoController.productos:
                    if i.nombre == seleccion:
                        st.subheader("Codigo:")
                        st.write(i.codigo)
                        st.subheader("Codigo de barras:")
                        st.write(i.codigoBarras)
                        st.subheader("Precio:")
                        st.write(str(i.precio))
                        if seleccion == i.nombre:
                            if i.cantidad == 0:
                                st.error("Producto agotado")
                            elif i.cantidad > 0:
                                st.subheader("Cantidad unidades:")
                                st.write(str(i.cantidad))
                        return
            elif seleccion == "" and codigo != "" and codigoBarras == "":
                for i in ProductoController.productos:
                    if i.codigo == codigo:
                        st.subheader("Nombre:")
                        st.write(i.nombre)
                        st.subheader("Codigo de barras:")
                        st.write(i.codigoBarras)
                        st.subheader("Precio:")
                        st.write(str(i.precio))
                        if seleccion == i.nombre:
                            if i.cantidad == 0:
                                st.error("Producto agotado")
                            elif i.cantidad > 0:
                                st.subheader("Cantidad unidades:")
                                st.write(str(i.cantidad))
                        return
                st.error("No se encontro ningun producto con este codigo")
            elif seleccion == "" and codigo == "" and codigoBarras != "":
                for i in ProductoController.productos:
                    if i.codigoBarras == codigoBarras:
                        st.subheader("Nombre:")
                        st.write(i.nombre)
                        st.subheader("Codigo:")
                        st.write(i.codigo)
                        st.subheader("Precio:")
                        st.write(str(i.precio))
                        if seleccion == i.nombre:
                            if i.cantidad == 0:
                                st.error("Producto agotado")
                            elif i.cantidad > 0:
                                st.subheader("Cantidad unidades:")
                                st.write(str(i.cantidad))
                    return
                st.error("No se encontro ningun producto con este codigo de barras")
        elif mostrar == 0:
            keyController.consultar[0] += 3
            keyController.consultar[1] += 3
            keyController.consultar[2] += 3
            seleccion = lista.selectbox('Selecciona o busca el nombre del producto', listaProductos,
                                        key=keyController.consultar[0], index=0)
            codigo = codes.text_input("Escribe el codigo del producto que quieres buscar:",
                                      key=keyController.consultar[1], value="")
            codigoBarras = codesBarr.text_input("Codigo de barras del producto que quieres buscar:",
                                                key=keyController.consultar[2], value="")

    else:
        st.error("Para buscar llena alguno de los recuadros")

def editarDatos(st, ProductoController, keyController):
    st.header("Editar datos de un producto")
    st.write(
        "Puedes buscar el producto por medio de su nombre buscandolo o escribiendolo en el primer recuadro, o por su codigo escribiendolo en el segundo recuadro, o por su codigo de barras en el tercer recuadro, recuerda que solo podras buscar mediante un metodo ya que al escribir en cualquier recuadro los otros dos se borraran")
    col1, col2, col3 = st.columns([1, 0.1, 1])
    lista = ProductoController.nombreProductosSistema()

    with col1:
        st.subheader("Buscar Producto")
        name = st.empty()
        code = st.empty()
        codeBarr = st.empty()
        seleccion = name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
        codigo = code.text_input("Codigo Producto:", key=keyController.compra[1])
        codigoBarras = codeBarr.text_input("Codigo de barras Producto:", key=keyController.compra[2])

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
        for i in range(15):
            st.write("|")

    with col3:
        st.subheader("Editar")
        datosProducto = ProductoController.buscarProducto(seleccion, codigo, codigoBarras)
        if datosProducto != None:
            index = ProductoController.buscarIndexProducto(seleccion, codigo, codigoBarras)
            nameEdit = st.empty()
            codeEdit = st.empty()
            codeBarrEdit = st.empty()
            price = st.empty()
            total = st.empty()
            nombre = nameEdit.text_input("Nombre del producto", key=keyController.agregarProducto[0], value= datosProducto.nombre)
            codigo = codeEdit.text_input("Codigo del producto", key=keyController.agregarProducto[1], value= datosProducto.codigo)
            codigoBarras = codeBarrEdit.text_input("Codigo de Barras", key=keyController.agregarProducto[2], value= datosProducto.codigoBarras)
            precio = price.number_input("Precio del producto", key=keyController.agregarProducto[3], value= datosProducto.precio)
            cantidad = total.number_input("Cantidad de unidades de este producto:",
                                                        key=keyController.agregarProducto[4], value= datosProducto.cantidad)
            editar = st.button("Editar")
            if editar:
                aprobado = ProductoController.verificarDatos(nombre, codigo, codigoBarras, index)
                if aprobado:
                    ProductoController.productos[index].nombre = nombre
                    ProductoController.productos[index].codigo = codigo
                    ProductoController.productos[index].codigoBarras = codigoBarras
                    ProductoController.productos[index].precio = precio
                    ProductoController.productos[index].cantidad = cantidad
                    keyController.compra[0] += 6
                    keyController.compra[1] += 6
                    keyController.compra[2] += 6
                    name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
                    code.text_input("Codigo Producto:",
                                             key=keyController.compra[1], value="")
                    codeBarr.text_input("Codigo de barras Producto:",
                                                       key=keyController.compra[2], value="")
                    st.button("Continuar")
                    st.success("Producto editado exitosamente")
                else:
                    st.error("Ya hay productos con estos datos")
        else:
            if( seleccion == "" and codigo == "" and codigoBarras == "" ):
                return
            st.error("No se encontro un producto con estos datos")

def eliminarProducto(st, ProductoController, keyController):
    col1, col2, col3 = st.columns([1, 0.1, 1])
    lista = ProductoController.nombreProductosSistema()
    with col1:
        st.subheader("Buscar Producto")
        name = st.empty()
        code = st.empty()
        codeBarr = st.empty()
        seleccion = name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
        codigo = code.text_input("Codigo Producto:", key=keyController.compra[1])
        codigoBarras = codeBarr.text_input("Codigo de barras Producto:", key=keyController.compra[2])

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
        for i in range(15):
            st.write("|")

    with col3:
        st.subheader("Datos producto")
        datosProducto = ProductoController.buscarProducto(seleccion, codigo, codigoBarras)
        if datosProducto != None:
            index = ProductoController.buscarIndexProducto(seleccion, codigo, codigoBarras)
            nameEdit = st.empty()
            codeEdit = st.empty()
            codeBarrEdit = st.empty()
            price = st.empty()
            total = st.empty()
            nombre = nameEdit.text_input("Nombre del producto", key=keyController.agregarProducto[0], value= datosProducto.nombre)
            codigo = codeEdit.text_input("Codigo del producto", key=keyController.agregarProducto[1], value= datosProducto.codigo)
            codigoBarras = codeBarrEdit.text_input("Codigo de Barras", key=keyController.agregarProducto[2], value= datosProducto.codigoBarras)
            precio = price.number_input("Precio del producto", key=keyController.agregarProducto[3], value= datosProducto.precio)
            cantidad = total.number_input("Cantidad de unidades de este producto:",
                                                        key=keyController.agregarProducto[4], value= datosProducto.cantidad)
            eliminar = st.button("Eliminar")

            if eliminar:
                aprobado = ProductoController.buscarProducto(seleccion, codigo, codigoBarras)
                if aprobado != None:
                    ProductoController.productos.pop(index)
                    st.button("Continuar")
                    st.success("Producto eliminado exitosamente")
                    keyController.compra[0] += 6
                    keyController.compra[1] += 6
                    keyController.compra[2] += 6
                    name.selectbox("Nombre producto:", lista, key=keyController.compra[0])
                    code.text_input("Codigo Producto:",
                                    key=keyController.compra[1], value="")
                    codeBarr.text_input("Codigo de barras Producto:",
                                        key=keyController.compra[2], value="")

        else:
            if (seleccion == "" and codigo == "" and codigoBarras == ""):
                return
            st.error("No se encontro un producto con estos datos")

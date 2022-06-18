
def agregarProveedor(st, provedoresController, keyController):
    st.header("Agregar proveedores")
    name = st.empty()
    nombre = name.text_input("Nombre del proveedor:", key = keyController.proveedores)
    agregarBoton = st.button("Agregar")
    if agregarBoton:
        for i in provedoresController.proveedores:
            if i == nombre:
                st.error("Ya existe este proveedor")
                return
        provedoresController.agregar_proveedor(nombre)
        keyController.proveedore += 1
        name.text_input("Nombre del proveedor:", key = (keyController.proveedore))
        st.success("Provedor guardado")











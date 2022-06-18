from PIL import Image


def soporte( st):
    st.header("Informacion de contacto y soporte")
    # se cargan las fotos que se van a usar dentro del home
    img = Image.open("cel.png")
    img1 = Image.open("correo.png")
    st.write("En caso de cualquier problema o solicitar soporte de cualquier tipo referente al software contarse a los siguientes telefono o whatsapp y correo:")
    col1, col2 = st.columns([0.8, 13])  # con estas columnas comodamos el titulo de la pagina

    with col1:
        st.image(img, width=45)
    with col2:
        st.subheader("3054622892")

    col3, col4 = st.columns([0.8, 13])  # con estas columnas comodamos el titulo de la pagina
    with col1:
        st.image(img1, width=45)
    with col2:
        st.subheader('william84859@hotmail.com')











import streamlit as st

import constantes as co

if 'usuario' in st.session_state:

    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)

    st.write(" En construccion :construction:  ... por favor vuelva pronto ... ")

    st.write(co.COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")    
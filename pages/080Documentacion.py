import streamlit as st
import time
import constantes as co

if 'usuario' in st.session_state:

    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())

    st.sidebar.write(co.ENCABEZADO)

    st.write(" En construccion :construction:  ... por favor vuelva pronto ... ")

    st.write(co.COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
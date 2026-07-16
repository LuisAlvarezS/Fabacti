import streamlit as st
import funciones as fu
import constantes as co
import time

if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())

    st.sidebar.write(co.ENCABEZADO)

    eventos, indicadores = st.tabs(['Eventos','Indicadores'])

    with eventos:
        dserveventos = fu.eventos()
        st.dataframe(dserveventos, hide_index = True, column_config={'id_evento': None})

    with indicadores:
        dserveindicadores = fu.datos_todos_indicadores()
        st.dataframe(dserveindicadores, hide_index = True, column_config={'id_indicador': None})

else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
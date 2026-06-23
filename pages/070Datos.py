import streamlit as st
import funciones as fu
import constantes as co


if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)

    eventos, dtf = st.tabs(['Eventos','DTF'])

    with eventos:
        dserveventos = fu.eventos()
        st.dataframe(dserveventos, hide_index = True, column_config={'id_evento': None})

    with dtf:
        dservdtf = fu.datosdtf()
        st.dataframe(dservdtf, hide_index = True, column_config={'iddtf': None})
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")    
import streamlit as st
import time

from constantes import COPYRIGHT
from funciones import presentar_encabezado, lista_eventos, datos_todos_indicadores

if 'usuario' in st.session_state:
    presentar_encabezado()

    eventos, indicadores = st.tabs(['Eventos','Indicadores'])

    with eventos:
        dserveventos = lista_eventos()
        st.dataframe(dserveventos, hide_index = True, column_config={'id_evento': None})

    with indicadores:
        dserveindicadores = datos_todos_indicadores()
        df_trm = dserveindicadores[dserveindicadores['indicador'] == 'TRM']
        df_dtf = dserveindicadores[dserveindicadores['indicador'] == 'DTF']
        df_ibr = dserveindicadores[dserveindicadores['indicador'] == 'IBR']

        col_trm, col_dtf, col_ibr = st.tabs(['TRM','DTF','IBR'])
        with col_trm:
            st.dataframe(df_trm, hide_index = True, column_config={'id_valor_indicador': None})
        with col_dtf:
            st.dataframe(df_dtf, hide_index = True, column_config={'id_valor_indicador': None})
        with col_ibr:
            st.dataframe(df_ibr, hide_index = True, column_config={'id_valor_indicador': None})
    st.divider()
    st.write(COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
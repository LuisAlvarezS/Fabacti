import streamlit as st
import funciones as fu

eventos, dtf = st.tabs(['Eventos','DTF'])

with eventos:
    dserveventos = fu.eventos()
    st.dataframe(dserveventos, hide_index = True, column_config={'id_evento': None})

with dtf:
    dservdtf = fu.datosdtf()
    st.dataframe(dservdtf, hide_index = True, column_config={'iddtf': None})

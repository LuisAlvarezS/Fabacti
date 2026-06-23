


import streamlit as st
import pandas as pd

import constantes as co


if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)

    st.subheader('Indice Global de Innovación')
    st.divider()
    indice_global_innovacion = [ {"fecha": "2019", "valor": 67}, {"fecha": "2020", "valor": 68}, {"fecha": "2021", "valor": 67}, {"fecha": "2022", "valor": 63}, {"fecha": "2023", "valor": 66}, {"fecha": "2024", "valor": 61}, {"fecha": "2025", "valor": 71} ]
 
    datos = pd.DataFrame({
        "Fecha": ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
        "Colombia": [67, 68, 67, 63, 66, 61, 71], 
        "Suiza": [65, 64, 62, 60, 58, 56, 54], 
        "Chile": [60, 59, 57, 55, 53, 51, 49]
        })
 
    st.line_chart(datos, x='Fecha', y=['Colombia', 'Suiza', 'Chile'], x_label='Fecha', y_label='Índice de Innovación', width='stretch')
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ") 
import streamlit as st

indice_global_innovacion = [ {"fecha": "2019", "valor": 67}, {"fecha": "2020", "valor": 68}, {"fecha": "2021", "valor": 67}, {"fecha": "2022", "valor": 63}, {"fecha": "2023", "valor": 66}, {"fecha": "2024", "valor": 61}, {"fecha": "2025", "valor": 71} ]
st.line_chart(indice_global_innovacion, y='valor', x_label='fecha', y_label='Índice de Innovación', width='stretch')

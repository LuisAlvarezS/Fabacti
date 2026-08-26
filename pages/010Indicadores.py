

import time

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from constantes import COPYRIGHT
from funciones import presentar_encabezado

if 'usuario' in st.session_state:
    
    presentar_encabezado()

    # Indicador de Posición de Colombia en el Índice Global de Innovación
    st.subheader('Posicion de Colombia en el Índice Global de Innovación')
    st.divider()

    datos_pcii = pd.DataFrame({
        "Fecha": ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
        "Colombia": [67, 68, 67, 63, 66, 61, 71]
        })

    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(
        x=datos_pcii['Fecha'], y=datos_pcii['Colombia'], mode='lines+markers+text', 
        text=datos_pcii['Colombia'], textposition='bottom center', textfont=dict(size=14, color='black'),
        name='Colombia', line=dict(color='blue', width=2), marker=dict(size=12)
    ))
    fig1.update_layout(xaxis_title='Año', yaxis_title='Posición')
    fig1.update_layout(
              yaxis=dict(autorange='reversed',
                  range=[0, 100],
                  ),
                  showlegend=False,
      )
    st.plotly_chart(fig1, width='stretch', theme="streamlit", config={"displayModeBar": False})

    # Indicador Per capita de espacio publico verde Medellin en m2/habitante
    st.subheader('Per capita de espacio publico verde Medellin en m2/habitante')
    st.divider()

    datos_ipcepv = pd.DataFrame({
        "Fecha": ["2006", "2019", "2022", "2026"],
        "Medellin": [6.87, 4.86, 4.80,5.31]
        })

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=datos_ipcepv['Fecha'], y=datos_ipcepv['Medellin'], mode='lines+markers+text', 
        text=datos_ipcepv['Medellin'], textposition='bottom center', textfont=dict(size=14, color='black'),
        name='Medellin', line=dict(color='blue', width=2), marker=dict(size=12)
    ))
    fig2.update_layout(xaxis_title='Año', yaxis_title='Indice')
    fig2.update_layout(
            yaxis=dict(range=[0, 20],
                ),
                showlegend=False,
    )
    st.plotly_chart(fig2, width='stretch', theme="streamlit", config={"displayModeBar": False})

    st.divider()
    st.write(COPYRIGHT)
    
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
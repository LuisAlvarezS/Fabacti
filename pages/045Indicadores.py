

import time

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from constantes import COPYRIGHT, APP
from funciones import presentar_encabezado, conectarse_fabacti

if 'usuario' in st.session_state:
    
    presentar_encabezado()
    st.title(APP + " - Indicadores")
    innovación, publicoverde, proyeccioninfacion, tasadesempleo, pronosticotipocambio = st.tabs(["Innovación", "Espacio Público Verde","Proyección Inflación","Tasa de desempleo urbano", "Pronóstico Tipo de Cambio"])

    with innovación:

        # Indicador de Posición de Colombia en el Índice Global de Innovación
        st.subheader('Posicion de Colombia en el Índice Global de Innovación')
        st.divider()

        datos_pcii = pd.DataFrame({
            "Fecha": ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
            "Colombia": [67, 68, 67, 63, 66, 61, 71]
            })
        rango_min = datos_pcii['Colombia'].min() - 5
        rango_max = datos_pcii['Colombia'].max() + 5

        fig1 = go.Figure()

        fig1.add_trace(go.Scatter(
            x=datos_pcii['Fecha'], y=datos_pcii['Colombia'], mode='lines+markers+text', 
            text=datos_pcii['Colombia'], textposition='bottom center', textfont=dict(size=14, color='black'),
            name='Colombia', line=dict(color='blue', width=2), marker=dict(size=12)
        ))
        fig1.update_layout(xaxis_title='Año', yaxis_title='Posición')
        fig1.update_layout(
                yaxis=dict(autorange='reversed',
                    range=[rango_min, rango_max],
                    ),
                    showlegend=False,
        )
        st.plotly_chart(fig1, width='stretch', theme="streamlit", config={"displayModeBar": False})

    with publicoverde:
        # Indicador Per capita de espacio publico verde Medellin en m2/habitante
        st.subheader('Per capita de espacio publico verde Medellin en m2/habitante')
        st.divider()

        datos_ipcepv = pd.DataFrame({
            "Fecha": ["2006", "2019", "2022", "2026"],
            "Medellin": [6.87, 4.86, 4.80,5.31]
            })
        rango_min = datos_ipcepv['Medellin'].min() - 1
        rango_max = datos_ipcepv['Medellin'].max() + 1

        fig2 = go.Figure()

        fig2.add_trace(go.Scatter(
            x=datos_ipcepv['Fecha'], y=datos_ipcepv['Medellin'], mode='lines+markers+text', 
            text=datos_ipcepv['Medellin'], textposition='bottom center', textfont=dict(size=14, color='black'),
            name='Medellin', line=dict(color='blue', width=2), marker=dict(size=12)
        ))
        fig2.update_layout(xaxis_title='Año', yaxis_title='Indice')
        fig2.update_layout(
                yaxis=dict(range=[rango_min, rango_max],
                    ),
                    showlegend=False,
        )
        st.plotly_chart(fig2, width='stretch', theme="streamlit", config={"displayModeBar": False})

    with proyeccioninfacion:

        # Proyeción de la inflación en Colombia
        st.subheader('Proyección de la inflación en Colombia')
        st.divider()

        datos_inflacion = pd.DataFrame({
            "Fecha": ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
            "Colombia": [5.6, 13.1, 9.3, 5.2, 5.1, 6.7, 5.5,4.1,3.6,3.3]
            })
        rango_min = datos_inflacion['Colombia'].min() - 5
        rango_max = datos_inflacion['Colombia'].max() + 5

        fig1 = go.Figure()

        fig1.add_trace(go.Scatter(
            x=datos_inflacion['Fecha'], y=datos_inflacion['Colombia'], mode='lines+markers+text', 
            text=datos_inflacion['Colombia'], textposition='bottom center', textfont=dict(size=14, color='black'),
            name='Colombia', line=dict(color='blue', width=2), marker=dict(size=12)
        ))
        fig1.update_layout(xaxis_title='Año', yaxis_title='Posición')
        fig1.update_layout(
                yaxis=dict(autorange=False,
                    range=[rango_min, rango_max],
                    ),
                    showlegend=False,
        )
        st.plotly_chart(fig1, width='stretch', theme="streamlit", config={"displayModeBar": False})
        st.divider()
        st.write(COPYRIGHT)

    with tasadesempleo:

        # Indicador de Tasa de Desempleo Urbano en Colombia
        st.subheader('Tasa de Desempleo Urbano en Colombia')
        st.divider()

        datos_tasadesempleo = pd.DataFrame({
            "Fecha": ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
            "Colombia": [15.2, 11.4, 10.4, 10.1, 8.6,9.0,9.3,9.4,9.6,9.9]
            })
        rango_min = datos_tasadesempleo['Colombia'].min() - 1
        rango_max = datos_tasadesempleo['Colombia'].max() + 1

        fig1 = go.Figure()

        fig1.add_trace(go.Scatter(
            x=datos_tasadesempleo['Fecha'], y=datos_tasadesempleo['Colombia'], mode='lines+markers+text', 
            text=datos_tasadesempleo['Colombia'], textposition='bottom center', textfont=dict(size=14, color='black'),
            name='Colombia', line=dict(color='blue', width=2), marker=dict(size=12)
        ))
        fig1.update_layout(xaxis_title='Año', yaxis_title='Tasa de Desempleo')
        fig1.update_layout(
                yaxis=dict(autorange=False,
                    range=[rango_min, rango_max],
                    ),
                    showlegend=False,
        )
        st.plotly_chart(fig1, width='stretch', theme="streamlit", config={"displayModeBar": False})

    with pronosticotipocambio:

        # Indicador de Tasa de Desempleo Urbano en Colombia
        st.subheader('Pronóstico del Tipo de Cambio en Colombia')
        st.divider()

        datos_pronosticotipocambio = pd.DataFrame({
            "Fecha": ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"],
            "ptcc": [3744, 4256, 4326, 4074, 4053,3417,3331,3495,3652,3756]
            })
        rango_min = datos_pronosticotipocambio['ptcc'].min() - 500
        rango_max = datos_pronosticotipocambio['ptcc'].max() + 500
    
        fig1 = go.Figure()

        fig1.add_trace(go.Scatter(
            x=datos_pronosticotipocambio['Fecha'], y=datos_pronosticotipocambio['ptcc'], mode='lines+markers+text', 
            text=datos_pronosticotipocambio['ptcc'], textposition='bottom center', textfont=dict(size=14, color='black'),
            name='Pronóstico', line=dict(color='blue', width=2), marker=dict(size=12)
        ))
        fig1.update_layout(xaxis_title='Fuente: LSEK Worspace. Pronostico Grupo Cibest', yaxis_title='Pronóstico tipo de cambio')
        fig1.update_layout(
                yaxis=dict(autorange=False,
                    range=[rango_min, rango_max],
                    ),
                    showlegend=False,
        )
        st.plotly_chart(fig1, width='stretch', theme="streamlit", config={"displayModeBar": False})

    st.divider()
    st.write(COPYRIGHT)
else:
    conectarse_fabacti()
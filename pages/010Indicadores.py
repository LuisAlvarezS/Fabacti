


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import constantes as co


if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)

    st.subheader('Posicion de Colombia en el Índice Global de Innovación')
    st.divider()
 
    datos = pd.DataFrame({
        "Fecha": ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
        "Colombia": [67, 68, 67, 63, 66, 61, 71]
        })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datos['Fecha'], y=datos['Colombia'], mode='lines+markers', name='Colombia'))
    fig.update_layout(xaxis_title='Fecha', yaxis_title='Índice de Innovación')
    fig.update_layout(
            yaxis=dict(autorange='reversed',
                       range=[0, 100])
    )
    st.plotly_chart(fig, use_container_width=True, theme="streamlit", config={"displayModeBar": False})
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ") 
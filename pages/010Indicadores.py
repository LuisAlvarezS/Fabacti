


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import constantes as co


if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)
    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())
    
    st.subheader('Posicion de Colombia en el Índice Global de Innovación')
    st.divider()
 
    datos = pd.DataFrame({
        "Fecha": ["2019", "2020", "2021", "2022", "2023", "2024", "2025"],
        "Colombia": [67, 68, 67, 63, 66, 61, 71]
        })
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=datos['Fecha'], y=datos['Colombia'], mode='lines+markers+text', 
        text=datos['Colombia'], textposition='middle right', textfont=dict(size=14, color='black'),
        name='Colombia', line=dict(color='blue', width=2), marker=dict(size=12)
    ))
    fig.update_layout(xaxis_title='Año', yaxis_title='Posicion')
    fig.update_layout(
            yaxis=dict(autorange='reversed',
                       range=[0, 100],
                ),
                showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True, theme="streamlit", config={"displayModeBar": False})
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ") 
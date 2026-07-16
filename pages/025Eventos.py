import streamlit as st

import pandas as pd
import sqlite3
from datetime import datetime
import time

from streamlit_calendar import calendar

import constantes as co
from funciones import guardarevento, existeevento

if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")

    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear(), help="Haga clic para cerrar sesión y borrar la información de usuario.")
    st.sidebar.write(co.ENCABEZADO)
        
    consulta, registro = st.tabs(['Consultar', 'Registrar'])

    with consulta:
        conn = sqlite3.connect('datos/fabacti.db')
        df = pd.read_sql_query("select fecha,evento from eventos", conn)
        conn.close()

        calendar_options = {
        "initialView": "dayGridMonth",
        "editable": True,
        "selectable": True
        }

        calendar_events = []
        for fila, evento in df.iterrows():
            ff = datetime.strptime(evento['fecha'], '%Y%m%d').date()
            calendar_events.append({'title': evento['evento'], 'start': str(ff), 'end': str(ff)})

        custom_css = """
        fc-event-title { font-weight: bold; }
        """

        calendar_component = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)

    with registro:
        fecha = st.date_input(label='Fecha', format='DD/MM/YYYY')
        wfecha = fecha.strftime('%Y%m%d')
        evento = st.text_input(label='Nombre Evento:',value='',max_chars=2000,placeholder='Digite nombre del evento ...')
        if st.button("Guardar Cambios"):
            if not evento.strip():
                st.error(' ⚠️ Nombre del evento es un dato Obligatorio')       
            else:
                st.success(f' Datos a almacenar {wfecha}: {evento}')
                existeevento = existeevento(wfecha, evento) 
                if existeevento:
                    mensaje = 'Evento  con el  mismo nombre ya existe para esa fecha'
                else:
                    mensaje = guardarevento(wfecha, evento)
                st.write(mensaje)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 

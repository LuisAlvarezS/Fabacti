import streamlit as st
import time

from constantes import COPYRIGHT, FUENTESNOTICIAS
from funciones import presentar_encabezado

if 'usuario' in st.session_state:
    presentar_encabezado()
    st.write("Fuentes de infomación: ")
    st.write(" - :blue[**Noticias**] :newspaper:  :green[**(NewsAPI)**] [https://newsapi.org/]")
    textofuentes = " "
    for fuente in FUENTESNOTICIAS:
        textofuentes = textofuentes + " - " + fuente
    st.write("     - " + textofuentes)
    st.write(" - :blue[**Frase del día**] :memo:  :green[**(Frasedeldia)**] [https://rasedeldia.azurewebsites.net/api/phrase]")
    st.write(" - :blue[**Indicadores financieros**] [https://www.datos.gov.co/resource/32sa-8pi3.json]")

    st.write(" - :blue[**Informacion de Colombia**] [https://api-colombia.com/api/v1]")
    st.divider()
    st.write(COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
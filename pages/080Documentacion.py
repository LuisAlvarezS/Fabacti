import streamlit as st
import time

import yfinance

from constantes import COPYRIGHT, FUENTESNOTICIAS
from funciones import presentar_encabezado

if 'usuario' in st.session_state:
    presentar_encabezado()
    st.divider()
    st.write("Fuentes de infomación: ")
    st.divider()
    
    st.write("A continuación se presentan las fuentes de información utilizadas en el proyecto:")
    st.write(" - :blue[**Valor del oro, café, petróleo y euro**] :moneybag:  :green[**(Yahoo Finance)**] [https://finance.yahoo.com/]")
    st.write("     - Los datos financieros fueron obtenidos mediante la librería yfinance de Python, que accede a la API pública de Yahoo Finance para fines educativos y de investigación.")
    st.write("     [yfinance] yfinance - Python library for Yahoo Finance data. Available: https://pypi.org/project/yfinance/")
    st.write(" - :blue[**Noticias**] :newspaper:  :green[**(NewsAPI)**] [https://newsapi.org/]")
    textofuentes = " "
    for fuente in FUENTESNOTICIAS:
        textofuentes = textofuentes + " - " + fuente
    st.write("     - " + textofuentes)
    st.write(" - :blue[**Frase del día**] :memo:  :green[**(Frasedeldia)**] [https://rasedeldia.azurewebsites.net/api/phrase]")
    st.write(" - :blue[**Indicadores financieros**] [https://www.datos.gov.co/resource/32sa-8pi3.json]")
    st.write(" - :blue[**Informacion de Colombia**] [https://api-colombia.com/api/v1]")

    st.divider()
    st.write("Herramientas de desarrollo: ")
    st.divider()
    
    st.write("A continuación se presentan las herramientas de desarrollo utilizadas en el proyecto:")
    st.write(" - :blue[**Streamlit**] [https://streamlit.io/]")
    st.write(" - :blue[**Python**] [https://www.python.org/]")
    st.write(" - :blue[**yfinance**] [https://pypi.org/project/yfinance/]")
    st.write(" - :blue[**NewsAPI**] [https://newsapi.org/]")
    st.write(" - :blue[**Frasedeldia**] [https://rasedeldia.azurewebsites.net/api/phrase]")
    st.write(" - :blue[**Datos abiertos de Colombia**] [https://www.datos.gov.co/]")
    st.write(" - :blue[**Constantes del proyecto**] [https://github.com/tu-repositorio/constantes]")
    st.write(" - :blue[**Funciones del proyecto**] [https://github.com/tu-repositorio/funciones]")
    st.write(" - :blue[**Página principal del proyecto**] [https://github.com/tu-repositorio/proyecto]")
    st.write(" - :blue[**Repositorio del proyecto**] [https://github.com/tu-repositorio/proyecto]")
    st.write(" - :blue[**Documentación del proyecto**] [https://github.com/tu-repositorio/proyecto/wiki]")
    st.write(" - :blue[**Licencia del proyecto**] [https://github.com/tu-repositorio/proyecto/LICENSE]")
    st.write("Base de datos del proyecto: Sqlite versión 3")
    st.write("Lenguaje de programación principal: Python")
    st.write("Framework principal: Streamlit")
    st.write("Sistema de control de versiones: Git")
    st.write("Repositorio principal del proyecto: https://github.com/tu-repositorio/proyecto")
    
    st.divider()
    st.write("Fin de la documentación del proyecto.")
    st.divider()
    
    st.write(COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
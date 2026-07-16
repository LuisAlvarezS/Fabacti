import streamlit as st
import time
import constantes as co

if 'usuario' in st.session_state:

    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())

    st.sidebar.write(co.ENCABEZADO)

    st.write("Fuentes de infomación: ")
    st.write(" - :blue[**Noticias**] :newspaper:  :green[**(NewsAPI)**] [https://newsapi.org/]")
    for fuente in co.FUENTESNOTICIAS:
        st.write(" - " + fuente)
    st.write(" - :blue[**Frase del día**] :memo:  :green[**(Frasedeldia)**] :link[https://rasedeldia.azurewebsites.net/api/phrase]")
    st.write(" - :blue[**Indicadores financieros**] :link[https://www.banrep.gov.co/es/estadisticas/indicadores-financieros]")

    st.write(co.COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
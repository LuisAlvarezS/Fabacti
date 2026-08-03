import streamlit as st
import time
from datetime import datetime
import json
import requests

from constantes import COPYRIGHT, FUENTESNOTICIAS, KEY_NEWSAPI
from funciones import presentar_encabezado

if 'usuario' in st.session_state:
    presentar_encabezado()

    st.title(' :red[NOTICIAS] ')

    # Noticias
    tema = 'Colombia'
    fecha = datetime.now()
    fecha = fecha.strftime('%Y%m%d')

    url = f'https://newsapi.org/v2/everything?q={tema}&from={fecha}&sortBy=publishedAt&apiKey={KEY_NEWSAPI}'
    resp = requests.get(url)
    texto = json.loads(resp.text)
    articulos = texto['articles']
    
    st.write('---')
    t1, t2, t3, t4, t5 = st.columns(5)
    with t1:
        st.write('**Fuente**')
    with t2:
        st.write('**Titulo**')
    with t3:
        st.write('**Descripcion**')
    with t4:
        st.write('**Imagen**')
    with t5:
        st.write('**Contenido**')
    st.write('---')
    totalarticulos = len(articulos)
    for i in range(1,totalarticulos):
        fuente = texto['articles'][i]['source']['name']
        fechapublicacion = texto['articles'][i]['publishedAt']
        if fuente in FUENTESNOTICIAS:
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                autor = texto['articles'][i]['author']
                if autor != None:
                    st.write(fuente + '\n\n' + texto['articles'][i]['author'] + '\n\n Fecha: ' + fechapublicacion)
            with c2:
                st.write(texto['articles'][i]['title'])
            with c3:
                st.write(texto['articles'][i]['description'])
            with c4:
                img = texto['articles'][i]['urlToImage']
                if img != None:
                    st.image(img)
            with c5:
                contenido = texto['articles'][i]['content']
                if contenido != None:
                    st.write(contenido)
    st.divider()
    st.write(COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
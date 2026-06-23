import streamlit as st

from datetime import datetime
import json
import requests

import constantes as co

if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write(co.ENCABEZADO)

    st.title(' :red[NOTICIAS] ')

    # Noticias
    tema = 'Colombia'
    fecha = datetime.now()
    fecha = fecha.strftime('%Y%m%d')

    url = f'https://newsapi.org/v2/everything?q={tema}&from={fecha}&sortBy=publishedAt&apiKey={co.KEY_NEWSAPI}'
    resp = requests.get(url)
    texto = json.loads(resp.text)
    articulos = texto['articles']
    #st.write(texto)
    totalarticulos = len(articulos)
    for i in range(1,totalarticulos):
        fuente = texto['articles'][i]['source']['name']
        fechapublicacion = texto['articles'][i]['publishedAt']
        if fuente in co.FUENTESNOTICIAS:
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
    st.write(co.COPYRIGHT)
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")    
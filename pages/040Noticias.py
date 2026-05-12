import streamlit as st

from datetime import datetime
import json
import requests


# Variables de contenido
ENCABEZADO = " :red[FABACTI] :registered: :blue[Consultoría especializada en tecnologías de la información y las comunicaciones]"
DERECHOSAUTOR = ":copyright: 2024 Todos los derechos reservados de autor :red[FABACTI] :registered:"

# URL Noticias
KEY_NEWSAPI = 'a039a8295b894d07bf4b4c2d2601359c'

#Fuentes de noticias
FUENTESNOTICIAS = ['France24','DW Español','Xataka','ComputerHoy','Xataka.com', 'Xataka.com.co','Elespectador.com','Republica.com','El Financiero',
                   'El Mundo','Nacion.com','La Nacion','Elperiodico.com','Eleconomista.es','Www.abc.es',
                   'Eldiario.es','Jotdown.es','Elconfidencialdigital.com']

st.write(ENCABEZADO)


st.title(' :red[NOTICIAS] ')

# Noticias
tema = 'Colombia'
fecha = datetime.now()
fecha = fecha.strftime('%Y%m%d')

url = f'https://newsapi.org/v2/everything?q={tema}&from={fecha}&sortBy=publishedAt&apiKey={KEY_NEWSAPI}'
resp = requests.get(url)
texto = json.loads(resp.text)
articulos = texto['articles']
#st.write(texto)
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
st.write(DERECHOSAUTOR)


import streamlit as st

#import pandas as pd
#import sqlite3 as sql
import time
import constantes as co
import funciones as fu

if 'usuario' in st.session_state:
    # Encabezado
    st.write( ":red[FABACTI] :registered: ")

    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear(), help="Haga clic para cerrar sesión y borrar la información de usuario.")
    st.sidebar.write(co.ENCABEZADO)
    df = fu.listalibros()
    dlibr = df
    totallibros = len(dlibr)
    dlibr = dlibr.sort_values(by = 'titulo', ascending=True)

    st.subheader(f"Total libros: {totallibros}")

    totallibros, consultatitulo, consultaautor, lista = st.tabs(['Libros', 'Consulta por titulo', 'Consulta por autor', 'Lista de libros'])
#    consultatitulo, consultaautor, lista = st.tabs(['Consulta por titulo', 'Consulta por autor', 'Lista de libros'])

    with totallibros:
        dft = df.sort_values(by = 'titulo', ascending = True)
        contadorcol = 0
        col1, col2, col3, col4 = st.columns(4, vertical_alignment="top")
        ctp = 0
        ctl = 0
        for linea in dft.iterrows():
            ctl = ctl + 1
            portada = linea[1]['portada'] 
            if contadorcol == 4:
                contadorcol = 0
            if portada is not None:
                ctp = ctp + 1
                contadorcol = contadorcol + 1
                try:
                    if contadorcol == 1:
                        col1.image(portada, caption=linea[1]['titulo'], width=200)
                    elif contadorcol == 2:
                        col2.image(portada, caption=linea[1]['titulo'], width=200)
                    elif contadorcol == 3:
                        col3.image(portada, caption=linea[1]['titulo'], width=200)
                    elif contadorcol == 4:
                        col4.image(portada, caption=linea[1]['titulo'], width=200)
                except:
                    continue
        st.write(f'Total libros con portada: {ctp} de {ctl}')

    with consultatitulo:
        libros = fu.lista_titulos()
        buscar = st.selectbox('Seleccionar ',libros)  
        if buscar:
            libro = df[df['titulo'] == buscar]
            indice = 0
            portada = libro.iat[indice,6]
            col1, col2 = st.columns(2)
            with col1:
                if portada is not None:
                    try: 
                        st.image(portada,caption=libro.iat[indice,3], width = 300)
                    except:
                        st.write('Imagen no encontrada')    
                else:
                    st.write(' Sin IMAGEN')
            with col2:
                st.write('**ISBN**              : ', libro.iat[indice,1])
                st.write('**Tiulo**             : ', libro.iat[indice,2])
                st.write('**Autor**             : ', libro.iat[indice,3])
                st.write('**Leido Miriam**      : ', libro.iat[indice,4])
                st.write('**Leido Luis**        : ', libro.iat[indice,5])
                st.write('**Resumen**           : ', libro.iat[indice,7])
                st.write('**Categoria**         : ', libro.iat[indice,8])
                st.write('**Fecha Publicacion** : ', libro.iat[indice,9])
                st.write('**Editorial**         : ', libro.iat[indice,10])
                st.write('**Paginas**           : ', libro.iat[indice,11])
                st.write('**Comentario**        : ', libro.iat[indice,12])
        else:
            st.write('Libro no encontrado')

    with consultaautor:
        libros = fu.lista_autores()
        buscar = st.selectbox('Seleccionar ',libros)  
        if buscar:
            libro = df[df['autor'] == buscar]
            for linea in libro.iterrows():
                portada = linea[1]['portada'] 
                col1, col2 = st.columns(2)
                with col1:
                    if portada is not None:
                        try: 
                            st.image(portada,caption=linea[1]['titulo'], width = 300)
                        except:
                            st.write('Imagen no encontrada')    
                    else:
                        st.write(' Sin IMAGEN')        
                with col2:
                    st.write('**ISBN**              : ', linea[1]['isbn'])
                    st.write('**Tiulo**             : ', linea[1]['titulo'])
                    st.write('**Autor**             : ', linea[1]['autor'])
                    st.write('**Leidom Miriam**     : ', linea[1]['leidom'])
                    st.write('**Ledo Luis**         : ', linea[1]['leidoa'])
                    st.write('**Resumen**           : ', linea[1]['resumen'])
                    st.write('**Categoria**         : ', linea[1]['categoria'])
                    st.write('**Fecha Publicacion** : ', linea[1]['fechapublicacion'])
                    st.write('**Editorial**         : ', linea[1]['editorial'])
                    st.write('**Paginas**           : ', linea[1]['paginas'])
                    st.write('**Comentario**        : ', linea[1]['comentario'])
    
        else:
            st.write('Libro no encontrado')

    with lista:
        st.dataframe(dlibr, column_config = {'id_libros':None,'Leidom':None, 'Leidoa':None,'portada':None})
#        st.dataframe(dlibr, column_config = {'id_libros':None,'Leidom':None, 'Leidoa':None})

else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py")     

import streamlit as st
import requests
import json
import time

from constantes import COPYRIGHT, APP
from funciones import presentar_encabezado, conectarse_fabacti

if 'usuario' in st.session_state:
    #st.write('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)
    presentar_encabezado()
    st.title(APP + " - Informacion Colombia")

    infognal , regiones, departamentos, presidentes, constitucion = st.tabs(["Informacion General","Regiones","Departamentos","Presidentes","Constitucion"]) 

    with infognal:
        urlcolombia = 'https://api-colombia.com/api/v1/Country/Colombia'
        
        resp_col = requests.get(urlcolombia)
        wregiones = json.loads(resp_col.text)

        wnombre = wregiones['name']
        wdescripcion = wregiones['description']
        wcapital = wregiones['stateCapital']
        wpoblacion = '{:,.0f}'.format(float(wregiones['population']))
        wbandera = wregiones['flags'][1]
        wmoneda = wregiones['currency'] + ' ' + wregiones['currencyCode'] + ' ' + wregiones['currencySymbol'] 
        wcodigopais = wregiones['isoCode']
        wcodigointernet = wregiones['internetDomain']
        wprefijo = wregiones['phonePrefix']

        st.write(f'*{wdescripcion}*')
        capital, poblacion, moneda, codigopais, codigointernet, prefijo, bandera = st.columns(7)
        with capital:
            st.subheader('Capital')
            st.write(f' {wcapital} ')
        with poblacion:
            st.subheader('Poblacion')
            st.write(f' **{wpoblacion}** ')
        with moneda:
            st.subheader("Moneda")
            st.write(f' Moneda {wmoneda}' )
        with codigopais:
            st.subheader('Codigo Pais')
            st.write(wcodigopais)
        with codigointernet:
            st.subheader('Codigo Internet')
            st.write(wcodigointernet)
        with prefijo:
            st.subheader('Prefijo Telefono')
            st.write(wprefijo)
        with bandera:
            st.subheader('Bandera')
            st.image(wbandera, width = 100)

    with regiones:
        urlregiones = 'https://api-colombia.com/api/v1/Region'
        
        respregiones = requests.get(urlregiones)
        wregiones = json.loads(respregiones.text)
        total = len(wregiones)
        for i in range (total):
            st.write(f"**{wregiones[i]['name']}**")
            st.write(f"*{wregiones[i]['description']}*")

    with departamentos:
            urldepartamentos = 'https://api-colombia.com/api/v1/Department'
            respdepartamentos = requests.get(urldepartamentos)
            
            wdepartamentos = json.loads(respdepartamentos.text) 
            
            totaldepartamentos = len(wdepartamentos)
            for i in range (totaldepartamentos):
                wcapitald = wdepartamentos[i]['cityCapital']['name']
                wpoblaciond = '{:,.0f}'.format(float(wdepartamentos[i]['population']))
                wpoblacionc = wdepartamentos[i]['cityCapital']['population']
            
                if wpoblacionc == None:
                    wpoblacionc = 0
                else:
                    wpoblacionc = '{:,.0f}'.format(float(wdepartamentos[i]['cityCapital']['population']))

                st.write(f" **{wdepartamentos[i]['name']}**: {wdepartamentos[i]['description']} con una poblacion de {wpoblaciond}. Su capital es **{wcapitald}** cuya **poblacion** es {wpoblacionc}")

    with presidentes:
        urlcolombia = 'https://api-colombia.com/api/v1/President'
        resp_presi = requests.get(urlcolombia)
        wpresidentes = json.loads(resp_presi.text)
        total = len(wpresidentes)
        wimages = []
        wtexto = []
        conimage = 0
        for i in range (total):
            if wpresidentes[i]['endPeriodDate'] == None:
                wpresidentes[i]['endPeriodDate'] = ''
            if wpresidentes[i]['image'] != "" and wpresidentes[i]['image'] != 'null':
                wimages.append(wpresidentes[i]['image']) 
                wtexto.append(wpresidentes[i]['startPeriodDate'][:4] + "/" + wpresidentes[i]['endPeriodDate'][:4] + " " + wpresidentes[i]['name'] + " " + wpresidentes[i]['lastName'])
                conimage += 1
        for k in range (0, conimage, 4):
            try:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.image(wimages[k], width = 100, caption=wtexto[k])
                with col2:
                    st.image(wimages[k+1], width = 100, caption=wtexto[k+1])
                with col3:
                    st.image(wimages[k+2], width = 100, caption=wtexto[k+2])
                with col4:
                    st.image(wimages[k+3], width = 100, caption=wtexto[k+3])
            except:
                pass

    with constitucion:
        urlconstitucion = 'https://api-colombia.com/api/v1/constitutionarticle'
        resp_cons = requests.get(urlconstitucion)
        warticulos = json.loads(resp_cons.text)
        totalarticulos = len(warticulos)
        buscararticulo, buscarpalabra = st.columns(2)
        with buscararticulo:
            larticulos= []
            for i in range(0, totalarticulos):
                larticulos.append(int(warticulos[i]['articleNumber']))
            larticulos = sorted(larticulos)
            wseleccion = st.selectbox('Seleccionar articulo a consultar',larticulos)
            for i in range(0, totalarticulos):
                if int(warticulos[i]['articleNumber']) == wseleccion:
                    st.subheader(warticulos[i]['title'] +  ' -- ' + warticulos[i]['chapter'] )
                    st.write(str(warticulos[i]['articleNumber']) + ' ' +warticulos[i]['content'])
                    break 
        with buscarpalabra:
            wbuscar = st.text_input('Buscar palabra en articulos de la constitucion')
            if wbuscar != "":
                wbuscar = wbuscar.lower()
                for i in range(0, totalarticulos):
                    if wbuscar in warticulos[i]['content'].lower():
                        st.subheader(warticulos[i]['title'] +  ' -- ' + warticulos[i]['chapter'] )
                        st.write(str(warticulos[i]['articleNumber']) + ' ' + warticulos[i]['content'])
    st.divider()
    st.write(COPYRIGHT)
else:
    conectarse_fabacti()
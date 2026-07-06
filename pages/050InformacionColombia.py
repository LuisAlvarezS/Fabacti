
import streamlit as st
import requests
import json
import time
import constantes as co


if 'usuario' in st.session_state:
    st.write('<style>div.block-container{padding-top:2.5rem;}</style>', unsafe_allow_html=True)

    # Encabezado
    st.write( ":red[FABACTI] :registered: ")
    st.sidebar.write('**Usuario** :blue[**' +st.session_state['usuario'] + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())

    st.sidebar.write(co.ENCABEZADO)

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
        larticulos = ['<seleccionar>']
        for i in range(1,totalarticulos):
            larticulos.append(i)
        wseleccion = st.selectbox('Seleccionar articulo a consultar',larticulos)
        if wseleccion != '<seleccionar>':
            st.subheader(warticulos[int(wseleccion)]['title'] +  ' -- ' + warticulos[int(wseleccion)]['chapter'] )
            st.write(warticulos[int(wseleccion)]['content'])
        else:
            st.write('Debe seleccionar el numero del articulo')
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 
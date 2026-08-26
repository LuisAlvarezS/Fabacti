
import datetime
import time
import streamlit as st

import pandas as pd
import os
import sqlite3 as sql
from streamlit_pdf_viewer import pdf_viewer

import constantes as co
import funciones as fu
import funcionessp as fsp

if 'usuario' in st.session_state:
    fu.presentar_encabezado()

    smeses = fu.obtener_anomes_seismeses_antes(datetime.datetime.now().strftime('%Y%m'), 12)
    smeses = smeses[:4] + '-' + smeses[4:]

    conn = sql.connect(co.BD)
    sqlsp = "select id_serviciospublicos, Unidad, Contrato, AnoMesFacturacion, InicioConsumo, " \
                    "FinConsumo, DiasConsumo, Acueducto, Alcantarillado, Energia, Gas, " \
                    "CAcueducto, CAlcantarillado, CEnergia, CGas, OtrasEntidades, CostoServicio " \
                    "from serviciospublicos where AnoMesFacturacion >= '" + smeses + "'"
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()

    dserv = df
    dserv = dserv.sort_values(by = ['Unidad','AnoMesFacturacion'], ascending=True)

    datosconsumo = dserv[['Unidad','AnoMesFacturacion','Energia','Acueducto','Gas']]
    datoscosto = dserv[['Unidad','AnoMesFacturacion','CEnergia', 'CGas','CAcueducto','CAlcantarillado','CGas','OtrasEntidades','CostoServicio']]

    pinares, terraverde, towers, riviere, remanso, paulita, riviere2, graficas, datosserv = st.tabs(['Pinares701','Terraverde406','77Towers1901','LaRiviere1519','ElRemanso318','LaPaulita104','LaRiviere1915','Graficas','Datos detallados'])
        
    with pinares:
        apto = 'Pinares701'

        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto) ) 

        datospinaresconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datospinarescosto = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datospinaresconsumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datospinaresconsumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datospinaresconsumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datospinarescosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datospinarescosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])
    
    with terraverde:
        apto = 'Terraverde406'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datosterraverdeconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datosterraverdecosto = datoscosto[datoscosto['Unidad'] == apto]
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datosterraverdeconsumo, 
                        x = 'AnoMesFacturacion', y = ['Energia'], 
                        x_label='Periodo Facturacion', y_label='Consumo Energia', 
                        color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datosterraverdeconsumo, 
                        x = 'AnoMesFacturacion', y = ['Gas'], 
                        x_label='Periodo Facturacion', y_label='Consumo Gas', 
                        color=[co.C_GAS])
        with acueducto:
            st.line_chart(datosterraverdeconsumo, 
                        x = 'AnoMesFacturacion', y = ['Acueducto'], 
                        x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                        color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datosterraverdecosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datosterraverdecosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])

    with towers:
        apto = '77Towers1901'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datostowersconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datostowerscosto = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datostowersconsumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datostowersconsumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datostowersconsumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datostowerscosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datostowerscosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])
    

    with riviere:
        apto = 'LaRiviere1519'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datoslariviereconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datoslarivierecosto = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datoslariviereconsumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datoslariviereconsumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datoslariviereconsumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datoslarivierecosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datoslarivierecosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])

    with remanso:
        apto = 'ElRemanso318'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datosremansoconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datosremansocosto = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datosremansoconsumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datosremansoconsumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datosremansoconsumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datosremansocosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datosremansocosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])

    with paulita:
        apto = 'LaPaulita104'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datospaulitaconsumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datospaulitacosto = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datospaulitaconsumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datospaulitaconsumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datospaulitaconsumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datospaulitacosto, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datospaulitacosto, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])
    with riviere2:
        apto = 'LaRiviere1915'
        st.subheader('Ultima Facturacion: ' + fsp.ultimafactura(apto))

        datoslariviere2consumo = datosconsumo[ datosconsumo['Unidad'] == apto] 
        datoslariviere2costo = datoscosto[datoscosto['Unidad'] == apto]
        
        st.subheader(f'Consumo por servicio {apto}' )
        energia, gas, acueducto  = st.columns(3)
        with energia:
            st.line_chart(datoslariviere2consumo, 
                    x = 'AnoMesFacturacion', y = ['Energia'], 
                    x_label='Periodo Facturacion', y_label='Consumo Energia', 
                    color=[co.C_ENERGIA])
        with gas:
            st.line_chart(datoslariviere2consumo, 
                    x = 'AnoMesFacturacion', y = ['Gas'], 
                    x_label='Periodo Facturacion', y_label='Consumo Gas', 
                    color=[co.C_GAS])
        with acueducto:
            st.line_chart(datoslariviere2consumo, 
                    x = 'AnoMesFacturacion', y = ['Acueducto'], 
                    x_label='Periodo Facturacion', y_label='Consumo Acueducto', 
                    color=[co.C_ACUEDUCTO])
        st.subheader(f'Costo por servicio {apto}')
        st.line_chart(datoslariviere2costo, 
                        x = 'AnoMesFacturacion', y = ['CEnergia', 'CGas','CAcueducto','CAlcantarillado'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO,co.C_ALCANTARILLADO])
        st.subheader(f'Costo total {apto}')
        st.line_chart(datoslariviere2costo, 
                        x = 'AnoMesFacturacion', y = ['CostoServicio'], 
                        x_label='Periodo Facturacion', y_label='Valor', 
                        color = [co.C_COSTO])
        
    with datosserv:
        st.dataframe(dserv, hide_index = True, column_config={'id_serviciospublicos': None})

    with graficas:
        graficas = ['Consumos Promedios','Costos Totales','Valor diario por servicios']
        seleccionar = st.selectbox('selecciona grafica: ',graficas)
        if seleccionar == 'Consumos Promedios':
            st.subheader('Consumos Promedios')
            st.line_chart(fsp.consumospromedios(), 
                            x = 'Unidad', y = ['AVG(Energia)', 'AVG(Gas)','AVG(Acueducto)'], 
                            x_label='Unidad', y_label='Promedio', 
                            color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO])
        elif seleccionar == 'Costos Totales':              
            st.subheader('Costos Totales')
            st.line_chart(fsp.costototal(), 
                            x = 'Unidad', y = ['SUM(CostoServicio)'], 
                            x_label='Unidad', y_label='Promedio', 
                            color=[co.C_COSTO])
        elif seleccionar == 'Valor diario por servicios':
            st.subheader('Consumos y costos promedios diarios')
            lista = fsp.lista_unidades()
            for i in range(0,len(lista)):
                unidad = lista['Unidad'][i]
                st.write(unidad)
                st.line_chart(fsp.consumodiariounidadmes(unidad), 
                    x = 'AnoMesFacturacion', y = ['Costo_Energia','Costo_Gas','Costo_Acueducto','Costo_Total'], 
                    x_label='Mes', y_label='Promedio Diario', 
                    color=[co.C_ENERGIA, co.C_GAS, co.C_ACUEDUCTO, co.C_COSTO])
    st.divider()
else:
    st.write(" :red[**Por favor inicie sesión para acceder a esta sección.**] ")
    with st.spinner("Direccionando a la página de inicio ...", show_time=True):  time.sleep(2)
    st.switch_page("Fabacti.py") 


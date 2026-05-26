
import os
import random

from anyio import Path

import streamlit as st
import requests
from datetime import datetime, timedelta
import json
import constantes as co
import xmltodict

# Funcion para consultar el TRM dada una fecha
def obtener_trm():
    # Realizar la solicitud
    #URL_TRM = f"https://www.datos.gov.co/resource/32sa-8pi3.json?vigenciadesde={fecha}T00:00:00.000"
    URL_TRM = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=30&$order=vigenciadesde%20DESC"
    response = requests.get(URL_TRM, timeout=10)
    response.raise_for_status()
        
    data = response.json()
        
    if not data:
        return None
    listatrm = []
    for registro in data:
        listatrm.append(float(registro["valor"]))
    return(listatrm) 

# Funcion para obtener la frase del dia
def frase():
    url = 'https://frasedeldia.azurewebsites.net/api/phrase'
    try:
        resp = requests.get(url)
        texto = json.loads(resp.text)
        frase = texto['phrase']
        autor = texto['author']
    except:
        frase = 'La suerte existe, pero tiene que encontrarte trabajando.'
        autor = 'Pablo Picasso'
    return(frase, autor)

# Funcion para obtener el pico y placa del dia, la fuente es la Secretaria de Movilidad de Medellin
# Los datos se cambian semestralmente manualmente y se guardan en la variabla PYP en el archivo constantes.py
# def obtenerpyp():
#     fecha = datetime.now()
#     dia = fecha.weekday()
#     wpyp = co.PYP[dia]
#     ndia = co.DIAS[dia].capitalize()
#     wpyp2 = co.PYP[dia+1]
#     ndia2 = co.DIAS[dia+1].capitalize()
#     return(wpyp, ndia, wpyp2, ndia2)

# Funcion para mostrar todos los dias con su pico y placa, resaltando el dia actual
def mostrartodopyp():
    fecha = datetime.now()
    ndia = fecha.weekday()
    texto = ''
    contador = 0
    for dia in co.DIAS:
        if ndia == contador:
            resaltar = dia + ': ' + co.PYP[contador]
        texto = texto + dia + ': ' + co.PYP[contador] + '  '
        contador += 1
    return(texto, resaltar) 

# Funcion para obtener una imgena aleatoria de una carpeta dada, se utiliza para mostrar el libro recomendado del dia
def obtener_imagen_aleatoria(ruta_directorio):
    extensiones = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    
    try:
        imagenes = [
            os.path.join(ruta_directorio, archivo)
            for archivo in os.listdir(ruta_directorio)
            if Path(archivo).suffix.lower() in extensiones
        ]
        
        if imagenes:
            return random.choice(imagenes)
        return None
    except FileNotFoundError:
        #print(f"Error: El directorio '{ruta_directorio}' no existe")
        return None

# Funcion para obtener un indicador del Banco de la Republica de Colombia  
def obtener_indicador(indicador, periodicidad, fecha, flow ):
    #periodicid  ad = 'DAILY'
    #if indicador == 'COLCAP':
    #    periodicidad = 'MONTHLY'
    # URL del servicio web SOAP Endpoint
    url = "https://totoro.banrep.gov.co/OCDEv1.0/Services/NSIStdV21WsService"
    # Encabecezado de la solicitud
    headers = {
    "Content-Type": "text/xml; charset=utf-8"
    }
    # Cuerpo de la solicitud SOAP, XML 
    body = """<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:web="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/webservices"
    xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message"
    xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"
    xmlns:quer="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/query">
    <soapenv:Header/>
    <soapenv:Body>
    <web:GetGenericData>
    <mes:GenericDataQuery>
    <mes:Header> 
    <mes:ID>""" + indicador + """</mes:ID>
    <mes:Test>false</mes:Test>
    <mes:Prepared>
    """
    #fechahoy = datetime.now()
    fecha = fecha.strftime("%Y-%m-%d")
    body = body + fecha + """ 
    </mes:Prepared>
    <mes:Sender id="Unknown">
    </mes:Sender>
    <mes:Receiver id="Unknown">
    </mes:Receiver>
    </mes:Header>
    <mes:Query>
    <quer:ReturnDetails detail="Full" observationAction="Active">
    <quer:Structure structureID="StructureId" dimensionAtObservation="TIME_PERIOD">
    <com:Structure>
    <Ref agencyID="OECD" id="STES" version="3.0" local="false"
    class="DataStructure" package="datastructure"/>
    </com:Structure>
    </quer:Structure>
    </quer:ReturnDetails>
    <quer:DataWhere>
    <quer:DataSetID operator="equal">DF_""" + indicador + """_""" + periodicidad + """_""" + flow + """</quer:DataSetID>
    <quer:Dataflow>
    <Ref agencyID="ESTAT" id="DF_""" + indicador + """_""" + periodicidad + """_""" + flow + """" version="1.0" local="false"
    class="Dataflow" package="datastructure"/>
    </quer:Dataflow>
    </quer:DataWhere>
    </mes:Query>
    </mes:GenericDataQuery>
    </web:GetGenericData>
    </soapenv:Body>
    </soapenv:Envelope>"""

    # Enviar la solicitud utilizando el método POST
    try:
        response = requests.post(url, data=body, headers=headers)
        data_dict = xmltodict.parse(response.content)
        json_output = json.dumps(data_dict, indent= 4)
        datos = json.loads(json_output)
    except:
        datos = ''
    return(datos)

# Funcion para obtener el DTF actual, se utiliza la función obtener_indicador para consultar el servicio web del Banco de la Republica de Colombia
def dtfactual():
    fechahoy = datetime.now()
    datos = obtener_indicador('DTF', 'DAILY', fechahoy, 'LATEST')
    dtf = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs'][0]['generic:ObsValue']['@value']
    return(dtf)

# Funcion para obtener el DTF historico, se utiliza la función obtener_indicador para consultar el servicio web del Banco de la Republica de Colombia
def dtfhistoricos():
    fechahoy = datetime.now()
    datos = obtener_indicador('DTF', 'DAILY', fechahoy, 'HIST')
    datos1 = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']
    lista_dtf = []
    for obs in datos1:
        lista_dtf.append(obs['generic:ObsValue']['@value'])
    lista_dtf.reverse()  # Invertir el orden de la lista para mostrar los valores más recientes al final
    listafinal = []
    for i in range(1, 80):
        listafinal.append('{:,.2f} '.format(float(lista_dtf[i])))
    listafinal = list(dict.fromkeys(listafinal))  # Eliminar valores duplicados
    listafinal.reverse()  # Invertir el orden de la lista para mostrar los valores más recientes al final
    return(listafinal)


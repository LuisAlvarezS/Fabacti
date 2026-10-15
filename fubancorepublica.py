import streamlit as st

import requests
import json
import xmltodict
from datetime import datetime

def obtener_indicador(indicador):
    periodicidad = 'DAILY'
    if indicador == 'COLCAP':
        periodicidad = 'MONTHLY'
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
    fechahoy = datetime.now()
    fecha = fechahoy.strftime("%Y-%m-%d")
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
    <quer:DataSetID operator="equal">DF_""" + indicador + """_""" + periodicidad + """_LATEST</quer:DataSetID>
    <quer:Dataflow>
    <Ref agencyID="ESTAT" id="DF_""" + indicador + """_""" + periodicidad + """_LATEST" version="1.0" local="false"
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

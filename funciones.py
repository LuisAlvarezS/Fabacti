
import streamlit as st
from suds.client import Client
from datetime import datetime
import constantes as const

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    #URL de referencia para consulta de la TRM (Tasa Representativa del Mercado). Valor de referencia del dolar USA
    URL_TRM = 'https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL'

    try:
        client = suds.client.Client(URL_TRM, location = URL_TRM, faults=True)
        trm =  client.service.queryTCRM(fecha)
    except Exception as e:
        return str(e)
    #trm = 3776.07
    return trm[4}
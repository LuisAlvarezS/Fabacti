import datetime

import streamlit as st

import suds.client

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    #URL de referencia para consulta de la TRM (Tasa Representativa del Mercado). Valor de referencia del dolar USA
    URL_TRM = 'https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL'

    try:
        client = suds.client.Client(URL_TRM, location = URL_TRM, faults=True)
        trm =  client.service.queryTCRM(fecha)
    except Exception as e:
        return str(e)
    return trm[4]


def fabacti():
  # Encabezado
  st.write(" :red[FABACTI] :registered: :blue[Consultoría especializada en tecnologías de la información y las comunicaciones]")
  fecha = datetime.now()
  trm = float(obtener_trm(fecha))
  ftrm = '${:,.2f} '.format(trm)

  st.write(f" :blue[La TRM del día {fecha.strftime('%Y-%m-%d')} es de :red[{ftrm}]]")
 
  st.write(' ...En construccion  ...')

  st.write(":copyright: 2026 Todos los derechos reservados de autor :red[FABACTI] :registered:")

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()


import requests
import streamlit as st
from datetime import datetime

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    # Realizar la solicitud
    URL_TRM = f"https://www.datos.gov.co/resource/32sa-8pi3.json?vigenciadesde={fecha}T00:00:00.000"
    response = requests.get(URL_TRM, timeout=10)
    response.raise_for_status()
        
    data = response.json()
        
    if not data:
        #rint(f"No se encontró TRM para la fecha {fecha}")
        return None
    # Extraer valor y fecha
    trm_valor = float(data[0]["valor"])
    trm_fecha = data[0]["vigenciadesde"].split("T")[0]
    return(trm_valor) 
    #{"fecha": trm_fecha, "valor": trm_valor}

# Funcion para obtener la frase del dia
def frase():
    url = 'https://frasedeldia.azurewebsites.net/api/phrase'
    try:
        resp = requests.get(url)
        texto = st.json.loads(resp.text)
        frase = texto['phrase']
        autor = texto['author']
    except:
        frase = 'La suerte existe, pero tiene que encontrarte trabajando.'
        autor = 'Pablo Picasso'
    return(frase, autor)
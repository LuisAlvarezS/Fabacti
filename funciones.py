
import streamlit as st
import requests
from datetime import datetime
import json
import locale

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    # Realizar la solicitud
    #URL_TRM = f"https://www.datos.gov.co/resource/32sa-8pi3.json?vigenciadesde={fecha}T00:00:00.000"
    URL_TRM = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=1&$order=vigenciadesde%20DESC"
    response = requests.get(URL_TRM, timeout=10)
    response.raise_for_status()
        
    data = response.json()
        
    if not data:
        return None
    trm_valor = float(data[0]["valor"])
    return(trm_valor) 

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


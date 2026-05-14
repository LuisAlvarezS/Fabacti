
import streamlit as st
import requests
from datetime import datetime
import json
import locale

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    # Realizar la solicitud
    URL_TRM = f"https://www.datos.gov.co/resource/32sa-8pi3.json?vigenciadesde={fecha}T00:00:00.000"
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

def fecha_en_espanol():
        # Configurar la localización a español (España o Latinoamérica)
        # 'es_ES.UTF-8' funciona en Linux/Mac, en Windows puede ser 'Spanish_Spain'
    try:
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain')
    except:
        locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')
    # Fecha y hora actual
    ahora = datetime.now()
    # Formato en español
    formato = ahora.strftime("%A, %d de %B de %Y")
    return(formato.capitalize())

def fechapantalla():
    fecha = datetime.now()
    fechapantalla = fecha_en_espanol() + ' ' + str(fecha.hour).zfill(2) + ':' + str(fecha.minute).zfill(2)
    return(fechapantalla)
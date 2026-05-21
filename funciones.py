
import os
import random

from anyio import Path

import streamlit as st
import requests
from datetime import datetime
import json
import constantes as co

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

def obtenerpyp():
    fecha = datetime.now()
    dia = fecha.weekday()
    wpyp = co.PYP[dia]
    ndia = co.DIAS[dia].capitalize()
    wpyp2 = co.PYP[dia+1]
    ndia2 = co.DIAS[dia+1].capitalize()
    return(wpyp, ndia, wpyp2, ndia2)

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
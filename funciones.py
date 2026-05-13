
import requests
import streamlit as st
from datetime import datetime

import constantes as const

# Funcion para consultar el TRM dada una fecha
def obtener_trm(fecha):
    # Realizar la solicitud
    response = requests.get(const.URL_TRM, timeout=10)
    response.raise_for_status()
        
    data = response.json()
        
    if not data:
        #rint(f"No se encontró TRM para la fecha {fecha}")
        return None
    # Extraer valor y fecha
    trm_valor = float(data[0]["valor"])
    trm_fecha = data[0]["vigenciadesde"].split("T")[0]
    return {"fecha": trm_fecha, "valor": trm_valor}

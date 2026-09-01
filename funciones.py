
import os
import random
import sqlite3

from anyio import Path

import streamlit as st
import requests
from datetime import datetime

from holidays_co import is_holiday_date

import json
import constantes as co
import pandas as pd

from zoneinfo import ZoneInfo

# Verifica si una fecha es dia festivo en Colombia
def es_festivo_colombia(fecha_str):
    # Parámetros: fecha_str (str): Fecha en formato 'YYYY-MM-DD'
    # Retorna: bool: True si es festivo, False si no
    try:
        # Convertir string a objeto date
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        # Verificar si es festivo
        return is_holiday_date(fecha)
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use 'YYYY-MM-DD'.")

# Función para obtener la fecha y hora local en una zona horaria específica
def obtener_fecha_hora_local(zona: str = None) -> datetime:
    try:
        if zona:
            return datetime.now(ZoneInfo(zona))
        else:
            # Hora local del sistema
            return datetime.now()
    except Exception as e:
        raise ValueError(f"Error al obtener la hora: {e}")

# Función para presentar el encabezado de la aplicación FABACTI
def presentar_encabezado():
    usuario = st.session_state['nombre_usuario']       
    st.sidebar.write('**Usuario** :blue[**' + usuario + '**]')
    st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())
    st.sidebar.write(co.ENCABEZADO)
    fechacolombia = obtener_fecha_hora_local("America/Bogota")
    fechahoy = fechacolombia.date()  
    ndia = co.DIAS[fechahoy.weekday()]
    nmes = co.MESES[fechahoy.month - 1]
    hora = fechacolombia.strftime("%H:%M:%S")
    # Veriificar e indicar si es festivo en Colombia
    es_festivo = es_festivo_colombia(str(fechahoy))
    if es_festivo:
        mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) + '  :red[**FESTIVO EN COLOMBIA**]'
    else:
        mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) 
    mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) + '  ' + hora
    st.success(mensaje, icon="🌎", title=':red[FABACTI] :registered:  Usuario: :red[' + usuario + ']')
    return(fechahoy)

# Funcion para obtener una frase del dia
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

# Funcion para consultar el TRM dada una fecha
def obtener_trm():
    # Realizar la solicitud
    URL_TRM = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=2&$order=vigenciadesde%20DESC"
    response = requests.get(URL_TRM, timeout=10)
    response.raise_for_status()
    data = response.json()
    trm = data[0]["valor"]
    delta = float(data[0]["valor"]) - float(data[1]["valor"])
    return(trm, delta)

def lista_eventos():
    conn = sqlite3.connect(co.BD)
    sqlsp = "select fecha, evento from eventos order by fecha DESC"
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()
    return(df)

# Funcion para mostrar todos los dias con su pico y placa, resaltando el dia actual
def mostrartodopyp(fecha):
    # fecha = datetime.now()
    ndia = fecha.weekday()
    texto = ''
    contador = 0
    for dia in co.DIAS:
        if ndia == contador:
            resaltar = dia + ': ' + co.PYP[contador]
        texto = texto + dia + ': ' + co.PYP[contador] + '  '
        contador += 1
    if es_festivo_colombia(fecha.strftime("%Y-%m-%d")):
        resaltar = co.DIAS[ndia] + ' Festivo, no aplica Pico y Placa'
    return(texto, resaltar) 

def guardarevento(fecha, evento):
    conn = sqlite3.connect(co.BD)
    cursor = conn.cursor()
    sqlinser = 'insert into eventos ( fecha, evento) values ( ?, ?)'
    datos = (fecha, evento )
    cursor.execute(sqlinser, datos)
    conn.commit()
    cursor.close()
    conn.close()
    return('Registro agregado')

def existeevento(fecha,  evento):
    conn = sqlite3.connect(co.BD)
    consulta = f"select count(*) total from eventos where fecha = '{fecha}' and evento = '{evento}'"
    #st.write(consulta)
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    total = df['total'][0]
    if total == 0:
        return(False)
    else:
        return(True)

# Lista de libros
def listalibros():
    conn = sqlite3.connect(co.BD)
    df = pd.read_sql_query("select id_libros, isbn, titulo, autor, leidom, leidoa, portada, resumen, categoria, fechapublicacion, editorial, paginas, comentario from libros", conn)
    conn.close()
    return(df)

def lista_titulos():
    conn = sqlite3.connect(co.BD)
    consulta = 'select distinct titulo from libros order by titulo'
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    return(df)

def lista_autores():
    conn = sqlite3.connect(co.BD)
    consulta = 'select distinct autor from libros order by autor'
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    return(df)

def tarjeta(col, titulo, valor, unidad, fecha, fuente, delta):
    with col:
        st.metric(label=f"{titulo}", value=f"{valor} {unidad}", delta=delta, delta_color="normal", help=f"Vigencia: {fecha}  Fuente: {fuente}")

def obtener_anomes_seismeses_antes(anomes, meses):
    """
    Obtiene el año y mes correspondientes a una cantidad de meses antes de un año y mes dado.
    Args:
        anomes (str): Año y mes en formato 'YYYYMM'
        meses (int): Cantidad de meses a restar
    Returns:
        str: Año y mes resultante en formato 'YYYYMM'
    """
    try:
        anio = int(anomes[:4])
        mes = int(anomes[4:])
        
        total_meses = anio * 12 + mes - meses
        nuevo_anio = total_meses // 12
        nuevo_mes = total_meses % 12
        
        if nuevo_mes == 0:
            nuevo_mes = 12
            nuevo_anio -= 1
        
        return f"{nuevo_anio:04d}{nuevo_mes:02d}"
    except ValueError:
        print("Error: El formato de 'anomes' debe ser 'YYYYMM'")
        return None
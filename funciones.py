
import os
import random
import sqlite3

from anyio import Path

import streamlit as st
import requests
from datetime import datetime, date

from holidays_co import is_holiday_date

import json
import constantes as co
import xmltodict
import pandas as pd
import bcrypt

from zoneinfo import ZoneInfo

# Funcion para consultar el TRM dada una fecha
def obtener_trm():
    # Realizar la solicitud
    URL_TRM = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=100&$order=vigenciadesde%20DESC"
    response = requests.get(URL_TRM, timeout=10)
    response.raise_for_status()
        
    data = response.json()
        
    if not data:
        return None
    listatrm = []
    listavigencia = []
    for registro in data:
        listatrm.append(float(registro["valor"]))
        listavigencia.append(registro["vigenciadesde"])
    return(listatrm, listavigencia)

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

def almacenardtf():
    fechahoy = datetime.now()
    datos = obtener_indicador('DTF', 'DAILY', fechahoy, 'LATEST')
    dtf = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs'][0]['generic:ObsValue']['@value']
    f1 = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs'][0]['generic:ObsDimension']['@value']
    f2 = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs'][6]['generic:ObsDimension']['@value']

    conn = sqlite3.connect(co.BD)
    consulta= 'select count(*)  as total from dtf where  fechainicio >= ' + f1 + ' and  fechafin <= ' + f2 
    df = pd.read_sql_query(consulta, conn)
    totales = df['total'][0]

    if totales == 0:
        cursor = conn.cursor()
        sqlinser = 'insert into dtf ( fechainicio, fechafin, valor) values ( ?, ?, ?)'
        datos = (f1, f2, dtf )
        cursor.execute(sqlinser, datos)
        conn.commit()
        cursor.close()
    conn.close()
    return()

def dtfactual():
    fecha = datetime.now()
    wfecha = fecha.strftime("%Y%m%d")
    conn = sqlite3.connect(co.BD)
    consulta= 'select count(*) as total from dtf where ' + wfecha + ' between fechainicio and fechafin' 
    df = pd.read_sql_query(consulta, conn)
    if df['total'][0] == 0:
        almacenardtf()
    consulta= 'select fechainicio, fechafin, valor from dtf where ' + wfecha + ' between fechainicio and fechafin' 
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    return(df['valor'][0], df['fechainicio'][0], df['fechafin'][0])

# Devuelve la lista historica del DTF
def dtftodos():
    conn = sqlite3.connect(co.BD)
    consulta= 'select valor from dtf order by fechainicio' 
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    dfanterior = df['valor'][len(df)-2]
    return(df, dfanterior)

def evento(fecha):
    wfecha = str(fecha.strftime("%Y%m%d"))
    conn = sqlite3.connect(co.BD)
    cursor = conn.cursor()
    consulta = "select evento from eventos where fecha =  '" + wfecha + "'"
    cursor.execute(consulta)
    res = cursor.fetchone()
    if res is None:
        res = ' '
    else:
        res = res[0]
    conn.close()
    return(res)

def obtener_fecha_hora_local(zona: str = None) -> datetime:
    """
    Retorna la fecha y hora local actual.
    Si se especifica una zona horaria válida (ej. 'America/Bogota'),
    devuelve la hora en esa zona.
    """
    try:
        if zona:
            return datetime.now(ZoneInfo(zona))
        else:
            # Hora local del sistema
            return datetime.now()
    except Exception as e:
        raise ValueError(f"Error al obtener la hora: {e}")
    
def eventos():
    conn = sqlite3.connect(co.BD)
    sqlsp = "select fecha, evento from eventos order by fecha DESC"
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()
    return(df)

def datosdtf():
    conn = sqlite3.connect(co.BD)
    sqlsp = "select fechainicio, fechafin, valor from dtf order by fechainicio DESC"
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()
    return(df)

def registrar_usuario(nombre: str, clave: str):
    if not nombre  or not clave:
        raise ValueError("Usuario y clave no pueden estar vacíos.")

    # Generar hash seguro con bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(clave.encode("utf-8"), salt)

    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, clave) VALUES (?, ?)",
            (nombre, hashed.decode("utf-8"))
        )
        conn.commit()
        print(f"Usuario '{nombre}' registrado correctamente.")
    except sqlite3.IntegrityError:
        print(f"Error: el usuario '{nombre}' ya existe.")
    finally:
        conn.close()

def verificar_usuario(nombre: str, clave: str) -> bool:
    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM usuarios WHERE nombre = ?", (nombre,))
    row = cursor.fetchone()
    conn.close()

    if row:
        stored_hash = row[0].encode("utf-8")
        return bcrypt.checkpw(clave.encode("utf-8"), stored_hash)
    return False


def es_festivo_colombia(fecha_str):
    """
    Verifica si una fecha es festivo en Colombia.
    
    Parámetros:
        fecha_str (str): Fecha en formato 'YYYY-MM-DD'
    
    Retorna:
        bool: True si es festivo, False si no.
    """
    try:
        # Convertir string a objeto date
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        
        # Verificar si es festivo
        return is_holiday_date(fecha)
    
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use 'YYYY-MM-DD'.")

# Funcion para mostrar todos los dias con su pico y placa, resaltando el dia actual
def mostrartodopyp(fecha):
    # fecha = datetime.now()
    ndia = fecha.weekday()
    texto = ''
    contador = 0
    if es_festivo_colombia(fecha.strftime("%Y-%m-%d")):
        resaltar = 'Hoy es festivo, no aplica Pico y Placa'
    else:
        for dia in co.DIAS:
            if ndia == contador:
                resaltar = dia + ': ' + co.PYP[contador]
            texto = texto + dia + ': ' + co.PYP[contador] + '  '
            contador += 1
    return(texto, resaltar) 

def obtener_ibr():
    fechahoy = datetime.now()
    datos = obtener_indicador('IBR', 'DAILY', fechahoy, 'LATEST')
    valores = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series'][1]['generic:Obs']
    dibr = valores['generic:ObsValue']['@value']
    return(dibr)

def obtener_uvr():
    fechahoy = datetime.now()
    datos = obtener_indicador('UVR', 'DAILY', fechahoy, 'LATEST')
    valores = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series'][1]['generic:Obs']
    duvr = 0
    duvr = valores[0]['generic:ObsValue']['@value']
    return(duvr)   

def obtener_ibr():
    fechahoy = datetime.now()
    datos = obtener_indicador('IBR', 'DAILY', fechahoy, 'LATEST')
    valores = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series'][1]['generic:Obs']
    dibr = valores['generic:ObsValue']['@value']
    return(dibr)
   
def obtener_ipc():
    fechahoy = datetime.now()
    ipc = co.IPC2025
    return(ipc)

def obtener_smmlv():
    fechahoy = datetime.now()
    smmlv = co.SMMLV2026
    return(smmlv)

def obtener_tib():
    fechahoy = datetime.now()
    datos = obtener_indicador('IR', 'DAILY', fechahoy, 'LATEST')
    valor = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']['generic:ObsValue']['@value']
    return(valor)

def obtener_colcap():
    fechahoy = datetime.now()
    datos = obtener_indicador('COLCAP', 'MONTHLY', fechahoy, 'LATEST')
    valor = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']['generic:ObsValue']['@value']
    return(valor)

def obtener_tpm():
    fechahoy = datetime.now()
    datos = obtener_indicador('CBR', 'DAILY', fechahoy, 'LATEST')
    valor = datos['S:Envelope']['S:Body']['impl:GetGenericDataResponse']['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']['generic:ObsValue']['@value']
    return(valor)

def obtener_indicador_varios(indicador):
    findicadores = {
        'UVR': obtener_uvr,
        'IBR': obtener_ibr,
        'IPC': obtener_ipc,
        'SMMLV': obtener_smmlv,
        'TIB': obtener_tib,
        'COLCAP': obtener_colcap,
        'TPM': obtener_tpm
    }
    res = findicadores[indicador]()
    return(res)

def formatoindicador(indicador, dato):
    if indicador in ['IBR','TIB','TPM']:
        datof = str(' {:,.2f} % '.format(float(dato)))    
    elif indicador == 'UVR':
        datof = str(' ${:,.4f} '.format(float(dato)))
    elif indicador == 'IPC':
        datof = str(' {:,.2f} % '.format(float(dato)))
    else:
        datof = str(' ${:,.2f} '.format(float(dato)))
    return(datof)

def calcular_indicadores(trm):
# Consultar y mostrar los valores para los indicadores UVR, IBR, IPC, TIB, SMMLV, COLCAP, TPM
    fecha = datetime.now()
    wfecha = fecha.strftime("%Y%m%d")
    dis = '        '
    textoindicadores = []
    for i in co.INDICADORES:
        try:
            valor = obtener_indicador_varios(i)
        except:
            valor = 0
        svalor = str(valor)
        if i == 'SMMLV':
            tabla = str.maketrans({'$': '', ',': ''})
            resd = svalor.translate(tabla)
            smmlvusd = str('USD {:,.2f} '.format(float(resd) / trm))
            textoindicadores.append(i + ': COP' + formatoindicador(i, svalor) + dis + ' SMMLV: ' + smmlvusd + dis)
        elif i == 'IPC':
            textoindicadores.append(i + ' 2025:  ' + formatoindicador(i, svalor) + dis)
        else:
#        elif i not in ['IBR', 'UVR']:
            textoindicadores.append(i + ':  ' + formatoindicador(i, svalor) + dis)
        # if i == 'IBR':
        #     wibr = svalor
        # if i == 'UVR':
        #     wuvr = svalor

    textindicadores = "   ".join(map(str, textoindicadores))
    return(textindicadores)

from datetime import datetime
import pandas as pd
import sqlite3 as sql

import constantes as co

def lista_unidades():
    conn = sql.connect(co.BD)
    consulta = 'select distinct Unidad from serviciospublicos order by Unidad'
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    return(df)

def ultimafactura(unidad):
    conn = sql.connect(co.BD)
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(AnoMesFacturacion) FROM serviciospublicos WHERE Unidad = ?', (unidad,))
    res = cursor.fetchall()
    valor = res[0][0]
    conn.close()
    return(str(valor))

def consumospromedios():
    conn = sql.connect(co.BD)
    periodo = '01062025'
    sqlsp = f'SELECT Unidad, AVG(Acueducto), AVG(Energia), AVG(Gas) FROM serviciospublicos WHERE InicioConsumo >= {periodo} GROUP BY Unidad'
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()
    return(df)

def costototal():
    conn = sql.connect(co.BD)
    periodo = '01062025'
    sqlsp = f'SELECT Unidad, SUM(CostoServicio) FROM serviciospublicos WHERE InicioConsumo >= {periodo} GROUP BY Unidad'
    df = pd.read_sql_query(sqlsp, conn)
    conn.close()
    return(df)

def costoactualserviciopublico(unidad, anomes):
    conn = sql.connect(co.BD)
    cursor = conn.cursor()
    cursor.execute('SELECT CostoServicio FROM serviciospublicos WHERE Unidad = ? and AnoMesFacturacion = ? ', (unidad, anomes))
    res = cursor.fetchall()
    valor = res[0][0]
    conn.close()
    return(valor)

def gastoservicios(agrupador):
    wfecha = datetime.now()
    wanomes = datetime.strftime(wfecha,'%Y%m')
    conn = sql.connect(co.BD)
    cursor = conn.cursor()
    wselect = f'select anomes, concepto, sum(valor) from gastos WHERE anomes = {wanomes} and id_agrupador = {agrupador} group by anomes, concepto'
    cursor.execute(wselect)
    res = cursor.fetchall()
    anomes = res[0][0]
    concepto = res[0][1]
    gasto = res[0][2]
    conn.close()
    return(anomes, concepto, gasto)

def consumodiariounidadmes(unidad):
    conn = sql.connect(co.BD)

    sqlcp = f"""
        SELECT
            Unidad, 
            AnoMesFacturacion,
            Energia/DiasConsumo as Consumo_Energia, 
            Acueducto/DiasConsumo as Consumo_Acueducto, 
            Gas/DiasConsumo as Consumo_Gas,
            CEnergia/DiasConsumo as Costo_Energia, 
            CAcueducto/DiasConsumo as Costo_Acueducto, 
            CGas/DiasConsumo as Costo_Gas,
            OtrasEntidades/DiasConsumo as Costo_OtrasEntidades,
            CostoServicio/DiasConsumo as Costo_Total
        FROM serviciospublicos
        WHERE Unidad = '{unidad}'
        GROUP BY Unidad, AnoMesFacturacion
        """
    df = pd.read_sql_query(sqlcp, conn)
    conn.close()
    return(df)

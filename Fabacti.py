import streamlit as st

import funciones as fu
import constantes as co
import acceso as ac

def fabacti():

  fechahoy = fu.presentar_encabezado()
  procesos = st.text('Cargando la información requerida, ... de las fuentes: Yahoo/Finance, Banco de la República, Datos abiertos de Colombia, Open Meteo ... por favor espere  ...')
  st.title("Indicadores Económicos y Clima")
# Indicadores
  wtrm = fu.obtener_trm()
  valor_trm = '$ {:,.2f} '.format(float(wtrm))
  valor_ibr = ' {:,.2f} %'.format(float(fu.obtener_ibr()))
  valor_dtf = ' {:,.2f} %'.format(float(fu.obtener_dtf()))
  valor_oro = '$ {:,.2f} '.format(fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("oro")))
  valor_euro = '$ {:,.2f} '.format(fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("euro")))
  valor_cafe = fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("cafe"))
  valor_cafe = valor_cafe / 100
  valor_cafe = 'US$ {:,.2f} '.format(valor_cafe)
  valor_petroleo = 'US$ {:,.2f} '.format(fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("petroleo")))
  clima = fu.obtener_clima()

  #st.write(valor_ibr + ' - IBR (Indicador Bancario de Referencia)')
  #st.write(valor_dtf + ' - DTF (Depósito a Término)')
  procesos.empty()

  c1, c2, c3, c4 = st.columns(4, border = True)
  fu.tarjeta(c1, "TRM - Dólar", valor_trm, "", fechahoy, "Banco de la República", "")
  fu.tarjeta(c2, "Euro", valor_euro, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c3, "Café", valor_cafe, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c4, "Oro", valor_oro, "", fechahoy, "Yahoo Finance", "")
  
  c5, c6, c7, c8 = st.columns(4, border = True)
  fu.tarjeta(c5, "Petróleo", valor_petroleo, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c6, "IBR", valor_ibr, "", fechahoy, "Banco de la República <Inicia aplicacion 01/01/2027>", "")
  fu.tarjeta(c7, "DTF", valor_dtf, "", fechahoy, "Banco de la República <Finaliza aplicacion 31/12/2026", "")
  fu.tarjeta(c8, "Clima", clima, "°C", fechahoy, "Open Meteo", "")
 
  st.title("Pico y Placa, Frase del Día y Libro Recomendado")
# Muestra la información de Pico y Placa, Frase del día y Libro recomendado
  picoplaca, frases, libro = st.columns(3, border = True)
  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp(fechahoy)
    st.text('Pico y Placa', help=co.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with frases:
    # Obtener frase del dia
    wfrase, wautor = fu.frase()
    st.text('FRASE DEL DIA', help=co.NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with libro:
    st.text('Libro recomendado', help=co.NOTASLIBRO)
    libro = fu.obtener_imagen_aleatoria('img/')
    st.image(libro, width=100)

  st.divider()
  st.write(co.COPYRIGHT)
  procesos.empty()

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        page_icon="🌎",
        initial_sidebar_state = "expanded"
        )
 
    ac.acceso()
    if 'usuario' in st.session_state:
        fabacti()

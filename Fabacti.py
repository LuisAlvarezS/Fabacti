
import streamlit as st

import funciones as fu
import funcionesindicadores as fi
import constantes as co
import acceso as ac

def fabacti():

  fechahoy = fu.presentar_encabezado()
  procesos = st.text('Cargando la información requerida, ... por favor espere  ...')

# Proceso de TRM
  valor_trm, delta_trm = fu.obtener_trm()
  valor_trm = '$ {:,.2f} '.format(float(valor_trm))
  delta_trm = '{:,.2f} '.format(float(delta_trm))

# Clima
  clima = fu.obtener_clima()

# Otros indicadores
  valor_oro = '$ {:,.2f} '.format(fi.valor_oro())
  valor_euro = '$ {:,.2f} '.format(fi.valor_euro())
  valor_cafe = 'US$ {:,.2f} '.format(fi.valor_cafe())
  valor_petroleo = 'US$ {:,.2f} '.format(fi.valor_petroleo())

  procesos.empty()

  c1, c2, c3 = st.columns(3, border = True)
  fu.tarjeta(c1, "TRM - Dólar", valor_trm, "", fechahoy, "Banco de la República", delta_trm)
  fu.tarjeta(c2, "Euro", valor_euro, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c3, "Café", valor_cafe, "", fechahoy, "Yahoo Finance", "")

  c4, c5, c6 = st.columns(3, border = True)
  fu.tarjeta(c4, "Oro", valor_oro, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c5, "Petróleo", valor_petroleo, "", fechahoy, "Yahoo Finance", "")
  fu.tarjeta(c6, "Clima", clima, "°C", fechahoy, "Open Meteo", "")

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

import streamlit as st

import funciones as fu
import constantes as co
import acceso as ac

def fabacti():
  fechahoy = fu.presentar_encabezado()
# indicadores económicos y clima
  if 'indicadores' not in st.session_state:
    st.session_state['indicadores'] = True
  if st.session_state['indicadores']:
    with st.spinner( co.APP + " - Procesando datos ... Espere por favor ... ", show_time=True):
      #procesos = st.text('Cargando la información requerida, ... de las fuentes: Superfinanciera (datos.gov.co),Yahoo/Finance, Banco de la República, Datos abiertos de Colombia, Open Meteo ... por favor espere  ...')
      st.session_state['indicadores'] = False

    # Obtener los indicadores económicos y clima
      wtrm, fuentetrm, vigenciatrm, deltatrm, df_trm = fu.obtener_trm(fechahoy)
      valor_trm = '$ {:,.2f} '.format(float(wtrm))
      deltatrm = ' {:,.2f} '.format(float(deltatrm))

      valor_euro, lista_euro, delta_euro, werror  = fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("euro"))
      valor_euro = '$ {:,.2f} '.format(float(valor_euro))
      delta_euro = ' {:,.2f} '.format(float(delta_euro))

      valor_cafe, lista_cafe, delta_cafe, werror = fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("cafe"))
      valor_cafe = valor_cafe / 100
      delta_cafe = delta_cafe / 100
      delta_cafe = ' {:,.2f} '.format(float(delta_cafe))
      valor_cafe = 'US$ {:,.2f} '.format(valor_cafe)

      valor_oro, lista_oro, delta_oro, werror = fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("oro"))
      valor_oro = 'US$ {:,.2f} '.format(valor_oro)
      delta_oro = ' {:,.2f} '.format(float(delta_oro))

      valor_petroleo, lista_petroleo, delta_petroleo, werror = fu.obtener_precio_cierre(fu.obtener_symbol_yfinance("petroleo"))
      valor_petroleo = 'US$ {:,.2f} '.format(valor_petroleo)
      delta_petroleo = ' {:,.2f} '.format(float(delta_petroleo))

      clima = fu.obtener_clima()

# Obtener frase del dia
      wfrase, wautor = fu.frase()
      
      st.session_state['frase'] = wfrase
      st.session_state['autor'] = wautor

      st.session_state['valor_trm'] = valor_trm
      st.session_state['deltatrm'] = deltatrm
      st.session_state['df_trm'] = df_trm
      st.session_state['fuentetrm'] = fuentetrm
      st.session_state['vigenciatrm'] = vigenciatrm

      st.session_state['valor_euro'] = valor_euro
      st.session_state['delta_euro'] = delta_euro
      st.session_state['lista_euro'] = lista_euro

      st.session_state['valor_cafe'] = valor_cafe
      st.session_state['delta_cafe'] = delta_cafe
      st.session_state['lista_cafe'] = lista_cafe

      st.session_state['valor_oro'] = valor_oro
      st.session_state['delta_oro'] = delta_oro
      st.session_state['lista_oro'] = lista_oro

      st.session_state['valor_petroleo'] = valor_petroleo
      st.session_state['delta_petroleo'] = delta_petroleo
      st.session_state['lista_petroleo'] = lista_petroleo
      st.session_state["werror"] = werror
      st.session_state['clima'] = clima

  st.title(co.APP)
  #fu.formato_fecha()
  c1, c2, c3 = st.columns(3, border = True)
  c4, c5, c6 = st.columns(3, border = True)
  fu.tarjeta(c1, "TRM - Dólar", st.session_state['valor_trm'], "", co.NOTASTRM, st.session_state['vigenciatrm'], st.session_state['fuentetrm'], st.session_state['deltatrm'], st.session_state['df_trm'],"line")
  if st.session_state["werror"] == "":
    fu.tarjeta(c2, "Euro", st.session_state['valor_euro'], "", co.NOTASEURO, fechahoy, "Yahoo Finance", st.session_state['delta_euro'], st.session_state['lista_euro'],"line") 
    fu.tarjeta(c3, "Café", st.session_state['valor_cafe'], "", co.NOTASCAFE, fechahoy, "Yahoo Finance", st.session_state['delta_cafe'], st.session_state['lista_cafe'],"line")
    fu.tarjeta(c4, "Oro", st.session_state['valor_oro'], "", co.NOTASORO, fechahoy, "Yahoo Finance", st.session_state['delta_oro'], st.session_state['lista_oro'],"line")
    fu.tarjeta(c5, "Petróleo", st.session_state['valor_petroleo'], "", co.NOTASPETROLEO, fechahoy, "Yahoo Finance", st.session_state['delta_petroleo'], st.session_state['lista_petroleo'],"line")
  fu.tarjeta(c6, "Clima", st.session_state['clima'], "°C", co.NOTASCLIMA, fechahoy, "Open Meteo",None,None,"line")

  st.write(f' Falla al consultar los indicadores, {st.session_state["werror"]} ') if st.session_state["werror"] != "" 

# Muestra la información de Pico y Placa, Frase del día y Libro recomendado
  picoplaca, frases, libro = st.columns(3, border = True)
  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp(fechahoy)
    st.text('Pico y Placa', help=co.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with frases:
  # Obtener frase del dia
    st.text('FRASE DEL DIA', help=co.NOTASFRASE) 
    st.write(st.session_state['frase'])
    st.write(' [' + st.session_state['autor'] + ']')

  with libro:
    st.text('Libro recomendado', help=co.NOTASLIBRO)
    libro = fu.obtener_imagen_aleatoria('img/')
    st.image(libro, width=100)

  st.divider()
  st.write(co.COPYRIGHT)

if __name__ == '__main__':
    st.set_page_config(
        page_title="Fabacti",
        layout="wide",
        page_icon="🌎",
        initial_sidebar_state = "expanded"
        )
 
    ac.acceso()
    if 'usuario' in st.session_state:
        fabacti()

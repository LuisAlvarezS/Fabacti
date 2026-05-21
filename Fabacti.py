
import streamlit as st
from datetime import datetime, timedelta

from funciones import frase, obtener_imagen_aleatoria, obtener_trm, mostrartodopyp
import constantes as const

def fabacti():
  proceso = st.text('Cargando la información requeridsa, ... por favor espere ...')

  # Encabezado
  st.write(const.ENCABEZADO)
  fechahoy = datetime.now()  
  ndia = const.DIAS[fechahoy.weekday() - 1]
  nmes = const.MESES[fechahoy.month - 1]
  st.write(ndia + ',' + str(fechahoy.day - 1) + ' de ' + nmes + ' de ' + str(fechahoy.year))

  listatrm = obtener_trm()
  trm = float(listatrm[0])
  ftrm = '${:,.2f} '.format(trm)
  trmayer = float(listatrm[1])
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)
  listatrm.reverse()

  trm, picoplaca, frases, libro = st.columns(4, border = True)  
  
  with trm:
    st.metric('**TRM  - Dólar**', ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=const.NOTASTRM)
  
  with frases:
    # Obtener frase del dia
    wfrase, wautor = frase()
    st.text('FRASE DEL DIA', help=const.NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with picoplaca:
    picoyplaca, parte_resaltar = mostrartodopyp()
    st.text('Pico y Placa', help=const.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with libro:
    st.text('Libro del Día', help=const.NOTASLIBRO)
    libro = obtener_imagen_aleatoria('img/')
    st.image(libro, width=200)

  st.write(' ...En construccion  ...')

  st.write(const.COPYRIGHT)
  proceso.empty()

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

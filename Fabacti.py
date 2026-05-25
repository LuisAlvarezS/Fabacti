
import streamlit as st
from datetime import datetime, timedelta

import funciones as fu
import constantes as con

def fabacti():
  proceso = st.text('Cargando la información requerida, ... por favor espere ...')

  # Encabezado
  st.write(con.ENCABEZADO)
  fechahoy = datetime.now()  
  ndia = con.DIAS[fechahoy.weekday()]
  nmes = con.MESES[fechahoy.month - 1]
  st.write(ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year))

  listatrm = fu.obtener_trm()
  trm = float(listatrm[0])
  ftrm = '${:,.2f} '.format(trm)
  trmayer = float(listatrm[1])
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)
  listatrm.reverse()

  # Obtener DTF
  #dtf = dtfactual()
  dtf = str('{:,.2f} '.format(float(fu.dtfactual())))
  #dtfhistorico, deltadtf = dtftodos()
  #deltadtf = '{:,.2f} '.format(float(dtf) - deltadtf)

  trm, dtf1, picoplaca, frases, libro = st.columns(5, border = True)  
  
  with trm:
    st.metric('**TRM  - Dólar**', ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=con.NOTASTRM)
  
  with dtf1:
    dtf1.metric('**DTF**', dtf + ' %', 0, border = False, width='stretch', height='content',  help=con.NOTASDTF)

  with frases:
    # Obtener frase del dia
    wfrase, wautor = fu.frase()
    st.text('FRASE DEL DIA', help=con.NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp()
    st.text('Pico y Placa', help=con.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with libro:
    st.text('Libro recomendado', help=con.NOTASLIBRO)
    libro = fu.obtener_imagen_aleatoria('img/')
    st.image(libro, width=200)

  st.write(' ...En construccion  ...')

  st.write(con.COPYRIGHT)
  proceso.empty()

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

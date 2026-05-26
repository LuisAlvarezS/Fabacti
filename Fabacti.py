
import streamlit as st
from datetime import datetime, timedelta

import funciones as fu
import constantes as co

def fabacti():
  # Encabezado
  st.write(co.ENCABEZADO)
  fechahoy = datetime.now()  
  ndia = co.DIAS[fechahoy.weekday()]
  nmes = co.MESES[fechahoy.month - 1]
  st.write(ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year))

  proceso = st.text('Cargando la información requerida, ... por favor espere ...')

# Proceso de TRM
  listatrm = fu.obtener_trm()
  trm = float(listatrm[0])
  ftrm = '${:,.2f} '.format(trm)
  trmayer = float(listatrm[1])
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)
  listatrm.reverse()
  
# Proceso de DTF
  # dtf = fu.dtfactual()
  # dtf = str('{:,.2f} '.format(float(dtf)))
  # datos = fu.dtfhistoricos()
  # dtfhistorico = datos
  # deltadtf = '{:,.2f} '.format(float(dtf) - float(datos[1]))
  dtf = str('{:,.2f} '.format(float(fu.dtfactual())))
  dtfhistorico, deltadtf = fu.dtftodos()
  deltadtf = '{:,.2f} '.format(float(dtf) - deltadtf)
  proceso.empty()

  trm, dtf1, picoplaca, frases, libro = st.columns(5, border = True)  
  
  with trm:
    st.metric('**TRM  - Dólar**', ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=co.NOTASTRM)
  
  with dtf1:
    dtf1.metric('**DTF**', dtf + ' %', deltadtf, delta_arrow='auto', delta_color="normal", chart_data=dtfhistorico, chart_type='line', width='stretch', height='content',  help=co.NOTASDTF)

  with frases:
    # Obtener frase del dia
    wfrase, wautor = fu.frase()
    st.text('FRASE DEL DIA', help=co.NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp()
    st.text('Pico y Placa', help=co.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with libro:
    st.text('Libro recomendado', help=co.NOTASLIBRO)
    libro = fu.obtener_imagen_aleatoria('img/')
    st.image(libro, width=200)

  st.write(co .COPYRIGHT)
  proceso.empty()

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

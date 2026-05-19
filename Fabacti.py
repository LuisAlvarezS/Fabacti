
import streamlit as st
from datetime import datetime, timedelta
from funciones import frase, obtener_trm
import constantes as const

def fabacti():
  # Encabezado
  st.write(const.ENCABEZADO)

  fechahoy = datetime.now()
  ayer = fechahoy - timedelta(days=1)
  proximasemana = fechahoy + timedelta(days=6)
  fecha = datetime.now().strftime("%Y-%m-%d")
  ayer = ayer.strftime("%Y-%m-%d")
  proximasemana = proximasemana.strftime("%Y-%m-%d")
  trm = obtener_trm(fecha)  
  st.write(trm)
  ftrm = '${:,.2f} '.format(trm)
  trmayer = obtener_trm(ayer)
  ftrmayer = '${:,.2f} '.format(trmayer)
  deltatrm = trm - trmayer
  fdeltatrm = '${:,.2f} '.format(deltatrm)

  trm, frases = st.columns(2, border = True)  
  trm.metric('**TRM  - Dólar**', ftrm, fdeltatrm, width='stretch', height='content', chart_type='line',help=const.NOTASTRM)

  # Obtener frase del dia
  wfrase, wautor = frase()
  
  frases.write(f'**FRASE DEL DIA**') 
  frases.write(wfrase)
  frases.write(' [' + wautor + ']')

  st.write(' ...En construccion  ...')

  st.write(const.COPYRIGHT)

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

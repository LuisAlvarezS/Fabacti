
import streamlit as st
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from funciones import frase, obtener_trm
import constantes as const

def fabacti():
  proceso = st.text('Cargando información, por favor espere...')

  # Encabezado
  st.write(const.ENCABEZADO)

  fechahoy = datetime.now(tz=ZoneInfo("America/Bogota"))  
  #ayer = fechahoy - timedelta(days=1)
  #proximasemana = fechahoy + timedelta(days=6)
  fecha = fechahoy.strftime(" %A, %d de %B de %Y")
  st.write(fecha)
  #ayer = ayer.strftime("%Y-%m-%d")
  #proximasemana = proximasemana.strftime("%Y-%m-%d")
  listatrm = obtener_trm()
  trm = float(listatrm[0])
  ftrm = '${:,.2f} '.format(trm)
  trmayer = float(listatrm[1])
  #ftrmayer = '${:,.2f} '.format(trmayer)
  deltatrm = trm - trmayer
  fdeltatrm = '${:,.2f} '.format(deltatrm)
  listatrm.reverse()

  trm, frases = st.columns(2, border = True)  
  trm.metric('**TRM  - Dólar**', ftrm, fdeltatrm,chart_data=listatrm, chart_type='line', width='stretch', height='content', help=const.NOTASTRM)

  # Obtener frase del dia
  wfrase, wautor = frase()
  
  frases.write(f'**FRASE DEL DIA**') 
  frases.write(wfrase)
  frases.write(' [' + wautor + ']')

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

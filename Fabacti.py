
import streamlit as st
import datetime
from funciones import obtener_trm
import constantes as const

def fabacti():
  # Encabezado
  st.write(const.ENCABEZADO)
  fecha = datetime.now()
  trm = float(obtener_trm(fecha))
  
  ftrm = '${:,.2f} '.format(trm)

  st.write(f" :blue[La TRM del día {fecha.strftime('%d-%m-%Y')} es de :red[{ftrm}]]")
 
  st.write(' ...En construccion  ...')

  st.write(const.COPYRIGHT)

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

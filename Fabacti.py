
import streamlit as st
from datetime import datetime
from funciones import obtener_trm
import constantes as const

def fabacti():
  # Encabezado
  st.write(const.ENCABEZADO)
  #fecha = datetime.now()
  fecha = datetime.now().strftime("%Y-%m-%d")
  trm = obtener_trm(fecha)  
  #ftrm = '${:,.2f} '.format(trm)

  st.write(f"TRM {trm['fecha']}: ${trm['valor']:,.2f} COP/USD")
 
  st.write(' ...En construccion  ...')

  st.write(const.COPYRIGHT)

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded"
        )
    fabacti()

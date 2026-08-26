
import streamlit as st

import funciones as fu
import constantes as co
import acceso as ac

def fabacti():

  fechahoy = fu.presentar_encabezado()
  proceso = st.text('Cargando la información requerida, ... por favor espere  ...')

# Proceso de TRM
  valor_trm, delta_trm = fu.obtener_trm()
  trm = '$ {:,.2f} '.format(float(valor_trm))
  delta_trm = '{:,.2f} '.format(float(delta_trm))

  proceso.empty()

  c1, c2, c3, c4, c5 = st.columns(5, border = True)
  fu.tarjeta(c1, "TRM - Dólar", trm, "", fechahoy, "Banco de la República", delta_trm)

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
    st.image(libro, width=200)

  st.divider()
  st.write(co.COPYRIGHT)
  proceso.empty()

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

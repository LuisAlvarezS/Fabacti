import streamlit as st

import funciones as fu
import constantes as co
import acceso as ac

def fabacti():
  fechahoy = fu.presentar_encabezado()
  if 'indicadores' not in st.session_state:
    st.session_state['indicadores'] = True
  if st.session_state['indicadores']:
    with st.spinner( co.APP + " - Procesando datos ... Espere por favor ... ", show_time=True):
      st.session_state['indicadores'] = False
      wtrm, fuentetrm, vigenciatrm, deltatrm, df_trm = fu.obtener_trm(fechahoy)
      valor_trm = '$ {:,.2f} '.format(float(wtrm))
      deltatrm = ' {:,.2f} '.format(float(deltatrm))
      clima = fu.obtener_clima()
      wfrase, wautor = fu.frase()
      
      st.session_state['frase'] = wfrase
      st.session_state['autor'] = wautor

      st.session_state['valor_trm'] = valor_trm
      st.session_state['deltatrm'] = deltatrm
      st.session_state['df_trm'] = df_trm
      st.session_state['fuentetrm'] = fuentetrm
      st.session_state['vigenciatrm'] = vigenciatrm
      st.session_state['clima'] = clima

  st.title(co.APP)

  trm, picoplaca, frases, libro = st.columns(4, border = True)
  with trm:
    ayuda_trm = co.NOTASTRM + ' Vigencia desde el 2026-01-01 hasta ' + st.session_state['vigenciatrm'] + ' ' + st.session_state['fuentetrm']
    st.metric(label="TRM - Dólar", value=st.session_state['valor_trm'], delta=st.session_state['deltatrm'], delta_color="normal",help=ayuda_trm, border= False, chart_data=st.session_state['df_trm'], chart_type="line")
    
  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp(fechahoy)
    st.text('Pico y Placa', help=co.NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])
  with frases:
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

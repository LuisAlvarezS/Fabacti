
from datetime import timedelta

import streamlit as st

import funciones as fu
import constantes as co
import acceso as ac

def fabacti(usuario=None):
  
  # Encabezado
  st.write( ":red[FABACTI] :registered: ")
  st.sidebar.write('**Usuario** :blue[**' + usuario + '**]')
  st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())
  st.sidebar.write(co.ENCABEZADO)
  fechacol = fu.obtener_fecha_hora_local("America/Bogota")
  fechahoy = fechacol.date()  
  ndia = co.DIAS[fechahoy.weekday()]
  nmes = co.MESES[fechahoy.month - 1]
  # Veriificar si es festivo en Colombia
  is_festivo = fu.es_festivo_colombia(str(fechahoy))
  wevento = fu.evento(fechahoy)
  
  if is_festivo:
    mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) + ' -> ' + wevento + ' :red[**FESTIVO**]'
  else:
    mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) + ' -> ' + wevento
  st.success(mensaje, icon="📆")
  
  proceso = st.text('Cargando la información requerida, ... por favor espere ...')

# Proceso de TRM
  listatrm = fu.obtener_trm()
  trm = float(listatrm[0])
  ftrm = '${:,.2f} '.format(trm)
  trmayer = float(listatrm[1])
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)
  listatrm.reverse()

# Calcular los indicadores UVR, IBR, IPC, TIB, SMMLV, COLCAP, TPM
  textoindicadores = fu.calcular_indicadores(trm)

# Proceso de DTF
  valor_dtf, fechainicio_dtf, fechafin_dtf = fu.dtfactual()
  fechainicio_dtf = str(fechainicio_dtf)[0:4] + '-' + str(fechainicio_dtf)[4:6] + '-' + str(fechainicio_dtf)[6:8]
  fechafin_dtf = str(fechafin_dtf)[0:4] + '-' + str(fechafin_dtf)[4:6] + '-' + str(fechafin_dtf)[6:8]
  dtf = str('{:,.2f} '.format(float(valor_dtf)))
  dtfhistorico, deltadtf = fu.dtftodos()
  deltadtf = '{:,.2f} '.format(float(dtf) - deltadtf)
  proceso.empty()

# # Preparar infomacion IBR 
#   ayer = fechahoy - timedelta(days=1)
#   wayer = ayer.strftime("%Y%m%d")
#   wibr = fu.obtener_indicador_varios('IBR')
#   wibr = str('{:,.2f} '.format(float(wibr)))

  trm, dtf1 = st.columns(2, border = True)   
  with trm:
    st.metric('**TRM  - Dólar**', ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=co.NOTASTRM)
  
  with dtf1:
    dtf1.metric('**DTF** Vigencia: ' + str(fechainicio_dtf) + ' - ' + str(fechafin_dtf), dtf + ' %', deltadtf, delta_arrow='auto', delta_color="normal", chart_data=dtfhistorico, chart_type='line', width='stretch', height='content',  help=co.NOTASDTF)

  # with ibr:
  #   st.metric('**IBR**', wibr + ' %', delta_arrow='auto', delta_color="normal", chart_data=None, chart_type='line', width='stretch', height='content', help=co.NOTASIBR)

  st.write('---')
  # Mostrar indicadores economicos adicionales 
  pos = textoindicadores.find('SMMLV')
  st.text(textoindicadores[0:pos-1])
  st.text(textoindicadores[pos:])
  st.write('---')

  picoplaca, frases, libro = st.columns(3, border = True)
  with frases:
    # Obtener frase del dia
    wfrase, wautor = fu.frase()
    st.text('FRASE DEL DIA', help=co.NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with picoplaca:
    picoyplaca, parte_resaltar = fu.mostrartodopyp(fechahoy)
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
 
    ac.acceso()
    if 'usuario' in st.session_state:
        fabacti(usuario=st.session_state['usuario'])

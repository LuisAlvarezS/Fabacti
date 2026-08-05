
import streamlit as st

from funciones import obtener_fecha_hora_local, es_festivo_colombia, consulta_indicador, lista_valores_indicador, frase, mostrartodopyp, obtener_imagen_aleatoria, presentar_encabezado
from constantes import NOTASFRASE, NOTASPICOYPLACA, NOTASLIBRO, NOTASTRM, NOTASDTF, NOTASIBR, COPYRIGHT
import acceso as ac

def fabacti():
  #nombre_usuario = ac.nombre_usuario(st.session_state['usuario'])
  fechahoy = presentar_encabezado()
  proceso = st.text('Cargando la información requerida, ... por favor espere ...')

# Proceso de TRM
  valor_trm, fecha_vigencia, fecha_vigencia2 = consulta_indicador('TRM')
  trm = float(valor_trm)
  fecha_vigencia_trm = str(fecha_vigencia)[0:4] + '-' + str(fecha_vigencia)[4:6] + '-' + str(fecha_vigencia)[6:8]
  ftrm = '$ {:,.2f} '.format(trm)
  listatrm, trmanterior = lista_valores_indicador('TRM')
  trmayer = trmanterior
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)

# Proceso de DTF
  valor_dtf, fechainicio_dtf, fechafin_dtf = consulta_indicador('DTF')
  fechainicio_dtf = str(fechainicio_dtf)[0:4] + '-' + str(fechainicio_dtf)[4:6] + '-' + str(fechainicio_dtf)[6:8]
  fechafin_dtf = str(fechafin_dtf)[0:4] + '-' + str(fechafin_dtf)[4:6] + '-' + str(fechafin_dtf)[6:8]
  dtf = str('{:,.2f} '.format(float(valor_dtf)))
  #dtfhistorico, deltadtf = dtftodos()
  dtfhistorico, deltadtf = lista_valores_indicador('DTF')
  deltadtf = '{:,.2f} '.format(float(dtf) - deltadtf)
  proceso.empty()

# Proceso de IBR 
  valor_ibr, fecha_vigencia_ibr, fecha_vigencia2 = consulta_indicador('IBR')
  fecha_vigencia_ibr_f = str(fecha_vigencia_ibr)[0:4] + '-' + str(fecha_vigencia_ibr)[4:6] + '-' + str(fecha_vigencia_ibr)[6:8]
  valor_ibr_f = str('{:,.2f} '.format(float(valor_ibr)))
  ibrhistorico, deltaibr = lista_valores_indicador('IBR')
  deltaibr = '{:,.2f} '.format(float(valor_ibr_f) - deltaibr)

  trm1, dtf1, ibr1 = st.columns(3, border = True)   
  with trm1:
    st.metric('**TRM  - Dólar** Vigencia: ' + str(fecha_vigencia_trm)[0:10], ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=NOTASTRM)
  
  with dtf1:
    dtf1.metric('**DTF** Vigencia: ' + str(fechainicio_dtf) + ' / ' + str(fechafin_dtf), dtf + ' %', deltadtf, delta_arrow='auto', delta_color="normal", chart_data=dtfhistorico, chart_type='line', width='stretch', height='content',  help=NOTASDTF)

  with ibr1:
    ibr1.metric('**IBR** Vigencia: ' + str(fecha_vigencia_ibr_f), valor_ibr_f + ' %', deltaibr, delta_arrow='auto', delta_color="normal", chart_data=ibrhistorico, chart_type='line', width='stretch', height='content',  help=NOTASIBR)

# # Calcular los indicadores UVR, IPC, TIB, SMMLV, COLCAP, TPM
#   proceso = st.info('Calculando indicadores economicos adicionales, ... un momento por favor ...')
#   #textoindicadores = fu.calcular_indicadores(trm)
#   listaindicadores = fu.calcular_indicadores(trm)
#   textoindicadores = "   ".join([f"{item['indicador']}: {item['valor']}" for item in listaindicadores])
#   proceso.empty()

#   # Mostrar indicadores economicos adicionales 
#   st.write('---')
#   st.text(textoindicadores)
#   st.write('---')

  picoplaca, frases, libro = st.columns(3, border = True)
  with frases:
    # Obtener frase del dia
    wfrase, wautor = frase()
    st.text('FRASE DEL DIA', help=NOTASFRASE) 
    st.write(wfrase)
    st.write(' [' + wautor + ']')

  with picoplaca:
    picoyplaca, parte_resaltar = mostrartodopyp(fechahoy)
    st.text('Pico y Placa', help=NOTASPICOYPLACA)
    st.write(f'**Hoy** :red[**{parte_resaltar}**]')
    st.write(picoyplaca[0:10] + ', ' + picoyplaca[12:23] + ', ' + picoyplaca[25:39] + ', ' +  picoyplaca[41:52] + ', ' + picoyplaca[54:66])

  with libro:
    st.text('Libro recomendado', help=NOTASLIBRO)
    libro = obtener_imagen_aleatoria('img/')
    st.image(libro, width=200)

  st.divider()
  st.write(COPYRIGHT)
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

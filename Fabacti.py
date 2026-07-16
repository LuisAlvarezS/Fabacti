
import streamlit as st

#from datetime import timedelta
import funciones as fu
import constantes as co
import acceso as ac

def fabacti(usuario=None):
  
  # Encabezado
  st.write( ":red[FABACTI] :registered: ")
  st.sidebar.write('**Usuario** :blue[**' + usuario + '**]')
  st.sidebar.button("Cerrar sesión", on_click=lambda: st.session_state.clear())
  st.sidebar.write(co.ENCABEZADO)
  fechacolombia = fu.obtener_fecha_hora_local("America/Bogota")
  fechahoy = fechacolombia.date()  
  
  ndia = co.DIAS[fechahoy.weekday()]
  nmes = co.MESES[fechahoy.month - 1]
  
  # Veriificar e indicar si es festivo en Colombia
  es_festivo = fu.es_festivo_colombia(str(fechahoy))
  if es_festivo:
    mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) + '  :red[**FESTIVO**]'
  else:
    mensaje = ndia + ', ' + str(fechahoy.day) + ' de ' + nmes + ' de ' + str(fechahoy.year) 
  st.success(mensaje, icon="📆")
  
  proceso = st.text('Cargando la información requerida, ... por favor espere ...')

# Proceso de TRM
  valor_trm, fecha_vigencia, fecha_vigencia2= fu.consulta_indicador('TRM')
  trm = float(valor_trm)
  fecha_vigencia_trm = str(fecha_vigencia)[0:4] + '-' + str(fecha_vigencia)[4:6] + '-' + str(fecha_vigencia)[6:8]
  ftrm = '${:,.2f} '.format(trm)
  listatrm, trmanterior = fu.lista_valores_indicador('TRM')
  trmayer = trmanterior
  deltatrm = trm - trmayer
  fdeltatrm = '{:,.2f} '.format(deltatrm)

# Proceso de DTF
  valor_dtf, fechainicio_dtf, fechafin_dtf = fu.consulta_indicador('DTF')
  fechainicio_dtf = str(fechainicio_dtf)[0:4] + '-' + str(fechainicio_dtf)[4:6] + '-' + str(fechainicio_dtf)[6:8]
  fechafin_dtf = str(fechafin_dtf)[0:4] + '-' + str(fechafin_dtf)[4:6] + '-' + str(fechafin_dtf)[6:8]
  dtf = str('{:,.2f} '.format(float(valor_dtf)))
  #dtfhistorico, deltadtf = fu.dtftodos()
  dtfhistorico, deltadtf = fu.lista_valores_indicador('DTF')
  deltadtf = '{:,.2f} '.format(float(dtf) - deltadtf)
  proceso.empty()

# Proceso de IBR 
  valor_ibr, fecha_vigencia_ibr, fecha_vigencia2 = fu.consulta_indicador('IBR')
  fecha_vigencia_ibr_f = str(fecha_vigencia_ibr)[0:4] + '-' + str(fecha_vigencia_ibr)[4:6] + '-' + str(fecha_vigencia_ibr)[6:8]
  valor_ibr_f = str('{:,.2f} '.format(float(valor_ibr)))
  ibrhistorico, deltaibr = fu.lista_valores_indicador('IBR')
  deltaibr = '{:,.2f} '.format(float(valor_ibr_f) - deltaibr)

  trm1, dtf1, ibr1 = st.columns(3, border = True)   
  with trm1:
    st.metric('**TRM  - Dólar** Vigencia: ' + str(fecha_vigencia_trm)[0:10], ftrm, fdeltatrm, delta_arrow='auto', delta_color="normal", chart_data=listatrm, chart_type='line', width='stretch', height='content', help=co.NOTASTRM)
  
  with dtf1:
    dtf1.metric('**DTF** Vigencia: ' + str(fechainicio_dtf) + ' / ' + str(fechafin_dtf), dtf + ' %', deltadtf, delta_arrow='auto', delta_color="normal", chart_data=dtfhistorico, chart_type='line', width='stretch', height='content',  help=co.NOTASDTF)

  with ibr1:
    ibr1.metric('**IBR** Vigencia: ' + str(fecha_vigencia_ibr_f), valor_ibr_f, deltaibr, delta_arrow='auto', delta_color="normal", chart_data=ibrhistorico, chart_type='line', width='stretch', height='content',  help=co.NOTASIBR)

# Calcular los indicadores UVR, IPC, TIB, SMMLV, COLCAP, TPM
  proceso = st.text('Calculando indicadores economicos adicionales, ... por favor espere ...')
  textoindicadores = fu.calcular_indicadores(trm)
  proceso.empty()

  # Mostrar indicadores economicos adicionales 
  st.write('---')
  #pos = textoindicadores.find('SMMLV')
  st.text(textoindicadores)
  #st.text(textoindicadores[pos:])
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

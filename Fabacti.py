import streamlit as st


def fabacti():
  # Encabezado
  enc1, enc2 = st.columns([10,6])
  enc1.write(" :red[FABACTI] :registered: :blue[Consultoría especializada en tecnologías de la información y las comunicaciones]")
  #enc2.badge(fechapantalla(), icon = co.ICON_EVENTOS, color = 'blue')
  st.sidebar.write(":copyright: 2024 Todos los derechos reservados de autor :red[FABACTI] :registered:")

  st.write(' ... Vamos para adelante con Fabacti con toda ...')
  st.write(' .. cambios ...')

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded",
    )
    fabacti()

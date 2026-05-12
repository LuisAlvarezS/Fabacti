import streamlit as st


def fabacti():
  # Encabezado
  st.write(" :red[FABACTI] :registered: :blue[Consultoría especializada en tecnologías de la información y las comunicaciones]")
  st.write(":copyright: 2026 Todos los derechos reservados de autor :red[FABACTI] :registered:")

  st.write(' ... Vamos para adelante con Fabacti con toda ...')
  st.write(' .. cambios ...')
  st.write(' ... cambios 2 ...')

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded",
    )
    fabacti()

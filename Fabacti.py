import streamlit as st


def fabacti():
  st.write('Vamos para adelante con Fabacti con toda')
  st.write('cambios')

if __name__ == '__main__':
    st.set_page_config(
        page_title="FABACTI",
        layout="wide",
        initial_sidebar_state = "expanded",
    )
    fabacti()

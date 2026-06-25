
import streamlit as st

import funciones as fu

def generarmenu(usuario):
    with st.sidebar:
        st.write(f"**{usuario}**")
        st.page_link("Fabacti.py", label="Fabacti")
        st.page_link("pages/040Noticias.py", label="Noticias")
        #botonsalir = st.form_submit_button("Cerrar sesión")
        #if botonsalir:
        #     st.session_state.clear()
        #     st.rerun()

def acceso():
    if "mostrar_form" not in st.session_state:
        st.session_state.mostrar_form = True
    if st.session_state.mostrar_form:
        with st.form("login_form"):
            st.write("🔒 Iniciar sesión")
            username = st.text_input("Usuario")
            password = st.text_input("Clave de acceso", type="password")
            submitted = st.form_submit_button("Iniciar sesión")
            if submitted:
                if fu.verificar_usuario(username, password):
                    st.session_state['usuario'] = username
                    st.session_state.mostrar_form = False
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
    return()
import sys

import streamlit as st
from datetime import datetime, timedelta

import funciones as fu
import constantes as co


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
    with st.form("login_form"):
        st.write("🔒 Iniciar sesión")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if fu.verificar_usuario(username, password):
                st.session_state['usuario'] = username
                del st.session_state['login_form']
    
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
    return()
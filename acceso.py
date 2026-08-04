
import streamlit as st

import bcrypt
import sqlite3

import re


def nombre_usuario(correo):
    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM usuarios WHERE correo = ?", (correo,))
    row = cursor.fetchone()
    conn.close()
    #st.write(row)
    return(row[0])   

def es_correo_valido(correo: str) -> bool:
    """
    Valida si una cadena es una dirección de correo electrónico válida.
    
    Parámetros:
        correo (str): La dirección a validar.
    
    Retorna:
        bool: True si es válida, False en caso contrario.
    """
    if not isinstance(correo, str):
        return False
    
    # Expresión regular para validar emails (básica pero efectiva)
    patron = re.compile(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
    return bool(patron.match(correo.strip()))

def registrar_usuario(nombre: str, clave: str, correo: str):
    if not nombre  or not clave or not correo:
        raise ValueError("Usuari, clave o correo no pueden estar vacíos.")

    # Generar hash seguro con bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(clave.encode("utf-8"), salt)

    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, clave, correo) VALUES (?, ?, ?)",
            (nombre, hashed.decode("utf-8"),correo)
        )
        conn.commit()
        print(f"Usuario '{nombre}' registrado correctamente.")
    except sqlite3.IntegrityError:
        print(f"Error: el usuario '{nombre}' ya existe.")
    finally:
        conn.close()

def verificar_usuario(correo: str, clave: str) -> bool:
    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM usuarios WHERE correo = ?", (correo,))
    row = cursor.fetchone()
    conn.close()

    if row:
        stored_hash = row[0].encode("utf-8")
        return bcrypt.checkpw(clave.encode("utf-8"), stored_hash)
    return False

def acceso():
    if "mostrar_form" not in st.session_state:
        st.session_state.mostrar_form = True
    if st.session_state.mostrar_form:
        with st.form("login_form"):
            st.write("🔒 Iniciar sesión")
#           username = st.text_input("Usuario")
            correouser = ""
            if not es_correo_valido(correouser): 
                correouser  = st.text_input("Correo")                
            password = st.text_input("Clave de acceso", type="password")
            submitted = st.form_submit_button("Iniciar sesión")
            if submitted:
                if es_correo_valido(correouser):
                    if verificar_usuario(correouser, password):
                        st.session_state['usuario'] = correouser
                        st.session_state['correo_usuario'] = correouser
                        st.session_state['nombre_usuario'] = nombre_usuario(correouser)
                        st.session_state.mostrar_form = False
                        st.rerun()
                    else:
                        st.error("Credenciales incorrectas")
                else:
                        st.error("Correo invalido")
    return()
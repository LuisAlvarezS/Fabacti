
import streamlit as st

import bcrypt
import sqlite3

def registrar_usuario(nombre: str, clave: str):
    if not nombre  or not clave:
        raise ValueError("Usuario y clave no pueden estar vacíos.")

    # Generar hash seguro con bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(clave.encode("utf-8"), salt)

    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, clave) VALUES (?, ?)",
            (nombre, hashed.decode("utf-8"))
        )
        conn.commit()
        print(f"Usuario '{nombre}' registrado correctamente.")
    except sqlite3.IntegrityError:
        print(f"Error: el usuario '{nombre}' ya existe.")
    finally:
        conn.close()

def verificar_usuario(nombre: str, clave: str) -> bool:
    conn = sqlite3.connect("datos/fabacti.db")
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM usuarios WHERE nombre = ?", (nombre,))
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
            username = st.text_input("Usuario")
            password = st.text_input("Clave de acceso", type="password")
            submitted = st.form_submit_button("Iniciar sesión")
            if submitted:
                if verificar_usuario(username, password):
                    st.session_state['usuario'] = username
                    st.session_state.mostrar_form = False
                    st.rerun()
                else:
                    st.error("Credenciales incorrectas")
    return()
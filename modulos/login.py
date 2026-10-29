import streamlit as st 
from config.conexion import obtener_conexion 
def verificar_usuario(usuario, contrasena): 
conexion = obtener_conexion() 
cursor = conexion.cursor() 
consulta = """ 
SELECT Id_Usuario 
FROM USUARIO 
WHERE Usuario = %s AND Contrasena = %s 
""" 
cursor.execute(consulta, (usuario, contrasena)) 
resultado = cursor.fetchone() 
cursor.close() 
conexion.close() 
return resultado 
def login(): 
st.title("Inicio de sesión") 
usuario = st.text_input("Usuario") 
contrasena = st.text_input("Contraseña", type="password") 
if st.button("Iniciar sesión"): 
resultado = verificar_usuario(usuario, contrasena) 
if resultado: 
st.session_state["sesion_iniciada"] = True 
st.session_state["usuario"] = usuario 
st.success("Sesión iniciada correctamente.") 
st.rerun() 
else: 
st.error("Usuario o contraseña incorrectos.")

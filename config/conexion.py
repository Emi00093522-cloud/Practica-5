import mysql.connector 
import streamlit as st 
def obtener_conexion(): 
conexion = mysql.connector.connect( 
host=st.secrets["mysql"]["host"], 
port=st.secrets["mysql"]["port"], 
user=st.secrets["mysql"]["user"], 
password=st.secrets["mysql"]["password"], 
database=st.secrets["mysql"]["database"] 
) 
return conexion

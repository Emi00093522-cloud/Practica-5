import streamlit as st 
from config.conexion import obtener_conexion 
def mostrar_venta(): 
st.header("Registrar venta") 
with st.form("form_venta"): 
producto = st.text_input("Nombre del producto") 
cantidad = st.number_input( 
"Cantidad", 
min_value=1, 
step=1 
) 
guardar = st.form_submit_button("Guardar venta") 
if guardar: 
if producto.strip() == "": 
st.warning("Debe ingresar el nombre del producto.") 
else: 
try: 
conexion = obtener_conexion() 
cursor = conexion.cursor() 
consulta = """ 
INSERT INTO Ventas (Producto, Cantidad) 
VALUES (%s, %s) 
""" 
cursor.execute( 
consulta, 
(producto, cantidad) 
) 
conexion.commit() 
st.success("Venta registrada correctamente.") 
except Exception as error: 
st.error( 
f"Error al registrar la venta: {error}" 
) 
finally: 
if "cursor" in locals(): 
cursor.close() 
if "conexion" in locals(): 
conexion.close()

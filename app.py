import streamlit as st
from modulos.login import login
from modulos.venta import mostrar_venta

# Comprobar si el usuario inició sesión
if st.session_state.get("sesion_iniciada"):
    st.sidebar.write(f"Usuario: {st.session_state['usuario']}")

    opciones = ["Ventas", "Información"]

    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )

    if seleccion == "Ventas":
        mostrar_venta()

    elif seleccion == "Información":
        st.header("Información del sistema")
        st.write(
            "Aplicación desarrollada durante "
            "el Laboratorio de SGI."
        )

    if st.sidebar.button("Cerrar sesión"):
        st.session_state["sesion_iniciada"] = False
        st.rerun()

else:
    login()

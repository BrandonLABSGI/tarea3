import streamlit as st
from modulos.venta import mostrar_venta
from modulos.clientes import mostrar_clientes
from modulos.productos import mostrar_productos
from modulos.login import login

# Si NO hay sesión, pedir login
if not st.session_state.get("sesion_iniciada"):
    login()
    st.stop()  # Evita que el resto del código siga sin login

# ✅ Si hay sesión, mostrar menú lateral
opciones = ["Clientes", "Productos", "Ventas"]
seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

# ✅ Contenido según selección
if seleccion == "Clientes":
    mostrar_clientes()

elif seleccion == "Productos":
    mostrar_productos()

elif seleccion == "Ventas":
    mostrar_venta()

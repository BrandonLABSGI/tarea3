import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_clientes():
    st.header("👥 Registrar Cliente")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar cliente
        with st.form("form_clientes"):
            nombre = st.text_input("Nombre del cliente")
            telefono = st.text_input("Teléfono")
            enviar = st.form_submit_button("✅ Guardar cliente")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del cliente.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Clientes (Nombre, Telefono) VALUES (%s, %s)",
                            (nombre, telefono)
                        )
                        con.commit()
                        st.success(f"✅ Cliente registrado: {nombre}")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el cliente: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

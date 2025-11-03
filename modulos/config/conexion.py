import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bjpiwgh2p8natts86c76-mysql.services.clever-cloud.com',
            user='umyehuxdggr9fce6',
            password='iLiRFCy4VrT9W4i1pbBU',
            database='bjpiwgh2p8natts86c76',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None

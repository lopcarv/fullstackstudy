# scripts_python/verificar_db.py
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="sistema_inventario"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, nome_usuario FROM usuarios WHERE nivel_acesso = 'admin'")
    
    print("--- Lista de Administradores ---")
    for (id_u, email) in cursor:
        print(f"ID: {id_u} | E-mail: {email}")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    if 'conn' in locals(): conn.close()
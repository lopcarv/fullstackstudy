import mysql.connector

def verificar_admin():
    print("\n🔍 Verificando Usuário no Banco de Dados...")
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema_inventario"
        )
        cursor = conn.cursor()
        
        query = "SELECT id_usuario, nome_usuario, nivel_acesso FROM usuarios WHERE nome_usuario = %s"
        cursor.execute(query, ("suporte@eetepa.com",))
        
        result = cursor.fetchone()
        
        if result:
            print(f"✅ USUÁRIO ENCONTRADO!")
            print(f"ID: {result[0]} | E-mail: {result[1]} | Status: {result[2]}")
        else:
            print("❌ Usuário não encontrado no banco de dados.")

    except mysql.connector.Error as err:
        print(f"Erro de Conexão: {err}")
    finally:
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    verificar_admin()
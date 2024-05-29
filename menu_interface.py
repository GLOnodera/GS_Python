import oracledb

def get_db_connection():
    """Estabelece a conexão com o banco de dados Oracle."""
    try:
        connection = oracledb.connect(
            user="seu_usuario",
            password="sua_senha",
            dsn="seu_host:seu_port/seu_servico"
        )
        return connection
    except oracledb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fetch_data(query):
    """Executa uma query e retorna os resultados."""
    connection = get_db_connection()
    if connection is None:
        return []
    
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
    finally:
        connection.close()

def show_menu():
    """Exibe o menu para o usuário."""
    while True:
        print("\nMenu:")
        print("1. Ver todas as reclamações")
        print("2. Ver reclamações por local")
        print("3. Ver reclamações por tipo")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            query = "SELECT * FROM reclamacoes"
            results = fetch_data(query)
            for row in results:
                print(row)
        elif choice == '2':
            local = input("Digite o local: ")
            query = f"SELECT * FROM reclamacoes WHERE local = '{local}'"
            results = fetch_data(query)
            for row in results:
                print(row)
        elif choice == '3':
            tipo = input("Digite o tipo: ")
            query = f"SELECT * FROM reclamacoes WHERE tipo = '{tipo}'"
            results = fetch_data(query)
            for row in results:
                print(row)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso
if __name__ == "__main__":
    show_menu()

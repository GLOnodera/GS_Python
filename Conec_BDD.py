import oracledb
import pandas as pd

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

def load_csv_to_db(file_path, table_name):
    """Lê um arquivo CSV e insere os dados na tabela especificada."""
    connection = get_db_connection()
    if connection is None:
        return
    
    try:
        df = pd.read_csv(file_path)
        cursor = connection.cursor()
        
        # Gerar a query de inserção dinamicamente com base nas colunas do DataFrame
        cols = ', '.join(df.columns)
        placeholders = ', '.join([':' + str(i+1) for i in range(len(df.columns))])
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
        
        # Inserir os dados
        for i, row in df.iterrows():
            cursor.execute(query, tuple(row))
        
        connection.commit()
        print(f"Dados inseridos com sucesso na tabela {table_name} a partir do arquivo {file_path}.")
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
    finally:
        connection.close()

# Exemplo de uso
if __name__ == "__main__":
    load_csv_to_db("caminho/para/seu_arquivo1.csv", "nome_da_tabela1")
    load_csv_to_db("caminho/para/seu_arquivo2.csv", "nome_da_tabela2")

import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//clientesCadastrados.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)
    

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_user():
    # Inicializadores
    #def __init__(self):
    def criar_tabela():
        c.execute(
            """CREATE TABLE IF NOT EXISTS dados (
                nome text,
                cpf text,
                telefone text,
                enderecoCobranca text,
                diasReservados INTEGER,
                senha text,
                autorizacao text,
                UNIQUE(nome, login)
                )""")
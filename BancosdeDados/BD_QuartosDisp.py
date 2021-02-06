import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados\Cache//QuartosDisponiveis.db"

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
                idQuarto text,
                disponivel INTEGER,
                quemAlugou text,
                PorQuantoTempo text,
                Datadeentrada INTEGER,
                datadesaida text,

                UNIQUE(nome, login)
                )""")
import sqlite3
import os

# Caminho do arquivo .db
caminho = "BancosdeDados//contEstoque.db"
if not os.path.exists(caminho):
    os.makedirs("BancosdeDados")

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_EstoqueCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (local text, listaItens text, UNIQUE(local))")
        c.execute("INSERT OR REPLACE INTO dados (local, listaItens) VALUES ('Recepção', 'Telefone, Bloco de notas e Canetas')")
        connection.commit()
        connection.commit()
    
    # Método de entrada dos dados de estoque no bd
    def insereDadosEst(self, local, texto):
        self.criar_tabela()
        c.execute("INSERT OR REPLACE INTO dados (local, listaItens) VALUES ('"+local+"','"+texto+"')")
        connection.commit()
    
    # Método de leitura dos dados de estoque no bd
    def leDadosEst(self):
        c.execute('SELECT local, listaItens FROM dados')
        data = c.fetchall()
        return data
    
    # Método de atualização dos dados de estoque no bd
    def atualizaEst(self, local, texto):
        sql = "UPDATE dados SET listaItens=? WHERE local=?"
        dado = (texto, local)
        c.execute(sql,dado)
        connection.commit()
        
    # Método de remoção dos dados de estoque no bd
    def deletaEst(self, local):
        sql = "DELETE FROM dados WHERE local=?"
        dado = (local,)
        c.execute(sql,dado)
        connection.commit()
    
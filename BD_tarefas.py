import sqlite3
import os

# Caminho do arquivo .db
caminho = "BancosdeDados//listaTarefas.db"
if not os.path.exists(caminho):
    os.makedirs("BancosdeDados")

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_TarefasCRUD():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (prioridade text, listaTarefas text, UNIQUE(prioridade))")
        c.execute("INSERT OR IGNORE INTO dados (prioridade, listaTarefas) VALUES ('Urgente', 'Limpeza da piscina')")
        connection.commit()
    
    # Método de escrita no banco de dados
    def insereDadosEst(self, prioridade, texto):
        self.criartabela()
        c.execute("INSERT OR REPLACE INTO dados (prioridade, listaTarefas) VALUES ('"+prioridade+"','"+texto+"')")
        connection.commit()
    
    # Método de leitura do banco de dados
    def leDadosEst(self):
        c.execute('SELECT prioridade, listaTarefas FROM dados')
        data = c.fetchall()
        return data
    
    # Método de atualização do banco de dados
    def atualizaEst(self, prioridade, texto):
        sql = "UPDATE dados SET listaTarefas=? WHERE prioridade=?"
        dado = (texto, prioridade)
        c.execute(sql,dado)
        connection.commit()
        
    # Método de exclusão do banco de dados
    def deletaEst(self, prioridade):
        sql = "DELETE FROM dados WHERE prioridade=?"
        dado = (prioridade,)
        c.execute(sql,dado)
        connection.commit()
    
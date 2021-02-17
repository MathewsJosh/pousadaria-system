import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//contEstoque.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

#idlista INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE(idItem
class BD_EstoqueCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (local text, listaItens text, UNIQUE(local))")
        connection.commit()
    
    # Método de entrada dos dados do estoque no bd
    def insereDadosEst(self, local, texto):
        self.criar_tabela()
        c.execute("INSERT OR REPLACE INTO dados (local, listaItens) VALUES ('"+local+"','"+texto+"')")
        connection.commit()
    
    def leDadosEst(self):
        c.execute('SELECT local, listaItens FROM dados')
        data = c.fetchall()
        return data
    
    def atualizaEst(self, local, texto):
        sql = "UPDATE dados SET listaItens=? WHERE local=?"
        dado = (texto, local)
        c.execute(sql,dado)
        connection.commit()
        
    def deletaEst(self, local):
        sql = "DELETE FROM dados WHERE local=?"
        dado = (local,)
        c.execute(sql,dado)
        connection.commit()
    
import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//reclamacoes.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_ReclamaSugest():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (idrec INTEGER PRIMARY KEY AUTOINCREMENT, cliente text, textoReclamacao text, datetime text, status text, UNIQUE(cliente))")
        c.execute("INSERT OR IGNORE INTO dados (cliente, textoReclamacao, datetime, status) VALUES ('ADMIN', 'Esse software é incrivel, obrigado!', '16/02/2021', 'Outros')")
        connection.commit()
    
    # Método de entrada dos dados do usuário para o cadastramento
    def insereDadosRec(self, nomeCliente, treclamacao, timestamp, situacao ):
        self.criar_tabela()
        c.execute("INSERT OR REPLACE INTO dados (cliente, textoReclamacao, datetime, status) VALUES ('"+nomeCliente+"','"+treclamacao+"','"+timestamp+"','"+situacao+"')")
        connection.commit()
    
    def leDadosRec(self):
        c.execute('SELECT idrec, cliente, textoReclamacao, datetime, status FROM dados')
        data = c.fetchall()
        return data
    
    def atualizaRec(self, cliente, status, rec):
        sql = "UPDATE dados SET textoReclamacao=?, status=? WHERE cliente=?"
        data = (rec, status, cliente)
        c.execute(sql,data)
        connection.commit()
        
    def deletaRec(self, cliente):
        sql = "DELETE FROM dados WHERE cliente=?"
        data = (cliente,)
        c.execute(sql,data)
        connection.commit()
        
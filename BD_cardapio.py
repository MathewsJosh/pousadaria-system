import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//cardapio.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_CardapioCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (dia text, textoCardapio text, UNIQUE(dia))")
        connection.commit()
    
    # Método de entrada dos dados do usuário para o cadastramento
    def insereDadosCar(self, data, refeicao):
        self.criar_tabela()
        c.execute("INSERT OR REPLACE INTO dados (dia, textoCardapio) VALUES ('"+data+"','"+refeicao+"')")
        connection.commit()
    
    def leDadosCar(self):
        c.execute('SELECT dia, textoCardapio FROM dados')
        data = c.fetchall()
        return data
    
    def atualizaCar(self, data, refeicao):
        sql = "UPDATE dados SET textoCardapio=? WHERE dia=?"
        dado = (refeicao, data)
        c.execute(sql,dado)
        connection.commit()
        
    def deletaCar(self, data):
        sql = "DELETE FROM dados WHERE dia=?"
        dado = (data,)
        c.execute(sql,dado)
        connection.commit()
    
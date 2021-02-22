import sqlite3

# Caminho do arquivo .db
caminho = "BancosdeDados//cardapio.db"

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_CardapioCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (dia text, textoCardapio text, UNIQUE(dia))")
        c.execute("INSERT OR IGNORE INTO dados (dia, textoCardapio) VALUES ('Segunda-Feira', 'Café da Manhã: Vitamina de Banana e pão de queijo\nAlmoço: Feijoada, Arroz, Farofa')")
        connection.commit()
    
    # Método de entrada dos dados do cardapio
    def insereDadosCar(self, data, refeicao):
        self.criar_tabela()
        c.execute("INSERT OR REPLACE INTO dados (dia, textoCardapio) VALUES ('"+data+"','"+refeicao+"')")
        connection.commit()
    
    # Método de leitura dos dados do cardapio
    def leDadosCar(self):
        c.execute('SELECT dia, textoCardapio FROM dados')
        data = c.fetchall()
        return data
    
    # Método de atualização dos dados do cardapio
    def atualizaCar(self, data, refeicao):
        sql = "UPDATE dados SET textoCardapio=? WHERE dia=?"
        dado = (refeicao, data)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de remoção dos dados do cardapio
    def deletaCar(self, data):
        sql = "DELETE FROM dados WHERE dia=?"
        dado = (data,)
        c.execute(sql,dado)
        connection.commit()
    
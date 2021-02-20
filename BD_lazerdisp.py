import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//lazerDisponiveis.db"

# Verifica se o arquivo funcionáriosCadastrados existe
#existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_Lazer():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute("CREATE TABLE IF NOT EXISTS dados (idArea text, status text, nome text, precoDia REAL, tempoDeLocação INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idArea))")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('01', 'Disponível', 'Churrasqueira ', '90.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('02', 'Ocupado', 'Sauna', '50.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('03', 'Disponível', 'Campo de Futebol', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('04', 'Disponível', 'Salão de Festas', '500.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('05', 'Disponível', 'Piscina', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('06', 'Disponível', 'Quadra', '50.00')")
        connection.commit()


    def leDadosBasicosArea(self):
        c.execute('SELECT idArea, status, nome, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    
    def leDadosCompletosArea(self):
        c.execute('SELECT idArea, status, nome, precoDia, tempoDeLocação, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    def buscaAreasDisponiveis(self, status):
        sql='SELECT nome, precoDia FROM dados WHERE status=?'
        dado = (status,)
        c.execute(sql,dado)
        data = c.fetchall()
        return data
    
    
    
    
    
    
    
    
    
    
    

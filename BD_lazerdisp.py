import sqlite3
from datetime import datetime
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
        c.execute("CREATE TABLE IF NOT EXISTS dados (idArea text, status text, nome text, precoDia REAL, tempoDeLocacao INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idArea))")
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
        c.execute('SELECT idArea, status, nome, precoDia, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    
    def buscaAreasDisponiveis(self, entrada, saida):
        sql='SELECT nome, precoDia, dataDeEntrada, dataDeSaida FROM dados'
        c.execute(sql)
        data = c.fetchall()
        entrada = datetime.strptime(entrada, '%d/%m/%Y').date()
        saida = datetime.strptime(saida, '%d/%m/%Y').date()
        aux=[]
        for x in range(len(data)):
            if(data[x][2] is None and data[x][3] is None):
                aux.append(data[x])
            else:
                entradaBD = datetime.strptime(data[x][2], '%d/%m/%Y').date()
                saidaBD = datetime.strptime(data[x][3], '%d/%m/%Y').date()
                if entradaBD<entrada and entradaBD<saida and saidaBD<entrada and saidaBD<saida:
                    aux.append(data[x])
                if entradaBD>entrada and entradaBD>saida and saidaBD>entrada and saidaBD>saida:
                    aux.append(data[x])
        return aux
    
    
    def buscaPrecosLazer(self):
        sql='SELECT nome, precoDia FROM dados'
        c.execute(sql)
        data = c.fetchall()
        return data
    
    def atualizaReservaLazer(self, nome, status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente):
        sql = "UPDATE dados SET status=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=?, cliente=? WHERE nome=?"
        dado = (status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente, nome)
        c.execute(sql,dado)
        connection.commit()
    
    
    
    
    
    
    
    
    

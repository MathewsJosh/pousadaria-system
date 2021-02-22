import sqlite3
from datetime import datetime

# Caminho do arquivo .db
caminho = "BancosdeDados//quartosDisponiveis.db"

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_Quartos():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        sql = "CREATE TABLE IF NOT EXISTS dados (idQuarto text, nome text, status text, tipo text, qtdCamas INTEGER, qtdComodos INTEGER, precoDia REAL, tempoDeLocacao INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idQuarto))"
        c.execute(sql)
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('01', 'Suíte 01', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('02', 'Suíte 02', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('03', 'Suíte 03', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('04', 'Suíte 04', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('05', 'Solteiro 01', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('06', 'Solteiro 02', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('07', 'Solteiro 03', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('08', 'Solteiro 04', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('09', 'Chalé 01', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('10', 'Chalé 02', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('11', 'Chalé 03', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        connection.commit()

    # Método de leitura basica dos quartos
    def leDadosBasicosQuarto(self):
        c.execute('SELECT idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    # Método de leitura completa dos quartos
    def leDadosCompletosQuarto(self):
        c.execute('SELECT idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    # Método de atualização de status do quarto
    def atualizaStatusQuarto(self, nome):
        sql = "UPDATE dados SET status=?,tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=?, cliente=? WHERE nome=?"
        dado = (None, None, None, None, None, nome)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de busca das quartos disponiveis para datas especificas
    def buscaQuartosDisponiveis(self, entrada, saida):
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
    
    # Método de atualização de status e outros dados dos quartos
    def atualizaReservaQuarto(self, nome, status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente):
        sql = "UPDATE dados SET status=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=?, cliente=? WHERE nome=?"
        dado = (status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente, nome)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de busca dos quartos ocupados para clientes especificos
    def buscaQuartosOcupadosCliente(self, cliente):
        sql='SELECT nome FROM dados WHERE cliente=?'
        dado = (cliente,)
        c.execute(sql,dado)
        data = c.fetchall()
        return data

    


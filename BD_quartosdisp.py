import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//quartosDisponiveis.db"

# Verifica se o arquivo funcionáriosCadastrados existe
#existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_Quartos():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        sql = "CREATE TABLE IF NOT EXISTS dados (idQuarto text, nome text, status text, tipo text, qtdCamas INTEGER, qtdComodos INTEGER, precoDia REAL, tempoDeLocação INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idQuarto))"
        c.execute(sql)
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('01', 'Suíte 01', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('02', 'Suíte 02', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('03', 'Suíte 03', 'Ocupado', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('04', 'Suíte 04', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('05', 'Solteiro 01', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('06', 'Solteiro 02', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('07', 'Solteiro 03', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('08', 'Solteiro 04', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('09', 'Chalé 01', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('10', 'Chalé 02', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('11', 'Chalé 03', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        connection.commit()


    def leDadosBasicosQuarto(self):
        c.execute('SELECT idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    def leDadosCompletosQuarto(self):
        c.execute('SELECT idQuarto, nome, status, tipo, qtdCamas, qtdComodos, precoDia, tempoDeLocação, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    def atualizaStatusQuarto(self, status, nome):
        sql = "UPDATE dados SET status=? WHERE nome=?"
        dado = (status, nome)
        c.execute(sql,dado)
        connection.commit()
    
    def buscaQuartosDisponiveis(self, status):
        sql='SELECT nome FROM dados WHERE status=?'
        dado = (status,)
        c.execute(sql,dado)
        data = c.fetchall()
        return data
    
    def buscaPrecosQuartos(self):
        sql='SELECT nome, precoDia FROM dados'
        c.execute(sql)
        data = c.fetchall()
        return data
    
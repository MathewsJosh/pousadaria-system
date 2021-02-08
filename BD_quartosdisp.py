import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//quartosDisponiveis.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
if existe:
    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_Quartos():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute(
            """CREATE TABLE IF NOT EXISTS dados (idQuarto text, disponibilidade text, tipo text, qtdCamas INTEGER, qtdComodos INTEGER, precoDia REAL, tempoDeLocação INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idQuarto))""")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('01', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('02', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('03', 'Ocupado', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('04', 'Disponível', 'Suíte', '1 Cama de casal', '2 Cômodos - Quarto e Banheiro', '150.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('05', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('06', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('07', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('08', 'Disponível', 'Solteiro', '1 Cama de solteiro', '1 Cômodo - Quarto', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('09', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('10', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        c.execute("INSERT OR IGNORE INTO dados (idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia) VALUES ('11', 'Disponível', 'Chalé', '1 Cama de casal', '3 Cômodos - Quarto, Cozinha e Banheiro', '250.00')")
        connection.commit()


    def leDadosBasicosQuarto(self):
        c.execute('SELECT idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    def leDadosCompletosQuarto(self):
        c.execute('SELECT idQuarto, disponibilidade, tipo, qtdCamas, qtdComodos, precoDia, tempoDeLocação, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    # # Método que retorna o nome e senha do usuário cadastrado
    # def leDados(dataReserva,self):
    #     sql = 'SELECT * FROM dados WHERE dataDeEntrada=?'
    #     c.execute(sql, (dataReserva,))
    #     data=c.fetchall()
    #     return data
        # for linha in c.execute(sql, (dataReserva,)):
        #     if linha == "":
        #         return False
        #     else:
        #         return True
            

#x10 = BD_Quartos()
#x10.criar_tabela()
#data2 = x10.leDadosBasicosQuarto()

#print(data2)
#print(data2[0])
#print(data2[0][0])

    # Método auxiliar de entrada de dados e criação de tabela
    #def entradaauxiliar(self):
        #self.criar_tabela()
        #connection.commit()


    # Método de entrada dos dados do usuário para o cadastramento
    #def entradaDados(nome, cpf, funcao, salario, login, senha, autorizacao, self):
        #self.criar_tabela()
        #if not existe:
            #self.entradaauxiliar()
        #c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('admin', 'admin', 'admin')")
        #c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('adm', 'adm', 'adm')")
        # Se autorização estiver correta, verifica se é funcionário da gerencia para adicionar nova autorizaçao, senão, só adiciona o novo funcionário mesmo
        #if self.leAutorizacao(autorizacao):
            #if funcao == "1 - Gerência":
                #c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha, autorizacao) VALUES ('" +nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"','"+autorizacao+"')")
            #c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('" +nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"')")
        #connection.commit()

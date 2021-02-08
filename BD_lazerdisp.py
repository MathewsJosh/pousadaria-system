import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//lazerDisponiveis.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
if existe:
    os.remove(caminho)


# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()


class BD_Areas():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        c.execute(
            """CREATE TABLE IF NOT EXISTS dados (idArea text, disponibilidade text, nome text, precoDia REAL, tempoDeLocação INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idArea))""")
        c.execute("INSERT OR IGNORE INTO dados (idArea, disponibilidade, nome, precoDia) VALUES ('01', 'Disponível', 'Churrasqueira ', '90.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, disponibilidade, nome, precoDia) VALUES ('02', 'Ocupado', 'Sauna', '50.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, disponibilidade, nome, precoDia) VALUES ('03', 'Disponível', 'Campo de Futebol', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, disponibilidade, nome, precoDia) VALUES ('04', 'Disponível', 'Salão de Festas', '500.00')")
        connection.commit()


    def leDadosBasicosArea(self):
        c.execute('SELECT idArea, disponibilidade, nome, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    
    def leDadosCompletosArea(self):
        c.execute('SELECT idArea, disponibilidade, nome, precoDia, tempoDeLocação, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # Testa impressão
        #for linha in data:  
            #print(linha[0])

#x10 = BD_Areas()
#x10.criar_tabela()
#data2 = x10.leDadosBasicosArea()

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

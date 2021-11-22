import sqlite3
import os

# Caminho do arquivo .db
caminho = "BancosdeDados//cadClientes.db"
if not os.path.exists(caminho):
    os.makedirs("BancosdeDados")

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_cadCliente():
    # Construtor
    def __init__(self):
        self.criartabela()
        
    # Método de criação da tabela do banco de dados    
    def criartabela(self):
        sql = "CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, telefone text, email text, tipo text, endereco text, quartosReservados text, AreasReservadas text, tempoDeLocacao INTEGER, dataDeEntrada text, dataDeSaida text, UNIQUE(nome))"
        c.execute(sql)
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('Yudi', '000.000.000-00', '4002-8922', 'yudiplaystation@sbt.com.br', 'Pessoa Física', 'Rodovia Anhanguera, Km 19, Industrial Anhanguera Av. das Comunicações, 4 Osasco - SP')")
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('Priscila', '111.111.111-11', '4002-8922', 'pribomdia@sbt.com.br', 'Pessoa Física', 'Rodovia Anhanguera, Km 19, Industrial Anhanguera Av. das Comunicações, 4 Osasco - SP')")
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('Elon-Musk', '222.222.222-22', '+(1)(425) 555-0100', 'musketeiro@spacex.com', 'Pessoa Física', 'Los Angeles, em Hawthorne, Califórnia')")
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('Faustão', '333.333.333-33', '4003-8000', 'faustosilva@globo.com', 'Pessoa Física', 'Los Angeles, em Hawthorne, Califórnia')")
        connection.commit()
    
    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, telefone, email, tipo, endereco):  
        sql ="INSERT OR REPLACE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('"+nome+"','"+cpf+"','"+telefone+"','"+email+"','"+tipo+"','"+endereco+"')"
        c.execute(sql)
        connection.commit()

    # Método de leitura dos nomes de clientes
    def leNomeCliente(self): 
        sql = 'SELECT nome FROM dados'
        c.execute(sql)
        data = c.fetchall()
        return data    
    
    # Método de leitura de todos os dados dos clientes
    def leTudoCliente(self, nome): 
        sql = 'SELECT nome, cpf, telefone, email, tipo, endereco, quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida FROM dados where nome=?'
        dados = (nome, )
        c.execute(sql,dados)
        data = c.fetchall()
        return data   
    
    # Método de Update do cliente, quando ele faz a reserva, salva alguns dados no bd
    def atualizaReserva(self, quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome ):
        sql = "UPDATE dados SET quartosReservados=?, AreasReservadas=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=? WHERE nome=?"
        dado = (quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de Update do cliente, quando ele faz a reserva, apaga os dados que ele armazenou quando reservou o quarto
    def desfazReserva(self, nome ):
        sql = "UPDATE dados SET quartosReservados=?, AreasReservadas=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=? WHERE nome=?"
        dado = (None, None, None, None, None, nome)
        c.execute(sql,dado)
        connection.commit()
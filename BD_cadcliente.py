import sqlite3
#import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//cadClientes.db"

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
        connection.commit()
    
    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, telefone, email, tipo, endereco):  
        sql ="INSERT OR REPLACE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('"+nome+"','"+cpf+"','"+telefone+"','"+email+"','"+tipo+"','"+endereco+"')"
        c.execute(sql)
        connection.commit()


    def leNomeCliente(self): 
        sql = 'SELECT nome FROM dados'
        c.execute(sql)
        data = c.fetchall()
        return data    
    
    
    def leTudoCliente(self, nome): 
        sql = 'SELECT nome, cpf, telefone, email, tipo, endereco, quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida FROM dados where nome=?'
        dados = (nome, )
        c.execute(sql,dados)
        data = c.fetchall()
        return data   
    
    
    def atualizaReserva(self, quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome ):
        sql = "UPDATE dados SET quartosReservados=?, AreasReservadas=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=? WHERE nome=?"
        dado = (quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome)
        c.execute(sql,dado)
        connection.commit()
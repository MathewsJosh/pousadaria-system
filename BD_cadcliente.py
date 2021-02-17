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
        sql = "CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, telefone text, email text, tipo text, endereco text, quartosReservados text, AreasReservadas text, UNIQUE(nome))"
        c.execute(sql)
        
    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, telefone, email, tipo, endereco):  
        sql ="INSERT OR REPLACE INTO dados (nome, cpf, telefone, email, tipo, endereco) VALUES ('"+nome+"','"+cpf+"','"+telefone+"','"+email+"','"+tipo+"','"+endereco+"')"
        c.execute(sql)
        connection.commit()

    # Método que Insere os quartos e/ou areas alugadas
    def insereQA(self, quartos, areas):
        #len(quartos)
        sql ="INSERT OR REPLACE INTO dados (quartosReservados, AreasReservadas) VALUES ('"+quartos+"','"+areas+"')"
        c.execute(sql)
        connection.commit() 

#Armazenar qtd de quartos alugados?
#Armazenas datas de entrada e saída dos clientes?
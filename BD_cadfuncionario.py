import sqlite3
import os

# Caminho do arquivo .db
caminho = "BancosdeDados//cadFuncionarios.db"
if not os.path.exists(caminho):
    os.makedirs("BancosdeDados")

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_cadFunc():
    # Construtor
    def __init__(self,controle):
        self.controle = controle
        self.cont=True
        self.criartabela()
        
    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql ="CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, funcao text, salario text, login text, senha text, UNIQUE(nome, login))"
        c.execute(sql)
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('admin', 'admin', 'admin', 'admin', 'admin', 'admin')")
        c.execute("INSERT OR IGNORE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('adm', 'adm', 'adm', 'adm','adm', 'adm')")
        connection.commit()
        #self.insereAux()
        
    # Método auxiliar de inserção
    def insereAux(self):
        if self.cont==True and self.controle==True:
            c.execute("INSERT OR IGNORE INTO dados (login, senha) VALUES ('admin', 'admin')")
            c.execute("INSERT OR IGNORE INTO dados (login, senha) VALUES ('adm', 'adm')")
            connection.commit()
        self.cont=False

    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, funcao, salario, login, senha):  
        c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('"+nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"')")
        connection.commit()

    # Método que valida o login com os dados armazenados no BD
    def leDados(self, login, senha):
        sql = 'SELECT * FROM dados WHERE login=? and senha=?'
        for linha in c.execute(sql, (login,senha,)):
            if linha == "":
                return False
                #return True
            else:
                return True
                #return False
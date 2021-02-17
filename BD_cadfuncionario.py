import sqlite3
#import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados//cadFuncionarios.db"

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

class BD_cadFunc():
    # Construtor
    def __init__(self):
        self.criartabela()
        self.entradaauxiliar()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql ="CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, funcao text, salario REAL, login text, senha text, UNIQUE(nome, cpf, login))"
        c.execute(sql)


    # Método auxiliar de entrada de dados e criação de tabela - Insere Login e Senha para o ADM
    def entradaauxiliar(self):
        c.execute("INSERT OR REPLACE INTO dados (login, senha) VALUES ('admin', 'admin')")
        c.execute("INSERT OR REPLACE INTO dados (login, senha) VALUES ('adm', 'adm')")
        connection.commit()


    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, funcao, salario, login, senha):  
        c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('"+nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"')")
        connection.commit()


    # Método que valida o login com os dados armazenados no BD
    def leDados(self, login, senha):
        sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
        for linha in c.execute(sql, (login,senha,)):
            if linha == "":
                return False
            else:
                return True



''' Descartados

def retornaFuncao(self, login,funcao):
        if not existe:
                entradaauxiliar()
        if funcao == "2 - Recepção" or funcao == "3 - Limpeza" or funcao == "4 - Cozinha":
            sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
            for linha in c.execute(sql, (login,funcao,)):
                if linha == "":
                    return False
                else:
                    return 1
        else:
            sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
            for linha in c.execute(sql, (login,funcao,)):
                if linha == "":
                    return False
                else:
                    return 2





# Método que verifica se a autorizacao de cadastro informada está cadastrada no sistema
def leAutorizacao(autorizacao):
    if not existe:
        entradaauxiliar()
    sql = 'SELECT * FROM dados WHERE autorizacao=?'
    for linha in c.execute(sql, (autorizacao,)):
        if linha == "":
            return False
        else:
            return True
    return False
    
    
    
    
    
    
        # Método que fecha a conexão com o banco de dados(nunca usado)
    def fechaConexao(self):
        c.close()
        connection.close()
'''
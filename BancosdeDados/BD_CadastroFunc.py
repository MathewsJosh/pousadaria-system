import sqlite3
import os.path

# Caminho do arquivo .db
caminho = "BancosdeDados\Cache//funcionariosCadastrados.db"

# Verifica se o arquivo funcionáriosCadastrados existe
existe = os.path.exists(caminho)

# Deleta o arquivo de dados de chat se o mesmo existir
#if existe:
#    os.remove(caminho)
    

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

# Método de criação da tabela do banco de dados
def criar_tabela():
    c.execute(
        """CREATE TABLE IF NOT EXISTS dados (
            nome text,
            cpf text,
            funcao text,
            salario text,
            login text,
            senha text,
            autorizacao text,
            UNIQUE(nome, login)
            )""")

# Método auxiliar de entrada de dados e criação de tabela
def entradaauxiliar():
    criar_tabela()
    c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('admin', 'admin', 'admin')")
    c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('adm', 'adm', 'adm')")
    connection.commit()

entradaauxiliar()

# Método de entrada dos dados do usuário para o cadastramento
def entradaDados(nome, cpf, funcao, salario, login, senha, autorizacao):
    criar_tabela()
    if not existe:
        entradaauxiliar()
    #c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('admin', 'admin', 'admin')")
    #c.execute("INSERT OR IGNORE INTO dados (nome, senha, autorizacao) VALUES ('adm', 'adm', 'adm')")
    # Se autorização estiver correta, verifica se é funcionário da gerencia para adicionar nova autorizaçao, senão, só adiciona o novo funcionário mesmo
    if leAutorizacao(autorizacao):
        if funcao == "1 - Gerência":
            c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha, autorizacao) VALUES ('"+nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"','"+autorizacao+"')")
        c.execute("INSERT OR REPLACE INTO dados (nome, cpf, funcao, salario, login, senha) VALUES ('"+nome+"','"+cpf+"','"+funcao+"','"+salario+"','"+login+"','"+senha+"')")
    connection.commit()

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


# Método que retorna o nome e senha do usuário cadastrado
def leDados(login,senha):
    if not existe:
        entradaauxiliar()
    sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
    for linha in c.execute(sql, (login,senha,)):
        if linha == "":
            return False
        else:
            return True


def retornaFuncao(login,funcao):
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

# Método que fecha a conexão com o banco de dados(nunca usado)
def fechaConexao():
    c.close()
    connection.close()


'''
OBS: 
1 - Somente as funções Recepçao e gerencia tem acesso ao sistema
2 - Somente adms podem cadastrar usuários
'''
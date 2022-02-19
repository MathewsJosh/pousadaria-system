import sqlite3
import os

# Caminho do arquivo .db
caminho = "BancosdeDados//pousadaria.db"
if not os.path.exists("BancosdeDados"):
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
        #sql = "CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, telefone text, email text, tipo text, endereco text, quartosReservados text, AreasReservadas text, tempoDeLocacao INTEGER, dataDeEntrada text, dataDeSaida text, UNIQUE(nome))"
        sql = """CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY,
            nome varchar(100) not null,
            telefone varchar(20),
            email varchar,
            endereco varchar,
            cpf varchar unique,
            cnpj varchar unique,
            cadastrado_por INTEGER not null REFERENCES Funcionario(id_func))"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Cliente")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Cliente (nome, cpf, telefone, email, endereco, cadastrado_por) VALUES ('Yudi Tamagoshi', '00000000000', '4002-8922', 'yudiplaystation@sbt.com.br', 'Rodovia Anhanguera, Km 19, Industrial Anhanguera Av. das Comunicações, 4 Osasco - SP', 1)")
            c.execute("INSERT INTO Cliente (nome, cpf, telefone, email, endereco, cadastrado_por) VALUES ('Priscila Alcantara', '11111111111', '4002-8922', 'pribomdia@sbt.com.br', 'Rodovia Anhanguera, Km 19, Industrial Anhanguera Av. das Comunicações, 4 Osasco - SP', 1)")
            c.execute("INSERT INTO Cliente (nome, cpf, telefone, email, endereco, cadastrado_por) VALUES ('Elon-Musk', '22222222222', '+(1)(425) 555-0100', 'musketeiro@spacex.com', 'Los Angeles, Hawthorne, Califórnia', 2)")
            c.execute("INSERT INTO Cliente (nome, cpf, telefone, email, endereco, cadastrado_por) VALUES ('Faustão', '33333333333', '4003-8000', 'faustosilva@globo.com', 'Los Angeles, em Hawthorne, Califórnia', 1)")
        connection.commit()
    
    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDadosPF(self, nome, cpf, telefone, email, endereco, cadastrado_por):  
        sql ="INSERT OR REPLACE INTO Cliente (nome, cpf, telefone, email, endereco, cadastrado_por) VALUES (?, ?, ?, ?, ?, ?)"
        dados = (nome, cpf, telefone, email, endereco, cadastrado_por)
        c.execute(sql, dados)
        connection.commit()

    def entradaDadosPJ(self, nome, cnpj, telefone, email, endereco, cadastrado_por):  
        sql ="INSERT OR REPLACE INTO Cliente (nome, cnpj, telefone, email, endereco, cadastrado_por) VALUES (?, ?, ?, ?, ?, ?)"
        dados = (nome, cnpj, telefone, email, endereco, cadastrado_por)
        c.execute(sql, dados)
        connection.commit()

    # Método de leitura dos nomes de clientes
    def leNomeCliente(self): 
        sql = 'SELECT nome FROM Cliente'
        c.execute(sql)
        data = c.fetchall()
        return data    
        
    # Método de leitura de todos os dados dos clientes
    def leTudoCliente(self, nome): 
        sql = 'SELECT * FROM Cliente where nome=?'
        dados = (nome, )
        c.execute(sql,dados)
        data = c.fetchall()
        return data   
    
    # Método de Update do cliente, quando ele faz a reserva, salva alguns dados no bd
    def atualizaReserva(self, quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome):
        sql = "UPDATE Cliente SET quartosReservados=?, AreasReservadas=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=? WHERE nome=?"
        dado = (quartosReservados, AreasReservadas, tempoDeLocacao, dataDeEntrada, dataDeSaida, nome)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de Update do cliente, quando ele faz a reserva, apaga os dados que ele armazenou quando reservou o quarto
    def desfazReserva(self, nome):
        sql = "UPDATE Cliente SET quartosReservados=?, AreasReservadas=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=? WHERE nome=?"
        dado = (None, None, None, None, None, nome)
        c.execute(sql,dado)
        connection.commit()
    
    def consultaId(self, nome):
        sql = 'SELECT id FROM Cliente where nome=?'
        dados = (nome, )
        c.execute(sql,dados)
        data = c.fetchall()
        return data 

class BD_cadFunc():
    # Construtor
    def __init__(self): #controle
        self.criartabela()
        
    # Método de criação da tabela do banco de dados
    def criartabela(self):
        #sql ="CREATE TABLE IF NOT EXISTS dados (nome text, cpf text, funcao text, salario text, login text, senha text, UNIQUE(nome, login))"
        sql = """CREATE TABLE IF NOT EXISTS Funcionario (
            id INTEGER PRIMARY KEY,
            nome varchar(100) not null, 
            cpf varchar unique, 
            funcao varchar, 
            salario numeric not null check(salario > 0),
            login varchar(30) not null unique,
            senha varchar(30) not null,
            UNIQUE(nome, login))"""
        c.execute(sql)
        
        # seed
        c.execute("SELECT * FROM Funcionario")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES ('admin', '111222333', 'admin', 2300, 'admin', 'admin')")
            c.execute("INSERT INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES ('adm', '111222334', 'adm', 2300, 'adm', 'adm')")
            c.execute("INSERT INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES ('Sebastiao Maia', '12345678910', 'admin', '1050.12', 'tim', 'admin')")
            c.execute("INSERT INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES ('Caetanto Veloso', '12345678912', 'recepcionista', '215.51', 'caet', 'veloz')")
            c.execute("INSERT INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES ('Zé Ramalho', '12345678913', 'cantor', '4215.51', 'zezin', 'marralho')")
        connection.commit()

    # Método de entrada dos dados do usuário para o cadastramento
    def entradaDados(self, nome, cpf, funcao, salario, login, senha):  
        sql = "INSERT OR REPLACE INTO Funcionario (nome, cpf, funcao, salario, login, senha) VALUES (?, ?, ?, ?, ?, ?)"
        dados = (nome, cpf, funcao, salario, login, senha)
        c.execute(sql,dados)
        connection.commit()

    # Método que valida o login com os dados armazenados no BD
    def leDados(self, login, senha):
        sql = 'SELECT id FROM Funcionario WHERE login=? and senha=?'
        c.execute(sql,(login,senha))
        data = c.fetchall()
        return data

class BD_CardapioCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        #sql = "CREATE TABLE IF NOT EXISTS dados (dia text, textoCardapio text, UNIQUE(dia))"
        sql = """CREATE TABLE IF NOT EXISTS Cardapio (
            numero INTEGER PRIMARY KEY, 
            dia_semana int not null, 
            descricao varchar,
            cadastrado_por INTEGER not null REFERENCES Funcionario(id),
            UNIQUE(dia_semana))"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Cardapio")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (1, 'Café da Manhã: Vitamina de Banana e pão de queijo\nAlmoço: Feijoada, Arroz, Farofa',1)")
            c.execute("INSERT INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (0, 'Café da Manhã: Vitamina de Banana e bolo de banana\nAlmoço: Feijoada, Arroz, Farofa e Banananada', 3)")
            c.execute("INSERT INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (2, 'Café da Manhã: Banana com aveia de banana e pão de banana\nAlmoço: Feijoada, Arroz, Farofa e suco de banana', 2)")
            c.execute("INSERT INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (3, 'Café da Manhã: Banana de Banana e bananada\nAlmoço: Vaca atolada com banana, Arroz, Farofa e limonada', 1)")
        connection.commit()
    
    # Método de entrada dos dados do cardapio
    def insereDadosCar(self, dia_semana, descricao, cadastrado_por):
        self.criar_tabela()
        sql = "INSERT OR REPLACE INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (?, ?, ?)"
        dado = (dia_semana, descricao, cadastrado_por)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de leitura dos dados do cardapio
    def leDadosCar(self):
        c.execute('SELECT dia_semana, descricao FROM Cardapio')
        data = c.fetchall()
        return data
    
    # Método de atualização dos dados do cardapio
    def atualizaCar(self, dia_semana, descricao, cadastrado_por):
        sql = "DELETE FROM Cardapio WHERE dia_semana=?"
        dado = (dia_semana,)
        c.execute(sql,dado)
        connection.commit()

        sql = "INSERT OR REPLACE INTO Cardapio (dia_semana, descricao, cadastrado_por) VALUES (?, ?, ?)"
        dado = (dia_semana, descricao, cadastrado_por)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de remoção dos dados do cardapio
    def deletaCar(self, dia_semana):
        sql = "DELETE FROM Cardapio WHERE dia_semana=?"
        dado = (dia_semana,)
        c.execute(sql,dado)
        connection.commit()

class BD_EstoqueCRUD():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        #sql = "CREATE TABLE IF NOT EXISTS dados (local text, listaItens text, UNIQUE(local))"
        sql = """CREATE TABLE IF NOT EXISTS Estoque (
            id INTEGER PRIMARY KEY, 
            descricao varchar(60) not null, 
            local varchar UNIQUE,
            cadastrado_por INTEGER not null REFERENCES Funcionario(id))"""
        c.execute(sql)
        #c.execute("INSERT OR REPLACE INTO dados (local, listaItens) VALUES ('Recepção', 'Telefone, Bloco de notas e Canetas')")

        # seed
        c.execute("SELECT * FROM Estoque")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Estoque (descricao, local, cadastrado_por) VALUES ('Grampeador', 'Recepção', 1)")
            c.execute("INSERT INTO Estoque (descricao, local, cadastrado_por) VALUES ('Panela', 'Cozinha', 1)")
            c.execute("INSERT INTO Estoque (descricao, local, cadastrado_por) VALUES ('2 Travesseiros', 'Sala', 3)")
        connection.commit()

    
    # Método de entrada dos dados de estoque no bd
    def insereDadosEst(self, local, descricao, cadastrado_por):
        self.criar_tabela()
        sql = "INSERT OR REPLACE INTO Estoque (local, descricao, cadastrado_por) VALUES (?, ?, ?)"
        dado = (local, descricao, cadastrado_por)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de leitura dos dados de estoque no bd
    def leDadosEst(self):
        c.execute('SELECT local, descricao FROM Estoque')
        data = c.fetchall()
        return data
    
    # Método de atualização dos dados de estoque no bd
    def atualizaEst(self, local, descricao, cadastrado_por):
        sql = "DELETE FROM Estoque WHERE local=?"
        dado = (local,)
        c.execute(sql,dado)
        connection.commit()

        sql = "INSERT OR REPLACE INTO Estoque (local, descricao, cadastrado_por) VALUES (?, ?, ?)"
        dado = (local, descricao, cadastrado_por)
        c.execute(sql,dado)
        connection.commit()
        
    # Método de remoção dos dados de estoque no bd
    def deletaEst(self, local):
        sql = "DELETE FROM Estoque WHERE local=?"
        dado = (local,)
        c.execute(sql,dado)
        connection.commit()

class BD_ReclamaSugest():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        #sql = "CREATE TABLE IF NOT EXISTS dados (idrec INTEGER PRIMARY KEY AUTOINCREMENT, cliente text, textoReclamacao text, datetime text, status text, UNIQUE(cliente))"
        sql = """CREATE TABLE IF NOT EXISTS Reclamacoes (
            id INTEGER PRIMARY KEY, 
            id_cliente INTEGER UNIQUE References Cliente(id), 
            descricao varchar, 
            data varchar, 
            status varchar)"""
        c.execute(sql)
        #c.execute("INSERT OR IGNORE INTO dados (cliente, textoReclamacao, datetime, status) VALUES ('Elon-Musk', 'Vou te contratar, rapaz!', '18/02/2021', 'Outros')")
        
        # seed
        c.execute("SELECT * FROM Reclamacoes")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (2,'Vazamento da torneira', '2020/11/03', 'Em aberto')")
            c.execute("INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (1,'Barulho', '2020/12/03', 'Resolvido')")
            c.execute("INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (3,'Luz piscando', '2021/07/19', 'Em aberto')")
            c.execute("INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (4,'Vazamento da torneira', '2021/11/11', 'Em aberto')")
        connection.commit()
    
    # Método de entrada dos dados de Reclamacao
    def insereDadosRec(self, id_cliente, descricao, data, status ):
        self.criar_tabela()
        sql = "INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (?, ?, ?, ?)"
        data = (id_cliente, descricao, data, status)
        c.execute(sql,data)
        connection.commit()
    
    def leDadosRec(self):
        c.execute('SELECT id_cliente, descricao, data, status FROM Reclamacoes')
        data = c.fetchall()
        return data

    # Método de leitura dos dados de Reclamacao
    def leDadosRecIDCliente(self, id_cliente):
        sql = 'SELECT * FROM Reclamacoes where id_cliente=?'
        dado = (id_cliente,)
        c.execute(sql, dado)
        data = c.fetchall()
        return data
    
    # Método de atualização dos dados de Reclamacao
    def atualizaRec(self, id_cliente, status, data, descricao):
        sql = "DELETE FROM Reclamacoes WHERE id_cliente=?"
        dados = (id_cliente,)
        c.execute(sql, dados)

        self.criar_tabela()
        sql = "INSERT OR REPLACE INTO Reclamacoes (id_cliente, descricao, data, status) VALUES (?, ?, ?, ?)"
        dados = (id_cliente, descricao, data, status)
        c.execute(sql, dados)
        
        connection.commit()

        '''
        sql = "UPDATE Reclamacoes SET descricao=?, status=? WHERE id_cliente=?"
        data = (descricao, status, id_cliente)
        c.execute(sql,data)
        connection.commit()
        '''

    # Método de remoção dos dados de Reclamacao
    def deletaRec(self, id_cliente):
        sql = "DELETE FROM Reclamacoes WHERE id_cliente=?"
        data = (id_cliente,)
        c.execute(sql,data)
        connection.commit()
        
class BD_TarefasCRUD():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        #sql = "CREATE TABLE IF NOT EXISTS dados (prioridade text, listaTarefas text, UNIQUE(prioridade))"
        sql = """CREATE TABLE IF NOT EXISTS Tarefas (
            numero INTEGER PRIMARY KEY, 
            descricao varchar(100) not null, 
            prioridade varchar,
            cadastrado_por INTEGER not null REFERENCES Funcionario(id))"""
        c.execute(sql)
        #c.execute("INSERT OR IGNORE INTO dados (prioridade, listaTarefas) VALUES ('Urgente', 'Limpeza da piscina')")

        # seed
        c.execute("SELECT * FROM Tarefas")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES ('Comprar panelas', 'minima', 1)")
            c.execute("INSERT INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES ('Trocar sofá', 'media',2)")
            c.execute("INSERT INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES ('Reconstruir garagem', 'maxima',2)")
            c.execute("INSERT INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES ('Criar um Jardim', 'minima',1)")
            c.execute("INSERT INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES ('Limpar a piscina', 'media',1)")
        connection.commit()
    
    # Método de escrita no banco de dados
    def insereDadosTarefa(self, prioridade, descricao, cadastrado_por):
        sql ="INSERT OR REPLACE INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES (?, ?, ?)"
        dados = (descricao, prioridade, cadastrado_por)
        c.execute(sql, dados)
        connection.commit()
    
    # Método de leitura do banco de dados
    def leDadosTarefa(self):
        c.execute('SELECT prioridade, descricao FROM Tarefas')
        data = c.fetchall()
        return data
    
    # Método de atualização do banco de dados
    def atualizaTarefa(self, prioridade, descricao, cadastrado_por):
        #sql = "UPDATE Tarefas SET descricao=? WHERE prioridade=?"
        sql = "DELETE FROM Tarefas WHERE prioridade=?"
        dado = (prioridade,)
        c.execute(sql,dado)
        connection.commit()

        sql ="INSERT OR REPLACE INTO Tarefas (descricao, prioridade, cadastrado_por) VALUES (?, ?, ?)"
        dados = (descricao, prioridade, cadastrado_por,)
        c.execute(sql, dados)
        connection.commit()
        
    # Método de exclusão do banco de dados
    def deletaTarefa(self, prioridade):
        sql = "DELETE FROM Tarefas WHERE prioridade=?"
        dado = (prioridade,)
        c.execute(sql,dado)
        connection.commit()

class BD_Reserva():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS Reserva (
            numero INTEGER PRIMARY KEY, 
            valor numeric check(valor>0), 
            dataEntrada date, 
            dataSaida date CHECK(dataSaida>dataEntrada), 
            cadastrado_por INTEGER REFERENCES Funcionario(id), 
            reservado_por INTEGER REFERENCES Cliente(id), 
            idComodo INTEGER REFERENCES Comodo(id))"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Reserva")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (250, '2022-01-01', '2023-01-05', 1, 1, 1)")
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (2400, '2021-12-12', '2021-12-26', 2, 2, 2)")
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (1723, '2021-02-25', '2021-03-19', 3, 3, 3)")
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (123, '2022-05-01', '2022-06-01', 1, 4, 4)")
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (579, '2022-07-07', '2022-07-15', 2, 4, 1)")
            c.execute("INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (687, '2020-12-29', '2021-01-15', 3, 3, 4)")
        connection.commit()
    
    def consultaReservas(self):
        c.execute("SELECT * FROM Reserva")
        data = c.fetchall()
        return data

    def consultaReservasQuartosDisponiveis(self, data_entrada_input, data_saida_input):
        sql = '''SELECT *
        FROM Comodo c
        WHERE (c.tipo_quarto IS NOT NULL)
        AND c.id NOT IN (
            SELECT r.idComodo
            FROM Reserva r
            WHERE ((DATE(r.dataEntrada) >= DATE(?) AND DATE(r.dataSaida) <= DATE(?) )
                    OR (DATE(r.dataEntrada) >= DATE(?) AND DATE(r.dataSaida) <= DATE(?))
                    OR (DATE(r.dataEntrada) >= DATE(?) AND DATE(r.dataSaida) <= DATE(?)))
                        AND r.numero NOT IN (
                            SELECT d.numero
                            FROM Devolucao d));'''
        dados = (data_entrada_input, data_entrada_input, data_saida_input, data_saida_input, data_entrada_input, data_saida_input)
        c.execute(sql, dados)
        data = c.fetchall()
        return data

    def consultaReservasAreasDisponiveis(self, data_entrada_input, data_saida_input):
        sql = '''SELECT *
        FROM Comodo c
        WHERE (c.tipo_quarto IS NULL)
        AND c.id NOT IN (
            SELECT r.idComodo
            FROM Reserva r
            WHERE ((DATE(r.dataEntrada) >= DATE(?) AND DATE(r.dataSaida) <= DATE(?) )
                    OR (DATE(r.dataEntrada) >= DATE(?) AND DATE(r.dataSaida) <= DATE(?))
                    OR (DATE(r.dataEntrada) >= DATE(?)  AND DATE(r.dataSaida) <= DATE(?)))
                    AND r.numero NOT IN (
                        SELECT d.numero
                        FROM Devolucao d));'''
        dados = (data_entrada_input, data_entrada_input, data_saida_input, data_saida_input, data_entrada_input, data_saida_input,)
        c.execute(sql, dados,)
        data = c.fetchall()
        return data

    def realizaReserva(self, valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo):
        sql = "INSERT INTO Reserva (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo) VALUES (?, ?, ?, ?, ?, ?)"
        dados = (valor, dataEntrada, dataSaida, cadastrado_por, reservado_por, idComodo,)
        c.execute(sql, dados)
        connection.commit()

    def ultimaReserva(self):
        sql = 'SELECT MAX(numero) FROM Reserva'
        c.execute(sql)
        data = c.fetchall()
        return data 

class BD_Devolucao():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS Devolucao (
            numero INTEGER PRIMARY KEY REFERENCES Reserva(numero),
            valor numeric check(valor>0),
            dataDevolucao date)"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Devolucao")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Devolucao (numero, valor, dataDevolucao) VALUES (1, 259, '2022/01/04')")
            c.execute("INSERT INTO Devolucao (numero, valor, dataDevolucao) VALUES (2, 1521, '2021/02/23')")
            c.execute("INSERT INTO Devolucao (numero, valor, dataDevolucao) VALUES (3, 432, '2022/05/08')")
            c.execute("INSERT INTO Devolucao (numero, valor, dataDevolucao) VALUES (5, 725, '2021/01/14')")
        connection.commit()
    
    def consultaDevolucoes(self):
        c.execute('SELECT * FROM Reserva')
        data = c.fetchall()
        return data

    def consultaDevolucoesQuartosPendentes(self, idCliente):
        sql = """SELECT r.numero, r.idComodo, r.valor, c.id, c.nome
                    FROM Reserva r
                    INNER JOIN Comodo c
                    ON r.idComodo = c.id
                    WHERE (c.tipo_quarto IS NOT NULL)
                    AND (r.reservado_por = ?)
                    AND r.numero NOT IN ( 
                        SELECT d.numero
                        FROM Devolucao d);"""
        dados = (idCliente,)
        c.execute(sql, dados)
        data = c.fetchall()
        return data

    def consultaDevolucoesAreasPendentes(self, idCliente):
        sql = """SELECT r.numero, r.idComodo, c.id, c.nome
                    FROM Reserva r
                    INNER JOIN Comodo c
                    ON r.idComodo = c.id
                    WHERE (c.tipo_quarto IS NULL)
                    AND (r.reservado_por = ?)
                    AND r.numero NOT IN ( 
                        SELECT d.numero
                        FROM Devolucao d);"""
        dados = (idCliente,)
        c.execute(sql, dados)
        data = c.fetchall()
        return data

    def realizaDevolucao(self, numeroReserva, valor, dataDevolucao):
        sql = "INSERT INTO Devolucao (numero, valor, dataDevolucao) VALUES (?, ?, ?)"
        dados = (numeroReserva, valor, dataDevolucao)
        c.execute(sql, dados)
        connection.commit()

class BD_Comodo():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS Comodo (
            id INTEGER PRIMARY KEY, 
            nome varchar, 
            preco_dia numeric check(preco_dia>0), 
            tipo_quarto varchar,
            qtd_camas integer check(qtd_camas > 0),
            qtd_comodos integer check(qtd_comodos > 0)
            )"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Comodo")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Suíte 01', '150.62', 'Suíte', '1 Cama(s) de casal', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Suíte 02', '155.15', 'Suíte', '2 Cama(s) de casal', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Suíte 03', '153.21', 'Suíte', '1 Cama(s) de casal', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Solteiro 01', '100.91', 'Solteiro', '3 Cama(s) de solteiro', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Solteiro 02', '59.27', 'Solteiro', '2 Cama(s) de solteiro', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Solteiro 03', '63.85', 'Solteiro', '1 Cama(s) de solteiro', '2 Cômodos - Quarto e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Chalé 01', '250.00', 'Chalé', '1 Cama(s) de casal', '3 Cômodos - Quarto, Cozinha e Banheiro')")
            c.execute("INSERT INTO Comodo (nome, preco_dia, tipo_quarto, qtd_camas, qtd_comodos) VALUES ('Chalé 02', '325.10', 'Chalé', '2 Cama(s) de casal', '3 Cômodos - Quarto, Cozinha e Banheiro')")

            c.execute("INSERT INTO Comodo (nome, preco_dia) VALUES ('Churrasqueira', '95.60')")
            c.execute("INSERT INTO Comodo (nome, preco_dia) VALUES ('Sauna', '87.41')")
            c.execute("INSERT INTO Comodo (nome, preco_dia) VALUES ('Piscina', '53.37')")
            c.execute("INSERT INTO Comodo (nome, preco_dia) VALUES ('Salão de Festas', '125.72')")

        connection.commit()

    def leDadosCompletosQuarto(self):
        c.execute("SELECT * FROM Comodo")
        return c.fetchall()

    def valorComodo(self, id):
        sql = "SELECT preco_dia FROM Comodo WHERE id = ?"
        dados = (id,)
        c.execute(sql, dados)
        return c.fetchall()

    def consultaComodosDisponiveis(self):
        c.execute("""
                    SELECT *
                    FROM Comodo c
                    WHERE c.id NOT IN (
                    SELECT r.idComodo
                    FROM Reserva r
                    WHERE (r.dataEntrada > DATE() OR r.dataSaida < DATE())
                        AND r.numero NOT IN (
                        SELECT d.numero
                        FROM Devolucao d));""")
        return c.fetchall()

    def consultaComodosOcupados(self):
        c.execute("""
                    SELECT c.id, c.nome, c.preco_dia, c.tipo_quarto, c.qtd_camas, c.qtd_comodos
                    FROM Comodo c
                    WHERE c.id IN (
                    SELECT r.idComodo
                    FROM Reserva r
                    WHERE (r.dataEntrada > DATE() OR r.dataSaida < DATE())
                        AND r.numero NOT IN (
                        SELECT d.numero
                        FROM Devolucao d));""")
        return c.fetchall()

class BD_NotaFiscal():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS NotaFiscal (
            id INTEGER PRIMARY KEY REFERENCES Reserva(numero), 
            data_emissao TIMESTAMP
            )"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM NotaFiscal")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (1, '2022-01-01')")
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (2, '2021-12-12')")
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (3, '2021-02-25')")
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (4, '2022-05-01')")
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (5, '2022-07-07')")
            c.execute("INSERT INTO NotaFiscal (id, data_emissao) VALUES (6, '2020-12-29')")
        connection.commit()

    def insereNota(self, id, data):
        sql = "INSERT INTO NotaFiscal (id, data_emissao) VALUES (?, ?)"
        dado = (id, data,)
        c.execute(sql,dado)
        connection.commit()

    def leDadosNotaFiscal(self):
        c.execute('SELECT * FROM NotaFiscal')
        data = c.fetchall()
        return data

class BD_NotaDevolucao():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS NotaDevolucao (
            id INTEGER PRIMARY KEY REFERENCES Reserva(numero), 
            data_emissao TIMESTAMP
            )"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM NotaDevolucao")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO NotaDevolucao (id, data_emissao) VALUES (1, '2022-01-04')")
            c.execute("INSERT INTO NotaDevolucao (id, data_emissao) VALUES (2, '2021-02-23')")
            c.execute("INSERT INTO NotaDevolucao (id, data_emissao) VALUES (3, '2022-05-08')")
            c.execute("INSERT INTO NotaDevolucao (id, data_emissao) VALUES (5, '2021-01-14')")
        connection.commit()
    
    def insereNotaDevolucao(self, id, data):
        sql = "INSERT INTO NotaDevolucao (id, data_emissao) VALUES (?, ?)"
        dado = (id, data,)
        c.execute(sql,dado)
        connection.commit()

    # Método de leitura do banco de dados
    def leNotaDevolucao(self):
        c.execute('SELECT * FROM NotaDevolucao')
        data = c.fetchall()
        return data

class BD_Pousadaria():
    # Construtor
    def __init__(self):
        self.criartabela()

    # Método de criação da tabela do banco de dados
    def criartabela(self):
        sql = """CREATE TABLE IF NOT EXISTS Pousadaria (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome varchar UNIQUE, 
            telefone varchar(20),
            cnpj varchar,
            endereco varchar)"""
        c.execute(sql)

        # seed
        c.execute("SELECT * FROM Pousadaria")
        data = c.fetchall()
        if len(data) == 0:
            c.execute("INSERT INTO Pousadaria (nome, telefone, endereco, cnpj) VALUES ('Pousadaria', '(xx) xxxx-xxxx', 'Rua dos bobos, 0', 'xx.xxx.xxx/xxxx-xx')")
        connection.commit()

    # Método de leitura do banco de dados
    def leDadosPousadaria(self):
        c.execute('SELECT * FROM Pousadaria')
        data = c.fetchall()
        return data

def instancia_tabelas():
    BD_cadCliente()
    BD_cadFunc()
    BD_CardapioCRUD()
    BD_EstoqueCRUD()
    BD_ReclamaSugest()
    BD_TarefasCRUD()
    BD_Reserva()
    BD_Devolucao()
    BD_Comodo()
    BD_NotaFiscal()
    BD_NotaDevolucao()
    BD_Pousadaria()










'''
#Lazer
class BD_Lazer():
    # Inicializadores
    def __init__(self):
        self.criar_tabela()

    # Método que cria o banco de dados
    def criar_tabela(self):
        #sql = "CREATE TABLE IF NOT EXISTS dados (idArea text, status text, nome text, precoDia REAL, tempoDeLocacao INTEGER, dataDeEntrada text, dataDeSaida text, cliente text, UNIQUE(idArea))"
        c.execute(sql)
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('01', 'Disponível', 'Churrasqueira ', '90.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('02', 'Disponível', 'Sauna', '50.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('03', 'Disponível', 'Campo de Futebol', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('04', 'Disponível', 'Salão de Festas', '500.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('05', 'Disponível', 'Piscina', '100.00')")
        c.execute("INSERT OR IGNORE INTO dados (idArea, status, nome, precoDia) VALUES ('06', 'Disponível', 'Quadra', '50.00')")
        connection.commit()

    # Método de leitura dos dados da area de lazer
    def leDadosBasicosArea(self):
        c.execute('SELECT idArea, status, nome, precoDia FROM dados')
        data = c.fetchall()
        return data
    
    # Método de leitura de todos os dados da area de lazer
    def leDadosCompletosArea(self):
        c.execute('SELECT idArea, status, nome, precoDia, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente FROM dados')
        data = c.fetchall()
        return data
    
    # Método de atualização de status da area de lazer
    def atualizaStatusArea(self, nome):
        sql = "UPDATE dados SET status=?,tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=?, cliente=? WHERE nome=?"
        dado = (None, None, None, None, None, nome)
        c.execute(sql,dado)
        connection.commit()
    
    # Método de busca das areas disponiveis para datas especificas da area de lazer
    def buscaAreasDisponiveis(self, entrada, saida):
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
    
    # Método de busca das areas ocupadas para clientes especificos da area de lazer
    def buscaAreasOcupadasCliente(self, cliente):
        sql='SELECT nome FROM dados WHERE cliente=?'
        dado = (cliente,)
        c.execute(sql,dado)
        data = c.fetchall()
        return data
    
    # Método de busca de preços das areas de lazer
    def buscaPrecosLazer(self):
        sql='SELECT nome, precoDia FROM dados'
        c.execute(sql)
        data = c.fetchall()
        return data
    
    # Método de atualização de status e datas das areas de lazer
    def atualizaReservaLazer(self, nome, status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente):
        sql = "UPDATE dados SET status=?, tempoDeLocacao=?, dataDeEntrada=?, dataDeSaida=?, cliente=? WHERE nome=?"
        dado = (status, tempoDeLocacao, dataDeEntrada, dataDeSaida, cliente, nome)
        c.execute(sql,dado)
        connection.commit()
'''
'''
#Quarto
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

'''

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from datetime import datetime
from tkcalendar import *
import os


#Importações de arquivos locais
from BD_pousadaria import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

if not os.path.exists("NotasDevolucao"):
    os.makedirs("NotasDevolucao")

class DevolverWindow():
    # Construtor da Classe
    def __init__(self, funcionarioID):
        # Janela
        self.DevolverJanela = 0
        # Auxiliares das conversões de imagem
        self.camDevolverButton = 0
        self.camVoltarButton = 0
        self.camSelecionarButton = 0
        self.camNotaFiscal = 0
        #Botões
        self.botaoDevolver = 0
        self.botaoSelecionar = 0
        self.botaoVoltar = 0
        self.botaoNota = 0
        # Comboboxes
        self.clienteCombobox = 0
        # CheckButtons
        self.quartoCheck = 0
        self.lazerCheck = 0
        # Instanciamento de classes
        self.bdClientes = BD_cadCliente()
        self.bdComodo = BD_Comodo()
        self.bdPousadaria = BD_Pousadaria()
        self.bdNotaDevolucao = BD_NotaDevolucao()
        self.bdReserva = BD_Reserva()
        self.bdDevolucao = BD_Devolucao()
        # Dados das classes
        self.nomecliente = []
        self.dadosQuartos = 0
        self.dadosLazer = 0
        # Frames
        self.DevolverFrame = 0
        self.clienteFrame = 0
        self.areaFrame = 0
        self.quartoFrame = 0
        # Lista de marcadaos
        self.listaQuartos = []
        self.listAreas = []
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.quartosMarcados = []
        self.lazerMarcados = []
        self.cont = 0
        self.funcionarioID = funcionarioID
        self.id = 0
        self.now = 0

        
        
    # Método de Gerencia da tela Devolver cliente
    def DevolverTela(self):
        self.formataTelaDevolver()
        
        self.botaoVoltar = Button(self.DevolverJanela, command=self.ApagaTelaDevolver, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.DevolverJanela.mainloop()
    
    # Método de formatação da tela devolução
    def formataTelaDevolver(self):
        # Cria uma janela e define suas principais configurações
        self.DevolverJanela = Toplevel()
        self.DevolverJanela.title("Recepção - Devoluções")
        self.DevolverJanela.wm_iconbitmap(camIco)
        self.DevolverJanela.focus_force()
        self.DevolverJanela.geometry(tam)
        
        # Converte os pngs dos botões para imagem
        self.camDevolverButton = PhotoImage(file="Images\Botões\inicio_devolver.png", master=self.DevolverJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.DevolverJanela)
        self.camSelecionarButton = PhotoImage(file="Images\Botões\inicio_selecionar.png", master=self.DevolverJanela)
        self.camNotaFiscal = PhotoImage(file="Images\Botões\inicio_emitirNota.png", master=self.DevolverJanela)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        for nome in self.bdClientes.leNomeCliente():
            self.nomecliente.append(nome[0])

        if len(self.nomecliente)>0:
            #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
            # Cria o Frame de selecao de clientes
            self.clienteFrame = LabelFrame(self.DevolverJanela, text = "Selecione um cliente", padx=40, pady=20)
            self.clienteFrame.place(relx=0.15, rely=0.15, anchor="n")
            
            # Cria e posiciona os campos necessários para a devolução
            lb1 = Label(self.clienteFrame, text="Nomes:")
            lb1.grid(row=0, column=0, pady=5, sticky=W)

            # Cria e posiciona a combobox de seleção de clientes cadastrados
            self.clienteCombobox = ttk.Combobox(self.clienteFrame, value=self.nomecliente, width=25, state="readonly")
            self.clienteCombobox.current(0)
            self.clienteCombobox.grid(row=0, column=1, pady=5, sticky=W)
            
            # Cria um botão Devolver nessa tela e verifica se é possivel Devolver o usuario
            self.botaoSelecionar = Button(self.clienteFrame,command=self.DevolverMetodo, image=self.camSelecionarButton, bd=0, relief=GROOVE)
            self.botaoSelecionar.grid(row=3, column=0, pady=10, columnspan = 2)
            
            # Cria e posiciona uma Label de Aviso
            #self.aviso = Label()
            #self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            
        else:
            self.aviso = Label(self.DevolverJanela, text="ERRO - Não há clientes cadastrados no BD, tente novamente!",foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
        

    # Método principal da tela de devolucao que cuida de toda a formatação e seleção de quartos
    def DevolverMetodo(self):
        # Zera os valores exibidos e as listas selecionadas se o botão selecionar for pressionado novamente
        self.zeraValoresEListas()
        
        #---------------------------------------------------Frame - Devolver------------------------------------------------------#
        # Cria o Frame de devolucao
        self.DevolverFrame = LabelFrame(self.DevolverJanela, text = "Selecione os quartos/areas a serem devolvidos", padx=20, pady=20)
        self.DevolverFrame.place(relx=0.6, rely=0.1, anchor="n")
        
        # Busca os quartos e areas disponíveis no bd, se não houver nenhum, exibe uma msg de erro na tela
        self.buscaValidaBD()
        
        if len(self.dadosQuartos) == 0 and len(self.dadosLazer) == 0 and self.DevolverFrame!=0:
            return
        
        #---------------------------------------------------Frame - Seleciona Quartos------------------------------------------------------#
        # Cria um frame só para exibir os quartos disponíveis em checkbuttons
        self.quartoframe = LabelFrame(self.DevolverFrame, text = "Selecione os quartos a serem devolvidos", padx=20, pady=20)
        self.quartoframe.grid(row=0, column=0, padx=10, sticky=W, columnspan=2)
        
        # Cria dinamicamente checkbuttons dos quartos disponiveis e os salva numa variável
        for x in range(len(self.dadosQuartos)):
            self.listaQuartos.append(StringVar())
            self.listaQuartos[-1].set(0)
            self.quartoCheck = Checkbutton(self.quartoframe, text=self.dadosQuartos[x][-1], command=lambda x=x: self.criaLista(x), variable=self.listaQuartos[-1], onvalue=self.dadosQuartos[x][0], offvalue=0)
            self.quartoCheck.grid(row=x, column=0, sticky=W)
        
        #---------------------------------------------------Frame - Seleciona Areas de Lazer------------------------------------------------------#
        # Cria um frame só para exibir as areas de lazer disponíveis em checkbuttons
        self.areaFrame = LabelFrame(self.DevolverFrame, text = "Selecione as áreas de lazer a serem devolvidas", padx=20, pady=20)
        self.areaFrame.grid(row=0, column=2, padx=10, sticky=E, columnspan=2)
        
        # Cria dinamicamente checkbuttons das areas disponiveis e os salva numa variável
        for x in range(len(self.dadosLazer)):
            self.listAreas.append(StringVar())
            self.listAreas[-1].set(0)
            self.lazerCheck = Checkbutton(self.areaFrame,text=self.dadosLazer[x][-1], command=lambda x=x: self.criaListaLazer(x), variable=self.listAreas[-1], onvalue = self.dadosLazer[x][0], offvalue=0)
            self.lazerCheck.grid(row=x, column=0, sticky=W)
        

        if self.aviso != 0:
            self.aviso.destroy()
        # Cria um botão Devolver nessa tela e realizadevolucao
        self.botaoDevolver = Button(self.DevolverJanela, command=self.realizadevolucao, image=self.camDevolverButton, bd=0, relief=GROOVE)
        self.botaoDevolver.place(relx=0.9, rely=0.9, anchor="n")
        self.now = datetime.now().date()
        
        
    # Método de "Update" da tela devolucao, nesse momento que finalmente será efetuado o salvamento das informações de devolucao no banco de dados 
    def realizadevolucao(self):
        if self.aviso != 0:
                self.aviso.destroy()
        if len(self.quartosMarcados) > 0 or len(self.lazerMarcados) > 0:
            #Atualizar status dos quartos/areas de lazer no banco de dados
            if len(self.quartosMarcados) > 0:
                for x in range(len(self.quartosMarcados)):
                    valor = self.bdComodo.valorComodo(self.quartosMarcados[x][0])[0][0]
                    numeroreserva = self.quartosMarcados[x]
                    self.bdDevolucao.realizaDevolucao(numeroreserva, valor, self.now)
                    self.bdNotaDevolucao.insereNotaDevolucao(numeroreserva, self.now)

            if len(self.lazerMarcados) > 0:
                for x in range(len(self.lazerMarcados)):
                    valor = self.bdComodo.valorComodo(self.lazerMarcados[x][0])[0][0]
                    numeroreserva = self.lazerMarcados[x]
                    self.bdDevolucao.realizaDevolucao(numeroreserva, valor, self.now)
                    self.bdNotaDevolucao.insereNotaDevolucao(numeroreserva, self.now)

            if len(self.quartosMarcados) > 0:
                self.aviso = Label(self.DevolverJanela, text = "Quartos devolvidos com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

            elif len(self.lazerMarcados) > 0:
                self.aviso = Label(self.DevolverJanela, text = "Áreas de lazer devolvidas com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

            elif len(self.quartosMarcados) > 0 and len(self.lazerMarcados) > 0:
                self.aviso = Label(self.DevolverJanela, text = "Quartos e dependências devolvidas com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n")    
            
            # Destroi o botão Devolver e cria o botao emitir nota de devolução
            self.botaoDevolver.destroy()
            self.botaoNota = Button(self.DevolverJanela, command=self.emiteNotaFiscal, image=self.camNotaFiscal, bd=0, relief=GROOVE)
            self.botaoNota.place(relx=0.9, rely=0.9, anchor="n")
        
        else:
            self.aviso = Label(self.DevolverJanela, text="ERRO - Selecione algum quarto a ser devolvido!",foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

    # Escreve em um arquivo txt os dados da devolucao, servindo assim de nota fiscal
    def emiteNotaFiscal(self):
        tudoCliente = self.bdClientes.leTudoCliente(self.clienteCombobox.get())[0]
        tudoPousadaria = self.bdPousadaria.leDadosPousadaria()[0]
        tudoNotaDevolucao = self.bdNotaDevolucao.leNotaDevolucao()


        now = datetime.now().date()
        titulo = "#-----------------------------------------Nota De Devolução--------------------------------------------# \n\n"
        dadosPousadaria = """DADOS DO EMITENTE:
\nNome: {} 
Telefone: {}
Endereço: {}
CNPJ: {}""".format(tudoPousadaria[1], tudoPousadaria[2], tudoPousadaria[4], tudoPousadaria[3])
        
        separador = " \n________________________________________________________________________________________________\n\n"

        dadoscliente = """DADOS DO CLIENTE:
\nNome: {}
CPF: {}
CNPJ: {}
Telefone: {}
E-mail: {}
Endereço: {}
Quartos Devolvidos: {}
Áreas de lazer devolvidas: {}""".format(tudoCliente[1], tudoCliente[5], tudoCliente[6], tudoCliente[2], tudoCliente[3], tudoCliente[4], self.quartosMarcados, self.lazerMarcados)
        dadosNota = "Data da devolução: " + str(now) + "\n\n\n"
        
        # Abre o arquivo e escreve as linhas no mesmo
        caminhoNota = "NotasDevolucao/" + self.clienteCombobox.get() + ".txt."
        arquivo = open(caminhoNota, "a")
        arquivo.writelines(titulo)
        arquivo.writelines(dadosPousadaria)
        arquivo.writelines(separador)
        arquivo.writelines(dadoscliente)
        arquivo.writelines(separador)
        arquivo.writelines(dadosNota)
        arquivo.close()
        
        self.botaoNota.destroy()
        self.aviso.destroy()
        self.aviso = Label(self.DevolverJanela, text = "Nota de devolução emitida com sucesso!", foreground='green', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")  

    #---------------------------------------------------Funções Auxiliares------------------------------------------------------#    
    # Criar uma lista de elementos marcados na checkbutton, no caso, uma lista de quartos selecionados
    def criaLista(self,i):
        if self.quartosMarcados.count(self.listaQuartos[i].get())==0 and self.listaQuartos[i].get() != "0":
            self.quartosMarcados.append(self.listaQuartos[i].get())  
        else:
            self.quartosMarcados.remove(str(self.dadosQuartos[i][0]))
                
    # Criar uma lista de elementos marcados na checkbutton, no caso, uma lista de areas de lazer selecionadas
    def criaListaLazer(self, i): 
        if self.lazerMarcados.count(self.listAreas[i].get())==0 and self.listAreas[i].get() != "0":
            self.lazerMarcados.append(self.listAreas[i].get())  
        else:
            self.lazerMarcados.remove(str(self.dadosLazer[i][0]))
    
    # Busca o nome dos quartos e areas disponiveis no BD para criar os checkbuttons
    def buscaValidaBD(self):
        # Busca os nomes dos quartos no BD
        self.id = int(self.bdClientes.consultaId(self.clienteCombobox.get())[0][0])
        self.dadosQuartos = self.bdDevolucao.consultaDevolucoesQuartosPendentes(self.id)
        self.dadosLazer = self.bdDevolucao.consultaDevolucoesAreasPendentes(self.id)

        if len(self.dadosQuartos) == 0 and len(self.dadosLazer) == 0 and self.DevolverFrame!=0:
            self.DevolverFrame.destroy()
            if self.botaoDevolver!=0:
                self.botaoDevolver.destroy()
            if self.aviso!=0:
                self.aviso.destroy()
            self.aviso = Label(self.DevolverJanela, text = "Não há dependências a serem devolvidas!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
            return
        
        if self.aviso != 0:
            self.aviso.destroy()
        
            
    # Método necessário para zerar os dados das listas todas as vezes que o botão selecionar for clicado
    def zeraValoresEListas(self):
        if self.cont>0:
            self.DevolverFrame.destroy()
        else:
            if self.aviso != 0:
                self.aviso.destroy()
            self.cont += 1
            self.quartosMarcados = 0
            self.quartosMarcados = []
            self.listaQuartos = 0
            self.listaQuartos = []
            
            self.listAreas = 0
            self.listAreas = []
            self.lazerMarcados = 0
            self.lazerMarcados = []
    
    # Destroi a janela atual
    def ApagaTelaDevolver(self):
        self.DevolverJanela.destroy()
        
'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()

instancia_tabelas()
x8 = DevolverWindow(1)
x8.DevolverTela()
'''
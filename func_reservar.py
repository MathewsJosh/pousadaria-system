from tkinter import *
from tkinter import ttk
import re 
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from datetime import datetime,timedelta
from tkcalendar import *

#Importações de arquivos locais
from BD_quartosdisp import *
from BD_lazerdisp import *
from BD_cadcliente import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

class ReservarWindow():
    # Construtor da Classe
    def __init__(self):
        # Janela
        self.ReservarJanela = 0
        # Auxiliares das conversões de imagem
        self.camReservarButton = 0
        self.camVoltarButton = 0
        self.camSelecionarButton = 0
        self.camCalcularButton = 0
        self.campousadaria = 0
        #Botões
        self.botaoReservar = 0
        self.botaoSelecionar = 0
        self.botaoCalcular = 0
        self.botaoVoltar = 0
        # Entradas de dados
        self.dataEntrada = 0
        self.dataSaida = 0
        # Datetimes
        self.entradaDatetime = 0
        self.saidaDatetime = 0
        # Comboboxes
        self.clienteCombobox = 0
        # CheckButtons
        self.quartoCheck = 0
        self.lazerCheck = 0
        # Instanciamento de classes
        self.bdClientes = BD_cadCliente()
        self.bdQuartos = BD_Quartos()
        self.bdLazer = BD_Lazer()
        # Dados das classes
        self.dadoscliente = 0
        self.nomecliente = 0
        self.dadosQuartos = 0
        self.dadosLazer = 0
        # Calculos
        self.totalquartos = 0
        self.totalareas = 0
        self.totaltotal = self.totalquartos + self.totalareas
        # Exibe calculos
        self.precoAreaEntry = 0
        self.precoQuartoEntry = 0
        self.totalEntry = 0
        # Frames
        self.reservarFrame = 0
        self.clienteFrame = 0
        self.areaFrame = 0
        self.quartoFrame = 0
        self.valoresFrame = 0
        # Lista de marcadaos
        self.listaQuartos = []
        self.listAreas = []
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.quartosMarcados = []
        
        
        
        
    # Método de Gerencia da tela Reservar cliente
    def ReservarTela(self):
        self.formataTelaCadastro()
        
        # Cria um botão Reservar nessa tela e verifica se é possivel Reservar o usuario
        self.botaoReservar = Button(self.ReservarJanela, command=self.reservarMetodo, image=self.camReservarButton, bd=0, relief=GROOVE)
        self.botaoReservar.place(relx=0.9, rely=0.9, anchor="n")
        
        self.botaoVoltar = Button(self.ReservarJanela, command=self.reservarMetodo, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.ReservarJanela.mainloop()
   
    def formataTelaCadastro(self):
        # Cria uma janela e define suas principais configurações
        self.ReservarJanela = Tk()
        self.ReservarJanela.title("Recepção - Reservar quartos e áreas de lazer")
        self.ReservarJanela.wm_iconbitmap(camIco)
        self.ReservarJanela.focus_force()
        self.ReservarJanela.geometry(tam)
        
        # Converte os pngs dos botões para imagem
        self.camReservarButton = PhotoImage(file="Images\Botões\inicio_reservar.png", master=self.ReservarJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.ReservarJanela)
        self.camSelecionarButton = PhotoImage(file="Images\Botões\inicio_selecionar.png", master=self.ReservarJanela)
        self.camCalcularButton = PhotoImage(file="Images\Botões\inicio_calcular.png", master=self.ReservarJanela)
        self.campousadaria = PhotoImage(file="Images\Pousadaria-Logo2.png", master=self.ReservarJanela)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        

        #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
        # Cria o Frame de cadastro
        self.clienteFrame = LabelFrame(self.ReservarJanela, text = "Selecione um cliente", padx=20, pady=20)
        self.clienteFrame.place(relx=0.15, rely=0.15, anchor="n")
        
        # Cria os campos necessários para o cadastro
        lb1 = Label(self.clienteFrame, text="Nomes:")
        lb2 = Label(self.clienteFrame, text="Data de entrada:")
        lb3 = Label(self.clienteFrame, text="Data de saída:")
        
        # Posiciona as Labels e entradas de dados
        lb1.grid(row=0, column=0, pady=5, sticky=W)
        lb2.grid(row=1, column=0, pady=5, sticky=W)
        lb3.grid(row=2, column=0, pady=5, sticky=W)
        
        # Cria e posiciona a combobox de seleção de clientes cadastrados
        self.nomecliente = self.bdClientes.leNomeCliente()
        self.clienteCombobox = ttk.Combobox(self.clienteFrame, value=self.nomecliente, width=15, state="readonly")
        self.clienteCombobox.current(0)
        self.clienteCombobox.grid(row=0, column=1, pady=5, sticky=W)
        
        # Cria e posiciona a entry de datas de entrada e saida
        self.dataEntrada = DateEntry(self.clienteFrame, width=15, date_pattern='dd/mm/yyyy', state="readonly")
        self.dataEntrada.grid(row=1, column=1, pady=10, sticky=W)
    
        self.dataSaida = DateEntry(self.clienteFrame, width=15, date_pattern='dd/mm/yyyy', state="readonly")
        self.dataSaida.grid(row=2, column=1, pady=10, sticky=W)
        
        # Cria um botão Reservar nessa tela e verifica se é possivel Reservar o usuario
        self.botaoSelecionar = Button(self.clienteFrame,command=lambda: self.checaDatas(self.dataEntrada.get(),self.dataSaida.get()), image=self.camSelecionarButton, bd=0, relief=GROOVE)
        self.botaoSelecionar.grid(row=3, column=0, pady=10, columnspan = 2)
        
        # Cria e posiciona uma Label de Aviso
        self.aviso = Label()
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")
        
        
    def reservarMetodo(self):
        self.aviso = Label(self.ReservarJanela, text = "", foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        
        #---------------------------------------------------Frame - Seleciona Quartos e Areas de Lazer------------------------------------------------------#
        # Cria o Frame de reserva
        self.reservarFrame = LabelFrame(self.ReservarJanela, text = "Selecione os quartos/areas desejadas", padx=20, pady=20)
        self.reservarFrame.place(relx=0.5, rely=0.05, anchor="n")
        
        # Busca os quartos e areas disponíveis no bd, se não houver nenhum, exibe uma msg de erro na tela
        self.buscaValidaBD()
        
        
        #---------------------------------------------------Frame - Seleciona Quartos------------------------------------------------------#
        # Cria um frame só para exibir os quartos disponíveis em checkbuttons
        self.quartoframe = LabelFrame(self.reservarFrame, text = "Selecione os quartos desejados", padx=20, pady=20)
        self.quartoframe.grid(row=0, column=0, padx=10, sticky=W, columnspan=2)
        
        # Cria dinamicamente checkbuttons dos quartos disponiveis e os salva numa variável
        for x in range(len(self.dadosQuartos)):
            self.listaQuartos.append(StringVar())
            self.listaQuartos[-1].set(0)
            self.quartoCheck = Checkbutton(self.quartoframe, text=self.dadosQuartos[x][0], command=lambda x=x: self.criaLista(x), variable=self.listaQuartos[-1], onvalue=self.dadosQuartos[x][0], offvalue=0)
            self.quartoCheck.grid(row=x, column=0, sticky=W)
            #command=lambda x=x: self.marcaQuartos(x)
        
       
        #---------------------------------------------------Frame - Seleciona Areas de Lazer------------------------------------------------------#
        # Cria um frame só para exibir as areas de lazer disponíveis em checkbuttons
        self.areaFrame = LabelFrame(self.reservarFrame, text = "Selecione as áreas de lazer desejadas", padx=20, pady=20)
        self.areaFrame.grid(row=0, column=2, padx=10, sticky=E, columnspan=2)
        
        # Cria dinamicamente checkbuttons das areas disponiveis e os salva numa variável
        for x in range(len(self.dadosLazer)):
            self.listAreas.append(StringVar())
            self.listAreas[-1].set(0)
            self.quartoCheck = Checkbutton(self.areaFrame,text=self.dadosLazer[x][0], variable=self.listAreas[-1], onvalue = self.dadosLazer[x])
            self.quartoCheck.grid(row=x, column=0, sticky=W)
            
        
        
        #---------------------------------------------------Posiciona o resto do frame reservar------------------------------------------------------#
        # Cria e posiciona label e entry com o valor total calculado dos quartos selecionados
        lb1 = Label(self.reservarFrame, text="Somatório quartos:")
        lb1.grid(row=1, column=0, pady=10, sticky=E)
        self.precoQuartoEntry = Label(self.reservarFrame, text=self.totalquartos)
        self.precoQuartoEntry.grid(row=1, column=1, pady=10, sticky=W)
        
        # Cria e posiciona label e entry com o valor total calculado das areas de lazer selecionadas
        lb2 = Label(self.reservarFrame, text="Somatório áreas:")
        lb2.grid(row=1, column=2, pady=10, sticky=E)
        self.precoAreaEntry = Label(self.reservarFrame, text=self.totalareas)
        self.precoAreaEntry.grid(row=1, column=3, pady=10, sticky=W)
            
        #---------------------------------------------------Frame - Preços reserva------------------------------------------------------#
        # Cria o Frame de reserva
        #self.valoresFrame = LabelFrame(self.ReservarJanela, text = "Valores da reserva:", padx=20, pady=20)
        #self.valoresFrame.place(relx=0.85, rely=0.15, anchor="n")
        """
        # Cria e posiciona label e entry com o valor total calculado dos quartos selecionados
        lb1 = Label(self.valoresFrame, text="Somatório quartos:")
        lb1.grid(row=0, column=0, pady=10, sticky=W)
        self.precoQuartoEntry = Label(self.valoresFrame, text=self.totalareas)
        self.precoQuartoEntry.grid(row=0, column=1, pady=10, sticky=W)
        
        
        # Cria e posiciona label e entry com o valor total calculado das areas de lazer selecionadas
        lb2 = Label(self.valoresFrame, text="Somatório áreas:")
        lb2.grid(row=1, column=0, pady=10, sticky=W)
        self.precoAreaEntry = Entry(self.valoresFrame, width=20)
        self.precoAreaEntry.grid(row=1, column=1, pady=10, sticky=W)
        
        
        # Cria e posiciona label com preço final
        lb3 = Label(self.valoresFrame, text="Somatório áreas:")
        lb3.grid(row=2, column=0, pady=10, sticky=W)
        self.totalEntry = Entry(self.valoresFrame, width=20)
        self.totalEntry.grid(row=2, column=1, pady=10, sticky=W)
        
        
        #self.botaoCalcular = Button(self.valoresFrame, command = self.calcTotalQuartos, image=self.camCalcularButton, bd=0, relief=GROOVE)
        #self.botaoCalcular.grid(row=3, column=1, pady=10)
        """
        
        
        
        
    #---------------------------------------------------Funções Auxiliares------------------------------------------------------#    
    def buscaValidaBD(self):
        # Busca os nomes dos quartos no BD
        self.dadosQuartos = self.bdQuartos.buscaQuartosDisponiveis("Disponível")
        self.dadosLazer = self.bdLazer.buscaAreasDisponiveis("Disponível")
        
        if len(self.dadosQuartos) == 0:
            self.aviso = Label(self.ReservarJanela, text = "Não há quartos disponíveis!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        if len(self.dadosLazer) == 0:
            self.aviso = Label(self.ReservarJanela, text = "Não há areas de lazer disponíveis!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
            
            
    # Vai Criar uma lista de elementos marcados na checkbutton
    def criaLista(self,i):
        if self.quartosMarcados.count(self.listaQuartos[i].get())==0 and self.listaQuartos[i].get() != "0":
            self.quartosMarcados.append(self.listaQuartos[i].get())  
        else:
            self.quartosMarcados.pop(i)
        self.calcTotalQuartos()
        
                
    # Calcula somatorio do valor dos quartos selecionados
    def calcTotalQuartos(self):
        self.dadosQuartos = self.bdQuartos.buscaPrecosQuartos()
        self.totalquartos = 0
        for x in range(len(self.dadosQuartos)):
            for y in range(len(self.quartosMarcados)):
                if self.quartosMarcados[y] == self.dadosQuartos[x][0]:
                    self.totalquartos += float(self.dadosQuartos[x][1])
                    
        self.precoQuartoEntry["text"] = self.totalquartos


        
        
    

    # Verifica se a data digitado é válida
    def checaDatas(self, dEnt, dSai):
        now = datetime.now().date()
        self.entradaDatetime = datetime.strptime(dEnt, '%d/%m/%Y').date()
        self.saidaDatetime = datetime.strptime(dSai, '%d/%m/%Y').date()
        if self.entradaDatetime<=self.saidaDatetime and now<=self.entradaDatetime and now<=self.saidaDatetime:
            if (self.aviso != 0):
                self.aviso.destroy()
            self.reservarMetodo()
        else:
            self.aviso.destroy()
            # Cria e posiciona uma Label de Aviso
            self.aviso = Label(self.ReservarJanela, text="A data informada é inválida!",foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
            if(self.areaFrame != 0):
                self.deletaFramesQA()
                
            
    def deletaFramesQA(self):
        self.reservarFrame.destroy()
        self.botaoCalcular.destroy()


    # Destroi a janela atual
    def destroiTela(self):
        self.ReservarJanela.destroy()

x2 = ReservarWindow()
x2.ReservarTela()
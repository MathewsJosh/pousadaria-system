from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from datetime import date, datetime
from tkcalendar import *
import os

#Importações de arquivos locais
from BD_pousadaria import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

if not os.path.exists("NotasFiscais"):
    os.makedirs("NotasFiscais")

class ReservarWindow():
    # Construtor da Classe
    def __init__(self, funcionarioID):
        # Janela
        self.ReservarJanela = 0
        # Auxiliares das conversões de imagem
        self.camReservarButton = 0
        self.camVoltarButton = 0
        self.camSelecionarButton = 0
        self.camNotaFiscal = 0
        #Botões
        self.botaoReservar = 0
        self.botaoSelecionar = 0
        self.botaoVoltar = 0
        self.botaoNota = 0
        # Entradas de dados
        self.dataEntrada = 0
        self.dataSaida = 0
        # Datetimes
        self.entradaDatetime = 0
        self.saidaDatetime = 0
        self.diasDEstadia = 0
        # Comboboxes
        self.clienteCombobox = 0
        # CheckButtons
        self.quartoCheck = 0
        self.lazerCheck = 0
        # Instanciamento de classes
        self.bdClientes = BD_cadCliente()
        self.bdComodo = BD_Comodo()
        self.bdPousadaria = BD_Pousadaria()
        self.bdNotaFiscal = BD_NotaFiscal()
        self.bdReserva = BD_Reserva()
        # Dados das classes
        self.nomecliente = 0
        self.dadosQuartos = []
        self.dadosReserva = []
        self.dadosLazer = []
        # Calculos
        self.totalquartos = 0
        self.totalLazer = 0
        self.estadiaTotal = self.totalquartos + self.totalLazer
        # Exibe calculos
        self.precoAreaEntry = 0
        self.precoQuartoEntry = 0
        self.precoTotalEntry = 0
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
        self.lazerMarcados = []
        self.funcionarioID = funcionarioID
        self.now = 0

        
        
    # Método de Gerencia da tela Reservar cliente
    def ReservarTela(self):
        self.formataTelaReservar()
        
        self.botaoVoltar = Button(self.ReservarJanela, command=self.ApagaTelaReservar, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.ReservarJanela.mainloop()
   
    # Método de formatação da tela reservar
    def formataTelaReservar(self):
        # Cria uma janela e define suas principais configurações
        self.ReservarJanela = Toplevel()
        self.ReservarJanela.title("Recepção - Reservar quartos e/ou áreas de lazer")
        self.ReservarJanela.wm_iconbitmap(camIco)
        self.ReservarJanela.focus_force()
        self.ReservarJanela.geometry(tam)
        
        # Converte os pngs dos botões para imagem
        self.camReservarButton = PhotoImage(file="Images\Botões\inicio_reservar.png", master=self.ReservarJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.ReservarJanela)
        self.camSelecionarButton = PhotoImage(file="Images\Botões\inicio_selecionar.png", master=self.ReservarJanela)
        self.camNotaFiscal = PhotoImage(file="Images\Botões\inicio_emitirNota.png", master=self.ReservarJanela)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        self.nomecliente=[]
        for nome in self.bdClientes.leNomeCliente():
            self.nomecliente.append(nome[0])

        if len(self.nomecliente)>0:
            #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
            # Cria o Frame de cadastro
            self.clienteFrame = LabelFrame(self.ReservarJanela, text = "Selecione um cliente", padx=20, pady=20)
            self.clienteFrame.place(relx=0.15, rely=0.15, anchor="n")
            
            # Cria os campos necessários para o cadastro
            lb1 = Label(self.clienteFrame, text="Clientes:")
            lb2 = Label(self.clienteFrame, text="Data de entrada:")
            lb3 = Label(self.clienteFrame, text="Data de saída:")
            
            # Posiciona as Labels e entradas de dados
            lb1.grid(row=0, column=0, pady=5, sticky=W)
            lb2.grid(row=1, column=0, pady=5, sticky=W)
            lb3.grid(row=2, column=0, pady=5, sticky=W)
            
            # Cria e posiciona a combobox de seleção de clientes cadastrados
            self.clienteCombobox = ttk.Combobox(self.clienteFrame, value=self.nomecliente, width=15, state="readonly")
            self.clienteCombobox.current(0)
            self.clienteCombobox.grid(row=0, column=1, pady=5, sticky=W)
            
            # Cria e posiciona a entry de datas de entrada e saida
            self.dataEntrada = DateEntry(self.clienteFrame, width=15, date_pattern='yyyy-mm-dd', state="readonly")
            self.dataEntrada.grid(row=1, column=1, pady=10, sticky=W)
        
            self.dataSaida = DateEntry(self.clienteFrame, width=15, date_pattern='yyyy-mm-dd', state="readonly")
            self.dataSaida.grid(row=2, column=1, pady=10, sticky=W)
            
            # Cria um botão Reservar nessa tela e verifica se é possivel Reservar o usuario
            self.botaoSelecionar = Button(self.clienteFrame, command=lambda: [self.checaDatas(self.dataEntrada.get(),self.dataSaida.get())], image=self.camSelecionarButton, bd=0, relief=GROOVE)
            self.botaoSelecionar.grid(row=3, column=0, pady=10, columnspan = 2)
            
            # Cria e posiciona uma Label de Aviso
            self.aviso = Label()
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            
        else:
            self.aviso = Label(self.ReservarJanela, text="ERRO - Não há clientes cadastrados no BD, tente novamente!",foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
        
        
    # Verifica se a data digitada é válida
    def checaDatas(self, dEnt, dSai):
        if(self.botaoReservar!=0):
            self.botaoReservar.destroy()
        if(self.botaoNota != 0):
            self.botaoNota.destroy()
        
        now = datetime.now().date()
        self.entradaDatetime = datetime.strptime(dEnt, '%Y-%m-%d').date()
        self.saidaDatetime = datetime.strptime(dSai, '%Y-%m-%d').date()

        if (self.aviso != 0):
            self.aviso.destroy()
        if self.entradaDatetime<self.saidaDatetime and now<=self.entradaDatetime and now<self.saidaDatetime:
            # Calcula e salva a quantidade de dias selecionados para reserva
            self.entradaDatetime = datetime.strptime(dEnt, '%Y-%m-%d').date()
            self.saidaDatetime = datetime.strptime(dSai, '%Y-%m-%d').date()
            self.diasDEstadia = self.saidaDatetime - self.entradaDatetime
            self.diasDEstadia = self.diasDEstadia.days
            if(self.reservarFrame!=0):
                self.reservarFrame.destroy()
            self.reservarMetodo()
            
        else:
            if self.entradaDatetime>self.saidaDatetime:
                self.aviso = Label(self.ReservarJanela, text="ERRO - A data de entrada é depois da data saída!",foreground='red', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
                
            elif now>=self.saidaDatetime:
                self.aviso = Label(self.ReservarJanela, text="ERRO - A data de saída deve ser futura!",foreground='red', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
                
            elif now>self.entradaDatetime:
                self.aviso = Label(self.ReservarJanela, text="ERRO - A data de entrada deve ser futura!",foreground='red', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
                
            if(self.areaFrame != 0):
                self.reservarFrame.destroy()


    # Método principal da tela de reserva que cuida de toda a formatação e seleção de quartos
    def reservarMetodo(self):
        # Zera os valores exibidos e as listas selecionadas se o botão selecionar for pressionado novamente
        self.zeraValoresEListas()
        
        self.aviso = Label(self.ReservarJanela, text = "", foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        
        #---------------------------------------------------Frame - Reservar------------------------------------------------------#
        # Cria o Frame de reserva
        self.reservarFrame = LabelFrame(self.ReservarJanela, text = "Selecione os quartos/areas desejadas", padx=20, pady=20)
        self.reservarFrame.place(relx=0.6, rely=0.1, anchor="n")
        
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
            self.quartoCheck = Checkbutton(self.quartoframe, text=self.dadosQuartos[x][1], command=lambda x=x: self.criaLista(x), variable=self.listaQuartos[-1], onvalue=self.dadosQuartos[x][0], offvalue=0)
            self.quartoCheck.grid(row=x, column=0, sticky=W)
        
       
        #---------------------------------------------------Frame - Seleciona Areas de Lazer------------------------------------------------------#
        # Cria um frame só para exibir as areas de lazer disponíveis em checkbuttons
        self.areaFrame = LabelFrame(self.reservarFrame, text = "Selecione as áreas de lazer desejadas", padx=20, pady=20)
        self.areaFrame.grid(row=0, column=2, padx=10, sticky=E, columnspan=2)
        
        # Cria dinamicamente checkbuttons das areas disponiveis e os salva numa variável
        for x in range(len(self.dadosLazer)):
            self.listAreas.append(StringVar())
            self.listAreas[-1].set(0)
            self.lazerCheck = Checkbutton(self.areaFrame,text=self.dadosLazer[x][1], command=lambda x=x: self.criaListaLazer(x), variable=self.listAreas[-1], onvalue = self.dadosLazer[x][0], offvalue=0)
            self.lazerCheck.grid(row=x, column=0, sticky=W)
            
            
        #---------------------------------------------------Posiciona o resto do frame reservar------------------------------------------------------#
        # Cria e posiciona label e entry com o valor total calculado dos quartos selecionados
        lb1 = Label(self.reservarFrame, text="Somatório quartos:")
        lb1.grid(row=1, column=0, pady=10, sticky=E)
        self.precoQuartoEntry = Label(self.reservarFrame, text=self.totalquartos)
        self.precoQuartoEntry.grid(row=1, column=1, pady=10, sticky=W)
        
        # Cria e posiciona label e entry com o valor total calculado das areas de lazer selecionadas
        lb2 = Label(self.reservarFrame, text="Somatório áreas:")
        lb2.grid(row=1, column=2, pady=10, sticky=E)
        self.precoAreaEntry = Label(self.reservarFrame, text=self.totalLazer)
        self.precoAreaEntry.grid(row=1, column=3, pady=10, sticky=W)
                  
        # Cria e posiciona label e entry com o valor total calculado dos quartos selecionados
        lb3 = Label(self.reservarFrame, text="Valor da reserva para "+str(self.diasDEstadia)+" dias: ")
        lb3.grid(row=2, column=1, pady=10, sticky=E)
        self.precoTotalEntry = Label(self.reservarFrame, text=self.totalquartos)
        self.precoTotalEntry.grid(row=2, column=2, pady=10, sticky=W)

        # Cria um botão Reservar nessa tela e realizaReserva
        self.botaoReservar = Button(self.ReservarJanela, command=self.realizaReserva, image=self.camReservarButton, bd=0, relief=GROOVE)
        self.botaoReservar.place(relx=0.9, rely=0.9, anchor="n")
        
        
    # Método de "Update" da tela reserva, nesse momento que finalmente será efetuado o salvamento das informações de reserva no banco de dados 
    def realizaReserva(self):
        if self.aviso != 0:
            self.aviso.destroy()
        if len(self.quartosMarcados) > 0 or len(self.lazerMarcados) > 0:
            self.aviso.destroy()
            #Busca o id do cliente que está fazendo a reserva
            id = self.bdClientes.consultaId(self.clienteCombobox.get())[0][0]
            entrada = datetime.fromisoformat(self.dataEntrada.get())
            saida = datetime.fromisoformat(self.dataSaida.get())

            self.now = datetime.now().date()

            #Atualizar status dos quartos/areas de lazer no banco de dados
            if len(self.quartosMarcados) > 0:
                for x in range(len(self.quartosMarcados)):
                    valor = self.bdComodo.valorComodo(self.quartosMarcados[x])
                    self.bdReserva.realizaReserva(float(valor[0][0]), entrada, saida, int(self.funcionarioID), int(id), int(self.quartosMarcados[x]))
                    numeroReserva = int(self.bdReserva.ultimaReserva()[0][0])
                    self.bdNotaFiscal.insereNota(numeroReserva, self.now)

            if len(self.lazerMarcados) > 0:
                for x in range(len(self.lazerMarcados)):
                    valor = self.bdComodo.valorComodo(self.lazerMarcados[x])
                    self.bdReserva.realizaReserva(float(valor[0][0]), entrada, saida, int(self.funcionarioID), int(id), int(self.lazerMarcados[x]))
                    numeroReserva = int(self.bdReserva.ultimaReserva()[0][0])
                    self.bdNotaFiscal.insereNota(numeroReserva, self.now)

            if len(self.quartosMarcados) > 0 and len(self.lazerMarcados) == 0:
                self.aviso = Label(self.ReservarJanela, text = "Dependências reservadas com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

            elif len(self.lazerMarcados) > 0 and len(self.quartosMarcados) == 0 :
                self.aviso = Label(self.ReservarJanela, text = "Áreas de lazer reservadas com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

            elif len(self.quartosMarcados) > 0 and len(self.lazerMarcados) > 0:
                self.aviso = Label(self.ReservarJanela, text = "Quartos e dependências reservadas com sucesso!", foreground='green', font=self.fontStyle)
                self.aviso.place(relx=0.5, rely=0.9, anchor="n")    
            
            # Destroi o botão reservar e cria o botao emitir nota fiscal
            self.botaoReservar.destroy()
            self.botaoNota = Button(self.ReservarJanela, command=self.emiteNotaFiscal, image=self.camNotaFiscal, bd=0, relief=GROOVE)
            self.botaoNota.place(relx=0.9, rely=0.9, anchor="n")
        else:
            self.aviso = Label(self.ReservarJanela, text="ERRO - Selecione algum quarto ou area de lazer a ser reservado!",foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n") 

    # Escreve em um arquivo txt os dados da reserva, servindo assim de nota fiscal
    def emiteNotaFiscal(self):
        tudoCliente = self.bdClientes.leTudoCliente(self.clienteCombobox.get())[0]
        tudoPousadaria = self.bdPousadaria.leDadosPousadaria()[0]
        tudoNotaFiscal = self.bdNotaFiscal.leDadosNotaFiscal()
        
        self.aviso.destroy()
                
        #Textos Nota Fiscal
        titulo = "#-----------------------------------------------Nota Fiscal--------------------------------------------------# \n\n"
        dadosPousadaria = """DADOS DO EMITENTE:
\nNome: {} 
Telefone: {}
Endereço: {}
CNPJ: {}""".format(tudoPousadaria[1], tudoPousadaria[2], tudoPousadaria[4], tudoPousadaria[3])
        separador = " \n_______________________________________________________________________________________________________________\n\n"
        dadoscliente = """DADOS DO CLIENTE:
Nome: {}
CPF: {}
CNPJ: {}
Telefone: {}
E-mail: {}
Endereço: {}
Quartos Alugados: {}
Áreas de lazer alugadas: {}
Tempo de estadia: {}
Data de Entrada: {}
Data de Saída: {}""".format(tudoCliente[1], tudoCliente[5], tudoCliente[6], tudoCliente[2], tudoCliente[3], tudoCliente[4], self.quartosMarcados, self.lazerMarcados, self.diasDEstadia, self.dataEntrada.get(), self.dataSaida.get())
        
        dadosNota = "Data de emissão: " + str(self.now) + "\t\t\t" + "Valor: " + str(self.estadiaTotal) + "\n\n\n"
        
        # Abre o arquivo e escreve as linhas no mesmo
        caminhoNota = "NotasFiscais/" + self.clienteCombobox.get() + ".txt."
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
        self.aviso = Label(self.ReservarJanela, text = "Nota Fiscal emitida com sucesso!", foreground='green', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")  

    
    #---------------------------------------------------Funções Auxiliares------------------------------------------------------#    
    # Criar uma lista de elementos marcados na checkbutton, no caso, uma lista de quartos selecionados
    def criaLista(self,i):
        if self.quartosMarcados.count(self.listaQuartos[i].get())==0 and self.listaQuartos[i].get() != "0":
            self.quartosMarcados.append(self.listaQuartos[i].get())  
        else:
            self.quartosMarcados.remove(str(self.dadosQuartos[i][0]))
        self.calcTotalQuartos()
        
    # Criar uma lista de elementos marcados na checkbutton, no caso, uma lista de areas de lazer selecionadas
    def criaListaLazer(self, i):   
        if self.lazerMarcados.count(self.listAreas[i].get())==0 and self.listAreas[i].get() != "0":
            self.lazerMarcados.append(self.listAreas[i].get())  
        else:
            self.lazerMarcados.remove(str(self.dadosLazer[i][0]))
        self.calcTotalLazer()
    
    # Busca o nome dos quartos e areas disponiveis no BD para criar os checkbuttons
    def buscaValidaBD(self):

        #Converte as entradas e saidas para o formato de data
        entrada = datetime.fromisoformat(self.dataEntrada.get())
        saida = datetime.fromisoformat(self.dataSaida.get())

        # Busca os nomes dos quartos no BD
        self.dadosQuartos = self.bdReserva.consultaReservasQuartosDisponiveis(entrada, saida)
        self.dadosLazer = self.bdReserva.consultaReservasAreasDisponiveis(entrada, saida)

        if len(self.dadosQuartos) == 0:
            self.aviso = Label(self.ReservarJanela, text = "Não há quartos disponíveis!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        if len(self.dadosLazer) == 0:
            self.aviso = Label(self.ReservarJanela, text = "Não há áreas de lazer disponíveis!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        if len(self.dadosQuartos) == 0 and len(self.dadosLazer) == 0:
            self.aviso = Label(self.ReservarJanela, text = "Não há Quartos nem Áreas de lazer disponíveis!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.9, anchor="n")
            
    # Método necessário para zerar os dados das listas todas as vezes que o botão selecionar for clicado
    def zeraValoresEListas(self):
        self.quartosMarcados = 0
        self.quartosMarcados = []
        self.listaQuartos = 0
        self.listaQuartos = []
        self.totalquartos = 0
        
        self.listAreas = 0
        self.listAreas = []
        self.lazerMarcados = 0
        self.lazerMarcados = []
        self.totalLazer = 0
        
        
    #---------------------------------------------------Funções Auxiliares - Calculos------------------------------------------------------#
    # Calcula o somatorio do valor dos quartos selecionados e exibe na tela
    def calcTotalQuartos(self):
        self.totalquartos = 0
        for x in range(len(self.dadosQuartos)):
            for y in range(len(self.quartosMarcados)):
                if self.quartosMarcados[y] == str(self.dadosQuartos[x][0]):
                    self.totalquartos += float(self.dadosQuartos[x][2])
 
        self.precoQuartoEntry["text"] = self.totalquartos
        self.calculaValorTotal()
    
    # Calcula o somatorio do valor das areas de lazer selecionadas e exibe na tela
    def calcTotalLazer(self):
        self.totalLazer = 0
        for x in range(len(self.dadosLazer)):
            for y in range(len(self.lazerMarcados)):
                if self.lazerMarcados[y] == str(self.dadosLazer[x][0]):
                    self.totalLazer += float(self.dadosLazer[x][2])
                    
        self.precoAreaEntry["text"] = self.totalLazer
        self.calculaValorTotal()
    
    # Calcula o valor total da estadia e exibe na tela
    def calculaValorTotal(self):
        self.estadiaTotal = self.diasDEstadia*(self.totalquartos + self.totalLazer) 
        self.precoTotalEntry["text"] = self.estadiaTotal
    
    # Destroi a janela atual
    def ApagaTelaReservar(self):
        self.ReservarJanela.destroy()

"""
#OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()
instancia_tabelas()
x7 = ReservarWindow(1)
x7.ReservarTela()
"""

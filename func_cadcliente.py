from tkinter import *
from tkinter import ttk
import re 
from BD_cadcliente import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

class cadastrarWindow():
    # Construtor da Classe
    def __init__(self):
        # Janela
        self.cadastrarJanela = 0
        # Auxiliares das conversões de imagem
        self.camCadastrarButton = 0
        self.camVoltarButton = 0
        self.campousadaria = 0
        # Entradas de dados
        self.nomeEntry = 0
        self.cpfEntry = 0
        self.emailEntry = 0
        self.telefoneEntry = 0
        self.tipoEntry = 0
        self.enderecoEntry = 0
        self.RuaEntry = 0
        self.NumEntry = 0
        self.bairroEntry = 0
        self.cidadeEntry = 0
        self.estadoEntry = 0
        # Instanciamento de classes
        self.bdcadCliente = BD_cadCliente()
        #Botões
        self.botaoCadastrar = 0
        self.botaoVoltar = 0
        # Frames
        self.cadastrarFrame = 0
        self.enderecoFrame = 0
        # Outros
        self.aviso = 0
        self.dadosCadCliente = 0
        
        
    # Método de Gerência da tela cadastrar cliente
    def cadastrarTela(self):
        self.formataTelaCadastro()
        
        # Cria um botão Cadastrar nessa tela e verifica se é possivel cadastrar o usuario
        self.botaoCadastrar = Button(self.cadastrarJanela, command=self.cadastrarMetodo, image=self.camCadastrarButton, bd=0, relief=GROOVE)
        self.botaoCadastrar.place(relx=0.9, rely=0.9, anchor="n")
        
        self.botaoVoltar = Button(self.cadastrarJanela, command=self.cadastrarMetodo, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.cadastrarJanela.mainloop()

    # Método principal da tela cadastrar cliente
    def cadastrarMetodo(self):
        # Apaga qualquer aviso anterior
        self.aviso.destroy()
        self.aviso.forget()
        
        if self.verificaCampos():
            self.aviso = Label(self.cadastrarJanela, text="Existem campos vazios, tente novamente!", foreground='red', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
        
        elif not(self.checaEmail(self.emailEntry.get())) and not(self.checaTelefone(self.telefoneEntry.get())):
            self.aviso = Label(self.cadastrarJanela, text="Telefone e email inválido, tente novamente!", foreground='red', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
               
        elif not(self.checaEmail(self.emailEntry.get())):
            self.aviso = Label(self.cadastrarJanela, text="Email inválido, tente novamente!", foreground='red', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            
        elif not(self.checaTelefone(self.telefoneEntry.get())):
            self.aviso = Label(self.cadastrarJanela, text="Telefone inválido, tente novamente!", foreground='red', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
                 
        else:
            self.aviso = Label(self.cadastrarJanela, text="Dados cadastrados com sucesso!", foreground='green', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            self.enderecoEntry = str(self.RuaEntry.get()) + ", " + str(self.NumEntry.get()) + " - " + str(self.bairroEntry.get()) + " - " + str(self.cidadeEntry.get()) + ", " + str(self.estadoEntry.get())
            self.bdcadCliente.entradaDados(self.nomeEntry.get(), self.cpfEntry.get(), self.telefoneEntry.get(), self.emailEntry.get(), self.tipoEntry.get(), self.enderecoEntry)
            
    # Método de formatação da tela de cadastro de clientes
    def formataTelaCadastro(self):
        # Cria uma janela e define suas principais configurações
        self.cadastrarJanela = Tk()
        self.cadastrarJanela.title("Cadastre-se no sistema")
        self.cadastrarJanela.wm_iconbitmap(camIco)
        self.cadastrarJanela.focus_force()
        self.cadastrarJanela.geometry(tam)
        
        # Converte os pngs dos botões para imagem
        self.camCadastrarButton = PhotoImage(file="Images\Botões\inicio_cadastrar.png", master=self.cadastrarJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.cadastrarJanela)
        self.campousadaria = PhotoImage(file="Images\Pousadaria-Logo2.png", master=self.cadastrarJanela)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.campousadaria)
        l1.place(relx=0.5, rely=0.03, anchor="n")
        
        #---------------------------------------------------Frame - Cadastro de Cliente------------------------------------------------------#
        # Cria o Frame de cadastro
        self.cadastrarFrame = LabelFrame(self.cadastrarJanela, text = "Dados do Cliente", padx=20, pady=20)
        self.cadastrarFrame.place(relx=0.3, rely=0.3, anchor="n")

        # Cria os campos necessários para o cadastro
        lb1 = Label(self.cadastrarFrame, text="Nome:")
        lb2 = Label(self.cadastrarFrame, text="CPF:")
        lb3 = Label(self.cadastrarFrame, text="E-mail:")
        lb4 = Label(self.cadastrarFrame, text="Telefone:")
        lb5 = Label(self.cadastrarFrame, text="Tipo:")
        
        self.nomeEntry = Entry(self.cadastrarFrame, width=20)
        self.cpfEntry = Entry(self.cadastrarFrame, width=20)
        self.emailEntry = Entry(self.cadastrarFrame, width=20)
        self.telefoneEntry = Entry(self.cadastrarFrame, width=20)
        self.pagamentoEntry = Entry(self.cadastrarFrame, width=20)

        # Posiciona as Labels e entradas de dados
        lb1.grid(row=0, column=0, pady=5, sticky=W)
        lb2.grid(row=1, column=0, pady=5, sticky=W)
        lb3.grid(row=2, column=0, pady=5, sticky=W)
        lb4.grid(row=3, column=0, pady=5, sticky=W)
        lb5.grid(row=4, column=0, pady=5, sticky=W)
        self.nomeEntry.grid(row=0, column=1, pady=5, sticky=E)
        self.cpfEntry.grid(row=1, column=1, pady=5, sticky=E)
        self.emailEntry.grid(row=2, column=1, pady=5, sticky=E)
        self.telefoneEntry.grid(row=3, column=1, pady=5, sticky=E)
        
        # Cria e posiciona a combobox de função - Irá definir o nível de acesso do funcionário ao sistema
        opcoes = ["Pessoa Física", "Pessoa Jurídica"]
        self.tipoEntry = ttk.Combobox(self.cadastrarFrame, value=opcoes, width=17, state="readonly")
        self.tipoEntry.current(0)
        self.tipoEntry.grid(row=4, column=1, pady=5, sticky=W)
        
        #---------------------------------------------------Frame - Endereço de cobrança------------------------------------------------------#
        # Cria o Frame de cadastro
        self.enderecoFrame = LabelFrame(self.cadastrarJanela, text = "Endereço", padx=20, pady=20)
        self.enderecoFrame.place(relx=0.7, rely=0.3, anchor="n")
        
        # Cria as labels e Entrys do frame endereço
        lb6 = Label(self.enderecoFrame, text="Rua:", width=10, anchor=W)
        lb7 = Label(self.enderecoFrame, text="Numero:", width=10, anchor=W)
        lb8 = Label(self.enderecoFrame, text="Bairro:", width=10, anchor=W)
        lb9 = Label(self.enderecoFrame, text="Cidade:", width=10, anchor=W)
        lb10 = Label(self.enderecoFrame, text="Estado:", width=10, anchor=W)
        self.RuaEntry = Entry(self.enderecoFrame)
        self.NumEntry = Entry(self.enderecoFrame, width=20)
        self.bairroEntry = Entry(self.enderecoFrame, width=20)
        self.cidadeEntry = Entry(self.enderecoFrame, width=20)
        self.estadoEntry = Entry(self.enderecoFrame, width=20)
        
        #Posiciona as Labels e Entrys
        lb6.grid(row=0, column=0, pady=5, sticky=W)
        lb7.grid(row=1, column=0, pady=5, sticky=W)
        lb8.grid(row=2, column=0, pady=5, sticky=W)
        lb9.grid(row=3, column=0, pady=5, sticky=W)
        lb10.grid(row=4, column=0, pady=5, sticky=W)
        self.RuaEntry.grid(row=0, column=1, pady=5, sticky=E)
        self.NumEntry.grid(row=1, column=1, pady=5, sticky=E)
        self.bairroEntry.grid(row=2, column=1, pady=5, sticky=E)
        self.cidadeEntry.grid(row=3, column=1, pady=5, sticky=E)
        self.estadoEntry.grid(row=4, column=1, pady=5, sticky=E)
        
        # Cria e posiciona uma Label de Aviso
        self.aviso = Label()
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")
        
    #---------------------------------------------------Funções Auxiliares------------------------------------------------------#
    # Verifica se o telefone digitado é válido
    def checaTelefone(self, telefone):
        regex = "^\(?[1-9]{2}\)? ?9?[0-9]{4}\-?[0-9]{4}$"
        if(re.search(regex, str(telefone))):
            # Caso seja válido    
            return True
        else: 
            # Caso seja inválido  
            return False
        
    # Verifica se o email digitado é valido
    def checaEmail(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+([.]\w+)?$' 
        if(re.search(regex, email)):  
            # Caso seja válido  
            return True
        else:  
            # Caso seja inválido  
            return False

    # Verifica se uma ou mais entradas de dados estão vazias
    def verificaCampos(self):
        if self.nomeEntry.get() == "" or self.cpfEntry.get() == "" or self.telefoneEntry.get() == "" or self.emailEntry.get() == "" or self.tipoEntry.get() == "" or self.RuaEntry.get() == "" or self.NumEntry.get() == "" or self.bairroEntry.get() == "" or self.cidadeEntry.get() == "" or self.estadoEntry.get() == "":
            return True
        return False

    # Destroi a janela atual
    def destroiTela(self):
        self.cadastrarJanela.destroy()

x2 = cadastrarWindow()
x2.cadastrarTela()
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from BD_cadfuncionario import *


#Variaveis Globais
tam = "800x600"
camIco = "Images\Icones\Pousadaria.ico"

class cadastrarWindow():
    # Construtor da Classe
    def __init__(self):
        # Janela
        self.cadastrarJanela = 0
        # Auxiliares das conversões de imagem
        self.camCadastrarButton = 0
        self.camVoltarButton = 0
        # Entradas de dados
        self.nomeEntry = 0
        self.cpfEntry = 0
        self.funcaoEntry = 0
        self.salarioEntry = 0
        self.loginEntry = 0
        self.senhaEntry = 0
        self.AutorizacaoEntry = 0
        # Botões
        self.botaoCadastrar = 0
        self.botaoVoltar = 0
        # Instanciamentos de classes
        self.CadFunc = BD_cadFunc(True)
        # Frames
        self.cadastrarFrame = 0
        # Outros
        self.aviso = 0
        self.dadosCadFunc = 0
        self.funcoes = ["Recepção", "Administração", "Limpeza", "Cozinha" , "Outros"]
        
    # Criar a janela principal de inserção de dados cadastrais
    def cadastrarTela(self):
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        self.formataTelaCadastro()
        
        # Cria um botão Cadastrar nessa tela e verifica se é possivel cadastrar o usuario
        self.botaoCadastrar = Button(self.cadastrarJanela, text="Cadastrar!", command=self.cadastrarMetodo, image=self.camCadastrarButton, bd=0, relief=GROOVE)
        self.botaoCadastrar.place(relx=0.9, rely=0.9, anchor="n")
        
        # Cria um botão Voltar para voltar para a tela de início
        self.botaoVoltar = Button(self.cadastrarJanela, command=self.destroiTela, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.cadastrarJanela.mainloop()

    # Método que salva os dados inseridos no banco de dados
    def cadastrarMetodo(self):
        # Apaga qualquer aviso anterior
        self.aviso.destroy()
        self.aviso.forget()
        
        if self.verificaCampos():
            # Avisa que existe algum campo vazio
            self.aviso = Label(self.cadastrarJanela, text="Existem campos vazios, tente novamente!", foreground='red', font=self.fontStyle)
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            #return 0
        else:
            # Adiciona os dados inseridos ao banco de dados
            self.CadFunc.entradaDados(self.nomeEntry.get(), self.cpfEntry.get(), self.funcaoEntry.get(), self.salarioEntry.get(), self.loginEntry.get(), self.senhaEntry.get())

            # Avisa que o cadastro deu certo
            self.aviso = Label(self.cadastrarJanela, text="Cadastro efetuado com sucesso!", foreground='green', font=self.fontStyle)
        
        # Posiciona a label de aviso
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")

    # Método que Formata a tela de cadastro
    def formataTelaCadastro(self):
        # Cria uma janela e define suas principais configurações
        self.cadastrarJanela = Toplevel()
        self.cadastrarJanela.title("Início - Cadastro de funcionários")
        self.cadastrarJanela.wm_iconbitmap(camIco)
        self.cadastrarJanela.focus_force()
        self.cadastrarJanela.geometry(tam)
        
        # Converte os pngs dos botões para imagem
        self.camCadastrarButton = PhotoImage(file="Images\Botões\inicio_cadastrar.png", master=self.cadastrarJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.cadastrarJanela)

        #---------------------------------------------------Frame - Cadastro de Funcionário------------------------------------------------------#
        # Cria o Frame de cadastro
        self.cadastrarFrame = LabelFrame(self.cadastrarJanela, text = "Insira os dados do Funcionário", padx=20, pady=20)
        self.cadastrarFrame.place(relx=0.5, rely=0.2, anchor="n")

        # Cria os campos necessários para o cadastro
        lb1 = Label(self.cadastrarFrame, text="Nome: ", font=self.fontStyle)
        lb2 = Label(self.cadastrarFrame, text="CPF:", font=self.fontStyle)
        lb3 = Label(self.cadastrarFrame, text="Função:", font=self.fontStyle)
        lb4 = Label(self.cadastrarFrame, text="Salario:", font=self.fontStyle)
        lb5 = Label(self.cadastrarFrame, text="Login:", font=self.fontStyle)
        lb6 = Label(self.cadastrarFrame, text="Senha:", font=self.fontStyle)
        self.nomeEntry = Entry(self.cadastrarFrame, width=20, font=self.fontStyle)
        self.cpfEntry = Entry(self.cadastrarFrame, width=20, font=self.fontStyle)
        self.salarioEntry = Entry(self.cadastrarFrame, width=20, font=self.fontStyle)
        self.loginEntry = Entry(self.cadastrarFrame, width=20, font=self.fontStyle)
        self.senhaEntry = Entry(self.cadastrarFrame, width=20, show='*', font=self.fontStyle)

        # Posiciona as Labels e entradas de dados
        lb1.grid(row=0, column=0, pady=5, sticky=W)
        lb2.grid(row=1, column=0, pady=5, sticky=W)
        lb3.grid(row=2, column=0, pady=5, sticky=W)
        lb4.grid(row=3, column=0, pady=5, sticky=W)
        lb5.grid(row=4, column=0, pady=5, sticky=W)
        lb6.grid(row=5, column=0, pady=5, sticky=W)
        self.nomeEntry.grid(row=0, column=1, pady=5, sticky=E)
        self.cpfEntry.grid(row=1, column=1, pady=5, sticky=E)
        self.salarioEntry.grid(row=3, column=1, pady=5, sticky=E)
        self.loginEntry.grid(row=4, column=1, pady=5, sticky=E)
        self.senhaEntry.grid(row=5, column=1, pady=5, sticky=E)

        # Cria e posiciona a combobox de função - Permite selecionar a função do funcionário
        self.funcaoEntry = ttk.Combobox(self.cadastrarFrame, value=self.funcoes, width=18, state="readonly", font=self.fontStyle)
        self.funcaoEntry.current(0)
        self.funcaoEntry.grid(row=2, column=1, pady=5, sticky=E)
        
        # Cria e posiciona uma Label de Aviso
        self.aviso = Label()
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")

    #---------------------------------------------------Funções Auxiliares------------------------------------------------------# 
    
    # Verifica se uma ou mais entradas de dados estão vazias
    def verificaCampos(self):
        if self.nomeEntry.get() == "" or self.cpfEntry.get() == "" or self.funcaoEntry.get() == "" or self.salarioEntry.get() == "" or self.loginEntry.get() == "" or self.senhaEntry.get() == "":
            return True
        return False

    # Destroi a janela atual
    def destroiTela(self):
        self.cadastrarJanela.destroy()

'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.tela_inicial.mainloop()
x2 = cadastrarWindow()
x2.cadastrarTela()
'''
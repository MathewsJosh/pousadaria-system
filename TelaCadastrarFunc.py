from tkinter import *

#Variaveis Globais
tam = "800x600"
camIco = "Icones\Pousadaria.ico"

class cadastrarWindow():
    # Construtor da Classe
    def __init__(self):
        self.cadastrarJanela = 0
        self.userEntry2 = 0
        self.passEntry2 = 0
        self.admKeyEntry2 = 0
        self.funcao=0
        self.aviso = 0
        self.botaoCadastrar = 0
        self.camCadastrarButton = 0
        self.camVoltarButton = 0

    # Criar uma janela sem valores
    def cadastrarTela(self):

        # Cria uma janela e define suas principais configurações
        self.cadastrarJanela = Tk()
        self.cadastrarJanela.title("Cadastre-se no sistema")
        self.cadastrarJanela.wm_iconbitmap(camIco)
        self.cadastrarJanela.focus_force()
        self.cadastrarJanela.geometry(tam)

        # Cria os campos necessários para o cadastro
        lb1 = Label(self.cadastrarJanela, text="Nome: ", width=5)
        lb2 = Label(self.cadastrarJanela, text="Senha: ", width=5)
        self.aviso = Label(self.cadastrarJanela)
        self.userEntry2 = Entry(self.cadastrarJanela, width=15)
        self.passEntry2 = Entry(self.cadastrarJanela, width=15, show='*')


        # Posiciona as Labels e entradas de dados
        lb1.place(relx=0.35, rely=0.13, anchor="n")
        lb2.place(relx=0.35, rely=0.25, anchor="n")
        self.userEntry2.place(relx=0.55, rely=0.13, anchor="n")
        self.passEntry2.place(relx=0.55, rely=0.25, anchor="n")

        # Converte os pngs dos botões para imagem
        self.camCadastrarButton = PhotoImage(file="Botões\Tela inicial//button_cadastrarTI.png", master=self.cadastrarJanela)
        self.camVoltarButton = PhotoImage(file="Botões\Tela inicial//button_voltarTI.png", master=self.cadastrarJanela)
        
        # Cria um botão Cadastrar nessa tela e verifica se é possivel cadastrar o usuario
        self.botaoCadastrar = Button(self.cadastrarJanela, text="Cadastrar!", command=self.cadastrarMetodo, image=self.camCadastrarButton, bd=0, relief=GROOVE)
        self.botaoCadastrar.place(relx=0.5, rely=0.6, anchor="n")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.cadastrarJanela.mainloop()

    def cadastrarMetodo(self):
        # Apaga qualquer aviso anterior
        self.aviso.destroy()
        self.aviso.forget()

        if self.userEntry2.get() == "" or self.passEntry2.get() == "":
            # Avisa que deu erro ao cadastrar
            self.aviso = Label(self.cadastrarJanela, text="Digite um nome de usuário e/ou senha!", foreground='red')
            self.aviso.place(relx=0.5, rely=0.4, anchor="n")
            return 0
        else:
            # Adiciona os dados inseridos no banco de dados
            #entradaDados(self.userEntry2.get(), self.passEntry2.get())

            # Avisa que o cadastro deu certo
            self.aviso = Label(self.cadastrarJanela, text="Cadastro efetuado com sucesso!", foreground='green')
            
            # Altera o botão cadastrar para "Voltar"
            self.botaoCadastrar.destroy()
            self.botaoCadastrar.forget()
            self.botaoCadastrar = Button(self.cadastrarJanela, command=self.destroiTela, image=self.camVoltarButton, bd=0, relief=GROOVE)
            self.botaoCadastrar.place(relx=0.5, rely=0.6, anchor="n")
            
            
            ######self.cadastrarJanela.mainloop()
        
        # Posiciona a label de aviso
        self.aviso.place(relx=0.5, rely=0.4, anchor="n")

    def destroiTela(self):
        self.cadastrarJanela.destroy()

#x2 = cadastrarWindow()
#x2.cadastrarTela()
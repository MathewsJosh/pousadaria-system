from tkinter import *
import tkinter.font as tkFont

# Importações locais
from BD_cadfuncionario import *
from func_menu import *

#Variaveis Globais
tam = "800x600"
camIco = "Images\Icones\Pousadaria.ico"

class loginWindow():
    # Construtor para a classe
    def __init__(self, telaiInicial):
        self.telaiInicial = telaiInicial
        # Janela
        self.loginJanela = 0
        # Auxiliares das conversões de imagem
        self.camLoginButton = 0
        self.camAbrirButton = 0
        # Botões
        self.botaoAbrir = 0
        self.botaoEntrar = 0
        self.botaoVoltar = 0
        # Instanciamento de classes
        self.dadosFunc = BD_cadFunc(False)
        self.chamMenu = MenuRecepcaoWindow()
        # Entradas de dados
        self.userEntry = 0
        self.passEntry = 0
        # Frames
        self.logarFrame = 0
        # Outros
        self.aviso = 0
        self.botaoEntrar = 0
        self.fontStyle = 0

    # Método de gerenciamento da tela de login
    def entrarTela(self):
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        self.formataTelaLogin()
        
        # Cria o botão entrar e chama o método para fazer o login
        self.botaoEntrar = Button(self.loginJanela, command=self.logarMetodo, image=self.camLoginButton, bd=0, relief=GROOVE)
        self.botaoEntrar.place(relx=0.9, rely=0.9, anchor="n")
        
        # Cria um botão Voltar para voltar para a tela de início
        self.botaoVoltar = Button(self.loginJanela, command=self.destroiTela, image=self.camVoltarButton, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.loginJanela.mainloop()

    # Verifica se os dados digitados pelo usuário batem com o que está cadastrado no BD
    def logarMetodo(self):
        # Apaga qualquer aviso anterior
        self.aviso.destroy()
        self.aviso.forget()

        if self.userEntry.get() == '' or self.passEntry.get() == '':
        # Avisa que faltam dados para fazer o login
            self.aviso = Label(self.loginJanela, text="Digite um nome de usuário e/ou senha!", foreground='red', font=self.fontStyle)
        
        elif self.dadosFunc.leDados(self.userEntry.get(), self.passEntry.get()):
        # Avisa sobre o sucesso no login
            self.aviso = Label(self.loginJanela, text="Usuario Logado! Você já pode usar o sistema!", foreground='green', font=self.fontStyle)
            self.botaoEntrar.destroy()
            self.botaoEntrar.forget()
            
            # Cria um botão Voltar para voltar para a tela de início
            self.botaoAbrir = Button(self.loginJanela, command=lambda:[self.destroiTela(),self.destroiTelaInicial(),self.chamMenu.menuRecepcao()], image=self.camAbrirButton, bd=0, relief=GROOVE)
            self.botaoAbrir.place(relx=0.9, rely=0.9, anchor="n")
                       
        else:
            # Avisa ao usuário que ele errou a senha ou nome
            self.aviso = Label(self.loginJanela, text="Usuário e/ou senha inválidos!\nRealize o cadastro antes do login!", foreground='red', font=self.fontStyle)
            
        # Posiciona a label de aviso
        self.aviso.place(relx=0.5, rely=0.6, anchor="n")

    # Método de Formatação da tela Login
    def formataTelaLogin(self):
        # Cria uma janela e define suas principais configurações
        self.loginJanela = Toplevel()
        self.loginJanela.title("Início - Login de Funcionário")
        self.loginJanela.wm_iconbitmap(camIco)
        self.loginJanela.focus_force()
        self.loginJanela.geometry(tam)

        #---------------------------------------------------Frame - Login de Funcionário------------------------------------------------------#
        # Cria um frame para a entrada de dados de login
        self.loginFrame = LabelFrame(self.loginJanela, text = "Insira os dados de Login", padx=25, pady=25)
        self.loginFrame.place(relx=0.5, rely=0.2, anchor="n")
        
        # Labels, entradas de texto e botões
        lb1 = Label(self.loginFrame, text="Login: ", width=5, font=self.fontStyle)
        lb2 = Label(self.loginFrame, text="Senha: ", width=5, font=self.fontStyle)
        self.aviso = Label(self.loginFrame, font=self.fontStyle)
        self.userEntry = Entry(self.loginFrame, width=15, font=self.fontStyle)
        self.passEntry = Entry(self.loginFrame, width=15, show='*', font=self.fontStyle)

        # Posicionamento dos elementos
        lb1.grid(row=0, column=0, pady=10, sticky=W)
        lb2.grid(row=1, column=0, pady=10, sticky=W)
        self.userEntry.grid(row=0, column=1, pady=5, sticky=W)
        self.passEntry.grid(row=1, column=1, pady=5, sticky=W)

        # Converte o png do botão para imagem
        self.camLoginButton = PhotoImage(file="Images\Botões\inicio_login.png", master=self.loginJanela)
        self.camAbrirButton = PhotoImage(file="Images\Botões\inicio_abrir.png", master=self.loginJanela)
        self.camVoltarButton = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.loginJanela)
        
    def destroiTelaInicial(self):
        self.telaiInicial.destroy()
        
    # Destroi a janela atual
    def destroiTela(self):
        self.loginJanela.destroy()
    

"""
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.tela_inicial.mainloop()

x3 = loginWindow()
x3.entrarTela()
"""
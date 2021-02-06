from tkinter import *
from tkinter import ttk
from BancosdeDados.BD_CadastroFunc import *

#Variaveis Globais
tam = "800x600"
camIco = "Icones\Pousadaria.ico"


class loginWindow():
  # Construtor para a classe
  def __init__(self):
    # Janela
    self.loginJanela = 0
    # Auxiliares das conversões de imagem
    self.camLoginButton = 0
    self.camAbrirButton = 0
    # Entradas de dados
    self.userEntry = 0
    self.passEntry = 0
    # Frames
    self.logarFrame = 0
    # Outros
    self.aviso = 0
    self.botaoEntrar = 0

  # Método de gerenciamento da tela de login
  def entrarTela(self):
    self.formataTelaLogin()
    print("AAAAAAA")
    
    # Cria o botão entrar e chama o método para fazer o login
    self.botaoEntrar = Button(self.loginJanela, command=self.logarMetodo, image=self.camLoginButton, bd=0, relief=GROOVE)
    self.botaoEntrar.place(relx=0.5, rely=0.7, anchor="n")

    # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
    self.loginJanela.mainloop()

  # Verifica se os dados digitados pelo usuário batem com o que está cadastrado no BD
  def logarMetodo(self):
    print("BBBBBB")
    # Apaga qualquer aviso anterior
    self.aviso.destroy()
    self.aviso.forget()

    if self.userEntry.get() == '' or self.passEntry.get() == '':
      # Avisa que faltam dados para fazer o login
      self.aviso = Label(self.loginJanela, text="Digite um nome de usuário e/ou senha!", foreground='red')
      
    elif leDados(self.userEntry.get(), self.passEntry.get()):
      # Avisa sobre o sucesso no login
      self.aviso = Label(self.loginJanela, text="Usuario Logado! Você já pode usar o chat!", foreground='green')

      # Abre a janela da gerencia ou recepcao
      # pesquisa no banco de dados se é gerencia ou recepcao
      # if else
      '''
      self.loginJanela.destroy()
      auxiliar = recepcaoTela()
      ou
      auxiliar = gerenciaTela()
      '''
      #if()
      
      # Muda o botão entrar para "Abrir chat"
      #self.botaoEntrar.destroy()
      #self.botaoEntrar.forget()
      #self.botaoEntrar = Button(self.loginJanela, command=self.criaChat, image=self.camAbrirButton, bd=0, relief=GROOVE)
      #self.botaoEntrar.place(relx=0.5, rely=0.6, anchor="n")
      
    else:
      # Avisa ao usuário que ele errou a senha ou nome
      self.aviso = Label(self.loginJanela, text="Usuário e/ou senha inválidos!", foreground='red')
    
    # Posiciona a label de aviso
    self.aviso.place(relx=0.5, rely=0.6, anchor="n")


  def formataTelaLogin(self):
    # Cria uma janela e define suas principais configurações
    self.loginJanela = Tk()
    self.loginJanela.title("Entre com os seus dados de Login!")
    self.loginJanela.wm_iconbitmap(camIco)
    self.loginJanela.focus_force()
    self.loginJanela.geometry(tam)

    #---------------------------------------------------Frame - Login de Funcionário------------------------------------------------------#
    # Cria um frame para a entrada de dados de login
    self.loginFrame = LabelFrame(self.loginJanela, text = "Insira os dados de Login", padx=25, pady=25)
    self.loginFrame.place(relx=0.5, rely=0.2, anchor="n")
    
    # Labels, entradas de texto e botões
    lb1 = Label(self.loginFrame, text="Login: ", width=5)
    lb2 = Label(self.loginFrame, text="Senha: ", width=5)
    self.aviso = Label(self.loginFrame)
    self.userEntry = Entry(self.loginFrame, width=15)
    self.passEntry = Entry(self.loginFrame, width=15, show='*')

    # Posicionamento dos elementos
    lb1.grid(row=0, column=0, pady=5, sticky=W)
    lb2.grid(row=1, column=0, pady=5, sticky=W)
    self.userEntry.grid(row=0, column=1, pady=5, sticky=W)
    self.passEntry.grid(row=1, column=1, pady=5, sticky=W)

    # Converte o png do botão para imagem
    self.camLoginButton = PhotoImage(file="Botões\Tela inicial//button_loginTI.png", master=self.loginJanela)
    self.camAbrirButton = PhotoImage(file="Botões\Tela inicial//button_abrirTI.png", master=self.loginJanela)
'''
  # Destroi a Tela de Login e cria a tela de chat
  def criaChat(self):
      self.loginJanela.destroy()
      auxiliar = chatWindow(self.nome)
      auxiliar.chatTela()
'''
x3 = loginWindow()
x3.entrarTela()
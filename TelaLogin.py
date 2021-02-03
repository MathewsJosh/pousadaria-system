from tkinter import *
#from BD_usuariosCadastrados import *
#from Tela_Cadastrar import *
#from Tela_Chat import *

#Variaveis Globais
tam = "800x600"
camIco = "Icones\Pousadaria.ico"

class loginWindow():
  # Construtor para a classe
  def __init__(self):
    self.loginJanela = 0
    self.userEntry = 0
    self.passEntry = 0
    self.aviso = 0
    self.botaoEntrar = 0
    self.nome = ""
    self.camLoginButton = 0
    self.camAbrirButton = 0

  # Método de gerenciamento da tela de login
  def entrarTela(self):

    # Apaga a janela anterior
    #ApagaInicial()

    # Cria uma janela e define suas principais configurações
    self.loginJanela = Tk()
    self.loginJanela.title("Entre com os seus dados de Login!")
    self.loginJanela.wm_iconbitmap(camIco)
    self.loginJanela.focus_force()
    self.loginJanela.geometry(tam)

    # Labels, entradas de texto e botões
    lb1 = Label(self.loginJanela, text="Login: ", width=5)
    lb2 = Label(self.loginJanela, text="Senha: ", width=5)
    self.aviso = Label(self.loginJanela)
    self.userEntry = Entry(self.loginJanela, width=15)
    self.passEntry = Entry(self.loginJanela, width=15, show='*')

    # Posicionamento dos elementos
    lb1.place(relx=0.35, rely=0.13, anchor="n")
    lb2.place(relx=0.35, rely=0.25, anchor="n")
    self.userEntry.place(relx=0.55, rely=0.13, anchor="n")
    self.passEntry.place(relx=0.55, rely=0.25, anchor="n")

    # Converte o png do botão para imagem
    self.camLoginButton = PhotoImage(file="Botões\Tela inicial//button_loginTI.png", master=self.loginJanela)
    #self.camAbrirButton = PhotoImage(file="Icones\Botoes\Abrir.png", master=self.loginJanela)
    
    # Cria o boão entrar e chama o método para fazer o login
    #, text="Entrar"
    self.botaoEntrar = Button(self.loginJanela, command=self.logarMetodo, image=self.camLoginButton, bd=0, relief=GROOVE)
    self.botaoEntrar.place(relx=0.5, rely=0.6, anchor="n")

  # Verifica se os dados digitados pelo usuário batem com o que está cadastrado no BD
  def logarMetodo(self):
    # Apaga qualquer aviso anterior
    self.aviso.destroy()
    self.aviso.forget()

    if self.userEntry.get() == '' or self.passEntry.get() == '':
      # Avisa que faltam dados para fazer o login
      self.aviso = Label(self.loginJanela, text="Digite um nome de usuário e/ou senha!", foreground='red')
      
    elif leDados(self.userEntry.get(), self.passEntry.get()):
      self.nome = self.userEntry.get()
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

      '''
      # Muda o botão entrar para "Abrir chat"
      self.botaoEntrar.destroy()
      self.botaoEntrar.forget()
      self.botaoEntrar = Button(self.loginJanela, command=self.criaChat, image=self.camAbrirButton, bd=0, relief=GROOVE)
      self.botaoEntrar.place(relx=0.5, rely=0.6, anchor="n")
      '''
    else:
      # Avisa ao usuário que ele errou a senha ou nome
      self.aviso = Label(self.loginJanela, text="Usuário e/ou senha inválidos!", foreground='red')
    
    # Posiciona a label de aviso
    self.aviso.place(relx=0.5, rely=0.4, anchor="n") 

'''
  # Destroi a Tela de Login e cria a tela de chat
  def criaChat(self):
      self.loginJanela.destroy()
      auxiliar = chatWindow(self.nome)
      auxiliar.chatTela()
'''
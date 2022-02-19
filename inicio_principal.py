from tkinter import *
from inicio_login import *
from inicio_cadfuncionario import *
from BD_pousadaria import *

#####################TELA PRINCIPAL DA APLICAÇÃO######################
#Execute esse arquivo

# Bibliotecas a serem importadas nesse projeto:
#pip install tkcalendar
#pip install tk


#Variaveis Globais
tam = "800x600"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class telaInicialWindow():
    def __init__(self):
        self.tela_inicial = 0
        self.camLoginButton = 0
        self.camCadastrarButton = 0
        self.pousadaria = 0

    def telaInicial(self):
        # Cria uma janela e define suas principais configurações
        self.tela_inicial = Tk()
        self.tela_inicial.title("Tela inicial - Logue ou cadastre-se no sistema")
        self.tela_inicial.wm_iconbitmap(camIco)
        self.tela_inicial.focus_force()
        self.tela_inicial.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camLoginButton = PhotoImage(file="Images\Botões\inicio_login.png", master=self.tela_inicial)
        self.pousadaria = PhotoImage(file="Images\Pousadaria-Logo.png", master=self.tela_inicial)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.pousadaria)
        l1.place(relx=0.5, rely=0.1, anchor="n")

        #Instanciamento de classes
        self.LoginTela = loginWindow(self.tela_inicial)
        self.CadastrarTela = cadastrarWindow()
        
        # Cria botões para Logar e Cadastrar
        botaoLogar = Button(command=lambda:[self.LoginTela.entrarTela()], image=self.camLoginButton, bd=0, relief=GROOVE)

        # Posicionamento dos botões
        botaoLogar.place(relx=0.5, rely=0.9, anchor="s")

        #self.camCadastrarButton = PhotoImage(file="Images\Botões\inicio_cadastrar.png", master=self.tela_inicial)
        #botaoCadastrar = Button(command=lambda:[self.CadastrarTela.cadastrarTela()], image=self.camCadastrarButton, bd=0, relief=GROOVE)
        #botaoCadastrar.place(relx=0.7, rely=0.9, anchor="s")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.tela_inicial.mainloop()

    def ApagaInicial(self):
        self.tela_inicial.destroy()
        
instancia_tabelas()
x1 = telaInicialWindow()
x1.telaInicial()

'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.tela_inicial.mainloop()

e coloque o seguinte comando adaptado para poder executa-la
#x1 = telaInicialWindow()
#x1.telaInicial()
''' 
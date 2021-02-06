from tkinter import *
from TelaLogin import *
from TelaCadastrarFunc import *

#####################TELA PRINCIPAL DA APLICAÇÃO######################
#Execute esse arquivo


#Variaveis Globais
tam = "800x600"
camIco = "Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class telaInicialWindow():
    def __init__(self):
        self.tela_inicial = 0
        self.camLoginButton = 0
        self.camCadastrarButton = 0
        self.pousadaria = 0
        self.bFrame = 0

    def telaInicial(self):
        # Cria uma janela e define suas principais configurações
        self.tela_inicial = Tk()
        self.tela_inicial.title("Tela inicial - Logue ou cadastre-se no sistema")
        self.tela_inicial.wm_iconbitmap(camIco)
        self.tela_inicial.focus_force()
        self.tela_inicial.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camLoginButton = PhotoImage(file="Botões\Tela inicial//button_loginTI.png", master=self.tela_inicial)
        self.camCadastrarButton = PhotoImage(file="Botões\Tela inicial//button_cadastrarTI.png", master=self.tela_inicial)
        self.pousadaria = PhotoImage(file="Icones\Pousadaria-Logo.png", master=self.tela_inicial)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.pousadaria)
        l1.place(relx=0.5, rely=0.25, anchor="n")

        # Cria instancias e botões para Logar e Cadastrar
        ltela = loginWindow()
        ctela = cadastrarWindow()
        #command=ltela.entrarTela, 
        botaoLogar = Button(command=lambda:[self.ApagaInicial(),ltela.entrarTela()], image=self.camLoginButton, bd=0, relief=GROOVE)
        #command=ctela.cadastrarTela,
        botaoCadastrar = Button(command=ctela.cadastrarTela, image=self.camCadastrarButton, bd=0, relief=GROOVE)

        # Posicionamento dos botões
        botaoLogar.place(relx=0.3, rely=0.7, anchor="s")
        botaoCadastrar.place(relx=0.7, rely=0.7, anchor="s")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.tela_inicial.mainloop()

    def ApagaInicial(self):
        print("Apagou tela inicial")
        self.tela_inicial.destroy()
        

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
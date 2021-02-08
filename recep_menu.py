from tkinter import *

#Variaveis Globais
tam = "1200x720"
camIco = "Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class MenuRecepcaoWindow():
    # Inicializadores
    def __init__(self):
        # Janela
        self.menuRecepcaoJanela = 0
        # Auxiliares das conversões de imagem
        self.camCadastrar = 0
        self.camConsultarQuarto = 0
        self.camReservarQuarto = 0
        self.camDevolverQuarto = 0
        self.camReclamacao = 0
        self.pousadaria = 0
        # Botões
        self.botaoCadastrar = 0
        self.botaoConsultar = 0
        self.botaoReservar = 0
        self.botaoDevolver = 0
        self.botaoReclamar = 0
        # Outros
        self.bFrame = 0

    def menuRecepcao(self):
        # Cria uma janela e define suas principais configurações
        self.menuRecepcaoJanela = Tk()
        self.menuRecepcaoJanela.title("Recepção - Escolha uma Opção")
        self.menuRecepcaoJanela.wm_iconbitmap(camIco)
        self.menuRecepcaoJanela.focus_force()
        self.menuRecepcaoJanela.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camCadastrar = PhotoImage(file="Botões\Recepção\Menu//button_cadastrarMenu.png", master=self.menuRecepcaoJanela)
        self.camConsultarQuarto = PhotoImage(file="Botões\Recepção\Menu//button_consultarMenu.png", master=self.menuRecepcaoJanela)
        self.camReservarQuarto = PhotoImage(file="Botões\Recepção\Menu//button_reservarMenu.png", master=self.menuRecepcaoJanela)
        self.camDevolverQuarto = PhotoImage(file="Botões\Recepção\Menu//button_devolucaoMenu.png", master=self.menuRecepcaoJanela)
        self.camReclamacao = PhotoImage(file="Botões\Recepção\Menu//button_reclamacaoMenu.png", master=self.menuRecepcaoJanela)
        self.pousadaria = PhotoImage(file="Icones\Pousadaria-Logo.png", master=self.menuRecepcaoJanela)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.pousadaria)
        l1.place(relx=0.5, rely=0.10, anchor="n")

        # Cria um frame só para os botões do menu
        self.bFrame = LabelFrame(self.menuRecepcaoJanela, text = "Recepção", padx=50)
        self.bFrame.place(relx=0.5, rely=0.3, anchor="n")

        # Cria os Botões e os posiciona
        self.botaoConsultar = Button(self.bFrame, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        self.botaoCadastrar = Button(self.bFrame, image=self.camCadastrar, bd=0, relief=GROOVE)
        self.botaoReservar = Button(self.bFrame, image=self.camReservarQuarto, bd=0, relief=GROOVE)
        self.botaoDevolver = Button(self.bFrame, image=self.camDevolverQuarto, bd=0, relief=GROOVE)
        self.botaoReclamar = Button(self.bFrame, image=self.camReclamacao, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=0, column=1, pady=50)
        self.botaoCadastrar.grid(row=0, column=3, pady=50)
        self.botaoReservar.grid(row=1, column=1, pady=50)
        self.botaoDevolver.grid(row=1, column=3, pady=50)
        self.botaoReclamar.grid(row=4, column=2, pady=50)


        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.menuRecepcaoJanela.mainloop()

    def ApagaInicial(self):
        print("Apagou tela inicial")
        self.menuRecepcaoJanela.destroy()
        

x4 = MenuRecepcaoWindow()
x4.menuRecepcao()

'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.menuRecepcaoJanela.mainloop()

e coloque o seguinte comando adaptado para poder executa-la
#x1 = telaInicialWindow()
#x1.telaInicial()
''' 
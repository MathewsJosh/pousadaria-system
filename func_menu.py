from tkinter import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria2.ico"

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
        self.camEstoque = 0
        self.camCardapio = 0
        self.camTarefas = 0
        self.campousadaria = 0
        # Botões
        self.botaoCadastrar = 0
        self.botaoConsultar = 0
        self.botaoReservar = 0
        self.botaoDevolver = 0
        self.botaoReclamar = 0
        self.botaoEstoque = 0
        self.botaoCardapio = 0
        self.botaoTarefas = 0
        # Frames
        self.recepframe = 0
        self.outrosframe = 0

    def menuRecepcao(self):
        # Cria uma janela e define suas principais configurações
        self.menuRecepcaoJanela = Tk()
        self.menuRecepcaoJanela.title("Recepção - Escolha uma Opção")
        self.menuRecepcaoJanela.wm_iconbitmap(camIco)
        self.menuRecepcaoJanela.focus_force()
        self.menuRecepcaoJanela.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camCadastrar = PhotoImage(file="Images\Botões\menu_cadCliente.png", master=self.menuRecepcaoJanela)
        self.camConsultarQuarto = PhotoImage(file="Images\Botões\menu_consultar.png", master=self.menuRecepcaoJanela)
        self.camReservarQuarto = PhotoImage(file="Images\Botões\menu_reservar.png", master=self.menuRecepcaoJanela)
        self.camDevolverQuarto = PhotoImage(file="Images\Botões\menu_devolver.png", master=self.menuRecepcaoJanela)
        self.camReclamacao = PhotoImage(file="Images\Botões\menu_reclamacoes.png", master=self.menuRecepcaoJanela)
        self.camEstoque = PhotoImage(file="Images\Botões\menu_estoque.png", master=self.menuRecepcaoJanela)
        self.camCardapio = PhotoImage(file="Images\Botões\menu_cardapio.png", master=self.menuRecepcaoJanela)
        self.camTarefas =  PhotoImage(file="Images\Botões\menu_tarefas.png", master=self.menuRecepcaoJanela)
        self.campousadaria = PhotoImage(file="Images\Pousadaria-Logo2.png", master=self.menuRecepcaoJanela)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.campousadaria)
        l1.place(relx=0.5, rely=0.03, anchor="n")
        
        #---------------------------------------------------Frame - Botões Recepção------------------------------------------------------#
        # Cria um frame só para os botões do menu
        self.recepframe = LabelFrame(self.menuRecepcaoJanela, text = "Recepção", padx=50)
        self.recepframe.place(relx=0.3, rely=0.3, anchor="n")

        # Cria os Botões e os posiciona
        self.botaoCadastrar = Button(self.recepframe, image=self.camCadastrar, bd=0, relief=GROOVE)
        self.botaoConsultar = Button(self.recepframe, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        self.botaoReservar = Button(self.recepframe, image=self.camReservarQuarto, bd=0, relief=GROOVE)
        self.botaoDevolver = Button(self.recepframe, image=self.camDevolverQuarto, bd=0, relief=GROOVE)
        self.botaoReclamar = Button(self.recepframe, image=self.camReclamacao, bd=0, relief=GROOVE)
        self.botaoCadastrar.grid(row=1, column=0, pady=20)
        self.botaoConsultar.grid(row=2, column=0, pady=20)
        self.botaoReservar.grid(row=3, column=0, pady=20)
        self.botaoDevolver.grid(row=4, column=0, pady=20)
        self.botaoReclamar.grid(row=5, column=0, pady=20)
        
        #---------------------------------------------------Frame - Outros Botões------------------------------------------------------#
        # Cria um frame só para os botões do menu
        self.outrosframe = LabelFrame(self.menuRecepcaoJanela, text = "Administração", padx=50)
        self.outrosframe.place(relx=0.7, rely=0.4, anchor="n")
        
        # Cria os botões em outra frame e os posiciona
        self.botaoCardapio = Button(self.outrosframe, image=self.camCardapio, bd=0, relief=GROOVE)
        self.botaoEstoque = Button(self.outrosframe, image=self.camEstoque, bd=0, relief=GROOVE)
        self.botaoTarefas = Button(self.outrosframe, image=self.camTarefas, bd=0, relief=GROOVE)
        self.botaoCardapio.grid(row=0, column=0, pady=20)
        self.botaoEstoque.grid(row=1, column=0, pady=20)
        self.botaoTarefas.grid(row=2, column=0, pady=20)


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
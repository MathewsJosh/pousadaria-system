from tkinter import *

#Variaveis Globais
tam = "1200x720"
camIco = "Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class MenuGerenciaWindow():
    # Inicializadores
    def __init__(self):
        # Janela
        self.menuGerenciaJanela = 0
        # Auxiliares das conversões de imagem
        self.camCardapio = 0
        self.camDisponibilidade = 0
        self.camEstoque = 0
        self.camTarefas = 0
        self.pousadaria = 0
        # Botões
        self.botaoCardapio = 0
        self.botaoDisponibilidade = 0
        self.botaoEstoque = 0
        self.botaoTarefas = 0
        # Outros
        self.bFrame = 0

    def menuGerencia(self):
        # Cria uma janela e define suas principais configurações
        self.menuGerenciaJanela = Tk()
        self.menuGerenciaJanela.title("Gerência - Escolha uma Opção")
        self.menuGerenciaJanela.wm_iconbitmap(camIco)
        self.menuGerenciaJanela.focus_force()
        self.menuGerenciaJanela.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camCardapio = PhotoImage(file="Botões\Gerência\Menu//button_cardapioMenu.png", master=self.menuGerenciaJanela)
        self.camDisponibilidade = PhotoImage(file="Botões\Gerência\Menu//button_disponibilidadeMenu.png", master=self.menuGerenciaJanela)
        self.camEstoque = PhotoImage(file="Botões\Gerência\Menu//button_estoqueMenu.png", master=self.menuGerenciaJanela)
        self.camTarefas = PhotoImage(file="Botões\Gerência\Menu//button_tarefasMenu.png", master=self.menuGerenciaJanela)
        self.pousadaria = PhotoImage(file="Icones\Pousadaria-Logo.png", master=self.menuGerenciaJanela)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.pousadaria)
        l1.place(relx=0.5, rely=0.10, anchor="n")

        # Cria um frame só para os botões do menu
        self.bFrame = LabelFrame(self.menuGerenciaJanela, text = "Gerência", padx=50)
        self.bFrame.place(relx=0.5, rely=0.3, anchor="n")

        # Cria os Botões e os posiciona
        self.botaoCardapio = Button(self.bFrame, image=self.camCardapio, bd=0, relief=GROOVE)
        self.botaoCardapio.grid(row=0, column=1, pady=50)
        self.botaoTarefas = Button(self.bFrame, image=self.camTarefas, bd=0, relief=GROOVE)
        self.botaoTarefas.grid(row=0, column=3, pady=50)
        self.botaoDisponibilidade = Button(self.bFrame, image=self.camDisponibilidade, bd=0, relief=GROOVE)
        self.botaoDisponibilidade.grid(row=1, column=3, pady=50, padx=20)
        self.botaoEstoque = Button(self.bFrame, image=self.camEstoque, bd=0, relief=GROOVE)
        self.botaoEstoque.grid(row=1, column=1, pady=50, padx=20)
        




        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.menuGerenciaJanela.mainloop()

    def ApagaInicial(self):
        print("Apagou tela inicial")
        self.menuGerenciaJanela.destroy()
        

x5 = MenuGerenciaWindow()
x5.menuGerencia()

'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.menuGerenciaJanela.mainloop()

e coloque o seguinte comando adaptado para poder executa-la
#x1 = telaInicialWindow()
#x1.telaInicial()
''' 
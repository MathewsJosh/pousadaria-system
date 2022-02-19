from tkinter import *

# Importações de outras classes locais
from func_cadcliente import *
from func_cardapio import *
from func_consquarto import *
from func_contEstoque import *
from func_devolver import *
from func_reclamar import *
from func_reservar import *
from func_tarefas import *
from inicio_cadfuncionario import *


#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class MenuRecepcaoWindow():
    # Inicializadores
    def __init__(self, funcionarioID):
        # Janela
        self.menuJanela = 0
        # Instanciamentos de classes
        self.chamaCad = 0
        self.chamaCard = 0
        self.chamaCons = 0
        self.chamaCont = 0
        self.chamaDev = 0
        self.chamaRec = 0
        self.chamaRes = 0
        self.chamaTar = 0
        self.chamaCadFunc = 0
        # Auxiliares das conversões de imagem
        self.camCadastrarCliente = 0
        self.camConsultarQuarto = 0
        self.camReservarQuarto = 0
        self.camDevolverQuarto = 0
        self.camReclamacao = 0
        self.camEstoque = 0
        self.camCardapio = 0
        self.camTarefas = 0
        self.campousadaria = 0
        self.camCadastrarFuncionario = 0
        # Botões
        self.botaoCadastrar = 0
        self.botaoConsultar = 0
        self.botaoReservar = 0
        self.botaoDevolver = 0
        self.botaoReclamar = 0
        self.botaoEstoque = 0
        self.botaoCardapio = 0
        self.botaoTarefas = 0
        self.botaoCadastrarFuncionario = 0
        # Frames
        self.recepframe = 0
        self.outrosframe = 0
        self.funcionarioID = funcionarioID

    # Método de exibição do menu principal
    def menuRecepcao(self):
        # Cria uma janela e define suas principais configurações
        self.menuJanela = Tk()
        self.menuJanela.title("Menu Pousadaria - Escolha uma Opção")
        self.menuJanela.wm_iconbitmap(camIco)
        self.menuJanela.focus_force()
        self.menuJanela.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camCadastrarCliente = PhotoImage(file="Images\Botões\menu_cadCliente.png", master=self.menuJanela)
        self.camConsultarQuarto = PhotoImage(file="Images\Botões\menu_consultar.png", master=self.menuJanela)
        self.camReservarQuarto = PhotoImage(file="Images\Botões\menu_reservar.png", master=self.menuJanela)
        self.camDevolverQuarto = PhotoImage(file="Images\Botões\menu_devolver.png", master=self.menuJanela)
        self.camReclamacao = PhotoImage(file="Images\Botões\menu_reclamacoes.png", master=self.menuJanela)
        self.camEstoque = PhotoImage(file="Images\Botões\menu_estoque.png", master=self.menuJanela)
        self.camCardapio = PhotoImage(file="Images\Botões\menu_cardapio.png", master=self.menuJanela)
        self.camTarefas =  PhotoImage(file="Images\Botões\menu_tarefas.png", master=self.menuJanela)
        self.campousadaria = PhotoImage(file="Images\Pousadaria-Logo2.png", master=self.menuJanela)
        
        self.camCadastrarFuncionario = PhotoImage(file="Images\Botões\menu_cadastrarFunc.png")

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.campousadaria)
        l1.place(relx=0.5, rely=0.03, anchor="n")
        
        #---------------------------------------------------Frame - Botões Recepção------------------------------------------------------#
        # Cria um frame só para os botões do menu
        self.recepframe = LabelFrame(self.menuJanela, text = "Recepção", padx=50)
        self.recepframe.place(relx=0.3, rely=0.3, anchor="n")

        self.chamaCad = cadastrarWindow(self.funcionarioID)
        self.chamaCons = consultaQuartoWindow(self.funcionarioID)
        self.chamaDev = DevolverWindow(self.funcionarioID)
        self.chamaRec = Reclamacao(self.funcionarioID)
        self.chamaRes = ReservarWindow(self.funcionarioID)
        self.chamaCard = Cardapio(self.funcionarioID)
        self.chamaCont = ContEstoque(self.funcionarioID)
        self.chamaTar = Tarefas(self.funcionarioID)
        self.chamaCadFunc = cadastrarWindowFunc()

        # Cria os Botões e os posiciona
        self.botaoCadastrarCliente = Button(self.recepframe, command=self.chamaCad.cadastrarTela, image=self.camCadastrarCliente, bd=0, relief=GROOVE)
        self.botaoCadastrarCliente.grid(row=1, column=0, pady=20)
        self.botaoConsultar = Button(self.recepframe, command=self.chamaCons.consultaQuarto, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=2, column=0, pady=20)
        self.botaoReservar = Button(self.recepframe, command=self.chamaRes.ReservarTela, image=self.camReservarQuarto, bd=0, relief=GROOVE)
        self.botaoReservar.grid(row=3, column=0, pady=20)
        self.botaoDevolver = Button(self.recepframe, command=self.chamaDev.DevolverTela, image=self.camDevolverQuarto, bd=0, relief=GROOVE)
        self.botaoDevolver.grid(row=4, column=0, pady=20)
        self.botaoReclamar = Button(self.recepframe, command=self.chamaRec.selecionaCRUDReclamacao, image=self.camReclamacao, bd=0, relief=GROOVE)
        self.botaoReclamar.grid(row=5, column=0, pady=20)
        
        
        #---------------------------------------------------Frame - Outros Botões------------------------------------------------------#
        # Cria um frame só para os botões do menu
        self.outrosframe = LabelFrame(self.menuJanela, text = "Administração - Selecione uma opção", padx=50)
        self.outrosframe.place(relx=0.7, rely=0.4, anchor="n")
        
        # Cria os botões em outra frame e os posiciona
        self.botaoCardapio = Button(self.outrosframe, command=self.chamaCard.selecionaCRUDCardapio, image=self.camCardapio, bd=0, relief=GROOVE)
        self.botaoEstoque = Button(self.outrosframe, command=self.chamaCont.selecionaCRUDEstoque, image=self.camEstoque, bd=0, relief=GROOVE)
        self.botaoTarefas = Button(self.outrosframe, command=self.chamaTar.selecionaCRUDTarefas, image=self.camTarefas, bd=0, relief=GROOVE)
        self.botaoCadastrarFuncionario = Button(self.outrosframe, command=lambda:[self.chamaCadFunc.cadastrarTela()], image=self.camCadastrarFuncionario, bd=0, relief=GROOVE)
        self.botaoCardapio.grid(row=0, column=0, pady=20)
        self.botaoEstoque.grid(row=1, column=0, pady=20)
        self.botaoTarefas.grid(row=2, column=0, pady=20)
        self.botaoCadastrarFuncionario.grid(row=3, column= 0, pady=20)

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.menuJanela.mainloop()
    
    def esconderTela(self):
        self.menuJanela.withdraw()
    
    def mostrarTela(self):
        self.menuJanela.deiconify() 
    
    def ApagaMenu(self):
        self.menuJanela.destroy()
        
'''
#OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()

instancia_tabelas()
x4 = MenuRecepcaoWindow(1)
x4.menuRecepcao()
'''


from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont

# Importações de outras classes locais
from BD_pousadaria import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class consultaQuartoWindow():
    # Inicializadores
    def __init__(self, funcionarioID):
        # Janela
        self.consultaQuartoJanela = 0
        # Auxiliares das conversões de imagem
        self.camConsultarQuarto = 0
        self.camVoltar = 0
        # Botões
        self.botaoConsultarQuarto = 0
        self.botaoVoltar = 0
        # Frames
        self.filtroframe = 0
        self.quartosdisp = 0
        self.areasdisp = 0
        # Outros
        self.Date2Entry = 0
        self.Date1Entry = 0
        self.aviso = 0
        self.textboxQuarto = 0
        self.textboxLazer = 0
        self.filtrobox = 0
        # Dados importados do BD
        self.dadosQuarto = 0
        #self.dadosLazer = 0
        self.dadosReservas = 0
        self.dadosDevolucoes = 0


    # Método inicial e gerenciador da tela de consulta
    def consultaQuarto(self):
        # Função que inicia e recupera dados dos BDs
        self.iniciaBDs()
        
        # Função que formata a tela
        self.formataTelaConsultaQuarto()
        
        # Cria os Botões e os posiciona
        botaoConsultarQuarto = Button(self.consultaQuartoJanela,command=self.consultaExibe, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        botaoConsultarQuarto.place(relx=0.9, rely=0.9, anchor="n")
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.consultaQuartoJanela.mainloop()


    # Método que consulta os bancos de dados e exibe na tela suas informações
    def consultaExibe(self):
        self.iniciaBDs()
        self.aviso = Label(self.consultaQuartoJanela, foreground='red')
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        self.aviso.destroy()
        self.aviso.forget()
        self.textboxQuarto.delete(1.0, END)
        self.textboxLazer.delete(1.0, END)

        # Consulta os Status do quartos e os imprime
        if self.filtrobox.get() == "Disponível":
            for comodo in self.dadosQuarto:
                if comodo[3] != 'Área de Lazer' and comodo[3] != None:
                    self.textboxQuarto.insert(INSERT, "====>IDQuarto: " + str(comodo[0]) + "<====\nNome: " + str(comodo[1]) + "\nPreço: " + str(comodo[2]) + "\nTipo: " + str(comodo[3]) + "\nQTD Camas: " + str(comodo[4]) + "\nQTD Cômodos: " + str(comodo[5]) + "\n\n")
                    self.textboxQuarto.insert(INSERT, "\n\n")
                else:
                    self.textboxLazer.insert(INSERT, "====>IDArea: " + str(comodo[0]) + " - " + str(comodo[1]) + "<====\nTipo: " + str(comodo[3])+ "\nDiária: " + str(comodo[2]) + "\n\n")
        else:
            for comodo in self.dadosComodoOcupado:
                    if comodo[3] != 'Área de Lazer' and comodo[3] != None:
                        self.textboxQuarto.insert(INSERT, "====>IDQuarto: " + str(comodo[0]) + "<====\nNome: " + str(comodo[1]) + "\nPreço: " + str(comodo[2]) + "\nTipo: " + str(comodo[3]) + "\nQTD Camas: " + str(comodo[4]) + "\nQTD Cômodos: " + str(comodo[5]) + "\n\n")
                        self.textboxQuarto.insert(INSERT, "\n\n")
                    else:
                        self.textboxLazer.insert(INSERT, "====>IDArea: " + str(comodo[0]) + " - " + str(comodo[1]) + "<====\nTipo: " + str(comodo[3])+ "\nDiária: " + str(comodo[2]) + "\n\n")

                            
    # Método para instanciar os bancos de dados e receber seus dados
    def iniciaBDs(self):
        self.dadosQuarto = BD_Comodo().consultaComodosDisponiveis()
        self.dadosComodoOcupado = BD_Comodo().consultaComodosOcupados()
        
    # Método para formatar a tela principal de consulta    
    def formataTelaConsultaQuarto(self):
        # Cria uma janela e define suas principais configurações
        self.consultaQuartoJanela = Toplevel()
        self.consultaQuartoJanela.title("Recepção - Consulta de Quartos")
        self.consultaQuartoJanela.wm_iconbitmap(camIco)
        self.consultaQuartoJanela.focus_force()
        self.consultaQuartoJanela.geometry(tam)
        self.consultaQuartoJanela.withdraw()
        self.consultaQuartoJanela.deiconify()

        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        # Converte os pngs dos botões para imagem
        self.camConsultarQuarto = tkinter.PhotoImage(file="Images\Botões\inicio_consultar.png")
        self.camVoltar = tkinter.PhotoImage(file="Images\Botões\inicio_voltar.png")

        # Cria o botão voltar e o posiciona
        botaoVoltar = Button(self.consultaQuartoJanela,image=self.camVoltar, command=self.ApagaTelaConsulta, bd=0, relief=GROOVE)
        botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")

        #---------------------------------------------------Frame - Entrada de datas e Filtro de quartos------------------------------------------------------#
        # Cria um frame para a entrada de datas
        self.filtroframe = LabelFrame(self.consultaQuartoJanela, text = "Filtro de disponibilidade", padx=10)
        self.filtroframe.place(relx=0.5, rely=0.05, anchor="n")
        
        # Cria e posiciona a combobox que irá permitir filtrar os quartos
        lb2 = Label(self.filtroframe, text="Status: ", width=8)
        lb2.grid(row=1, column=0, pady=10)
        opcoesStatus = ["Disponível", "Ocupado"]
        self.filtrobox = ttk.Combobox(self.filtroframe, value=opcoesStatus, width=15, state="readonly")
        self.filtrobox.current(0)
        self.filtrobox.grid(row=1, column=1, pady=5, sticky=E)
        
        #---------------------------------------------------Frame - Quartos disponíveis------------------------------------------------------#
        # Cria um frame exibir os quartos disponiveis
        self.quartosdisp = LabelFrame(self.consultaQuartoJanela, text = "Quartos", padx=10, pady=10)
        self.quartosdisp.place(relx=0.26, rely=0.23, anchor="n")
        
        # Cria um textbox com os detalhes do quarto
        self.textboxQuarto = scrolledtext.ScrolledText(self.quartosdisp, height=20, width=50, font=fontStyle)
        self.textboxQuarto.grid(row=0, column=1, padx=10, pady=10)
        
        # Função necessária para não permitir que o textbox seja editado
        self.textboxQuarto.bind("<Key>", lambda e: "break")
        
        #---------------------------------------------------Frame - Area de lazer------------------------------------------------------#
        # Cria um frame exibir as Areas de Lazer Disponíveis
        self.areasdisp = LabelFrame(self.consultaQuartoJanela, text = "Áreas de lazer", padx=10, pady=10)
        self.areasdisp.place(relx=0.74, rely=0.23, anchor="n")

        # Cria um textbox com os detalhes do quarto
        self.textboxLazer = scrolledtext.ScrolledText(self.areasdisp, height=20, width=50, font=fontStyle)
        self.textboxLazer.grid(row=0, column=1, padx=10, pady=10)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxLazer.bind("<Key>", lambda e: "break")
        

    # Método que apaga a janela atual
    def ApagaTelaConsulta(self):
        self.consultaQuartoJanela.destroy()

'''
#OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()

instancia_tabelas()
x6 = consultaQuartoWindow()
x6.consultaQuarto()
'''
from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from PIL import ImageTk
from PIL import Image as PilImage


# Importações de outras classes locais
from BD_quartosdisp import *
from BD_lazerdisp import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class consultaQuartoWindow():
    # Inicializadores
    def __init__(self):
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
        self.dadosLazer = 0


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
        self.aviso = Label(self.consultaQuartoJanela, foreground='red')
        self.aviso.place(relx=0.5, rely=0.9, anchor="n")
        self.aviso.destroy()
        self.aviso.forget()
        self.textboxQuarto.delete(1.0, END)
        self.textboxLazer.delete(1.0, END)
        
        contador=len(self.dadosQuarto)
        # Consulta os Status do quartos e os imprime 
        for x in self.dadosQuarto:
        
            if x[1] == self.filtrobox.get() and self.filtrobox.get() == "Disponível":
                self.textboxQuarto.insert(INSERT, "====>IDQuarto: " + x[0] + "<====\nStatus: " + x[1] + "\nTipo: " + x[2] + "\nCamas: " + x[3] + "\nCômodos: " + x[4] + "\nDiária: ")
                self.textboxQuarto.insert(INSERT, x[5])
                self.textboxQuarto.insert(INSERT, "\n\n")
                contador-=1
              
            elif x[1] == self.filtrobox.get() and self.filtrobox.get() == "Ocupado":
                self.textboxQuarto.insert(INSERT, "====>IDQuarto: " + x[0] + "<====\nStatus: " + x[1] + "\nTipo: " + x[2] + "\nCamas: " + x[3] + "\nCômodos: " + x[4] + "\nDiária: ")
                self.textboxQuarto.insert(INSERT, x[5])
                self.textboxQuarto.insert(INSERT, "\nTempo de Locação: " + str(x[6]) + "\nData de Entrada: " + str(x[7]) + "\nData de Saída: " + str(x[8]) + "\nLocador: " + str(x[9]) + "\n\n")
                contador-=1
                
            elif x[1] == self.filtrobox.get() and self.filtrobox.get() == "Manutenção":    
                self.textboxQuarto.insert(INSERT, "====>IDQuarto: " + x[0] + "<====\nStatus: " + x[1] + "\nTipo: " + x[2])
                contador-=1
                
            else:
                self.textboxQuarto.insert(INSERT, "")
                     
        if contador == len(self.dadosQuarto):
                self.textboxQuarto.insert(INSERT, "Nenhum quarto disponível para o filtro selecionado!")
                
               
        contador2=len(self.dadosLazer)
        # Consulta os Status do quartos e os imprime 
        for x in self.dadosLazer:
        
            if x[1] == self.filtrobox.get() and self.filtrobox.get() == "Disponível":
                self.textboxLazer.insert(INSERT, "====>IDArea: " + x[0] + " - " + x[2] + "<====\nStatus: " + x[1]+ "\nDiária: " + str(x[3]) + "\n\n")
                #self.textboxLazer.insert(INSERT, "\nTempo de Reserva: " + str(x[4]) + "\nData de Entrada: " + str(x[5]) + "\nData de Saída: " + str(x[6]) + "\n\n")
                contador2-=1
              
            elif x[1] == self.filtrobox.get() and self.filtrobox.get() == "Ocupado":
                self.textboxLazer.insert(INSERT, "====>IDArea: " + x[0] + " - " + x[2] + "<====\nStatus: " + x[1]+ "\nDiária: " + str(x[3]) + "\nTempo de Reserva: " + str(x[4]))
                self.textboxLazer.insert(INSERT, "\nData de Entrada: " + str(x[5]) + "\nData de Saída: " + str(x[6]) + "\nLocador: " + str(x[7]) + "\n\n")
                contador2-=1
                
            elif x[1] == self.filtrobox.get() and self.filtrobox.get() == "Manutenção":    
                self.textboxLazer.insert(INSERT, "====>IDArea: " + x[0] + "<====\nStatus: " + x[1] + "\nTipo: " + x[2])
                contador2-=1
                
            else:
                self.textboxLazer.insert(INSERT, "")
                     
        if contador2 == len(self.dadosLazer):
                self.textboxLazer.insert(INSERT, "Nenhuma Área de Lazer disponível para o filtro selecionado!")
                
                            
    # Método para instanciar os bancos de dados e receber seus dados
    def iniciaBDs(self):
        # Importa banco de dados
        auxConsulta = BD_Quartos()
        self.dadosQuarto=auxConsulta.leDadosCompletosQuarto()
        
        auxConsultaLazer = BD_Lazer()
        self.dadosLazer=auxConsultaLazer.leDadosCompletosArea()
        
        
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
        opcoesStatus = ["Disponível", "Ocupado", "Manutenção"]
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
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()

x6 = consultaQuartoWindow()
x6.consultaQuarto()
'''
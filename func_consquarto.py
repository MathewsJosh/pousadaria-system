from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont

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
        self.botaoConsultarQuarto = Button(command=self.consultaExibe, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        self.botaoConsultarQuarto.place(relx=0.9, rely=0.9, anchor="n")
        
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
        
        auxConsultaLazer = BD_Areas()
        self.dadosLazer=auxConsultaLazer.leDadosCompletosArea()
        
        
    # Método para formatar a tela principal de consulta    
    def formataTelaConsultaQuarto(self):
        # Cria uma janela e define suas principais configurações
        self.consultaQuartoJanela = Tk()
        self.consultaQuartoJanela.title("Recepção - Escolha uma Opção")
        self.consultaQuartoJanela.wm_iconbitmap(camIco)
        self.consultaQuartoJanela.focus_force()
        self.consultaQuartoJanela.geometry(tam)

        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        # Converte os pngs dos botões para imagem
        self.camConsultarQuarto = PhotoImage(file="Images\Botões\inicio_consultar.png", master=self.consultaQuartoJanela)
        self.camVoltar = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.consultaQuartoJanela)

        # Cria o botão voltar e o posiciona
        self.botaoVoltar = Button(image=self.camVoltar, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")

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
        print("Apagou Consulta")
        self.consultaQuartoJanela.destroy()
        

x6 = consultaQuartoWindow()
x6.consultaQuarto()


'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
self.consultaQuartoJanela.mainloop()

e coloque o seguinte comando adaptado para poder executa-la
#x1 = telaInicialWindow()
#x1.telaInicial()
''' 


''' BACKUP
        # Cria uma listbox com os quartos disponíveis
        #listaQuartos = Listbox(self.quartosdisp)
        #listaQuartos.grid(row=0, column=0, pady=10)

        #nomes = ['Quarto 1','pedro','bailarina']
        #for z in nomes:
            #listaQuartos.insert(END,z)
        #print(listaQuartos.get())
'''

'''
        # Cria e posiciona as labels e entrys dentro do self.filtroframe
        lb1 = Label(self.filtroframe, text="Data da Reserva: ", width=15)
        self.Date1Entry = DateEntry(self.filtroframe, width=15, date_pattern='dd/mm/yyyy')
        lb1.grid(row=0, column=0, pady=10)
        self.Date1Entry.grid(row=0, column=1, pady=10)
'''

'''BACKUP
        #self.aviso = Label(self.consultaQuartoJanela, text="Da", foreground='red')
        # Apaga qualquer aviso anterior
        #self.aviso.destroy()
        #self.aviso.forget()
        # Posiciona a label de aviso
        #self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
        
        
        #self.datadeSaida = datetime.strptime(self.Date2Entry.get(), '%d/%m/%Y').date()
        #print(self.datadeSaida, type(self.datadeSaida))
        #print("data_hoje < data_passada", self.data_hoje <= self.datadeEntrada)
        #Verifica se alguma das datas selecionadas é invalida (Passado)
        
        
        
        #print(data_hoje, type(data_hoje))
        #data_hoje = str(datetime.now().date().strftime("%d/%m/%Y"))                         # Pega a data atual e converte para string
        #date_hojeDatetime = datetime.strptime(data_hoje, '%d/%m/%Y').date()                 # Converte a data para dateTime
        print(date_hojeDatetime, type(date_hojeDatetime))
        
        
        #Testa uma data anterior
        #data_passada = datetime.strptime("06/02/2021", '%d/%m/%Y').date()
        print(data_passada, type(data_passada))
        '''
        
'''      
        #data_final = datetime.strptime(self.datadeSaida, "%dd/%mm/%yyyy")
        #if data_inicial <= data_modificacao <= data_final:
           # print('data_modificacao está entre o período selecionado')
       # else:
            #print('data_modificacao está fora do período selecionado')
'''

'''
        # Pego a data de hoje
        self.data_hoje = datetime.now().date()
        #SOMA DATAS
        #print(self.data_hoje + timedelta(days=10))
        
        # Converte a data selecionada no formulário para datetime
        self.datadeEntrada = datetime.strptime(self.Date1Entry.get(), '%d/%m/%Y').date()
        
        # Converter todas as datas do self.dadosQuarto (Data de entrada 8 e saida 9) para datetime e armazenar na mesma posição
        for x in self.dadosQuarto:
            if x[8] != None and x[9] != None:
                x[8] = datetime.strptime(x[8], '%d/%m/%Y').date()
                x[9] = datetime.strptime(x[9], '%d/%m/%Y').date()
                #print(x[8],type(x[8]))
            
        
        # Verificar se está ocupado naquela data
        for x in self.dadosQuarto:
            if x[8] != None and x[9] != None:
                self.aviso = Label(self.consultaQuartoJanela,text="Sem informação dessa data no BD", foreground='red')
                self.aviso.place(relx=0.5, rely=0.9, anchor="n")
                print("Sem informação dessa data no BD")
            elif self.datadeEntrada > x[8] and self.datadeEntrada < self.x[9]:
                print("Data dentro da reserva, quarto ocupado")
                self.textboxLazer.delete(1.0, END)
                self.textboxLazer.insert(INSERT, "Nenhum Quarto disponível para essa data para esse filtro!")
                
'''

'''
#from datetime import datetime,timedelta
#from tkinter.filedialog import askopenfilename
#from tkcalendar import *
'''
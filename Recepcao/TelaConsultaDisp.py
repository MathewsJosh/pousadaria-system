from tkinter import *
from tkcalendar import *
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from datetime import datetime
#from ..BancosdeDados import BD_CadastroFunc
from .. import BancosdeDados
#from .. import BancosdeDados


#from .. import BancosdeDados
#from BancosdeDados import 
#print(dir())
#from ..BancosdeDados import BD_QuartosDisp
#import importlib
#m1 = importlib.import_module("..BancosdeDados\BD_QuartosDisp.py", ".BD_QuartosDisp")
#print (m1)
#from Pousadaria.


#pip install tkcalendar


#Variaveis Globais
tam = "1200x720"
camIco = "Icones\Pousadaria.ico"

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
        self.insereData = 0
        self.quartosdisp = 0
        self.areasdisp = 0
        # Outros
        self.Date1Entry = 0
        #self.Date2Entry = 0
        self.aviso = 0
        self.textboxQuarto = 0
        self.textboxLazer = 0
        # Dados a serem enviados ao BD
        self.datadeEntrada = 0
        #self.datadeSaida = 0
        self.data_hoje = 0

    def consultaQuarto(self):
        self.formataTelaConsultaQuarto()
        
        # Cria os Botões e os posiciona
        self.botaoConsultarQuarto = Button(command=self.consultaQuartosDisp, image=self.camConsultarQuarto, bd=0, relief=GROOVE)
        self.botaoConsultarQuarto.place(relx=0.9, rely=0.9, anchor="n")
        


        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.consultaQuartoJanela.mainloop()

    def consultaQuartosDisp(self):
        # Pego a data de hoje
        self.data_hoje = datetime.now().date()
        
        # Converte a data selecionada no formulário para datetime
        self.datadeEntrada = datetime.strptime(self.Date1Entry.get(), '%d/%m/%Y').date()
        print(self.datadeEntrada, type(self.datadeEntrada))
        
        
        #auxConsulta = BD_Quartos()
        #dadosauxiliar = auxConsulta.leDadosBasicosQuarto()
        #print(dadosauxiliar)
        
        
        
        
        
        
        
        
        
        
        '''BACKUP
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
        if data_teste2 < data_atual2:
            print ("DEU CERTOOOO")
        else:
            print ("DEU ERRADO")
        '''
        #data_final = datetime.strptime(self.datadeSaida, "%dd/%mm/%yyyy")
        #if data_inicial <= data_modificacao <= data_final:
           # print('data_modificacao está entre o período selecionado')
       # else:
            #print('data_modificacao está fora do período selecionado')
        
        
        
        #Verificar se as datas são no passado
        
        
        
        #print(self.datadeEntrada)
        
    
    def formataTelaConsultaQuarto(self):
        # Cria uma janela e define suas principais configurações
        self.consultaQuartoJanela = Tk()
        self.consultaQuartoJanela.title("Recepção - Escolha uma Opção")
        self.consultaQuartoJanela.wm_iconbitmap(camIco)
        self.consultaQuartoJanela.focus_force()
        self.consultaQuartoJanela.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camConsultarQuarto = PhotoImage(file="Botões\Recepção\Internos//button_consultarInt.png", master=self.consultaQuartoJanela)
        self.camVoltar = PhotoImage(file="Botões\Recepção\Internos//button_voltarInt.png", master=self.consultaQuartoJanela)

        # Cria o botão voltar e o posiciona
        self.botaoVoltar = Button(image=self.camVoltar, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")

        #---------------------------------------------------Frame - Entrada de datas------------------------------------------------------#
        # Cria um frame para a entrada de datas
        self.insereData = LabelFrame(self.consultaQuartoJanela, text = "Insira a data desejada", padx=10)
        self.insereData.place(relx=0.12, rely=0.05, anchor="n")

        # Cria e posiciona as labels e entrys dentro do self.insereData
        lb1 = Label(self.insereData, text="Data da Reserva: ", width=15)
        self.Date1Entry = DateEntry(self.insereData, width=15, date_pattern='dd/mm/yyyy')
        lb1.grid(row=0, column=0, pady=10)
        self.Date1Entry.grid(row=0, column=1, pady=10)
        #lb2 = Label(self.insereData, text="Data de fim: ", width=15)
        #lb2.grid(row=1, column=0, pady=10)
        #self.Date2Entry = DateEntry(self.insereData, width=15, date_pattern='dd/mm/yyyy')
        #self.Date2Entry.grid(row=1, column=1, pady=10)

        #---------------------------------------------------Frame - Quartos disponíveis------------------------------------------------------#
        # Cria um frame exibir os quartos disponiveis
        self.quartosdisp = LabelFrame(self.consultaQuartoJanela, text = "Quartos disponíveis", padx=10,pady=10)
        self.quartosdisp.place(relx=0.25, rely=0.35, anchor="n")

        # Cria uma listbox com os quartos disponíveis
        listaQuartos = Listbox(self.quartosdisp)
        listaQuartos.grid(row=0, column=0, pady=10)

        nomes = ['Quarto 1','pedro','bailarina']
        for z in nomes:
            listaQuartos.insert(END,z)
        #print(listaQuartos.get())

        # Cria um textbox com os detalhes do quarto
        fontfamilylist = list(tkFont.families())
        fontindex = 0
        fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        self.textboxQuarto = scrolledtext.ScrolledText(self.quartosdisp, height=10, width=30, font=fontStyle)
        self.textboxQuarto.grid(row=0, column=1, padx=10, pady=10)

        # Função necessária para não permitir que o textbox seja editado
        self.textboxQuarto.bind("<Key>", lambda e: "break")


        #---------------------------------------------------Frame - Area de lazer------------------------------------------------------#
        # Cria um frame exibir as Areas de Lazer Disponíveis
        self.areasdisp = LabelFrame(self.consultaQuartoJanela, text = "Áreas de lazer disponíveis", padx=10,pady=10)
        self.areasdisp.place(relx=0.75, rely=0.35, anchor="n")

        # Cria uma listbox com os quartos disponíveis
        listaQuartos = Listbox(self.areasdisp)
        listaQuartos.grid(row=0, column=0, pady=10)

        nomes = ['Churrasqueira','pedro','bailarina']
        for z in nomes:
            listaQuartos.insert(END,z)
        #print(listaQuartos.get())

        # Cria um textbox com os detalhes do quarto
        fontfamilylist = list(tkFont.families())
        fontindex = 0
        fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        self.textboxLazer = scrolledtext.ScrolledText(self.areasdisp, height=10, width=30, font=fontStyle)
        self.textboxLazer.grid(row=0, column=1, padx=10, pady=10)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxLazer.bind("<Key>", lambda e: "break")

        #---------------------------------------------------Aviso------------------------------------------------------#
        # Cria e posiciona aviso de erro
        self.aviso = Label(self.consultaQuartoJanela, text="avisar algo", foreground='red')
        # Apaga qualquer aviso anterior
        #self.aviso.destroy()
        #self.aviso.forget()
        # Posiciona a label de aviso
        self.aviso.place(relx=0.5, rely=0.9, anchor="n") 
        
        
        
        
        
        
    
    def ApagaInicial(self):
        print("Apagou tela inicial")
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

'''PROBLEMAS
Fazer o usuário escrever somente numeros
data ser valida
data não ser do passado
limitar numero de digitos
'''
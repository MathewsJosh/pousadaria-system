from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from tkcalendar import *

# Importações de outras classes locais
from BD_cardapio import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class Cardapio():
    # Inicializadores
    def __init__(self):
        # Janela
        self.telaCardapio = 0
        # Auxiliares das conversões de imagem
        self.cambotaoConsulta = 0
        self.cambotaoInserir = 0
        self.cambotaoRemover = 0
        self.cambotaoProximo = 0
        self.cambotaoVoltar = 0
        self.cambotaoAtualizar = 0
        self.cambotaoDeletar = 0
        # Botões
        self.botaoConsulta = 0
        self.botaoInserir = 0
        self.botaoProximo = 0
        self.botaoVoltar = 0
        self.botaoSelecionar = 0
        self.botaoAtualizar = 0
        self.botaoDeletar = 0
        # Frames
        self.filtroframe = 0
        self.insereframe = 0
        self.consultaframe = 0
        self.atualizaframe = 0
        self.deletaframe = 0
        self.dataFrame = 0
        # Comboboxes
        self.crudCombobox = 0
        #self.idCombobox = 0
        self.statusCombobox = 0
        # Textboxes
        self.textboxInsere = 0
        self.textboxAtualiza = 0
        self.textboxConsulta = 0
        # Instancia de cardapio
        self.bdcardapio = BD_CardapioCRUD() 
        # Booleanos
        self.inseresim = 0
        self.consultasim = 0
        self.atualizasim = 0
        self.deletasim = 0
        # Dados retornados do banco de dados
        self.dadosLidosCardapio = 0
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.textCardapio = 0
        self.opcoesClientes = []
        self.IDsRecs = []
        self.DateEntry = 0
        

    # Método de controle da tela cardapio
    def selecionaCRUDCardapio(self):
        # Cria uma janela e define suas principais configurações
        self.telaCardapio = Tk()
        self.telaCardapio.title("Administração - Cardápio")
        self.telaCardapio.wm_iconbitmap(camIco)
        self.telaCardapio.focus_force()
        self.telaCardapio.geometry(tam)
        
        # Converte as imagens em PhotoImage para serem usadas como botões
        self.cambotaoConsulta = PhotoImage(file="Images\Botões\inicio_consultar.png", master=self.telaCardapio)
        self.cambotaoInserir = PhotoImage(file="Images\Botões\inicio_inserir.png", master=self.telaCardapio)
        self.cambotaoProximo = PhotoImage(file="Images\Botões\inicio_proximo.png", master=self.telaCardapio)
        self.cambotaoVoltar = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.telaCardapio)
        self.cambotaoAtualizar = PhotoImage(file="Images\Botões\inicio_atualizar.png", master=self.telaCardapio)
        self.cambotaoDeletar = PhotoImage(file="Images\Botões\inicio_deletar.png", master=self.telaCardapio)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        
        #---------------------------------------------------Frame - Filtro de Cardapio------------------------------------------------------#
        # Cria um frame para a entrada de filtros
        self.filtroframe = LabelFrame(self.telaCardapio, text = "Filtragem de funções", padx=10)
        self.filtroframe.place(relx=0.45, rely=0.05, anchor="n")
        
        # Cria e posiciona Labels
        lb1 = Label(self.filtroframe, text="Operação: ")
        lb1.grid(row=0, column=0, padx=5, sticky=W)
        
        # Cria e posiciona a combobox de escolha do CRUD
        opcoesFiltros = ["Inserir", "Consultar", "Atualizar", "Deletar"]
        self.crudCombobox = ttk.Combobox(self.filtroframe, value=opcoesFiltros, width=10, state="readonly")
        self.crudCombobox.current(0)
        self.crudCombobox.grid(row=0, column=1, sticky=E, padx=5, pady=10)
        
        #---------------------------------------------------Fim------------------------------------------------------#
        
        # Cria e posiciona botões
        self.botaoProximo = Button(self.telaCardapio, command=self.controleCRUD, image=self.cambotaoProximo, bd=0, relief=GROOVE)
        self.botaoProximo.place(relx=0.6, rely=0.07, anchor="n")
        
        #, command= tela anterior (menu)
        self.botaoVoltar = Button(self.telaCardapio, image=self.cambotaoVoltar, command=self.ApagatelaCardapio, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Cria e posiciona uma label de aviso
        self.aviso = Label(self.telaCardapio, foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9)
        
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.telaCardapio.mainloop()
        
    # Método de controle do CRUD Cardapio
    def controleCRUD(self):
        if self.crudCombobox.get() == "Inserir":
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.inseresim = 1
            self.formataInsereCardapio()
        if self.crudCombobox.get() == "Consultar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.consultasim = 1
            self.formataConsultaCardapio()
        if self.crudCombobox.get() == "Atualizar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.deletasim == 1:
                self.apagaDelete()
            self.atualizasim = 1
            self.atualizaCardapio()
        if self.crudCombobox.get() == "Deletar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            self.deletasim = 1
            self.deletaCardapio()

    #---------------------------------------------------Insere Cardapio------------------------------------------------------#
    # Formata a tela de Cardapio
    def formataInsereCardapio(self):
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.atualizasim == 1:
            self.apagaAtualiza()
        if self.deletasim == 1:
            self.apagaDelete()
            
        #---------------------------------------------------Frame - Insere data e refeições------------------------------------------------------#    
        # Cria um frame para a entrada de refeições e data
        self.insereframe = LabelFrame(self.telaCardapio, text = "Insira a Cardapio", padx=10)
        self.insereframe.place(relx=0.5, rely=0.2, anchor="n")

        # Cria e posiciona a label
        lb1 = Label(self.insereframe, text="Data: ", width=8)
        lb1.grid(row=0, column=1, pady=10, sticky=E)
        
        # Cria e posiciona entrada de datas
        self.DateEntry = DateEntry(self.insereframe, width=15, date_pattern='dd/mm/yyyy')
        self.DateEntry.grid(row=0, column=2, pady=10, sticky=W)

        # Cria um textbox para a entrada da Cardapio
        self.textboxInsere = scrolledtext.ScrolledText(self.insereframe, height=15, width=70, font=self.fontStyle)
        self.textboxInsere.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
        
        # Cria e posiciona o botão inserir
        self.botaoInserir = Button(self.telaCardapio, image=self.cambotaoInserir, command=self.insereCardapio, bd=0, relief=GROOVE)
        self.botaoInserir.place(relx=0.9, rely=0.9, anchor="n")

    # Método de inserção do cardapio no banco de dados
    def insereCardapio(self):
        self.textCardapio = self.textboxInsere.get("1.0",'end-1c')
        # Verifica se algo escrito antes de salvar no banco de dados
        if self.textCardapio == "":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Caixa de texto vazia!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
        else:
            # Salva todas as informações no banco de dados
            self.bdcardapio.insereDadosCar(str(self.DateEntry.get()), self.textCardapio)
            # Cria e posiciona uma label de aviso
            self.textboxInsere.delete(1.0, 'end')
            self.aviso = Label(self.telaCardapio,text="Cardapio registrado!", foreground='green', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
            
    # Apaga frame de inserção
    def apagaInsercao(self):
        self.insereframe.destroy()
        self.botaoInserir.destroy()
        self.aviso.destroy()
    #---------------------------------------------------FIM - Insere Cardapio------------------------------------------------------#    
    
    
    #---------------------------------------------------Consulta Cardapio------------------------------------------------------#     
    # Exibe as Cardapio na tela
    def formataConsultaCardapio(self):
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.atualizasim == 1:
            self.apagaAtualiza()
        if self.deletasim == 1:
            self.apagaDelete()
        
        #---------------------------------------------------Frame - Consulta Cardápio------------------------------------------------------# 
        # Cria um frame para exibir detalhes de uma Cardapio
        self.consultaframe = LabelFrame(self.telaCardapio, text = "Refeições", padx=10)
        self.consultaframe.place(relx=0.5, rely=0.25, anchor="n")

        # Cria e posiciona Labels
        lb2 = Label(self.consultaframe, text="Dia: ", width=8)
        lb2.grid(row=0, column=0, padx=0, sticky=E)
        
        # Cria e posiciona entrada de datas
        self.DateEntry = DateEntry(self.consultaframe, width=15, date_pattern='dd/mm/yyyy')
        self.DateEntry.grid(row=0, column=1, pady=10, sticky=W)
        
        # Cria um textbox para exibir Cardapio
        self.textboxConsulta = scrolledtext.ScrolledText(self.consultaframe, height=15, width=50, font=self.fontStyle)
        self.textboxConsulta.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxConsulta.bind("<Key>", lambda e: "break")
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.telaCardapio, command=self.consultaCar, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.place(relx=0.9, rely=0.9, anchor="n")
    
    # Busca o Cardapio no banco de dados
    def consultaCar(self):
        self.dadosLidosCardapio = self.bdcardapio.leDadosCar()
        cont=0
        self.textboxConsulta.delete(1.0, 'end')
        for x in self.dadosLidosCardapio:
            if (x[0] == str(self.DateEntry.get())):
                cont+=1
                self.textboxConsulta.insert(INSERT, str(x[1]))
        
        if(cont>=1):
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaCardapio,text="Processo de consulta realizado com sucesso!", foreground='green', font=12)
            self.aviso.place(relx=0.35, rely=0.9)
        else:
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaCardapio,text="Não foi encontrado Cardápio para essa data", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9)    
    
    # Apaga o frame de consulta
    def apagaConsulta(self):
        self.consultaframe.destroy()
        self.botaoConsultar.destroy()
        self.aviso.destroy()
            
    #---------------------------------------------------Fim - Consulta Cardapio------------------------------------------------------#     
        
        
    #---------------------------------------------------Atualiza Cardapio------------------------------------------------------#    
    # Exibe o Cardapio na tela
    def atualizaCardapio(self):
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.deletasim == 1:
            self.apagaDelete()
            
        #---------------------------------------------------Frame - Seleciona Data------------------------------------------------------#
        # Cria um frame de seleção de clientes e ids
        self.dataFrame = LabelFrame(self.telaCardapio, text = "Selecione uma data", padx=10)
        self.dataFrame.place(relx=0.3, rely=0.25, anchor="n")    
            
        # Cria e posiciona Labels
        lb3 = Label(self.dataFrame, text="Cliente: ", width=8)
        lb3.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona entrada de datas
        self.DateEntry = DateEntry(self.dataFrame, width=15, date_pattern='dd/mm/yyyy')
        self.DateEntry.grid(row=0, column=1, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.dataFrame, command=self.consAtualizaCar, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
        #---------------------------------------------------Frame - Atualiza Cardapio------------------------------------------------------#
        # Cria um frame para exibir detalhes do Cardapio
        self.atualizaframe = LabelFrame(self.telaCardapio, text = "Edição de Cardápio", padx=10)
        self.atualizaframe.place(relx=0.7, rely=0.25, anchor="n")
        
        # Cria um textbox para exibir Cardapio
        self.textboxAtualiza = scrolledtext.ScrolledText(self.atualizaframe, height=15, width=50, font=self.fontStyle)
        self.textboxAtualiza.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        #Cria botão atualizar mas NÃO O POSICIONA
        self.botaoAtualizar = Button(self.telaCardapio, command=self.consAtualizaCar, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        
    
    # Busca as reclamações do cliente no banco de dados
    def consAtualizaCar(self):
        self.dadosLidosCardapio = self.bdcardapio.leDadosCar()
        cont=0
        self.textboxAtualiza.delete(1.0, 'end')
        for x in self.dadosLidosCardapio:
            if x[0] == self.DateEntry.get():
                cont+=1
                self.textboxAtualiza.insert(INSERT, x[1])
                break
        
        if(cont==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Não foi encontrado Cardápio para essa Data!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            
        # Cria e posiciona o botão Atualizar
        self.botaoAtualizar = Button(self.telaCardapio, command=self.atualizaCarBD, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        self.botaoAtualizar.place(relx=0.9, rely=0.9, anchor="n")   
    
    # Método que atualiza a Cardapio do cliente no banco de dados
    def atualizaCarBD(self):
        if self.textboxAtualiza.get(1.0, END)=="":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Caixa de refeições vazia, tente novamente!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
        else:
            self.bdcardapio.atualizaCar(str(self.DateEntry.get()), str(self.textboxAtualiza.get(1.0, END)))
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Cardápio atualizado no banco de dados!", foreground='Green', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
    
    # Apaga o frame de atualização
    def apagaAtualiza(self):
        self.atualizaframe.destroy()
        self.dataFrame.destroy()
        self.botaoAtualizar.destroy()
        self.aviso.destroy()
        
        
    #---------------------------------------------------Deleta reclamações------------------------------------------------------#     
    # Deleta reclamações
    def deletaCardapio(self):
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.atualizasim == 1:
            self.apagaAtualiza()
            
        #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
        # Cria um frame de seleção de clientes e ids
        self.dataFrame = LabelFrame(self.telaCardapio, text = "Selecione um cliente", padx=10)
        self.dataFrame.place(relx=0.5, rely=0.4, anchor="n")    
            
        # Cria e posiciona Labels
        lb4 = Label(self.dataFrame, text="Data: ", width=8)
        lb4.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona entrada de datas
        self.DateEntry = DateEntry(self.dataFrame, width=15, date_pattern='dd/mm/yyyy')
        self.DateEntry.grid(row=0, column=1, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoDeletar = Button(self.dataFrame, command=self.deletaRecBD, image=self.cambotaoDeletar, bd=0, relief=GROOVE)
        self.botaoDeletar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
    # Deleta o Cardapio daquela data do banco de dados
    def deletaRecBD(self):
        self.dadosLidosCardapio = self.bdcardapio.leDadosCar()
        contador=0
        for x in self.dadosLidosCardapio:
            if x[0] == self.DateEntry.get():
                self.bdcardapio.deletaCar(str(self.DateEntry.get()))
                contador+=1
        
        self.aviso.destroy()
        if(contador==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Não há nenhuma refeição para essa data no banco de dados!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        else:
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaCardapio,text="Cardápio deletado do banco de dados com sucesso!", foreground='Green', font=12)
            
            self.aviso.place(relx=0.4, rely=0.9) 
             
    # Destroy a tela de Delete
    def apagaDelete(self):
        self.dataFrame.destroy()
        self.aviso.destroy()
    
    # Método que apaga a janela atual
    def ApagatelaCardapio(self):
        print("Apagou Cardapio")
        self.telaCardapio.destroy()

'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()
  
x10 = Cardapio()
x10.selecionaCRUDCardapio()
'''
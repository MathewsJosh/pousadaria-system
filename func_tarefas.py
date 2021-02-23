from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from tkcalendar import *

# Importações de outras classes Prioridades
from BD_tarefas import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Classe de Controle de Tarefas
class Tarefas():
    # Inicializadores
    def __init__(self):
        # Janela
        self.telaTarefas = 0
        # Auxiliares das conversões de imagem
        self.cambotaoConsulta = 0
        self.cambotaoInserir = 0
        self.cambotaoProximo = 0
        self.cambotaoVoltar = 0
        self.cambotaoAtualizar = 0
        self.cambotaoDeletar = 0
        # Botões
        self.botaoConsulta = 0
        self.botaoInserir = 0
        self.botaoProximo = 0
        self.botaoVoltar = 0
        self.botaoAtualizar = 0
        self.botaoDeletar = 0
        # Frames
        self.filtroframe = 0
        self.insereframe = 0
        self.consultaframe = 0
        self.atualizaframe = 0
        self.deletaframe = 0
        self.prioridadeFrame = 0
        # Comboboxes
        self.crudCombobox = 0
        self.prioridadeCombobox = 0
        #self.idCombobox = 0
        # Textboxes
        self.textboxInsere = 0
        self.textboxAtualiza = 0
        self.textboxConsulta = 0
        # Instancia de Tarefas
        self.bdTarefas = BD_TarefasCRUD() 
        # Booleanos
        self.inseresim = 0
        self.consultasim = 0
        self.atualizasim = 0
        self.deletasim = 0
        # Dados retornados do banco de dados
        self.dadosLidosTarefas = 0
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.textTarefas = 0
        self.opcaoPrioridades = ["Urgente", "Alta", "Média", "Baixa"]
        

    # Método de controle da tela Tarefas
    def selecionaCRUDTarefas(self):
        # Cria uma janela e define suas principais configurações
        self.telaTarefas = Tk()
        self.telaTarefas.title("Administração - Tarefas")
        self.telaTarefas.wm_iconbitmap(camIco)
        self.telaTarefas.focus_force()
        self.telaTarefas.geometry(tam)
        
        # Converte as imagens em PhotoImage para serem usadas como botões
        self.cambotaoConsulta = PhotoImage(file="Images\Botões\inicio_consultar.png", master=self.telaTarefas)
        self.cambotaoInserir = PhotoImage(file="Images\Botões\inicio_inserir.png", master=self.telaTarefas)
        self.cambotaoProximo = PhotoImage(file="Images\Botões\inicio_proximo.png", master=self.telaTarefas)
        self.cambotaoVoltar = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.telaTarefas)
        self.cambotaoAtualizar = PhotoImage(file="Images\Botões\inicio_atualizar.png", master=self.telaTarefas)
        self.cambotaoDeletar = PhotoImage(file="Images\Botões\inicio_deletar.png", master=self.telaTarefas)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        
        #---------------------------------------------------Frame - Filtro de Tarefas------------------------------------------------------#
        # Cria um frame para a entrada de filtros
        self.filtroframe = LabelFrame(self.telaTarefas, text = "Filtragem de funções", padx=10)
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
        self.botaoProximo = Button(self.telaTarefas, command=self.controleCRUD, image=self.cambotaoProximo, bd=0, relief=GROOVE)
        self.botaoProximo.place(relx=0.6, rely=0.07, anchor="n")
        
        #, command= tela anterior (menu)
        self.botaoVoltar = Button(self.telaTarefas, image=self.cambotaoVoltar, command=self.ApagaTelaTarefas, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Cria e posiciona uma label de aviso
        self.aviso = Label(self.telaTarefas, foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9)
        
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.telaTarefas.mainloop()
    
    # Método de controle do Crud da tela Tarefas
    def controleCRUD(self):
        if self.crudCombobox.get() == "Inserir":
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.inseresim = 1
            self.formataInsereTarefas()
        if self.crudCombobox.get() == "Consultar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.consultasim = 1
            self.formataConsultaTarefas()
        if self.crudCombobox.get() == "Atualizar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.deletasim == 1:
                self.apagaDelete()
            self.atualizasim = 1
            self.atualizaTarefas()
        if self.crudCombobox.get() == "Deletar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            self.deletasim = 1
            self.deletaTarefas()

    #---------------------------------------------------Insere Tarefas------------------------------------------------------#
    # Formata a tela de Tarefas
    def formataInsereTarefas(self):
        #---------------------------------------------------Frame - Insere data e refeições------------------------------------------------------#    
        # Cria um frame para a entrada de refeições e data
        self.insereframe = LabelFrame(self.telaTarefas, text = "Insira as Tarefas", padx=10)
        self.insereframe.place(relx=0.5, rely=0.2, anchor="n")

        # Cria e posiciona a label
        lb1 = Label(self.insereframe, text="Prioridade: ", width=8)
        lb1.grid(row=0, column=1, pady=10, sticky=E)
        
        # Cria e posiciona a combobox que irá filtrar o prioridade
        self.prioridadeCombobox = ttk.Combobox(self.insereframe, value=self.opcaoPrioridades, width=10, state="readonly")
        self.prioridadeCombobox.current(0)
        self.prioridadeCombobox.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # Cria um textbox para a entrada da Tarefas
        self.textboxInsere = scrolledtext.ScrolledText(self.insereframe, height=15, width=70, font=self.fontStyle)
        self.textboxInsere.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
        
        # Cria e posiciona o botão inserir
        self.botaoInserir = Button(self.telaTarefas, image=self.cambotaoInserir, command=self.insereTarefas, bd=0, relief=GROOVE)
        self.botaoInserir.place(relx=0.9, rely=0.9, anchor="n")

    # Método de inserção de novas tarefas
    def insereTarefas(self):
        self.textTarefas = self.textboxInsere.get("1.0",'end-1c')
        # Verifica se algo escrito antes de salvar no banco de dados
        self.aviso.destroy()
        if self.textTarefas == "":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Caixa de texto vazia!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
        else:
            # Salva todas as informações no banco de dados
            self.bdTarefas.insereDadosEst(str(self.prioridadeCombobox.get()), self.textTarefas)
            # Cria e posiciona uma label de aviso
            self.textboxInsere.delete(1.0, 'end')
            self.aviso = Label(self.telaTarefas,text="Tarefa registrada!", foreground='green', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
            
    # Método de remoção da tela de inserção
    def apagaInsercao(self):
        self.insereframe.destroy()
        self.botaoInserir.destroy()
        self.aviso.destroy()
    #---------------------------------------------------FIM - Insere Tarefas------------------------------------------------------#    
    
    
    #---------------------------------------------------Consulta Tarefas------------------------------------------------------#     
    # Exibe as Tarefas na tela
    def formataConsultaTarefas(self):
        #---------------------------------------------------Frame - Consulta Tarefas------------------------------------------------------# 
        # Cria um frame para exibir detalhes de uma Tarefas
        self.consultaframe = LabelFrame(self.telaTarefas, text = "Informações do Tarefas", padx=10)
        self.consultaframe.place(relx=0.5, rely=0.25, anchor="n")

        # Cria e posiciona Labels
        lb2 = Label(self.consultaframe, text="prioridade: ", width=8)
        lb2.grid(row=0, column=0, padx=0, sticky=E)
        
        # Cria e posiciona a combobox que irá filtrar o prioridade
        self.prioridadeCombobox = ttk.Combobox(self.consultaframe, value=self.opcaoPrioridades, width=10, state="readonly")
        self.prioridadeCombobox.current(0)
        self.prioridadeCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria um textbox para exibir Tarefas
        self.textboxConsulta = scrolledtext.ScrolledText(self.consultaframe, height=15, width=50, font=self.fontStyle)
        self.textboxConsulta.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxConsulta.bind("<Key>", lambda e: "break")
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.telaTarefas, command=self.consultaEst, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.place(relx=0.9, rely=0.9, anchor="n")
    
    # Busca o Tarefas no banco de dados
    def consultaEst(self):
        self.dadosLidosTarefas = self.bdTarefas.leDadosEst() 
        self.textboxConsulta.delete(1.0, 'end')
        cont=0
        for x in self.dadosLidosTarefas:
            if (x[0] == str(self.prioridadeCombobox.get())):
                cont+=1
                self.textboxConsulta.insert(INSERT, str(x[1]))
        
        if(cont>=1):
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaTarefas,text="Processo de consulta realizado com sucesso!", foreground='green', font=12)
            self.aviso.place(relx=0.35, rely=0.9)
        else:
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaTarefas,text="Não foram encontradas tarefas para essa prioridade!", foreground='red', font=12)
            self.aviso.place(relx=0.35, rely=0.9)    
    
    # Método de remoção da tela de consulta
    def apagaConsulta(self):
        self.consultaframe.destroy()
        self.botaoConsultar.destroy()
        self.aviso.destroy()
        
    #---------------------------------------------------Fim - Consulta Tarefas------------------------------------------------------#     
        
         
    #---------------------------------------------------Atualiza Tarefas------------------------------------------------------#    
    # Exibe o Tarefas na tela
    def atualizaTarefas(self):
        #---------------------------------------------------Frame - Seleciona Data------------------------------------------------------#
        # Cria um frame de seleção de Prioridades e ids
        self.prioridadeFrame = LabelFrame(self.telaTarefas, text = "Selecione um prioridade", padx=10)
        self.prioridadeFrame.place(relx=0.3, rely=0.25, anchor="n")    
            
        # Cria e posiciona Labels
        lb3 = Label(self.prioridadeFrame, text="prioridade: ", width=8)
        lb3.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar o prioridade
        self.prioridadeCombobox = ttk.Combobox(self.prioridadeFrame, value=self.opcaoPrioridades, width=10, state="readonly")
        self.prioridadeCombobox.current(0)
        self.prioridadeCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.prioridadeFrame, command=self.consAtualizaEst, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
        #---------------------------------------------------Frame - Atualiza Tarefas------------------------------------------------------#
        # Cria um frame para exibir detalhes do Tarefas
        self.atualizaframe = LabelFrame(self.telaTarefas, text = "Edição de Tarefas", padx=10)
        self.atualizaframe.place(relx=0.7, rely=0.25, anchor="n")
        
        # Cria um textbox para exibir Tarefas
        self.textboxAtualiza = scrolledtext.ScrolledText(self.atualizaframe, height=15, width=50, font=self.fontStyle)
        self.textboxAtualiza.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        #Cria botão atualizar mas NÃO O POSICIONA
        self.botaoAtualizar = Button(self.telaTarefas, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        
    
    # Busca as reclamações do Locai no banco de dados
    def consAtualizaEst(self):
        self.dadosLidosTarefas = self.bdTarefas.leDadosEst()
        cont=0
        self.textboxAtualiza.delete(1.0, 'end')
        for x in self.dadosLidosTarefas:
            if x[0] == self.prioridadeCombobox.get():
                cont+=1
                self.textboxAtualiza.insert(INSERT, x[1])
                break
        
        if(cont==0):
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Não foram encontradas tarefas para essa prioridade!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            
        # Cria e posiciona o botão Atualizar
        self.botaoAtualizar = Button(self.telaTarefas, command=lambda: self.atualizaCarBD(cont), image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        self.botaoAtualizar.place(relx=0.9, rely=0.9, anchor="n")   
    
    # Método que atualiza a Tarefas do Locai no banco de dados
    def atualizaCarBD(self, cont):
        self.aviso.destroy()
        if(cont==0):
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Essa prioridade não pode ser atualizada, tente reconsulta-la!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            return
        if self.textboxAtualiza.get(1.0, END) == "":
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Caixa de tarefas vazia, tente novamente!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
        else:
            self.aviso.destroy()
            self.bdTarefas.atualizaEst(str(self.prioridadeCombobox.get()), str(self.textboxAtualiza.get(1.0, END)))
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Tarefas atualizadas no banco de dados!", foreground='Green', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
    
    # Método de remoção da tela de atualização
    def apagaAtualiza(self):
        self.atualizaframe.destroy()
        self.prioridadeFrame.destroy()
        self.botaoAtualizar.destroy()
        self.aviso.destroy()
        
        
    #---------------------------------------------------Deleta reclamações------------------------------------------------------#     
    # Deleta reclamações
    def deletaTarefas(self):
            
        #---------------------------------------------------Frame - Seleciona Prioridades------------------------------------------------------#
        # Cria um frame de seleção de Prioridades
        self.prioridadeFrame = LabelFrame(self.telaTarefas, text = "Selecione um prioridade", padx=10)
        self.prioridadeFrame.place(relx=0.5, rely=0.4, anchor="n")    
            
        # Cria e posiciona Labels
        lb4 = Label(self.prioridadeFrame, text="prioridade: ", width=8)
        lb4.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar o prioridade
        self.prioridadeCombobox = ttk.Combobox(self.prioridadeFrame, value=self.opcaoPrioridades, width=10, state="readonly")
        self.prioridadeCombobox.current(0)
        self.prioridadeCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoDeletar = Button(self.prioridadeFrame, command=self.deletaEstBD, image=self.cambotaoDeletar, bd=0, relief=GROOVE)
        self.botaoDeletar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
    # Deleta o Tarefas daquela data do banco de dados
    def deletaEstBD(self):
        self.dadosLidosTarefas = self.bdTarefas.leDadosEst()
        contador=0
        for x in self.dadosLidosTarefas:
            if x[0] == self.prioridadeCombobox.get():
                self.bdTarefas.deletaEst(str(self.prioridadeCombobox.get()))
                contador+=1
        
        self.aviso.destroy()
        if(contador==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Não há nenhuma tarefa para essa prioridade no banco de dados!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        else:
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaTarefas,text="Tarefas da prioridade selecionada foram deletadas com sucesso!", foreground='Green', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        
    # Destroy a tela de Delete
    def apagaDelete(self):
        self.prioridadeFrame.destroy()
        self.aviso.destroy()
    
    # Método que apaga a janela atual
    def ApagaTelaTarefas(self):
        print("Apagou Tarefas")
        self.telaTarefas.destroy()


'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.telaEstoque.mainloop()
      
x11 = Tarefas()
x11.selecionaCRUDTarefas()
'''

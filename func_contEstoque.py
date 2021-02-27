from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from tkcalendar import *

# Importações de outras classes locais
from BD_contestoque import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class ContEstoque():
    # Inicializadores
    def __init__(self):
        # Janela
        self.telaEstoque = 0
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
        self.localFrame = 0
        # Comboboxes
        self.crudCombobox = 0
        self.localCombobox = 0
        #self.idCombobox = 0
        # Textboxes
        self.textboxInsere = 0
        self.textboxAtualiza = 0
        self.textboxConsulta = 0
        # Instancia de Estoque
        self.bdEstoque = BD_EstoqueCRUD() 
        # Booleanos
        self.inseresim = 0
        self.consultasim = 0
        self.atualizasim = 0
        self.deletasim = 0
        # Dados retornados do banco de dados
        self.dadosLidosEstoque = 0
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.textEstoque = 0
        self.opcaoLocais = ["Recepção", "Cozinha", "Administração", "Banheiros", "Quartos", "Chalés", "Áreas de lazer"]
        self.qtdEntry = 0
        

    # Método de controle da tela Estoque
    def selecionaCRUDEstoque(self):
        # Cria uma janela e define suas principais configurações
        self.telaEstoque = Toplevel()
        self.telaEstoque.title("Administração - Estoque")
        self.telaEstoque.wm_iconbitmap(camIco)
        self.telaEstoque.focus_force()
        self.telaEstoque.geometry(tam)
        
        # Converte as imagens em PhotoImage para serem usadas como botões
        self.cambotaoConsulta = PhotoImage(file="Images\Botões\inicio_consultar.png", master=self.telaEstoque)
        self.cambotaoInserir = PhotoImage(file="Images\Botões\inicio_inserir.png", master=self.telaEstoque)
        self.cambotaoProximo = PhotoImage(file="Images\Botões\inicio_proximo.png", master=self.telaEstoque)
        self.cambotaoVoltar = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.telaEstoque)
        #self.cambotaoSelecionar = PhotoImage(file="Images\Botões\inicio_selecionar.png", master=self.telaEstoque)
        self.cambotaoAtualizar = PhotoImage(file="Images\Botões\inicio_atualizar.png", master=self.telaEstoque)
        self.cambotaoDeletar = PhotoImage(file="Images\Botões\inicio_deletar.png", master=self.telaEstoque)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        
        #---------------------------------------------------Frame - Filtro de Estoque------------------------------------------------------#
        # Cria um frame para a entrada de filtros
        self.filtroframe = LabelFrame(self.telaEstoque, text = "Filtragem de funções", padx=10)
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
        self.botaoProximo = Button(self.telaEstoque, command=self.controleCRUD, image=self.cambotaoProximo, bd=0, relief=GROOVE)
        self.botaoProximo.place(relx=0.6, rely=0.07, anchor="n")
        
        #, command= tela anterior (menu)
        self.botaoVoltar = Button(self.telaEstoque, image=self.cambotaoVoltar, command=self.ApagaTelaEstoque, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Cria e posiciona uma label de aviso
        self.aviso = Label(self.telaEstoque, foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9)
        
        
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.telaEstoque.mainloop()
        
    def controleCRUD(self):
        if self.crudCombobox.get() == "Inserir":
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.inseresim = 1
            self.formataInsereEstoque()
        if self.crudCombobox.get() == "Consultar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            if self.deletasim == 1:
                self.apagaDelete()
            self.consultasim = 1
            self.formataConsultaEstoque()
        if self.crudCombobox.get() == "Atualizar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.deletasim == 1:
                self.apagaDelete()
            self.atualizasim = 1
            self.atualizaEstoque()
        if self.crudCombobox.get() == "Deletar":
            if self.inseresim == 1:
                self.apagaInsercao()
            if self.consultasim == 1:
                self.apagaConsulta()
            if self.atualizasim == 1:
                self.apagaAtualiza()
            self.deletasim = 1
            self.deletaEstoque()

    #---------------------------------------------------Insere Estoque------------------------------------------------------#
    # Formata a tela de Estoque
    def formataInsereEstoque(self):
        #---------------------------------------------------Frame - Insere data e refeições------------------------------------------------------#    
        # Cria um frame para a entrada de refeições e data
        self.insereframe = LabelFrame(self.telaEstoque, text = "Insira o Estoque", padx=10)
        self.insereframe.place(relx=0.5, rely=0.2, anchor="n")

        # Cria e posiciona a label
        lb1 = Label(self.insereframe, text="Local: ", width=8)
        lb1.grid(row=0, column=1, pady=10, sticky=E)
        
        # Cria e posiciona a combobox que irá filtrar o local
        self.localCombobox = ttk.Combobox(self.insereframe, value=self.opcaoLocais, width=10, state="readonly")
        self.localCombobox.current(0)
        self.localCombobox.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # Cria um textbox para a entrada da Estoque
        self.textboxInsere = scrolledtext.ScrolledText(self.insereframe, height=15, width=70, font=self.fontStyle)
        self.textboxInsere.grid(row=1, column=0, padx=10, pady=10, columnspan=4)
        
        # Cria e posiciona o botão inserir
        self.botaoInserir = Button(self.telaEstoque, image=self.cambotaoInserir, command=self.insereEstoque, bd=0, relief=GROOVE)
        self.botaoInserir.place(relx=0.9, rely=0.9, anchor="n")

        
    def insereEstoque(self):
        self.textEstoque = self.textboxInsere.get("1.0",'end-1c')
        # Verifica se algo escrito antes de salvar no banco de dados
        self.aviso.destroy()
        if self.textEstoque == "":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Caixa de texto vazia!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
        else:
            # Salva todas as informações no banco de dados
            self.bdEstoque.insereDadosEst(str(self.localCombobox.get()), self.textEstoque)
            # Cria e posiciona uma label de aviso
            self.textboxInsere.delete(1.0, 'end')
            self.aviso = Label(self.telaEstoque,text="Estoque registrado!", foreground='green', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
            
    
    def apagaInsercao(self):
        self.insereframe.destroy()
        self.botaoInserir.destroy()
        self.aviso.destroy()
    #---------------------------------------------------FIM - Insere Estoque------------------------------------------------------#    
    
    
    #---------------------------------------------------Consulta Estoque------------------------------------------------------#     
    # Exibe as Estoque na tela
    def formataConsultaEstoque(self):
        #---------------------------------------------------Frame - Consulta Estoque------------------------------------------------------# 
        # Cria um frame para exibir detalhes de uma Estoque
        self.consultaframe = LabelFrame(self.telaEstoque, text = "Informações do estoque", padx=10)
        self.consultaframe.place(relx=0.5, rely=0.25, anchor="n")

        # Cria e posiciona Labels
        lb2 = Label(self.consultaframe, text="Local: ", width=8)
        lb2.grid(row=0, column=0, padx=0, sticky=E)
        
        # Cria e posiciona a combobox que irá filtrar o local
        self.localCombobox = ttk.Combobox(self.consultaframe, value=self.opcaoLocais, width=10, state="readonly")
        self.localCombobox.current(0)
        self.localCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria um textbox para exibir Estoque
        self.textboxConsulta = scrolledtext.ScrolledText(self.consultaframe, height=15, width=50, font=self.fontStyle)
        self.textboxConsulta.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxConsulta.bind("<Key>", lambda e: "break")
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.telaEstoque, command=self.consultaEst, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.place(relx=0.9, rely=0.9, anchor="n")
    
    # Busca o Estoque no banco de dados
    def consultaEst(self):
        self.dadosLidosEstoque = self.bdEstoque.leDadosEst() 
        self.textboxConsulta.delete(1.0, 'end')
        cont=0
        for x in self.dadosLidosEstoque:
            if (x[0] == str(self.localCombobox.get())):
                cont+=1
                self.textboxConsulta.insert(INSERT, str(x[1]))
        
        if(cont>=1):
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaEstoque,text="Processo de consulta realizado com sucesso!", foreground='green', font=12)
            self.aviso.place(relx=0.35, rely=0.9)
        else:
            # Cria e posiciona uma label de aviso
            self.aviso.destroy()
            self.aviso = Label(self.telaEstoque,text="Não foram encontrados dados para esse local!", foreground='red', font=12)
            self.aviso.place(relx=0.35, rely=0.9)    
            
    def apagaConsulta(self):
        self.consultaframe.destroy()
        self.botaoConsultar.destroy()
        self.aviso.destroy()
            
    #---------------------------------------------------Fim - Consulta Estoque------------------------------------------------------#     
        
        
    #---------------------------------------------------Atualiza Estoque------------------------------------------------------#    
    # Exibe o Estoque na tela
    def atualizaEstoque(self):
        #---------------------------------------------------Frame - Seleciona Data------------------------------------------------------#
        # Cria um frame de seleção de Locais e ids
        self.localFrame = LabelFrame(self.telaEstoque, text = "Selecione um Local", padx=10)
        self.localFrame.place(relx=0.3, rely=0.25, anchor="n")    
            
        # Cria e posiciona Labels
        lb3 = Label(self.localFrame, text="Local: ", width=8)
        lb3.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar o local
        self.localCombobox = ttk.Combobox(self.localFrame, value=self.opcaoLocais, width=10, state="readonly")
        self.localCombobox.current(0)
        self.localCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.localFrame, command=self.consAtualizaEst, image=self.cambotaoConsulta, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
        #---------------------------------------------------Frame - Atualiza Estoque------------------------------------------------------#
        # Cria um frame para exibir detalhes do Estoque
        self.atualizaframe = LabelFrame(self.telaEstoque, text = "Edição de Estoque", padx=10)
        self.atualizaframe.place(relx=0.7, rely=0.25, anchor="n")
        
        # Cria um textbox para exibir Estoque
        self.textboxAtualiza = scrolledtext.ScrolledText(self.atualizaframe, height=15, width=50, font=self.fontStyle)
        self.textboxAtualiza.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        #Cria botão atualizar mas NÃO O POSICIONA
        self.botaoAtualizar = Button(self.telaEstoque, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        
    
    # Busca as reclamações do Locai no banco de dados
    def consAtualizaEst(self):
        self.dadosLidosEstoque = self.bdEstoque.leDadosEst()
        cont=0
        self.textboxAtualiza.delete(1.0, 'end')
        for x in self.dadosLidosEstoque:
            if x[0] == self.localCombobox.get():
                cont+=1
                self.textboxAtualiza.insert(INSERT, x[1])
                break
        
        if(cont==0):
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Não foi encontrado Estoque para essa Data!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            
        # Cria e posiciona o botão Atualizar
        self.botaoAtualizar = Button(self.telaEstoque, command=lambda: self.atualizaCarBD(cont), image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        self.botaoAtualizar.place(relx=0.9, rely=0.9, anchor="n")   
    
    # Método que atualiza a Estoque do Locai no banco de dados
    def atualizaCarBD(self, cont):
        self.aviso.destroy()
        if(cont==0):
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Esse local não pode ser atualizado, tente reconsulta-lo!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            return
        if self.textboxAtualiza.get(1.0, END) == "":
            self.aviso.destroy()
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Caixa de refeições vazia, tente novamente!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
        else:
            self.aviso.destroy()
            self.bdEstoque.atualizaEst(str(self.localCombobox.get()), str(self.textboxAtualiza.get(1.0, END)))
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Estoque atualizado no banco de dados!", foreground='Green', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
            
    def apagaAtualiza(self):
        self.atualizaframe.destroy()
        self.localFrame.destroy()
        self.botaoAtualizar.destroy()
        self.aviso.destroy()
        
        
    #---------------------------------------------------Deleta reclamações------------------------------------------------------#     
    # Deleta reclamações
    def deletaEstoque(self):
            
        #---------------------------------------------------Frame - Seleciona Locais------------------------------------------------------#
        # Cria um frame de seleção de Locais
        self.localFrame = LabelFrame(self.telaEstoque, text = "Selecione um Local", padx=10)
        self.localFrame.place(relx=0.5, rely=0.4, anchor="n")    
            
        # Cria e posiciona Labels
        lb4 = Label(self.localFrame, text="Local: ", width=8)
        lb4.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar o local
        self.localCombobox = ttk.Combobox(self.localFrame, value=self.opcaoLocais, width=10, state="readonly")
        self.localCombobox.current(0)
        self.localCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoDeletar = Button(self.localFrame, command=self.deletaEstBD, image=self.cambotaoDeletar, bd=0, relief=GROOVE)
        self.botaoDeletar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
    # Deleta o Estoque daquela data do banco de dados
    def deletaEstBD(self):
        self.dadosLidosEstoque = self.bdEstoque.leDadosEst()
        contador=0
        for x in self.dadosLidosEstoque:
            if x[0] == self.localCombobox.get():
                self.bdEstoque.deletaEst(str(self.localCombobox.get()))
                contador+=1
        
        self.aviso.destroy()
        if(contador==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Não há nenhuma refeição para essa data no banco de dados!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        else:
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaEstoque,text="Estoque deletado do banco de dados com sucesso!", foreground='Green', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        
        
    # Destroy a tela de Delete
    def apagaDelete(self):
        self.localFrame.destroy()
        self.aviso.destroy()

    #---------------------------------------------------Funções Auxiliares------------------------------------------------------# 
    
    # Método que apaga a janela atual
    def ApagaTelaEstoque(self):
        self.telaEstoque.destroy()
        
'''
OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.telaEstoque.mainloop()

x11 = ContEstoque()
x11.selecionaCRUDEstoque()
''' 

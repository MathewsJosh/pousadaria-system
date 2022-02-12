from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont
from datetime import datetime

# Importações de outras classes locais
from BD_pousadaria import *

#Variaveis Globais
tam = "1200x720"
camIco = "Images\Icones\Pousadaria.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class Reclamacao():
    # Inicializadores
    def __init__(self, funcionarioID):
        # Janela
        self.telaReclamacao = 0
        # Auxiliares das conversões de imagem
        self.cambotaoConsReclama = 0
        self.cambotaoInserir = 0
        self.cambotaoProximo = 0
        self.cambotaoVoltar = 0
        self.cambotaoSelecionar = 0
        self.cambotaoAtualizar = 0
        self.cambotaoDeletar = 0
        # Botões
        self.botaoConsReclamacao = 0
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
        self.clienteframe = 0
        self.telaframe = 0
        # Comboboxes
        self.crudCombobox = 0
        self.clienteCombobox = 0
        self.idCombobox = 0
        self.statusCombobox = 0
        # Textboxes
        self.textboxInsere = 0
        self.textboxAtualiza = 0
        self.textboxConsulta = 0
        # Instancia de reclamacoes
        self.rec = BD_ReclamaSugest() 
        self.bdclientes = BD_cadCliente()
        # Armazena BD
        self.nomecliente = []
        # Booleanos
        self.inseresim = 0
        self.consultasim = 0
        self.atualizasim = 0
        self.deletasim = 0
        # Dados retornados do banco de dados
        self.dadosLidosRec = 0
        # Outros
        self.aviso = 0
        self.fontStyle = 0
        self.textReclamacao = 0
        self.opcoesClientes = []
        self.IDsRecs = []
        self.opcoesFiltros = ["Inserir", "Consultar", "Atualizar", "Deletar"]
        self.opcoesStatus = ["Resolvida", "Em aberto", "Outros"]
        self.funcionarioID = funcionarioID

        

    # Método de seleção do Crud reclamações
    def selecionaCRUDReclamacao(self):
        # Cria uma janela e define suas principais configurações
        self.telaReclamacao = Toplevel()
        self.telaReclamacao.title("Recepção - Reclamações, Sugestões ou Avaliações")
        self.telaReclamacao.wm_iconbitmap(camIco)
        self.telaReclamacao.focus_force()
        self.telaReclamacao.geometry(tam)
        
        # Converte as imagens em PhotoImage para serem usadas como botões
        self.cambotaoConsReclama = PhotoImage(file="Images\Botões\inicio_consultar.png", master=self.telaReclamacao)
        self.cambotaoInserir = PhotoImage(file="Images\Botões\inicio_inserir.png", master=self.telaReclamacao)
        self.cambotaoProximo = PhotoImage(file="Images\Botões\inicio_proximo.png", master=self.telaReclamacao)
        self.cambotaoVoltar = PhotoImage(file="Images\Botões\inicio_voltar.png", master=self.telaReclamacao)
        self.cambotaoSelecionar = PhotoImage(file="Images\Botões\inicio_selecionar.png", master=self.telaReclamacao)
        self.cambotaoAtualizar = PhotoImage(file="Images\Botões\inicio_atualizar.png", master=self.telaReclamacao)
        self.cambotaoDeletar = PhotoImage(file="Images\Botões\inicio_deletar.png", master=self.telaReclamacao)
        
        # Define as fontes para caixas de texto
        fontfamilylist = list(tkFont.families())
        fontindex = 20
        self.fontStyle = tkFont.Font(family=fontfamilylist[fontindex])
        
        #---------------------------------------------------Frame - Filtro de reclamações------------------------------------------------------#
        # Cria um frame para a entrada de filtros
        self.filtroframe = LabelFrame(self.telaReclamacao, text = "Filtragem de funções", padx=10)
        self.filtroframe.place(relx=0.45, rely=0.05, anchor="n")
        
        # Cria e posiciona Labels
        lb1 = Label(self.filtroframe, text="Operação: ")
        lb1.grid(row=0, column=0, padx=5, sticky=W)
        
        # Cria e posiciona a combobox de escolha do CRUD
        
        self.crudCombobox = ttk.Combobox(self.filtroframe, value=self.opcoesFiltros, width=10, state="readonly")
        self.crudCombobox.current(0)
        self.crudCombobox.grid(row=0, column=1, sticky=E, padx=5, pady=10)
        
        #---------------------------------------------------Fim------------------------------------------------------#
        
        # Cria e posiciona botões
        self.botaoProximo = Button(self.telaReclamacao, command=self.controleCRUD, image=self.cambotaoProximo, bd=0, relief=GROOVE)
        self.botaoProximo.place(relx=0.6, rely=0.07, anchor="n")
        
        #, command= tela anterior (menu)
        self.botaoVoltar = Button(self.telaReclamacao, image=self.cambotaoVoltar, command = self.ApagaTelaReclamacao, bd=0, relief=GROOVE)
        self.botaoVoltar.place(relx=0.1, rely=0.9, anchor="n")
        
        # Cria e posiciona uma label de aviso
        self.aviso = Label(self.telaReclamacao, foreground='red', font=self.fontStyle)
        self.aviso.place(relx=0.5, rely=0.9)
             
        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.telaReclamacao.mainloop()
    
    # Método de controle de opções de filtragem do crud reclamações
    def controleCRUD(self):
        if len(self.nomecliente) == 0:
            for nome in self.bdclientes.leNomeCliente():
                self.nomecliente.append(nome[0])

        if self.aviso!= 0:
            self.aviso.destroy()
        self.opcoesClientes = []
        self.auxOpcClientes()
        if self.crudCombobox.get() == "Inserir":
            self.inseresim = 1
            self.formataInsereReclamacao()
        if self.crudCombobox.get() == "Consultar":
            self.consultasim = 1
            self.formataConsultaReclamacao()
        if self.crudCombobox.get() == "Atualizar":
            self.atualizasim = 1
            self.atualizaReclamacao()
        if self.crudCombobox.get() == "Deletar":
            self.deletasim = 1
            self.deletaReclamacao()

    #---------------------------------------------------Insere reclamações------------------------------------------------------#
    # Formata a tela de reclamação
    def formataInsereReclamacao(self):
        self.inseresim = 1
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.atualizasim == 1:
            self.apagaAtualiza()
        if self.deletasim == 1:
            self.apagaDelete()
        
        # Cria um frame para a entrada de reclamacões
        self.insereframe = LabelFrame(self.telaReclamacao, text = "Insira a reclamação", padx=10)
        self.insereframe.place(relx=0.35, rely=0.25, anchor="n")

        # Cria um textbox para a entrada da reclamação
        self.textboxInsere = scrolledtext.ScrolledText(self.insereframe, height=15, width=70, font=self.fontStyle)
        self.textboxInsere.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        
        # Cria e posiciona Labels
        lb2 = Label(self.insereframe, text="Cliente: ", width=8)
        lb3 = Label(self.insereframe, text="Status: ", width=8)
        lb2.grid(row=1, column=0, padx=0, sticky=E)
        lb3.grid(row=1, column=2, padx=0, sticky=E)
        
        # Cria e posiciona a combobox que irá permitir filtrar os quartos
        self.clienteCombobox = ttk.Combobox(self.insereframe, value=self.nomecliente, width=15, state="readonly")
        self.clienteCombobox.current(0)
        self.clienteCombobox.grid(row=1, column=1, padx=5, pady=10, sticky=W, )
        
        # Cria e posiciona a combobox de escolha do status da reclamação
        
        self.statusCombobox = ttk.Combobox(self.insereframe, value=self.opcoesStatus, width=10, state="readonly")
        self.statusCombobox.current(0)
        self.statusCombobox.grid(row=1, column=3, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão inserir
        self.botaoInserir = Button(self.telaReclamacao, image=self.cambotaoInserir, command=self.insereReclamacao, bd=0, relief=GROOVE)
        self.botaoInserir.place(relx=0.8, rely=0.5, anchor="n")

    # Método que salva a reclamação no banco de dados
    def insereReclamacao(self):
        self.textReclamacao = self.textboxInsere.get("1.0",'end-1c')
        # Verifica se algo escrito antes de salvar no banco de dados
        if self.aviso!= 0:
            self.aviso.destroy()
        if self.textReclamacao == "":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Caixa de texto vazia!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
        else:
            # Pega o timestamp do momento que o botão é clicado
            dateTimeObj = datetime.now()
            ts = dateTimeObj.strftime("%d/%m/%Y (%H:%M:%S)")
            # Salva todas as informações no banco de dados
            clienteID = self.bdclientes.consultaId(self.clienteCombobox.get())[0][0]
            self.rec.insereDadosRec(clienteID, self.textReclamacao, ts, self.statusCombobox.get())
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Reclamação/Sugestão registrada!", foreground='green', font=12)
            self.aviso.place(relx=0.4, rely=0.9)
            
    # Método que destroy os frames de Inserção
    def apagaInsercao(self):
        self.insereframe.destroy()
        self.botaoInserir.destroy()
        self.aviso.destroy()
    #---------------------------------------------------FIM - Insere reclamações------------------------------------------------------#    
    
    
    #--------------------------------------------------- Consulta reclamações------------------------------------------------------#     
    # Exibe as reclamações na tela
    def formataConsultaReclamacao(self):
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.atualizasim == 1:
            self.apagaAtualiza()
        if self.deletasim == 1:
            self.apagaDelete()
            
        # Cria um frame para exibir detalhes de uma reclamação
        self.consultaframe = LabelFrame(self.telaReclamacao, text = "Consulta de reclamações", padx=10)
        self.consultaframe.place(relx=0.5, rely=0.25, anchor="n")

        # Cria e posiciona Labels
        lb4 = Label(self.consultaframe, text="Cliente: ", width=8)
        lb4.grid(row=0, column=0, padx=0, sticky=E)
        
        
        # Cria e posiciona a combobox que irá permitir filtrar os clientes
        self.clienteCombobox = ttk.Combobox(self.consultaframe, value=self.nomecliente, width=15, state="readonly")
        self.clienteCombobox.current(0)
        self.clienteCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria um textbox para exibir reclamação
        self.textboxConsulta = scrolledtext.ScrolledText(self.consultaframe, height=15, width=50, font=self.fontStyle)
        self.textboxConsulta.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        # Função necessária para não permitir que o textbox seja editado - Somente leitura
        self.textboxConsulta.bind("<Key>", lambda e: "break")
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.telaReclamacao, command=self.consultaRec, image=self.cambotaoConsReclama, bd=0, relief=GROOVE)
        self.botaoConsultar.place(relx=0.9, rely=0.9, anchor="n")
    
    # Busca as reclamações do cliente no banco de dados
    def consultaRec(self):
        clienteID = self.bdclientes.consultaId(self.clienteCombobox.get())[0][0]
        self.dadosLidosRec = self.rec.leDadosRecIDCliente(clienteID)
        cont=0
        if self.aviso!= 0:
            self.aviso.destroy()

        self.textboxConsulta.delete(1.0, 'end')
        for x in self.dadosLidosRec:
            if x[1] == clienteID:
                cont+=1
                self.textboxConsulta.insert(INSERT, "IdReclamação: " + str(x[0]) + "\nCliente: " + str(x[1]) + "\nStatus: " + x[4] + "\nData e hora: " + x[3] + "\n\nMensagem: " + x[2] + "\n\n====================X====================\n")
        
        if(cont>=1):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Processo de consulta realizado com sucesso!", foreground='green', font=12)
            self.aviso.place(relx=0.35, rely=0.9)
        else:
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Não foi encontrada reclamação para esse cliente!", foreground='red', font=12)
            self.aviso.place(relx=0.35, rely=0.9)    
    
    # Método que destroy os frames de consulta
    def apagaConsulta(self):
        self.consultaframe.destroy()
        self.botaoConsultar.destroy()
        self.aviso.destroy()
            
    #---------------------------------------------------Fim - Consulta reclamações------------------------------------------------------#     
        
        
    #---------------------------------------------------Atualiza reclamações------------------------------------------------------#    
    # Exibe as reclamações na tela
    def atualizaReclamacao(self):
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.deletasim == 1:
            self.apagaDelete()
            
        #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
        # Cria um frame de seleção de clientes e ids
        self.clienteframe = LabelFrame(self.telaReclamacao, text = "Selecione um cliente", padx=10)
        self.clienteframe.place(relx=0.3, rely=0.25, anchor="n")    
            
        # Cria e posiciona Labels
        lb5 = Label(self.clienteframe, text="Cliente: ", width=8)
        lb5.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar os clientes
        self.clienteCombobox = ttk.Combobox(self.clienteframe, value=self.nomecliente, width=15, state="readonly")
        self.clienteCombobox.current(0)
        self.clienteCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoConsultar = Button(self.clienteframe, command=self.consultaRecAtualiza, image=self.cambotaoConsReclama, bd=0, relief=GROOVE)
        self.botaoConsultar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
        
        #---------------------------------------------------Frame - Atualiza Reclamações------------------------------------------------------#
        # Cria um frame para exibir detalhes de uma reclamação
        self.atualizaframe = LabelFrame(self.telaReclamacao, text = "Atualiza reclamação", padx=10)
        self.atualizaframe.place(relx=0.7, rely=0.25, anchor="n")
        
        # Cria e posiciona Labels de statusCombobox
        lb5 = Label(self.atualizaframe, text="Status: ", width=8)
        lb5.grid(row=0, column=0, padx=0, sticky=E)
        
        # Cria e posiciona a combobox de escolha do status da reclamação
        self.statusCombobox = ttk.Combobox(self.atualizaframe, value=self.opcoesStatus, width=10, state="readonly")
        self.statusCombobox.current(0)
        self.statusCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria um textbox para exibir reclamação
        self.textboxAtualiza = scrolledtext.ScrolledText(self.atualizaframe, height=15, width=50, font=self.fontStyle)
        self.textboxAtualiza.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        #Cria botão atualizar mas NÃO O POSICIONA
        self.botaoAtualizar = Button(self.telaReclamacao, command=self.atualizaRecBD, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        
    
    # Busca as reclamações do cliente no banco de dados
    def consultaRecAtualiza(self):
        clienteID = self.bdclientes.consultaId(self.clienteCombobox.get())[0][0]
        self.dadosLidosRec = self.rec.leDadosRecIDCliente(clienteID)
        #self.dadosLidosRec = self.rec.leDadosRec()
        cont=0
        self.textboxAtualiza.delete(1.0, 'end')
        for x in self.dadosLidosRec:
            if x[1] == clienteID:
                cont+=1
                self.textboxAtualiza.insert(INSERT, x[2])
                #self.textboxAtualiza.insert(INSERT, "IdReclamação: " + str(x[0]) + "\nCliente: " + str(x[1]) + "\nStatus: " + x[4] + "\nData e hora: " + x[3] + "\n\nMensagem: " + x[2] + "\n\n====================X====================\n")

                #break
        
        if(cont==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Não foi encontrada reclamação para esse cliente!", foreground='red', font=12)
            self.aviso.place(relx=0.35, rely=0.9) 
            
        # Cria e posiciona o botão Atualizar
        self.botaoAtualizar = Button(self.telaReclamacao, command=self.atualizaRecBD, image=self.cambotaoAtualizar, bd=0, relief=GROOVE)
        self.botaoAtualizar.place(relx=0.9, rely=0.9, anchor="n")   
    
    # Método que atualiza a reclamação do cliente no banco de dados
    def atualizaRecBD(self):
        if self.aviso!= 0:
            self.aviso.destroy()
        clienteID = self.bdclientes.consultaId(self.clienteCombobox.get())[0][0]
        if self.textboxAtualiza.get(1.0, END)=="":
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Caixa de reclamação vazia, tente novamente!", foreground='red', font=12)
            self.aviso.place(relx=0.3, rely=0.9) 
        else:
            dateTimeObj = datetime.now()
            ts = dateTimeObj.strftime("%d/%m/%Y (%H:%M:%S)")
            self.rec.atualizaRec(clienteID, str(self.statusCombobox.get()), ts, str(self.textboxAtualiza.get(1.0, END)))
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Reclamação atualizada no banco de dados!", foreground='Green', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
    
    # Método que destroy os frames de atualização
    def apagaAtualiza(self):
        self.atualizaframe.destroy()
        self.clienteframe.destroy()
        self.botaoAtualizar.destroy()
        self.aviso.destroy()
        
        
    #---------------------------------------------------Deleta reclamações------------------------------------------------------#     
    # Deleta reclamações
    def deletaReclamacao(self):
        self.deletasim == 1
        # Apaga outras telas que ja foram criadas
        if self.inseresim == 1:
            self.apagaInsercao()
        if self.consultasim == 1:
            self.apagaConsulta()
        if self.atualizasim == 1:
            self.apagaAtualiza()
            
        #---------------------------------------------------Frame - Seleciona Cliente------------------------------------------------------#
        # Cria um frame de seleção de clientes e ids
        self.clienteframe = LabelFrame(self.telaReclamacao, text = "Selecione um cliente", padx=10)
        self.clienteframe.place(relx=0.5, rely=0.4, anchor="n")    
            
        # Cria e posiciona Labels
        lb6 = Label(self.clienteframe, text="Cliente: ", width=8)
        lb6.grid(row=0, column=0, padx=0, sticky=E) 

        # Cria e posiciona a combobox que irá filtrar os clientes
        self.clienteCombobox = ttk.Combobox(self.clienteframe, value=self.nomecliente, width=15, state="readonly")
        self.clienteCombobox.current(0)
        self.clienteCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        
        # Cria e posiciona o botão Consultar
        self.botaoDeletar = Button(self.clienteframe, command=self.deletaRecBD, image=self.cambotaoDeletar, bd=0, relief=GROOVE)
        self.botaoDeletar.grid(row=1, column=0, padx=5, pady= 10, columnspan = 2)
    
    # Deleta a reclamação do cliente do banco de dados
    def deletaRecBD(self):
        if self.aviso!= 0:
            self.aviso.destroy()
        clienteID = self.bdclientes.consultaId(self.clienteCombobox.get())[0][0]
        self.dadosLidosRec = self.rec.leDadosRecIDCliente(clienteID)
        contador=0
        for x in self.dadosLidosRec:
            if x[1] == clienteID:
                self.rec.deletaRec(clienteID)
                contador+=1
        
        if(contador==0):
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Não há nenhuma reclamação desse cliente no banco de dados!", foreground='red', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
        else:
            # Cria e posiciona uma label de aviso
            self.aviso = Label(self.telaReclamacao,text="Reclamação do cliente deletada do banco de dados com sucesso!", foreground='Green', font=12)
            self.aviso.place(relx=0.4, rely=0.9) 
    
    # Destroy a tela de Delete
    def apagaDelete(self):
        self.clienteframe.destroy()
        self.aviso.destroy()
    

    #---------------------------------------------------Funções Auxiliares------------------------------------------------------# 
    # Método que atualiza as opções de nomes de clientes
    def auxOpcClientes(self):
        if self.aviso!= 0:
            self.aviso.destroy()
        dadosLidosRec = self.rec.leDadosRec()
        for x in dadosLidosRec:
            self.opcoesClientes.append(x[1])
        #.split(" ")

    # Método que apaga a janela atual
    def ApagaTelaReclamacao(self):
        self.telaReclamacao.destroy()

'''
#OBS: Para testar uma tela especifica, coloque esse comando ao final da função "definidora" daquela tela
# Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
#self.tela_inicial.mainloop()
'''
x9 = Reclamacao(1)
x9.selecionaCRUDReclamacao()


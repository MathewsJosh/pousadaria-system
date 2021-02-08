from tkinter import *
from tkinter import ttk
from BD_cadfuncionario import *

'''
import sys
sys.path.append('../')

#https://qastack.com.br/programming/4383571/importing-files-from-different-folder
'''

#Variaveis Globais
tam = "800x600"
camIco = "Icones\Pousadaria.ico"

class cadastrarWindow():
    # Construtor da Classe
    def __init__(self):
        # Janela
        self.cadastrarJanela = 0
        # Auxiliares das conversões de imagem
        self.camCadastrarButton = 0
        self.camVoltarButton = 0
        # Entradas de dados
        self.nomeEntry = 0
        self.cpfEntry = 0
        self.funcaoEntry = 0
        self.salarioEntry = 0
        self.loginEntry = 0
        self.senhaEntry = 0
        self.AutorizacaoEntry = 0
        # Frames
        self.cadastrarFrame = 0
        # Outros
        self.aviso = 0
        self.botaoCadastrar = 0
        
        
    # Criar uma janela sem valores
    def cadastrarTela(self):
        self.formataTelaCadastro()
        
        # Cria um botão Cadastrar nessa tela e verifica se é possivel cadastrar o usuario
        self.botaoCadastrar = Button(self.cadastrarJanela, text="Cadastrar!", command=self.cadastrarMetodo, image=self.camCadastrarButton, bd=0, relief=GROOVE)
        self.botaoCadastrar.place(relx=0.5, rely=0.8, anchor="n")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.cadastrarJanela.mainloop()

    def cadastrarMetodo(self):
        # Apaga qualquer aviso anterior
        self.aviso.destroy()
        self.aviso.forget()
        
        if self.verificaCampos():
            # Avisa que deu erro ao cadastrar
            self.aviso = Label(self.cadastrarJanela, text="Existem campos vazios, tente novamente!", foreground='red', font=('Helvetica', 10, 'bold'))
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            #return 0
        elif not leAutorizacao(self.AutorizacaoEntry.get()):
            # Avisa que o cadastro deu errado
            self.aviso = Label(self.cadastrarJanela, text="Erro ao realizar o cadastro, verifique o codigo de autorização", foreground='red', font=('Helvetica', 10, 'bold'))
            self.AutorizacaoEntry.delete(0, 'end')
            self.AutorizacaoEntry.focus_force()
            self.aviso.place(relx=0.5, rely=0.7, anchor="n")
            #return 0
        else:
            # Adiciona os dados inseridos ao banco de dados
            entradaDados(self.nomeEntry.get(), self.cpfEntry.get(), self.funcaoEntry.get(), self.salarioEntry.get(), self.loginEntry.get(), self.senhaEntry.get(), self.AutorizacaoEntry.get())

            # Avisa que o cadastro deu certo
            self.aviso = Label(self.cadastrarJanela, text="Cadastro efetuado com sucesso!", foreground='green', font=('Helvetica', 10, 'bold'))
            
            # Altera o botão cadastrar para "Voltar"
            self.botaoCadastrar.destroy()
            self.botaoCadastrar.forget()
            self.botaoCadastrar = Button(self.cadastrarJanela, command=self.destroiTela, image=self.camVoltarButton, bd=0, relief=GROOVE)
            self.botaoCadastrar.place(relx=0.5, rely=0.8, anchor="n")
            
            
            ######self.cadastrarJanela.mainloop()
        
        # Posiciona a label de aviso
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")

    def formataTelaCadastro(self):
        # Cria uma janela e define suas principais configurações
        self.cadastrarJanela = Tk()
        self.cadastrarJanela.title("Cadastre-se no sistema")
        self.cadastrarJanela.wm_iconbitmap(camIco)
        self.cadastrarJanela.focus_force()
        self.cadastrarJanela.geometry(tam)

        #---------------------------------------------------Frame - Cadastro de Funcionário------------------------------------------------------#
        # Cria o Frame de cadastro
        self.cadastrarFrame = LabelFrame(self.cadastrarJanela, text = "Insira os dados do Funcionário", padx=20, pady=20)
        self.cadastrarFrame.place(relx=0.5, rely=0.2, anchor="n")

        # Cria os campos necessários para o cadastro
        lb1 = Label(self.cadastrarFrame, text="Nome: ")
        lb2 = Label(self.cadastrarFrame, text="CPF:")
        lb3 = Label(self.cadastrarFrame, text="Função:")
        lb4 = Label(self.cadastrarFrame, text="Salario:")
        lb5 = Label(self.cadastrarFrame, text="Login:")
        lb6 = Label(self.cadastrarFrame, text="Senha:")
        lb7 = Label(self.cadastrarFrame, text="Autorização: ")
        self.nomeEntry = Entry(self.cadastrarFrame, width=20)
        self.cpfEntry = Entry(self.cadastrarFrame, width=20)
        self.salarioEntry = Entry(self.cadastrarFrame, width=20)
        self.loginEntry = Entry(self.cadastrarFrame, width=20)
        self.senhaEntry = Entry(self.cadastrarFrame, width=20, show='*')
        self.AutorizacaoEntry = Entry(self.cadastrarFrame, width=20, show='*')

        # Posiciona as Labels e entradas de dados
        lb1.grid(row=0, column=0, pady=5, sticky=W)
        lb2.grid(row=1, column=0, pady=5, sticky=W)
        lb3.grid(row=2, column=0, pady=5, sticky=W)
        lb4.grid(row=3, column=0, pady=5, sticky=W)
        lb5.grid(row=4, column=0, pady=5, sticky=W)
        lb6.grid(row=5, column=0, pady=5, sticky=W)
        lb7.grid(row=6, column=0, pady=5, sticky=W)
        self.nomeEntry.grid(row=0, column=1, pady=5, sticky=E)
        self.cpfEntry.grid(row=1, column=1, pady=5, sticky=E)
        self.salarioEntry.grid(row=3, column=1, pady=5, sticky=E)
        self.loginEntry.grid(row=4, column=1, pady=5, sticky=E)
        self.senhaEntry.grid(row=5, column=1, pady=5, sticky=E)
        self.AutorizacaoEntry.grid(row=6, column=1, pady=5, sticky=E)

        # Cria e posiciona uma Label de Aviso
        self.aviso = Label()
        self.aviso.place(relx=0.5, rely=0.7, anchor="n")

        # Cria e posiciona a combobox de função - Irá definir o nível de acesso do funcionário ao sistema
        opcoes = ["1 - Gerência", "2 - Recepção", "3 - Limpeza", "4 - Cozinha"]
        self.funcaoEntry = ttk.Combobox(self.cadastrarFrame, value=opcoes, width=17, state="readonly")
        self.funcaoEntry.current(0)
        self.funcaoEntry.grid(row=2, column=1, pady=5, sticky=E)

        # Converte os pngs dos botões para imagem
        self.camCadastrarButton = PhotoImage(file="Botões\Tela inicial//button_cadastrarTI.png", master=self.cadastrarJanela)
        self.camVoltarButton = PhotoImage(file="Botões\Tela inicial//button_voltarTI.png", master=self.cadastrarJanela)



    # Verifica se uma ou mais entradas de dados estão vazias
    def verificaCampos(self):
        if self.nomeEntry.get() == "" or self.cpfEntry.get() == "" or self.funcaoEntry.get() == "" or self.salarioEntry.get() == "" or self.loginEntry.get() == "" or self.senhaEntry.get() == "" or self.AutorizacaoEntry.get() == "":
            return True
        return False



    # Destroi a janela atual
    def destroiTela(self):
        self.cadastrarJanela.destroy()

x2 = cadastrarWindow()
x2.cadastrarTela()
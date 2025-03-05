from tkinter import * #Importa todos os modulos do Tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk # Importa o módulo de widgets temáticos tkinter
from Database import Database #Importa a classe DataBase do módulo DataBase

#Criar a janela

janela = Tk()
janela.title("CA Solutions - Painel de acesso")
janela.geometry("600x300")
janela.configure(background='white')
janela.resizable(width=False,height=False) #Garante que o usuário não consiga alterar o tamanho da tela
janela.attributes("-alpha",0.9) #Define a transparência da tela 0.0 até 1.0)


#janela.iconbitmap(default=) #Define o icon da tela


logo = PhotoImage (file = 'icon/Caio Aires.png') #Define o icon da tela

LeftFrame = Frame(janela,width=200,height=300,bg='MIDNIGHTBLUE',relief='raise')
LeftFrame.pack(side=LEFT) #Posiciona o frame a esquerda

RightFrame = Frame(janela,width=395,height=300,bg='MIDNIGHTBLUE',relief='raise')
RightFrame.pack(side=RIGHT) #Posiciona o frame a esquerda

#Adicionar a logo
LogoLabel = Label(LeftFrame,image=logo, bg="MIDNIGHTBLUE") #Cria um logo posicionado à esquerda e chama a imagem do logo
LogoLabel.place(x=50,y=100)

#Adicionar campos de usuário e senha
UserLabel = Label(RightFrame,text="Usuário",font=("Century Gothic",20),bg='MIDNIGHTBLUE',fg='white')
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=120,y=115)

SenhaLabel = Label(RightFrame,text="Senha",font=("Century Gothic",20),bg='MIDNIGHTBLUE',fg='white')
SenhaLabel.place(x=5,y=150)

SenhaEntry = ttk.Entry(RightFrame,width=30,show="°")
SenhaEntry.place(x=120,y=165)

#Função de login
def Login():
    #Obtém valor do campo preechido
    user = UserEntry.get() 
    senha = SenhaEntry.get()
    
    #Conectar ao banco de dados
    db = Database() #Cria uma instância da classe Database
    db.cursor.execute("""
    SELECT * FROM usuario1
    WHERE usuario = %s AND senha =%s""",(user,senha))                   
    VerifyLogin = db.cursor.fetchone() #Obtém  resultado da consulta

    #Verifica se o usuário já foi encontrado
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN",message="Acesso confirmado. Bem vindo!") #Mensagem de login bem sucessedido
    else:
        messagebox.showerror(title="INFO LOGIN",message="Acesso negado. Verifique se está cadatrado no sistema") #Mensagem de erro

#Criando os botões
LoginButton = ttk.Button(RightFrame,text="Login",width=15,command=Login)
LoginButton.place(x=80,y=225)

#Função para registrar novo usuário
def Registrar():
    #Removendo botões de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #Inserindo widgets de cadastro
    NameLabel = Label(RightFrame,text="Nome:",font=("Century Gothic",20),bg= "MIDNIGHTBLUE",fg= "White")
    NameLabel.place(x=5,y=5)

    NameEntry = ttk.Entry(RightFrame,width=30)
    NameEntry.place(x=120,y=20)

    EmailLabel = Label(RightFrame,text="Email:",font=("Century Gothic",20),bg= "MIDNIGHTBLUE",fg= "White")
    EmailLabel.place(x=5,y=40)

    EmailEntry = ttk.Entry(RightFrame,width= 30)
    EmailEntry.place(x=120,y=55)

    def RegistrarNoBanco():
        #Obtém os valores inseridos nos campos de entrada

        nome = NameEntry.get()
        email = EmailEntry.get()
        usuario = UserEntry.get()
        senha = SenhaEntry.get()

        #Verifica se todos os campos estão preenchidos
        if nome =="" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de registro",message="Preencha todos os campos!")
        else:
            db = Database() #Cria uma instância da classe Database
            db.RegistrarNobanco(nome,email,usuario,senha) #Chama o metódo para registrar no banco de dados
            messagebox.showinfo("Sucesso!","Usuário registrado com sucesso")
            
            #Limpa os campos após os registros
            NameEntry.delete(0,END)
            EmailEntry.delete(0,END)
            UserEntry.delete(0,END)
            SenhaEntry.delete(0,END)

    Register = ttk.Button(RightFrame,text="Registrar",width=15, command= RegistrarNoBanco) #Cria um botão de registro
    Register.place(x=80,y=225) 

    def VoltarLogin():
        #Remove os botões da tela de login
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        VoltarButton.place(x=5000)
    
    #Trazendo de volta os widgets
        LoginButton.place(x=80)
        RegisterButton.place(x=150)
    
    #Criando botão login
    VoltarButton = ttk.Button(RightFrame,text="VOLTAR",width=15,command=VoltarLogin)
    VoltarButton.place(x=220,y=225)

RegisterButton = ttk.Button(RightFrame,text="Registrar",width=15, command= Registrar) #Cria um botão de registro
RegisterButton.place(x=220,y=225)

janela.mainloop()



from tkinter import * #Importa todos os modulos do Tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk # Importa o módulo de widgets temáticos tkinter
from DataBase import DataBase #Importa a classe DataBase do módulo DataBase

#Criar a janela

janela = Tk()
janela.title("CA Solutions - Painel de acesso")
janela.geometry("600x300")
janela.configure(background='white')
janela.resizable(width=False,height=False) #Garante que o usuário não consiga alterar o tamanho da tela
janela.attributes("-alpha,09") #Define a transparência da tela 0.0 até 1.0)


#janela.iconbitmap(default=) #Define o icon da tela


logo = PhotoImage (file = 'icon/Caio Aires.png') #Define o icon da tela

LeftFrame = Frame(janela,width=200,height=300,bg='MIDNIGHTBLUE',relief='raise')
LeftFrame.pack(side=RIGHT) #Posiciona o frame a esquerda

RightFrame = Frame(janela,width=395,height=300,bg='MIDNIGHTBLUE',relief='raise')
RightFrame.pack(side=RIGHT) #Posiciona o frame a esquerda

#Adicionar a logo
LogoLabel = Label(LeftFrame,image=logo, bg="MIDNIGHTBLUE") #Cria um logo posicionado à esquerda e chama a imagem do logo
LogoLabel.place(x=50,y=100)

#Adicionar campos de usuário e senha
UserLabel = Label(RightFrame,text="Usuário: ,",font=("Century Gothic",20),bg='MIDNIGHTBLUE',fg='white')
UserLabel.place(x=5,x=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=120,y=115)

SenhaLabel = Label(RightFrame,text="Senha",font=("Century Gothic",20),bg='MIDNIGHTBLUE',fg='white')
SenhaLabel.place(x=120,y=165)

SenhaEntry = ttk.Entry(RightFrame,width=30,show="°")
SenhaEntry.place(x=120,y=165)

#Função de login
def Login():
    #Obtém valor do campo preechido
    user = UserEntry.get() 
    senha = SenhaEntry.get()
    
    #Conectar ao banco de dados
    db = DataBase() #Cria uma instância da classe DataBase
    db.cursor.execute("SELECT * FROM usuario") 



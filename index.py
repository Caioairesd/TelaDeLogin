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
janela.attributes("-alpha,09") #Define a transparência da tela ()
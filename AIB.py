from tkinter import *
import getpass
import time, json, os
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from dateutil import tz
import webbrowser

e = 'robotfinanceiq@gmail.com'
s = 'botfinance24'

def tela_login():
	janela_login = Tk()
	janela_login.title("AIB - Login")

	editEmail = Entry(janela_login,)
	editSenha = Entry(janela_login, show="*")
	labelEmail = Label(janela_login, text="Email: ")
	labelSenha = Label(janela_login, text="Senha: ")

	btnEntrar = Button(janela_login, text="Entrar",command= lambda: entrar(self, editEmail.get(), editSenha.get()))
	btnCadastro = Button(janela_login, text="Cadastro", command=cadastro)

	labelEmail.place(x=10, y=10)
	labelSenha.place(x=10, y=35)
	editEmail.place(x=60, y=10)
	editSenha.place(x=60, y=35)
	btnEntrar.place(x=10, y=65)
	btnCadastro.place(x=90, y=65)

	janela_login.geometry("250x100+100+100")
	janela_login.resizable(False, False)
	janela_login.mainloop()

def tela_principal():
	tela_principal = Tk()
	tela_principal.title("AIB - Operacional")

	espaço = Label(tela_principal, text="    ")
	labelPorcentagemLugro = Label(tela_principal, text="Porcentagem de lucro: ")
	editPorcentagemLugro = Entry(tela_principal)
	labelEntrada = Label(tela_principal, text="Valor da Entrada: ")
	editEntrada = Entry(tela_principal)
	labelMoeda = Label(tela_principal, text="Moeda: ")
	editMoeda = Entry(tela_principal)

	#espaço.grid(row=0, column=0)
	labelPorcentagemLugro.grid(row=1, column=1)
	editPorcentagemLugro.grid(pady=10, row=1, column=2)
	labelEntrada.grid(row=2, column=1)
	editEntrada.grid(pady=10, row=2, column=2)
	labelMoeda.grid(row=3, column=1)
	editMoeda.grid(pady=10, row=3, column=2)

	tela_principal.geometry("600x300+100+100")
	tela_principal.mainloop()
	pass

def cadastro():
	webbrowser.open("https://iqoption.com/pt/register")
	pass

def entrar(editEmail, editSenha):
	#print(editSenha.get())
	API = IQ_Option(editEmail, editSenha)
	API.connect()
	API.change_balance("PRACTICE")
	#API.set_max_reconnect(5)

	while True:
	    if API.check_connect() == False:
	        print("Erro ao Conectar")
	        API.reconnect()
	    else:
	        print("Conectado com sucesso!")
	        tela_principal()
	        break
	    time.sleep(5)
	pass

#tela_principal()
tela_login()
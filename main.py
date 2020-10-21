from iqoptionapi.stable_api import IQ_Option
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import sys, time, os

janela = Tk()
label = Label(janela, text='AIB - Login')
label.pack()

def tela_operacional(email, senha):
    global janela
    janela.destroy()
    janela = Tk()

    janela.resizable(False,False)
    var1 = "as"
    var2 = "ass"

    def sel():
        selection = "You selected the option " + str(var1.get())
        label.config(text = selection)            

    bg = ImageTk.PhotoImage(file="images/aib.jpg")
    bg_image=Label(janela, image=bg)
    bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    Frame_Main=Frame(janela, bg="white")
    Frame_Main.place(x=60, y=50, height=670, width=830)

    lbl_valorEntrada=Label(Frame_Main,text="Operacional",font=("Goudy old style", 17, "bold"),fg= "black",bg="white")
    lbl_valorEntrada.place(x=90,y=100)

    lbl_valorEntrada=Label(Frame_Main,text="Valor de Entrada: ",font=("Goudy old style", 12, "bold"),fg= "black",bg="white")
    lbl_valorEntrada.place(x=90,y=150)

    txt_valEntrada=Entry(Frame_Main,font=("times new roman",12),bg="snow")
    txt_valEntrada.place(x=300,y=150, width=100,height=35)

    lbl_porcLucro=Label(Frame_Main,text="Porcentagem de lucro: ",font=("Goudy od Style", 12, "bold"),fg= "black",bg="white")
    lbl_porcLucro.place(x=90,y=200)
    txt_porcLucro=Entry(Frame_Main,font=("times new roman",12),bg="snow")
    txt_porcLucro.place(x=300,y=200, width=100,height=35)

    lbl_tipoMoeda=Label(Frame_Main,text="Tipo de Moeda: ",font=("Goudy od Style", 12, "bold"),fg= "black",bg="white")
    lbl_tipoMoeda.place(x=90,y=250)
    txt_tipoMoeda=Entry(Frame_Main,font=("times new roman",12),bg="snow")
    txt_tipoMoeda.place(x=300,y=250, width=100,height=35)
    #txt_tipoMoeda.text("EURUSD")

    lbl_tipoConta=Label(Frame_Main, text="Tipo de Conta", font=("Goudy od Style", 17, "bold"), fg="black", bg="white")
    lbl_tipoConta.place(x=90,y=360)

    treinamento=Radiobutton(Frame_Main, font=("Goudy old style", 12), bg="white", text="Treinamento", variable=var1, value=2, command=sel)
    treinamento.place(x=90 ,y=400, width=120, height=35)

    real=Radiobutton(Frame_Main, font=("Goudy old style", 12), bg="white", text="Real      ", variable=var1, value=1, command=sel)
    real.place(x=90, y=430, width=90, height=35)

    lbl_tipoOperacao=Label(Frame_Main, text="Tipo de Operação", font=("Goudy od Style", 17, "bold"), fg="black" ,bg="white")
    lbl_tipoOperacao.place(x=400, y=360)

    tipoDeConta=Radiobutton(Frame_Main, font=("Goudy old style",12), bg="white", text="Compra    ", variable=var2, value=2, command=sel)
    tipoDeConta.place(x=400, y=400, width=90, height=35)

    venda=Radiobutton(Frame_Main, font=("Goudy old style", 12), bg="white", text="Venda      ",  variable=var2, value=1, command=sel)
    venda.place(x=400,y=430, width=90,height=35)

    aplicar_btn=Button(janela, text="Aplicar", bg="Black", fg="White", font=("Goudy old style",15), command= lambda: aplicar(email, senha, txt_porcLucro.get(), txt_valEntrada.get(), txt_tipoMoeda.get()))
    aplicar_btn.place(x=650,y=600)

    janela.title("AIB - Login")
    janela.geometry("950x750+100+50")


def aplicar(e, s, pl, et, m):

    api = IQ_Option(e, s)
    api.connect()

    porcentagem_lucro = float(pl)
    entrada = float(et)
    moeda = m #  EURUSD
    tipoConta = "PRACTICE"  # PRACTICE / REAL
    operacao = "put" #put / call
    timeframe = 1

    valor_minimo = round(float(entrada) * (float(porcentagem_lucro / 100)), 2)

    api.subscribe_strike_list(moeda, timeframe)

    status,id = api.buy_digital_spot(moeda, entrada, operacao, timeframe)
    time.sleep(0.3)

    while api.get_async_order(id)['position-changed']['msg']['status'] == 'open':
        vpv = round(api.get_digital_spot_profit_after_sale(id), 2)
        
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Atual: $' + str(vpv) + ' - Minimo para venda: $' + str(valor_minimo))
        
        if vpv > valor_minimo:
            print('Fechando operação')
            api.close_digital_option(id)
            break
        
        time.sleep(0.3)
        
    status,valor = api.check_win_digital_v2(id)
    print('Resultado da operação: ' + str('WIN +' if valor > 0 else 'LOSS ') + str(round(valor, 2)))


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
            tela_operacional(editEmail, editSenha)
            break
        time.sleep(5)

janela.resizable(False,False)

bg=ImageTk.PhotoImage(file="images/aib.jpg")
bg_image=Label(janela ,image=bg)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

Frame_login = Frame(janela, bg="black")
Frame_login.place(x=150, y=150, height=330, width=500)

title = Label(Frame_login, text="Login", font=("one day", 35, "bold"), fg= "snow", bg="black")
title.place(x=165,y=30)

lbl_email = Label(Frame_login, text="Email:", font=("Goudy old style", 15, "bold"), fg= "snow",bg="black")
lbl_email.place(x=100,y=100)

txt_email = Entry(Frame_login, font=("times new roman",15))
txt_email.place(x=90,y=130, width=350,height=35)

lbl_password = Label(Frame_login, text="Password:", font=("Goudy old style", 15, "bold"),fg="snow", bg="black")
lbl_password.place(x=100,y=180)

txt_password = Entry(Frame_login, show="*", font=("times new roman", 15))
txt_password.place(x=90, y=210, width=350, height=35)

forget_btn = Button(Frame_login, text="Criar Uma Conta", bg="black", fg="snow", bd=0, font=("Goudy old style", 12), command=cadastro)
forget_btn.place(x=90,y=250)

login_btn = Button(janela, text="Login", bg="snow", fg="black", font=("Goudy old style", 20), command= lambda: entrar(txt_email.get(), txt_password.get()))
login_btn.place(x=450, y=450)

janela.geometry("950x750+100+50")
janela.title("AIB - Login")

janela.mainloop()

from tkinter import*
from PIL import ImageTk

class TelaPrincipal:

    def __init__(self, root):
        self.root=root
        self.root.title("IQ Option")
        self.root.geometry("950x750+100+50")
        self.root.resizable(False,False)
        var = "as"
        var2 = "ass"

        def sel():
            selection = "You selected the option " + str(var.get())
            label.config(text = selection)            
    
         
#=======BGImage=======
        self.bg=ImageTk.PhotoImage(file="images/aib.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

#======Login Frame====
        Frame_Main=Frame(self.root,bg="white")
        Frame_Main.place(x=60, y=50, height=670, width=830)

        lbl_valorEntrada=Label(Frame_Main,text="Operacional",font=("Goudy old style", 17, "bold"),fg= "black",bg="white").place(x=90,y=100)

        lbl_valorEntrada=Label(Frame_Main,text="Valor de Entrada: ",font=("Goudy old style", 12, "bold"),fg= "black",bg="white").place(x=90,y=150)
        self.txt_valEntrada=Entry(Frame_Main,font=("times new roman",12),bg="snow").place(x=300,y=150, width=100,height=35)

        lbl_porcLucro=Label(Frame_Main,text="Porcentagem de lucro: ",font=("Goudy od Style", 12, "bold"),fg= "black",bg="white").place(x=90,y=200)
        self.txt_porcLucro=Entry(Frame_Main,font=("times new roman",12),bg="snow").place(x=300,y=200, width=100,height=35)

        lbl_porcLucro=Label(Frame_Main,text="Tipo de Moeda: ",font=("Goudy od Style", 12, "bold"),fg= "black",bg="white").place(x=90,y=250)
        self.txt_porcLucro=Entry(Frame_Main,font=("times new roman",12),bg="snow").place(x=300,y=250, width=100,height=35)

        #===== TIPO DE CONTA

        lbl_tipoConta=Label(Frame_Main,text="Tipo de Conta",font=("Goudy od Style", 17, "bold"),fg= "black",bg="white").place(x=90,y=360)

        treinamento=Radiobutton(Frame_Main,font=("Goudy old style",12),bg="white", text="Treinamento", variable=var, value=2, command=sel).place(x=90,y=400, width=120,height=35)

        real=Radiobutton(Frame_Main,font=("Goudy old style",12),bg="white", text="Real      ",  variable=var, value=1, command=sel).place(x=90,y=430, width=90,height=35)

        #===== TIPO DE OPERAÇÃO

        lbl_tipoOperacao=Label(Frame_Main,text="Tipo de Operação",font=("Goudy od Style", 17, "bold"),fg= "black",bg="white").place(x=400,y=360)

        tipoDeConta=Radiobutton(Frame_Main,font=("Goudy old style",12),bg="white", text="Compra    ", variable=var2, value=2, command=sel).place(x=400,y=400, width=90,height=35)

        venda=Radiobutton(Frame_Main,font=("Goudy old style",12),bg="white", text="Venda      ",  variable=var2, value=1, command=sel).place(x=400,y=430, width=90,height=35)
        
        #forget_btn=Button(Frame_Main, text="Criar Uma Conta",bg="black", fg="snow",bd=0, font=("Goudy old style",12)).place(x=90,y=250)

        aplicar_btn=Button(self.root, text="Aplicar",bg="Black", fg="White", font=("Goudy old style",15)).place(x=650,y=600)


root=Tk()
obj=TelaPrincipal(root)
root.mainloop()
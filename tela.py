from tkinter import*
from PIL import ImageTk

class TelaLogin:
    def __init__(self, root):
        self.root=root
        self.root.title("IQ Option")
        self.root.geometry("950x750+100+50")
        self.root.resizable(False,False)
         
#=======BGImage=======
        self.bg=ImageTk.PhotoImage(file="images/aib.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

#======Login Frame====
        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=150, y=150, height=330, width=500)

        title = Label(Frame_login, text="Login", font=("one day", 35, "bold"), fg= "snow", bg="black")
        title.place(x=165,y=30)
        #desc=Label(Frame_login,text="Area de Login para IQ Option",font=("Goudy old style", 15, ""),fg= "snow",bg="black").place(x=100,y=100)

        lbl_email=Label(Frame_login,text="Email:",font=("Goudy old style", 15, "bold"),fg= "snow",bg="black").place(x=100,y=100)
        self.txt_email=Entry(Frame_login,font=("times new roman",15))
        self.txt_email.place(x=90,y=130, width=350,height=35)

        lbl_password=Label(Frame_login,text="Password:",font=("Goudy old style", 15, "bold"),fg= "snow",bg="black").place(x=100,y=180)
        self.txt_password=Entry(Frame_login,font=("times new roman",15))
        self.txt_password.place(x=90,y=210, width=350,height=35)

        forget_btn=Button(Frame_login, text="Criar Uma Conta",bg="black", fg="snow",bd=0, font=("Goudy old style",12)).place(x=90,y=250)

        login_btn=Button(self.root, text="Login",bg="snow", fg="black", font=("Goudy old style",20)).place(x=450,y=450)


root=Tk()
obj=TelaLogin(root)
root.mainloop()
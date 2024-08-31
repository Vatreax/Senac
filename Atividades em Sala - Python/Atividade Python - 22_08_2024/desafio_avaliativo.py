from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#
def voltar1():
        abrir_bebidas.withdraw()
        restaurante_do_ederson()

def bebidas():
    global abrir_bebidas
    abrir_bebidas = Toplevel()
    abrir_bebidas.title("Restaurante do Ederson - Bebidas")
    abrir_bebidas.geometry('1920x1080')
    
    button_v = Button(abrir_bebidas, fg="white", bg="black", text="Fechar",command=voltar1)
    button_v.place(x=900,y=450)
    
    img_beb1 = PhotoImage(file=r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\\agua_de_coco.png")
    imgb1_label = Label(abrir_bebidas, image=img_beb1).place(x=10,y=10).resize((1000,1000), Image.ANTIALIAS)

    img_beb2 = PhotoImage(file=r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\\água_tônica.png")
    imgb2_label = Label(abrir_bebidas, image=img_beb2).place(x=100,y=190)
    
    img_beb3 = PhotoImage(file=r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\\suquinho.png")
    imgb3_label = Label(abrir_bebidas, image=img_beb3).place(x=200,y=200)
    
    abrir_bebidas.mainloop()
#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#
def voltar2():
    bebidas_alc.withdraw()
    restaurante_do_ederson()


def bebidas_alcool():
    global bebidas_alc
    bebidas_alc = Toplevel()
    bebidas_alc.title("Restaurante do Ederson - Bebidas Alcoólicas")
    bebidas_alc.geometry('1920x1080')

    button_vo = Button(bebidas_alc, fg="white", bg="black", text="Fechar",command=voltar2)
    button_vo.place(x=900,y=450)

    bebidas_alc.mainloop()
#--------------------------------------------  Bebidas Alcoólicas  ---------------------------------------------------------------------------------------------------#

#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#

def voltar3():
    entrada.withdraw()
    restaurante_do_ederson()

def entrada():
    global entrada
    entrada = Toplevel()
    entrada.title("Restaurante do Ederson - Entrada")
    entrada.geometry('1920x1080')

    button_vol = Button(entrada, fg="white", bg="black", text="Fechar",command=voltar3)
    button_vol.place(x=900,y=450)

    entrada.mainloop()
#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#

def voltar4():
    escolha_da_casa.withdraw()
    restaurante_do_ederson()


def escolha():
    global escolha_da_casa
    escolha_da_casa = Toplevel()
    escolha_da_casa.title("Restaurante do Ederson - Escolha da Casa")
    escolha_da_casa.geometry('1920x1080')

    button_volt = Button(escolha_da_casa, fg="white", bg="black", text="Fechar",command=voltar4)
    button_volt.place(x=900,y=450)

    escolha_da_casa.mainloop()
#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#
def voltar5():
    doces.withdraw()
    restaurante_do_ederson()

def doces():
    global doces
    doces = Toplevel()
    doces.title("Restaurante do Ederson - Doces")
    doces.geometry('1920x1080')

    button_volta = Button(doces, fg="white", bg="black", text="Fechar",command=voltar4)
    button_volta.place(x=900,y=450)

    doces.mainloop()
#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Restaurante do Ederson  -----------------------------------------------------------------------------------------------#
def ver_bebidas():
    bebidas()

def ver_alcool():
    bebidas_alcool()

def ver_entrada():
    entrada()

def ver_escolha_da_casa():
    escolha()

def ver_doces():
    doces()

def abrir_restaurante():
    global restaurante_do_ederson
    restaurante_do_ederson = Tk()
    restaurante_do_ederson.title("Restaurante do Ederson")
    restaurante_do_ederson.geometry('1000x800')
    restaurante_do_ederson.config(bg='blue')

    frame_buttons = Frame(restaurante_do_ederson, bg='white').place(x=475,y=400)

    #frame_buttons.pack(expand=True)

    texto = Label(frame_buttons, text=f"Bem Vindo {text_user}, ao Restaurante do Ederson!")
    #texto.place(x=10,y=100)

    button_beb = Button(frame_buttons, fg="white", bg="black", text="Bebidas", width=15,height=3, command=ver_bebidas)
    #button_beb.place(x=500,y=300)

    button_alco = Button(frame_buttons, fg="white", bg="black", text="Bebidas Alcoólicas", width=15, height=3, command=ver_alcool)
    #button_alco.place(x=500,y=250)

    button_ent = Button(frame_buttons, fg="white", bg="black", text="Entrada", width=15, height=3, command=ver_entrada)
    #button_ent.place(x=500,y=200)

    button_esc = Button(frame_buttons, fg="white", bg="black", text="Escolha da Casa", width=15, height=3, command=ver_escolha_da_casa)
    #button_esc.place(x=500,y=150)

    button_doc = Button(frame_buttons, fg="white", bg="black", text="Doces", width=15, height=3, command=ver_doces)
    #button_doc.place(x=500,y=100)

    restaurante_do_ederson.mainloop()
#--------------------------------------------  Restaurante do Ederson  ---------------------------------------------------------------------------------------------#

#--------------------------------------------  Login  --------------------------------------------------------------------------------------------------------------#
def verificar():
    global text_user
    if usuario_entry.get() == "" or senha_entry.get() == "":
        messagebox.showerror("Login Falho", "Campo não preenchido, confira os campos de cadastro e tente novamente") 

    elif usuario_entry.get() == senha_entry.get():
        messagebox.showerror("Login Falho", "Usuário e Senha Não Podem Coincidir!")
    else:
        try:
            messagebox.showinfo("Login Bem Sucedido", "Cadastro Realizado com Sucesso!")
            text_user = usuario_entry.get()
            root.destroy()
            abrir_restaurante()

        except Exception:
            messagebox.showerror('Erro', f'Não foi possível executar o sistema')

root = Tk()
root.geometry("300x200")
root.title("Login")

usuario_label = Label(root, text="Usuário:")
usuario_label.pack()
usuario_label.place(x=100,y=15)
usuario_entry = Entry(root)
usuario_entry.pack()
usuario_entry.place(x=90,y=40)


senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_label.place(x=100,y=70)

senha_entry = Entry(root, show="*")
senha_entry.pack()
senha_entry.place(x=90,y=90)


cadastro_button = Button(root, text="Login", command=verificar)
cadastro_button.pack()
cadastro_button.place(x=120,y=120)
root.mainloop()
#--------------------------------------------  Login  --------------------------------------------------------------------------------------------------------------#
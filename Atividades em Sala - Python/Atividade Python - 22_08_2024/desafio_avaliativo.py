from tkinter import *
from tkinter import messagebox

def darkmode():
    restaurante_do_ederson.config(bg='black')
    
def abrir_restaurante():
    global restaurante_do_ederson
    restaurante_do_ederson = Tk()
    restaurante_do_ederson.title("Restaurante do Ederson")


    button1 = Button(root, fg="white", bg="black", text="Dark",command=darkmode)
    button1.place(x=1750,y=950)
    restaurante_do_ederson.geometry('1800x1000')



    restaurante_do_ederson.mainloop()




def verificar():
    if usuario_entry.get() == "" or senha_entry.get() == "":
        messagebox.showerror("Login Falho", "Campo não preenchido, confira os campos de cadastro e tente novamente") 

    elif usuario_entry.get() == senha_entry.get():
        messagebox.showerror("Login Falho", "Usuário e Senha Não Podem Coincidir!")
    else:
        try:
            messagebox.showinfo("Login Bem Sucedido", "Cadastro Realizado com Sucesso!")
            root.destroy()
            abrir_restaurante()

        except Exception:
            messagebox.showerror('Erro', f'Não foi possível executar o sistema')

root = Tk()
root.geometry("300x200")
root.title("Login")

usuario_label = Label(root, text="Usuário:")
usuario_label.pack()
usuario_entry = Entry(root)
usuario_entry.pack()
usuario_entry.place(x=90,y=25)

senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_entry = Entry(root, show="*")
senha_entry.pack()
senha_entry.place(x=90,y=70)
senha_label.place(x=90,y=65)

cadastro_button = Button(root, text="Cadastro", command=verificar)
cadastro_button.pack()
cadastro_button.place(x=120,y=95)
root.mainloop()
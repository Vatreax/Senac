from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox



def verificar():
    global login
    if usuario_entry.get() == "" and senha_entry.get() == "":
       messagebox.showerror("Login Falho", "Campo não preenchido, confira os campos de cadastro e tente novamente") 
    elif usuario_entry.get() == senha_entry.get():
        messagebox.showerror("Login Falho","Usuário e Senha Não Podem Coincidir!")
    else:
        try:
            messagebox.showinfo("Login Bem Sucedido", "Cadastro Realizado com Sucesso!")
            root.destroy    

            restaurante_do_ederson = Tk()
            restaurante_do_ederson.title("Restaurante do Ederson")
            restaurante_do_ederson.geometry('1250x650')

            restaurante_do_ederson.mainloop()

        except:
            messagebox.showerror('Erro','Não foi possivel executar o sistema')

root = Tk()
root.geometry("300x200")
root.title("Login")

usuario_label = Label(root, text="Usuario:")
usuario_label.pack()
usuario_entry = Entry(root)
usuario_entry.pack()

senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_entry = Entry(root, show="*")
senha_entry.pack()

cadastro_button = Button(root, text="Cadastro", command=verificar)
cadastro_button.pack()

root.mainloop()
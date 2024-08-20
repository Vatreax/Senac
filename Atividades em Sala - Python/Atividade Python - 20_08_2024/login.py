from tkinter import *
from tkinter import messagebox

def verificar():
    if usuario_entry.get() == "tafarildo" and senha_entry.get() == "1234":
        messagebox.showinfo("Cadastro Bem Sucedido", "Cadastro Realizado com Sucesso!")
    elif confirmar_senha_entry.get() != senha_entry.get():
        messagebox.showerror("Cadastro Falho", "Senhas Não Coincidem!!")
    elif usuario_entry.get() == senha_entry.get():
        messagebox.showerror("Cadastro Falho","Usuário e Senha Não Podem Coincidir!")
    else:
        messagebox.showerror("Cadastro Falho", "Campo não preenchido, confira os campos de cadastro e tente novamente")

root = Tk()
root.geometry("300x200")
root.title("cadastro")

usuario_label = Label(root, text="Usuario:")
usuario_label.pack()
usuario_entry = Entry(root)
usuario_entry.pack()

senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_entry = Entry(root, show="*")
senha_entry.pack()

confirmar_senha_label = Label(root, text="Confirmar Senha:")
confirmar_senha_label.pack()
confirmar_senha_entry = Entry(root, show="*")
confirmar_senha_entry.pack()

cadastro_button = Button(root, text="Cadastro", command=verificar)
cadastro_button.pack()

root.mainloop()
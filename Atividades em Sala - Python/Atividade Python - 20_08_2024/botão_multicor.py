from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Meu Botão")

def red():
    root.config(bg='red')

def big_black():
    root.config(bg='black')

def blue():
    root.config(bg='blue')

def nenhum():
    root.config(bg='white')

cadastro_button1 = Button(root, fg="white", bg="red", text="BOTÃO 1",command=red)
cadastro_button1.place(relx=0.5 , rely=0.8, anchor="center")

cadastro_button2 = Button(root, fg="white", bg="black", text="BOTÃO 2",command=big_black)
cadastro_button2.place(relx=0.5 , rely=0.6, anchor="center")

cadastro_button3 = Button(root, fg="white", bg="blue", text="BOTÃO 3",command=blue)
cadastro_button3.place(relx=0.5 , rely=0.4, anchor="center")

cadastro_button4 = Button(root, fg="black", bg="white", text="Normal",command=nenhum)
cadastro_button4.place(relx=0.5 , rely=0.2, anchor="center")




root.mainloop()
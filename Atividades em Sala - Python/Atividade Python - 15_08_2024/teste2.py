from tkinter import *
from tkinter import ttk

n1 = 0
def contador():
    global n1
    n1 +=1
    print(n1)
    n3.config (text=f"Clique em Mim! {n1}")


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text=f"Clique no Botão :D     ",font='ariel 20').grid(column=0, row=0)
n1 = 0
n3 = ttk.Button(frm, text=f"Clique em Mim! {n1}", command=contador)
n3.grid(column=0, row=2)
root.mainloop()
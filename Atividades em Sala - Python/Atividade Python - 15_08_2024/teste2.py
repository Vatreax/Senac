from tkinter import *
from tkinter import ttk

n1 = 0
def contador():
    global n1
    n1 = (n1+1)
    print(n1)


root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text=f"Clique no Botão :D     ",font='ariel 20').grid(column=0, row=0)
ttk.Button(frm, text="Clique em Mim!", command=contador).grid(column=0, row=2)
ttk,Label(frm, text=f"Contador {n1}",font='ariel 20').grid(column=0, row=1)
root.mainloop()
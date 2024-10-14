from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Olá Mundo").grid(column=1, row=0)
root.mainloop()
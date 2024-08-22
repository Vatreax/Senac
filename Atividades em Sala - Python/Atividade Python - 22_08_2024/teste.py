from tkinter import *
from tkinter import PhotoImage

root=Tk()
root.title("image galery")
root.geometry('618x500')
root.config(bg='teal')

f=("chalkduster",30,'bold')

heading=Label(root,text="image galery :)", font=f)
heading.grid(row=0,column=0)

img1=PhotoImage(file='C:\Users\RafaelMontiel\Downloads\\pingu2.png')
img2=PhotoImage(file='file=r"C:\Users\RafaelMontiel\Downloads\\ek9de07iikf51.png')

img1.grid(row=1,column=1)
img2.grid(row=1,column=1)

root.mainloop
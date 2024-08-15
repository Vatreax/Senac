from tkinter import*
janela = Tk()
text = 0


def bt7_click(): #botao +
    soma =(text)
    lb4["text"] = str(text + 1)

def bt8_click():
    soma =(text)
    lb4["text"] = str(text - 1)



lb4 = Label(janela,text="0",font="Arial 50", fg= "red", bg="white")
lb4.place(x=50, y=50)


bt7 = Button(janela, width=1, text="+", command=bt7_click)
bt7.place(x=130, y=90)
bt8 = Button(janela, width=1, text="-", command=bt8_click)
bt8.place(x=150, y=90)


janela.geometry("200x200")
janela.mainloop()
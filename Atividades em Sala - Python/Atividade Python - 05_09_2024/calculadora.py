from tkinter import *



quantidade_entrada1_var = ''

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("282x238")

screen_width = calculadora.winfo_screenwidth()
screen_height = calculadora.winfo_screenheight()

frame = Frame(calculadora, bg='black', width=screen_width, height=screen_height)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)



def printada(equatorius):

    entrada = equatorius.get()
    resultado = eval(entrada)
    equatorius.delete(0, 'end')
    equatorius.insert('end', resultado)
    print(resultado)


equatorius = Entry(frame, width=44)
equatorius.grid(row=0, column=0, columnspan=20, padx=5, pady=5)



porcentus = Button(frame, fg="white", bg="navy", text='√', font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "**0.5"))
porcentus.grid(row=2, column=0, padx=5, pady=5)

decimus = Button(frame, fg="white", bg="navy", text='.', font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "."))
decimus.grid(row=3, column=0, padx=5, pady=5)

zero = Button(frame, fg="white", bg="navy", text="0", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 0))
zero.grid(row=4, column=1, padx=5, pady=5)

igualitarius = Button(frame, fg="white", bg="navy", text='=', font='bold', width=4, height=1, command=lambda: printada(equatorius))
igualitarius.grid(row=4, column=3, padx=5, pady=5)

apagar = Button(frame, fg="white", bg="navy", text='Clear', font='bold', width=4, height=1, command=lambda:  equatorius.delete(0, 'end'))
apagar.grid(row=4, column=2, padx=5, pady=5)

um = Button(frame, fg="white", bg="navy", text="1", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 1))
um.grid(row=3, column=1, padx=5, pady=5)

dois = Button(frame, fg="white", bg="navy", text="2", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 2))
dois.grid(row=3, column=2, padx=5, pady=5)

tres = Button(frame, fg="white", bg="navy", text="3", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 3))
tres.grid(row=3, column=3, padx=5, pady=5)

quatro = Button(frame, fg="white", bg="navy", text="4", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 4))
quatro.grid(row=2, column=1, padx=5, pady=5)

cinco = Button(frame, fg="white", bg="navy", text="5", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 5))
cinco.grid(row=2, column=2, padx=5, pady=5)

seis = Button(frame, fg="white", bg="navy", text="6", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 6))
seis.grid(row=2, column=3, padx=5, pady=5)

sete = Button(frame, fg="white", bg="navy", text="7", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 7))
sete.grid(row=1, column=1, padx=5, pady=5)

oito = Button(frame, fg="white", bg="navy", text="8", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 8))
oito.grid(row=1, column=2, padx=5, pady=5)

nove = Button(frame, fg="white", bg="navy", text="9", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 9))
nove.grid(row=1, column=3, padx=5, pady=5)

somarius = Button(frame, fg="white", bg="navy", text="+", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "+"))
somarius.grid(row=1, column=4, padx=5, pady=5)

subtrarius = Button(frame, fg="white", bg="navy", text="-", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "-"))
subtrarius.grid(row=2, column=4, padx=5, pady=5)

multiplicus = Button(frame, fg="white", bg="navy", text="x", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "*"))
multiplicus.grid(row=3, column=4, padx=5, pady=5)

dividorus = Button(frame, fg="white", bg="navy", text="÷", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "/"))
dividorus.grid(row=4, column=4, padx=5, pady=5)

calculadora.mainloop()
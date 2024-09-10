from tkinter import *

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("278x200")

screen_width = calculadora.winfo_screenwidth()
screen_height = calculadora.winfo_screenheight()

frame = Frame(calculadora, bg='black', width=screen_width, height=screen_height)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

def printada(equatorius):
    entrada = equatorius.get()
    try:
        entrada = entrada.replace('√', '**0.5').replace('%', '/100')
        resultado = eval(entrada)
        equatorius.delete(0, 'end')
        equatorius.insert('end', resultado)
        print(resultado)

    except Exception as e:
        equatorius.delete(0, 'end')
        equatorius.insert('end', 'Erro')
        print(e)

def delete(equatorius):
    texto = equatorius.get()
    if texto:
        equatorius.delete(len(texto) - 1, 'end')

def porcem(equatorius):
    texto = equatorius.get()
    if texto and texto[-1] not in "+-*/%√":
        equatorius.insert('end', '%')

def raiz_quadrada(equatorius):
    texto2 = equatorius.get()
    if texto2 and texto2[-1] not in "+-*/√%":
        equatorius.insert('end', '√')

equatorius = Entry(frame, width=44)
equatorius.grid(row=0, column=0, columnspan=10, padx=5, pady=5)

deletado = Button(frame, fg="white", bg="red", text='Del', font='bold', width=4, height=1, command=lambda: delete(equatorius))
deletado.grid(row=1, column=0, padx=5, pady=5)

raiz = Button(frame, fg="white", bg="navy", text='√', font='bold', width=4, height=1, command=lambda: raiz_quadrada(equatorius))
raiz.grid(row=2, column=0, padx=5, pady=5)

percentual = Button(frame, fg="white", bg="navy", text='%', font='bold', width=4, height=1, command=lambda: porcem(equatorius))
percentual.grid(row=3, column=0, padx=5, pady=5)

decimus = Button(frame, fg="white", bg="navy", text='.', font='bold', width=4, height=1, command=lambda: equatorius.insert('end', "."))
decimus.grid(row=4, column=0, padx=5, pady=5)

zero = Button(frame, fg="white", bg="navy", text="0", font='bold', width=4, height=1, command=lambda: equatorius.insert('end', 0))
zero.grid(row=4, column=1, padx=5, pady=5)

igualitarius = Button(frame, fg="white", bg="navy", text='=', font='bold', width=4, height=1, command=lambda: printada(equatorius))
igualitarius.grid(row=4, column=3, padx=5, pady=5)

apagar = Button(frame, fg="white", bg="navy", text='Clear', font='bold', width=4, height=1, command=lambda: equatorius.delete(0, 'end'))
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
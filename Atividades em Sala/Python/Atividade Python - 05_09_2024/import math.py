from tkinter import *
import math

def calcular(entrada):
    try:
        entrada = entrada.replace('x', '*').replace('÷', '/')
        resultado = eval(entrada)
        return resultado
    except Exception as e:
        return f"Erro: {e}"

def atualizar_display(equatorius, texto):
    equatorius.insert('end', texto)

def calcular_resultado(equatorius):
    entrada = equatorius.get()
    resultado = calcular(entrada)
    equatorius.delete(0, 'end')
    equatorius.insert('end', resultado)

def raiz_quadrada():
    entrada = equatorius.get()
    try:
        valor = float(entrada)
        resultado = math.sqrt(valor)
        equatorius.delete(0, 'end')
        equatorius.insert('end', resultado)
    except ValueError:
        equatorius.delete(0, 'end')
        equatorius.insert('end', "Erro")

def limpar_entrada():
    equatorius.delete(0, 'end')

calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("312x312")

screen_width = calculadora.winfo_screenwidth()
screen_height = calculadora.winfo_screenheight()

frame = Frame(calculadora, bg='black', width=screen_width, height=screen_height)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Campo de entrada
equatorius = Entry(frame, width=40)
equatorius.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Função combinada para o botão √
def funcao_porcentus():
    limpar_entrada()  # Primeiro limpa o campo
    raiz_quadrada()   # Depois calcula a raiz quadrada

# Botões
buttons = [
    ('√', 4, 0, funcao_porcentus),
    ('.', 5, 2, lambda: atualizar_display(equatorius, ".")),
    ('0', 4, 1, lambda: atualizar_display(equatorius, '0')),
    ('=', 4, 3, lambda: calcular_resultado(equatorius)),
    ('Clear', 4, 2, lambda: equatorius.delete(0, 'end')),
    ('1', 3, 1, lambda: atualizar_display(equatorius, '1')),
    ('2', 3, 2, lambda: atualizar_display(equatorius, '2')),
    ('3', 3, 3, lambda: atualizar_display(equatorius, '3')),
    ('4', 2, 1, lambda: atualizar_display(equatorius, '4')),
    ('5', 2, 2, lambda: atualizar_display(equatorius, '5')),
    ('6', 2, 3, lambda: atualizar_display(equatorius, '6')),
    ('7', 1, 1, lambda: atualizar_display(equatorius, '7')),
    ('8', 1, 2, lambda: atualizar_display(equatorius, '8')),
    ('9', 1, 3, lambda: atualizar_display(equatorius, '9')),
    ('+', 1, 4, lambda: atualizar_display(equatorius, '+')),
    ('-', 2, 4, lambda: atualizar_display(equatorius, '-')),
    ('x', 3, 4, lambda: atualizar_display(equatorius, 'x')),
    ('÷', 4, 4, lambda: atualizar_display(equatorius, '÷'))
]

for (text, row, col, command) in buttons:
    Button(frame, fg="white", bg="navy", text=text, font='bold', width=4, height=1, command=command).grid(row=row, column=col, padx=5, pady=5)

calculadora.mainloop()
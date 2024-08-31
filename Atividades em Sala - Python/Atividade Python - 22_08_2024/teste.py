from tkinter import *

def ver_bebidas():
    pass

def ver_alcool():
    pass

def ver_entrada():
    pass

def ver_escolha_da_casa():
    pass

def ver_doces():
    pass

global restaurante_do_ederson
restaurante_do_ederson = Tk()
restaurante_do_ederson.title("Restaurante do Ederson")
restaurante_do_ederson.geometry('1920x1080')
restaurante_do_ederson.config(bg='red')

texto = Label(restaurante_do_ederson, text="Bem Vindo ao Restaurante do Ederson!", bg='red', fg='white')
texto.pack(pady=20)

# Criar um frame para conter os botões
frame_buttons = Frame(restaurante_do_ederson, bg='red')
frame_buttons.pack(expand=True)

# Configurar o tamanho e centralizar os botões
button_beb = Button(frame_buttons, fg="white", bg="black", text="Bebidas", command=ver_bebidas, width=15, height=3)
button_beb.pack(pady=10)

button_alco = Button(frame_buttons, fg="white", bg="black", text="Bebidas Alcoólicas", command=ver_alcool, width=15, height=3)
button_alco.pack(pady=10)

button_ent = Button(frame_buttons, fg="white", bg="black", text="Entrada", command=ver_entrada, width=15, height=3)
button_ent.pack(pady=10)

button_esc = Button(frame_buttons, fg="white", bg="black", text="Escolha da Casa", command=ver_escolha_da_casa, width=15, height=3)
button_esc.pack(pady=10)

button_doc = Button(frame_buttons, fg="white", bg="black", text="Doces", command=ver_doces, width=15, height=3)
button_doc.pack(pady=10)

restaurante_do_ederson.mainloop()
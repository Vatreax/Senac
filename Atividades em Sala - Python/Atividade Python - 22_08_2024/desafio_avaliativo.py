from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

comanda = {
    # --- Bebidas --- #
    'Água de Coco': {'quantidade': 0, 'preço_unitário': 10},
    'Água Tônica': {'quantidade': 0, 'preço_unitário': 12},
    'Sucos': {'quantidade': 0, 'preço_unitário': 14},
    'Coca-Cola': {'quantidade': 0, 'preço_unitário': 9},
    'Fanta': {'quantidade': 0, 'preço_unitário': 8.99},

    # --- Bebidas Alcoólicas --- #
    'Caipirinha': {'quantidade': 0, 'preço_unitário': 13.85},
    'Heineken': {'quantidade': 0, 'preço_unitário': 16.00},
    'Smirnoff': {'quantidade': 0, 'preço_unitário': 15.00},
    'Vodka': {'quantidade': 0, 'preço_unitário': 80.75},
    'Red Label': {'quantidade': 0, 'preço_unitário': 100.00},

    # --- Entrada --- #
    'Batata Frita': {'quantidade': 0, 'preço_unitário': 14.00},
    'Bolinho de Carne': {'quantidade': 0, 'preço_unitário': 18.00},
    'Salada': {'quantidade': 0, 'preço_unitário': 12.00},
    'Polenta': {'quantidade': 0, 'preço_unitário': 15.00},
    'Bruchetta': {'quantidade': 0, 'preço_unitário': 20.00},

    # --- Escolha da Casa --- #
    'Bife à Milanesa': {'quantidade': 0, 'preço_unitário': 25.00},
    'Feijoada': {'quantidade': 0, 'preço_unitário': 28.55},
    'Hambúrguer': {'quantidade': 0, 'preço_unitário': 25.00},
    'Acarajé': {'quantidade': 0, 'preço_unitário': 50.00},
    'Picanha': {'quantidade': 0, 'preço_unitário': 50.00},

    # --- Doces --- #
    'Pizza Doce': {'quantidade': 0, 'preço_unitário': 25.00},
    'Sorvete': {'quantidade': 0, 'preço_unitário': 15.00},
    'Torta de Chocolate': {'quantidade': 0, 'preço_unitário': 45.50},
    'Pudim de Leite': {'quantidade': 0, 'preço_unitário': 50.00},
    'Bolo de Cenoura': {'quantidade': 0, 'preço_unitário': 50.00},

    # --- Principal --- #
    'Baião de Dois': {'quantidade': 0, 'preço_unitário': 25.00},
    'Lasanha': {'quantidade': 0, 'preço_unitário': 15.00},
    'Pastel': {'quantidade': 0, 'preço_unitário': 18.00},
    'Frango a Parmegiana': {'quantidade': 0, 'preço_unitário': 30.00},
    'Bife a Cavalo': {'quantidade': 0, 'preço_unitário': 35.00}

}


    
#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return 0

def validar_e_converter():
    global quantidade_bebidas1, quantidade_bebidas2, quantidade_bebidas3, quantidade_bebidas4, quantidade_bebidas5
    quantidade_bebidas1 = quantidade_bebidas1_var.get()
    quantidade_bebidas2 = quantidade_bebidas2_var.get()
    quantidade_bebidas3 = quantidade_bebidas3_var.get()
    quantidade_bebidas4 = quantidade_bebidas4_var.get()
    quantidade_bebidas5 = quantidade_bebidas5_var.get()

    numero_bebidas1 = converter_para_inteiro(quantidade_bebidas1)
    numero_bebidas2 = converter_para_inteiro(quantidade_bebidas2)
    numero_bebidas3 = converter_para_inteiro(quantidade_bebidas3)
    numero_bebidas4 = converter_para_inteiro(quantidade_bebidas4)
    numero_bebidas5 = converter_para_inteiro(quantidade_bebidas5)

    if not (numero_bebidas1 or numero_bebidas2 or numero_bebidas3 or numero_bebidas4 or numero_bebidas5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_bebidas1 < 0 or numero_bebidas2 < 0 or numero_bebidas3 < 0 or
        numero_bebidas4 < 0 or numero_bebidas5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Água de Coco']['quantidade'] = numero_bebidas1
    comanda['Água Tônica']['quantidade'] = numero_bebidas2
    comanda['Sucos']['quantidade'] = numero_bebidas3
    comanda['Coca-Cola']['quantidade'] = numero_bebidas4
    comanda['Fanta']['quantidade'] = numero_bebidas5

    total_bebida1 = comanda['Água de Coco']['quantidade'] * comanda['Água de Coco']['preço_unitário']
    total_bebida2 = comanda['Água Tônica']['quantidade'] * comanda['Água Tônica']['preço_unitário']
    total_bebida3 = comanda['Sucos']['quantidade'] * comanda['Sucos']['preço_unitário']
    total_bebida4 = comanda['Coca-Cola']['quantidade'] * comanda['Coca-Cola']['preço_unitário']
    total_bebida5 = comanda['Fanta']['quantidade'] * comanda['Fanta']['preço_unitário']

    print(comanda)
    messagebox.showinfo("Compras Confirmadas - Bebidas",
f"""Água de Coco: R$ {total_bebida1:.2f} | Água Tônica: R$ {total_bebida2:.2f}
Sucos: R$ {total_bebida3:.2f} | Coca-Cola: R$ {total_bebida4:.2f}
Fanta: R$ {total_bebida5:.2f}""")

def voltar1():
    abrir_bebidas.withdraw()
    restaurante_do_ederson()

def abrir_bebidas():
    global bebidas
    bebidas = Toplevel()
    bebidas.title("Restaurante do Ederson - Bebidas")
    bebidas.geometry('1400x900')

    # ---- Background + Variáveis ---- #
    imagem_bg1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\refrescos (1).jpg"
    bg_imagem1 = Image.open(imagem_bg1)

    screen_width1 = bebidas.winfo_screenwidth()
    screen_height1 = bebidas.winfo_screenheight()
    bg_imagem1 = bg_imagem1.resize((screen_width1, screen_height1), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem1)

    bg_label1 = Label(bebidas, image=bg_image_tk)
    bg_label1.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_bebidas1_var, quantidade_bebidas2_var, quantidade_bebidas3_var, quantidade_bebidas4_var, quantidade_bebidas5_var

    quantidade_bebidas1_var = StringVar()
    quantidade_bebidas2_var = StringVar()
    quantidade_bebidas3_var = StringVar()
    quantidade_bebidas4_var = StringVar()
    quantidade_bebidas5_var = StringVar()

    # ---- Primeira Bebida ---- #
    frame_bebida1 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_bebida1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\agua_de_coco.png"
    bebida_image1 = Image.open(imagem_bebida1)
    bebida_image1 = bebida_image1.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image1_tk = ImageTk.PhotoImage(bebida_image1)
    img_bebida1 = Label(frame_bebida1, image=bebida_image1_tk, bg='white')
    img_bebida1.image = bebida_image1_tk
    img_bebida1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida1, text="Água de Coco", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida1, text="R$ 12,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida1, width=5, textvariable=quantidade_bebidas1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Bebida ---- #
    frame_bebida2 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_bebida2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\agua_tonica.jpeg"
    bebida_image2 = Image.open(imagem_bebida2)
    bebida_image2 = bebida_image2.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image2_tk = ImageTk.PhotoImage(bebida_image2)
    img_bebida2 = Label(frame_bebida2, image=bebida_image2_tk, bg='white')
    img_bebida2.image = bebida_image2_tk
    img_bebida2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida2, text="Água Tônica", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida2, text="R$ 8,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida2, width=5, textvariable=quantidade_bebidas2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Bebida ---- #
    frame_bebida3 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_bebida3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\suquinho.png"
    bebida_image3 = Image.open(imagem_bebida3)
    bebida_image3 = bebida_image3.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image3_tk = ImageTk.PhotoImage(bebida_image3)
    img_bebida3 = Label(frame_bebida3, image=bebida_image3_tk, bg='white')
    img_bebida3.image = bebida_image3_tk
    img_bebida3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida3, text="Sucos", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida3, text="R$ 14,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida3, width=5, textvariable=quantidade_bebidas3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarta Bebida ---- #
    frame_bebida4 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_bebida4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\coca_cola.png"
    bebida_image4 = Image.open(imagem_bebida4)
    bebida_image4 = bebida_image4.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image4_tk = ImageTk.PhotoImage(bebida_image4)
    img_bebida4 = Label(frame_bebida4, image=bebida_image4_tk, bg='white')
    img_bebida4.image = bebida_image3_tk
    img_bebida4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida4, text="Coca-Cola", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida4, text="R$ 8,99", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida4, width=5, textvariable=quantidade_bebidas4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinta Bebida ---- #
    frame_bebida5 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_bebida5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\fanta-latas.jpg"
    bebida_image5 = Image.open(imagem_bebida5)
    bebida_image5 = bebida_image5.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image5_tk = ImageTk.PhotoImage(bebida_image5)
    img_bebida5 = Label(frame_bebida5, image=bebida_image5_tk, bg='white')
    img_bebida5.image = bebida_image5_tk
    img_bebida5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida5, text="Fanta", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida5, text="R$ 9,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida5, width=5, textvariable=quantidade_bebidas5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Validar ---- #
    button_validar1 = Button(bebidas, text="Validar Compra", command=validar_e_converter)
    button_validar1.place(relx=0.50, rely=0.90, anchor='center')
                    
    # ---- Fechar ---- #
    button_fechar1 = Button(bebidas, fg="black", bg="white", text="Cancelar", command=bebidas.destroy)
    button_fechar1.place(relx=0.50, rely=0.85, anchor='center')

    bebidas.mainloop()


#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Bebidas Alcoólicas  ---------------------------------------------------------------------------------------------------#
def validar_e_converter_alcool():
    global quantidade_alcool1, quantidade_alcool2, quantidade_alcool3, quantidade_alcool4, quantidade_alcool5
    quantidade_alcool1 = quantidade_alcool1_var.get()
    quantidade_alcool2 = quantidade_alcool2_var.get()
    quantidade_alcool3 = quantidade_alcool3_var.get()
    quantidade_alcool4 = quantidade_alcool4_var.get()
    quantidade_alcool5 = quantidade_alcool5_var.get()

    numero_alcool1 = converter_para_inteiro(quantidade_alcool1)
    numero_alcool2 = converter_para_inteiro(quantidade_alcool2)
    numero_alcool3 = converter_para_inteiro(quantidade_alcool3)
    numero_alcool4 = converter_para_inteiro(quantidade_alcool4)
    numero_alcool5 = converter_para_inteiro(quantidade_alcool5)

    if not (numero_alcool1 or numero_alcool2 or numero_alcool3 or numero_alcool4 or numero_alcool5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_alcool1 < 0 or numero_alcool2 < 0 or numero_alcool3 < 0 or
        numero_alcool4 < 0 or numero_alcool5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Caipirinha']['quantidade'] = numero_alcool1
    comanda['Heineken']['quantidade'] = numero_alcool2
    comanda['Smirnoff']['quantidade'] = numero_alcool3
    comanda['Vodka']['quantidade'] = numero_alcool4
    comanda['Red Label']['quantidade'] = numero_alcool5

    total_alcool1 = comanda['Caipirinha']['quantidade'] * comanda['Caipirinha']['preço_unitário']
    total_alcool2 = comanda['Heineken']['quantidade'] * comanda['Heineken']['preço_unitário']
    total_alcool3 = comanda['Smirnoff']['quantidade'] * comanda['Smirnoff']['preço_unitário']
    total_alcool4 = comanda['Vodka']['quantidade'] * comanda['Vodka']['preço_unitário']
    total_alcool5 = comanda['Red Label']['quantidade'] * comanda['Red Label']['preço_unitário']

    print(comanda)
    messagebox.showinfo("Compras Confirmadas - Alcoól",
f"""Caipirinha: R$ {total_alcool1:.2f} | Heineken: R$ {total_alcool2:.2f}
Smirnoff: R$ {total_alcool3:.2f} | Vodka: R$ {total_alcool4:.2f}
Red Label: R$ {total_alcool5:.2f}""")


def bebidas_alcool():
    global bebidas_alc
    bebidas_alc = Toplevel()
    bebidas_alc.title("Restaurante do Ederson - Bebidas Alcoólicas")
    bebidas_alc.geometry('1400x900')

    # ---- Background+Variáveis ---- #
    imagem_bg2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\bebidas-refrescantes.jpg"
    bg_imagem2 = Image.open(imagem_bg2)

    screen_width2 = bebidas_alc.winfo_screenwidth()
    screen_height2 = bebidas_alc.winfo_screenheight()
    bg_imagem2 = bg_imagem2.resize((screen_width2, screen_height2), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem2)

    bg_label2 = Label(bebidas_alc, image=bg_image_tk)
    bg_label2.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_alcool1_var, quantidade_alcool2_var, quantidade_alcool3_var, quantidade_alcool4_var, quantidade_alcool5_var
    quantidade_alcool1_var = StringVar()
    quantidade_alcool2_var = StringVar()
    quantidade_alcool3_var = StringVar()
    quantidade_alcool4_var = StringVar()
    quantidade_alcool5_var = StringVar()

    # ---- Primeiro Alcoólico ---- #
    frame_alcool1 = Frame(bebidas_alc, bg='white', width=300, height=400)
    frame_alcool1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_alcool1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas_alcoólicas\\caipirinha.png"
    alcool_image1 = Image.open(imagem_alcool1)
    alcool_image1 = alcool_image1.resize((200, 200), Image.Resampling.LANCZOS)
    alcool_image1_tk = ImageTk.PhotoImage(alcool_image1)
    img_alcool1 = Label(frame_alcool1, image=alcool_image1_tk, bg='white')
    img_alcool1.image = alcool_image1_tk
    img_alcool1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_alcool1, text="Caipirinha", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool1, text="R$ 13,85", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_alcool1, width=5, textvariable=quantidade_alcool1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segundo Alcoólico ---- #
    frame_alcool2 = Frame(bebidas_alc, bg='white', width=300, height=400)
    frame_alcool2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_alcool2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas_alcoólicas\\heineken.png"
    alcool_image2 = Image.open(imagem_alcool2)
    alcool_image2 = alcool_image2.resize((200, 200), Image.Resampling.LANCZOS)
    alcool_image2_tk = ImageTk.PhotoImage(alcool_image2)
    img_alcool2 = Label(frame_alcool2, image=alcool_image2_tk, bg='white')
    img_alcool2.image = alcool_image2_tk
    img_alcool2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_alcool2, text="Heineken", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool2, text="R$ 16,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_alcool2, width=5, textvariable=quantidade_alcool2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceiro Alcoólico ---- #
    frame_alcool3 = Frame(bebidas_alc, bg='white', width=300, height=400)
    frame_alcool3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_alcool3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas_alcoólicas\\smirnoff.png"
    alcool_image3 = Image.open(imagem_alcool3)
    alcool_image3 = alcool_image3.resize((200, 200), Image.Resampling.LANCZOS)
    alcool_image3_tk = ImageTk.PhotoImage(alcool_image3)
    img_alcool3 = Label(frame_alcool3, image=alcool_image3_tk, bg='white')
    img_alcool3.image = alcool_image3_tk
    img_alcool3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_alcool3, text="Smirnoff", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool3, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_alcool3, width=5, textvariable=quantidade_alcool3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarto Alcoólico ---- #
    frame_alcool4 = Frame(bebidas_alc, bg='white', width=300, height=400)
    frame_alcool4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_alcool4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas_alcoólicas\\vodka.png"
    alcool_image4 = Image.open(imagem_alcool4)
    alcool_image4 = alcool_image4.resize((200, 200), Image.Resampling.LANCZOS)
    alcool_image4_tk = ImageTk.PhotoImage(alcool_image4)
    img_alcool4 = Label(frame_alcool4, image=alcool_image4_tk, bg='white')
    img_alcool4.image = alcool_image4_tk
    img_alcool4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_alcool4, text="Vodka", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool4, text="R$ 80,75", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_alcool4, width=5, textvariable=quantidade_alcool4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinto Alcoólico ---- #
    frame_alcool5 = Frame(bebidas_alc, bg='white', width=300, height=400)
    frame_alcool5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_alcool5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas_alcoólicas\\red_label.jpg"
    alcool_image5 = Image.open(imagem_alcool5)
    alcool_image5 = alcool_image5.resize((200, 200), Image.Resampling.LANCZOS)
    alcool_image5_tk = ImageTk.PhotoImage(alcool_image5)
    img_alcool5 = Label(frame_alcool5, image=alcool_image5_tk, bg='white')
    img_alcool5.image = alcool_image5_tk
    img_alcool5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_alcool5, text="Red Label", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool5, text="R$ 100,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_alcool5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_alcool5, width=5, textvariable=quantidade_alcool5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Validar ---- #
    button_validar2 = Button(bebidas_alc, text="Validar Compra", command=validar_e_converter_alcool)
    button_validar2.place(relx=0.50, rely=0.90, anchor='center')

    # ---- Fechar ---- #
    button_fechar2 = Button(bebidas_alc, fg="black", bg="white", text="Cancelar", command=bebidas_alc.destroy)
    button_fechar2.place(relx=0.50, rely=0.85, anchor='center')


    bebidas_alc.mainloop()

#--------------------------------------------  Bebidas Alcoólicas  ---------------------------------------------------------------------------------------------------#

#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return 0

def validar_e_converter_entrada():
    global quantidade_entrada1_var, quantidade_entrada2_var, quantidade_entrada3_var, quantidade_entrada4_var, quantidade_entrada5_var
    quantidade_entrada1 = quantidade_entrada1_var.get()
    quantidade_entrada2 = quantidade_entrada2_var.get()
    quantidade_entrada3 = quantidade_entrada3_var.get()
    quantidade_entrada4 = quantidade_entrada4_var.get()
    quantidade_entrada5 = quantidade_entrada5_var.get()

    numero_entrada1 = converter_para_inteiro(quantidade_entrada1)
    numero_entrada2 = converter_para_inteiro(quantidade_entrada2)
    numero_entrada3 = converter_para_inteiro(quantidade_entrada3)
    numero_entrada4 = converter_para_inteiro(quantidade_entrada4)
    numero_entrada5 = converter_para_inteiro(quantidade_entrada5)

    if not (numero_entrada1 or numero_entrada2 or numero_entrada3 or numero_entrada4 or numero_entrada5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_entrada1 < 0 or numero_entrada2 < 0 or numero_entrada3 < 0 or
        numero_entrada4 < 0 or numero_entrada5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Batata Frita']['quantidade'] = numero_entrada1
    comanda['Bolinho de Carne']['quantidade'] = numero_entrada2
    comanda['Salada']['quantidade'] = numero_entrada3
    comanda['Polenta']['quantidade'] = numero_entrada4
    comanda['Bruchetta']['quantidade'] = numero_entrada5

    total_entrada1 = comanda['Batata Frita']['quantidade'] * comanda['Batata Frita']['preço_unitário']
    total_entrada2 = comanda['Bolinho de Carne']['quantidade'] * comanda['Bolinho de Carne']['preço_unitário']
    total_entrada3 = comanda['Salada']['quantidade'] * comanda['Salada']['preço_unitário']
    total_entrada4 = comanda['Polenta']['quantidade'] * comanda['Polenta']['preço_unitário']
    total_entrada5 = comanda['Bruchetta']['quantidade'] * comanda['Bruchetta']['preço_unitário']

    messagebox.showinfo("Compras Confirmadas - Entradas",
f"""Batata Frita: R$ {total_entrada1:.2f} | Bolinho de Carne: R$ {total_entrada2:.2f}
Salada: R$ {total_entrada3:.2f} | Polenta: R$ {total_entrada4:.2f}
Bruchetta: R$ {total_entrada5:.2f}""")


def entradas():
    global abrir_entrada
    abrir_entrada = Toplevel()
    abrir_entrada.title("Restaurante do Ederson - Entrada")
    abrir_entrada.geometry('1400x900')

    # ---- Background ---- #
    imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\opcoes-de-entrada-restaurante.jpg"
    bg_imagem = Image.open(imagem_bg)

    screen_width4 = abrir_entrada.winfo_screenwidth()
    screen_height4 = abrir_entrada.winfo_screenheight()
    bg_imagem = bg_imagem.resize((screen_width4, screen_height4), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem)

    bg_label = Label(abrir_entrada, image=bg_image_tk)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_entrada1_var, quantidade_entrada2_var, quantidade_entrada3_var, quantidade_entrada4_var, quantidade_entrada5_var
    quantidade_entrada1_var = StringVar()
    quantidade_entrada2_var = StringVar()
    quantidade_entrada3_var = StringVar()
    quantidade_entrada4_var = StringVar()
    quantidade_entrada5_var = StringVar()

    # ---- Primeira Entrada ---- #
    frame_entrada1 = Frame(abrir_entrada, bg='white', width=900, height=450)
    frame_entrada1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_entrada1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\batata_frita.png"
    entrada_image1 = Image.open(imagem_entrada1)
    entrada_image1 = entrada_image1.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image1_tk = ImageTk.PhotoImage(entrada_image1)
    img_entrada1 = Label(frame_entrada1, image=entrada_image1_tk, bg='white')
    img_entrada1.image = entrada_image1_tk
    img_entrada1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada1, text="Batata Frita", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada1, text="R$ 14,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada1, width=5, textvariable=quantidade_entrada1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Entrada ---- #
    frame_entrada2 = Frame(abrir_entrada, bg='white', width=900, height=450)
    frame_entrada2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_entrada2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\bolinho de carne.png"
    entrada_image2 = Image.open(imagem_entrada2)
    entrada_image2 = entrada_image2.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image2_tk = ImageTk.PhotoImage(entrada_image2)
    img_entrada2 = Label(frame_entrada2, image=entrada_image2_tk, bg='white')
    img_entrada2.image = entrada_image2_tk
    img_entrada2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada2, text="Bolinho de Carne", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada2, text="R$ 18,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada2, width=5, textvariable=quantidade_entrada2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Entrada ---- #
    frame_entrada3 = Frame(abrir_entrada, bg='white', width=900, height=450)
    frame_entrada3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_entrada3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\salada.png"
    entrada_image3 = Image.open(imagem_entrada3)
    entrada_image3 = entrada_image3.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image3_tk = ImageTk.PhotoImage(entrada_image3)
    img_entrada3 = Label(frame_entrada3, image=entrada_image3_tk, bg='white')
    img_entrada3.image = entrada_image3_tk
    img_entrada3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada3, text="Salada", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada3, text="R$ 12,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada3, width=5, textvariable=quantidade_entrada3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarta Entrada ---- #
    frame_entrada4 = Frame(abrir_entrada, bg='white', width=900, height=450)
    frame_entrada4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_entrada4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\polenta.jpg"
    entrada_image4 = Image.open(imagem_entrada4)
    entrada_image4 = entrada_image4.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image4_tk = ImageTk.PhotoImage(entrada_image4)
    img_entrada4 = Label(frame_entrada4, image=entrada_image4_tk, bg='white')
    img_entrada4.image = entrada_image4_tk
    img_entrada4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada4, text="Polenta", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada4, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada4, width=5, textvariable=quantidade_entrada4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinta Entrada ---- #
    frame_entrada5 = Frame(abrir_entrada, bg='white', width=900, height=450)
    frame_entrada5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_entrada5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\bruchetta1.png"
    entrada_image5 = Image.open(imagem_entrada5)
    entrada_image5 = entrada_image5.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image5_tk = ImageTk.PhotoImage(entrada_image5)
    img_entrada5 = Label(frame_entrada5, image=entrada_image5_tk, bg='white')
    img_entrada5.image = entrada_image5_tk
    img_entrada5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada5, text="Bruchetta", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada5, text="R$ 20,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada5, width=5, textvariable=quantidade_entrada5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Validar ---- #
    button_validar3 = Button(abrir_entrada, fg="black", bg="white", text="Validar Compra", command=validar_e_converter_entrada)
    button_validar3.place(relx=0.50, rely=0.90, anchor='center')

    # ---- Botão Fechar ---- #
    button_voltar3 = Button(abrir_entrada, fg="black", bg="white", text="Cancelar", command=abrir_entrada.destroy)
    button_voltar3.place(relx=0.50, rely=0.85, anchor='center')

    abrir_entrada.mainloop()
#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return 0

def validar_e_converter_casa():
    global quantidade_casa1_var, quantidade_casa2_var, quantidade_casa3_var, quantidade_casa4_var, quantidade_casa5_var
    quantidade_casa1 = quantidade_casa1_var.get()
    quantidade_casa2 = quantidade_casa2_var.get()
    quantidade_casa3 = quantidade_casa3_var.get()
    quantidade_casa4 = quantidade_casa4_var.get()
    quantidade_casa5 = quantidade_casa5_var.get()

    numero_casa1 = converter_para_inteiro(quantidade_casa1)
    numero_casa2 = converter_para_inteiro(quantidade_casa2)
    numero_casa3 = converter_para_inteiro(quantidade_casa3)
    numero_casa4 = converter_para_inteiro(quantidade_casa4)
    numero_casa5 = converter_para_inteiro(quantidade_casa5)

    if not (numero_casa1 or numero_casa2 or numero_casa3 or numero_casa4 or numero_casa5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_casa1 < 0 or numero_casa2 < 0 or numero_casa3 < 0 or
        numero_casa4 < 0 or numero_casa5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Bife à Milanesa']['quantidade'] = numero_casa1
    comanda['Feijoada']['quantidade'] = numero_casa2
    comanda['Hambúrguer']['quantidade'] = numero_casa3
    comanda['Acarajé']['quantidade'] = numero_casa4
    comanda['Picanha']['quantidade'] = numero_casa5

    total_casa1 = comanda['Bife à Milanesa']['quantidade'] * comanda['Bife à Milanesa']['preço_unitário']
    total_casa2 = comanda['Feijoada']['quantidade'] * comanda['Feijoada']['preço_unitário']
    total_casa3 = comanda['Hambúrguer']['quantidade'] * comanda['Hambúrguer']['preço_unitário']
    total_casa4 = comanda['Acarajé']['quantidade'] * comanda['Acarajé']['preço_unitário']
    total_casa5 = comanda['Picanha']['quantidade'] * comanda['Picanha']['preço_unitário']

    print(comanda)
    messagebox.showinfo("Compras Confirmadas - Escolha da Casa",
f"""Bife à Milanesa: R$ {total_casa1:.2f} | Feijoada: R$ {total_casa2:.2f}
Hambúrguer: R$ {total_casa3:.2f} | Acarajé: R$ {total_casa4:.2f}
Picanha: R$ {total_casa5:.2f}""")

def abrir_escolha_da_casa():
    global escolha_da_casa
    escolha_da_casa = Toplevel()
    escolha_da_casa.title("Restaurante do Ederson - Escolha da Casa")
    escolha_da_casa.geometry('1400x900')

    # ---- Background ---- #
    imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\feijoada.jpg"
    bg_imagem = Image.open(imagem_bg)

    screen_width4 = escolha_da_casa.winfo_screenwidth()
    screen_height4 = escolha_da_casa.winfo_screenheight()
    bg_imagem = bg_imagem.resize((screen_width4, screen_height4), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem)

    bg_label = Label(escolha_da_casa, image=bg_image_tk)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_casa1_var, quantidade_casa2_var, quantidade_casa3_var, quantidade_casa4_var, quantidade_casa5_var

    quantidade_casa1_var = StringVar()
    quantidade_casa2_var = StringVar()
    quantidade_casa3_var = StringVar()
    quantidade_casa4_var = StringVar()
    quantidade_casa5_var = StringVar()

    # ---- Primeira Escolha ---- #
    frame_casa1 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_casa1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\bife_a_milanesa.png"
    casa_image1 = Image.open(imagem_casa1)
    casa_image1 = casa_image1.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image1_tk = ImageTk.PhotoImage(casa_image1)
    img_casa1 = Label(frame_casa1, image=casa_image1_tk, bg='white')
    img_casa1.image = casa_image1_tk
    img_casa1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa1, text="Bife à Milanesa", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa1, text="R$ 25,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa1, width=5, textvariable=quantidade_casa1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Escolha ---- #
    frame_casa2 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_casa2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\feijoada_potente.png"
    casa_image2 = Image.open(imagem_casa2)
    casa_image2 = casa_image2.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image2_tk = ImageTk.PhotoImage(casa_image2)
    img_casa2 = Label(frame_casa2, image=casa_image2_tk, bg='white')
    img_casa2.image = casa_image2_tk
    img_casa2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa2, text="Feijoada", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa2, text="R$ 28,55", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa2, width=5, textvariable=quantidade_casa2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Escolha ---- #
    frame_casa3 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_casa3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\hamburguer.png"
    casa_image3 = Image.open(imagem_casa3)
    casa_image3 = casa_image3.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image3_tk = ImageTk.PhotoImage(casa_image3)
    img_casa3 = Label(frame_casa3, image=casa_image3_tk, bg='white')
    img_casa3.image = casa_image3_tk
    img_casa3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa3, text="Hambúrguer", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa3, text="R$ 25,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa3, width=5, textvariable=quantidade_casa3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarta Escolha ---- #
    frame_casa4 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_casa4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\acaraje.jpg"
    casa_image4 = Image.open(imagem_casa4)
    casa_image4 = casa_image4.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image4_tk = ImageTk.PhotoImage(casa_image4)
    img_casa4 = Label(frame_casa4, image=casa_image4_tk, bg='white')
    img_casa4.image = casa_image4_tk
    img_casa4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa4, text="Acarajé", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa4, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa4, width=5, textvariable=quantidade_casa4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinta Escolha ---- #
    frame_casa5 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_casa5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\picanha.png"
    casa_image5 = Image.open(imagem_casa5)
    casa_image5 = casa_image5.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image5_tk = ImageTk.PhotoImage(casa_image5)
    img_casa5 = Label(frame_casa5, image=casa_image5_tk, bg='white')
    img_casa5.image = casa_image5_tk
    img_casa5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa5, text="Picanha", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa5, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa5, width=5, textvariable=quantidade_casa5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Validar ---- #
    button_confirmar5 = Button(escolha_da_casa, text="Validar Compra", command=validar_e_converter_casa)
    button_confirmar5.place(relx=0.50, rely=0.90, anchor='center')

    # ---- Botão Fechar ---- #
    button_voltar5 = Button(escolha_da_casa, text="Cancelar", command=escolha_da_casa.destroy)
    button_voltar5.place(relx=0.50, rely=0.85, anchor='center')

    escolha_da_casa.mainloop()

#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return 0

def validar_e_converter_doces():
    global quantidade_doce1_var, quantidade_doce2_var, quantidade_doce3_var, quantidade_doce4_var, quantidade_doce5_var
    quantidade_doce1 = quantidade_doce1_var.get()
    quantidade_doce2 = quantidade_doce2_var.get()
    quantidade_doce3 = quantidade_doce3_var.get()
    quantidade_doce4 = quantidade_doce4_var.get()
    quantidade_doce5 = quantidade_doce5_var.get()

    numero_doce1 = converter_para_inteiro(quantidade_doce1)
    numero_doce2 = converter_para_inteiro(quantidade_doce2)
    numero_doce3 = converter_para_inteiro(quantidade_doce3)
    numero_doce4 = converter_para_inteiro(quantidade_doce4)
    numero_doce5 = converter_para_inteiro(quantidade_doce5)

    if not (numero_doce1 or numero_doce2 or numero_doce3 or numero_doce4 or numero_doce5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_doce1 < 0 or numero_doce2 < 0 or numero_doce3 < 0 or
        numero_doce4 < 0 or numero_doce5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Pizza Doce']['quantidade'] = numero_doce1
    comanda['Sorvete']['quantidade'] = numero_doce2
    comanda['Torta de Chocolate']['quantidade'] = numero_doce3
    comanda['Pudim de Leite']['quantidade'] = numero_doce4
    comanda['Bolo de Cenoura']['quantidade'] = numero_doce5

    total_doce1 = comanda['Pizza Doce']['quantidade'] * comanda['Pizza Doce']['preço_unitário']
    total_doce2 = comanda['Sorvete']['quantidade'] * comanda['Sorvete']['preço_unitário']
    total_doce3 = comanda['Torta de Chocolate']['quantidade'] * comanda['Torta de Chocolate']['preço_unitário']
    total_doce4 = comanda['Pudim de Leite']['quantidade'] * comanda['Pudim de Leite']['preço_unitário']
    total_doce5 = comanda['Bolo de Cenoura']['quantidade'] * comanda['Bolo de Cenoura']['preço_unitário']

    print(comanda)
    messagebox.showinfo("Compras Confirmadas - Doces",
f"""Pizza Doce: R$ {total_doce1:.2f} | Sorvete: R$ {total_doce2:.2f}
Torta de Chocolate: R$ {total_doce3:.2f} | Pudim de Leite: R$ {total_doce4:.2f}
Bolo de Cenoura: R$ {total_doce5:.2f}""")

def abrir_doces():
    global doces
    doces = Toplevel()
    doces.title("Restaurante do Ederson - Doces")
    doces.geometry('1400x900')

    # ---- Background ---- #
    imagem_bg5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\balcao-de-padaria.png"
    bg_imagem5 = Image.open(imagem_bg5)

    screen_width5 = doces.winfo_screenwidth()
    screen_height5 = doces.winfo_screenheight()
    bg_imagem5 = bg_imagem5.resize((screen_width5, screen_height5), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem5)

    bg_label5 = Label(doces, image=bg_image_tk)
    bg_label5.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_doce1_var, quantidade_doce2_var, quantidade_doce3_var, quantidade_doce4_var, quantidade_doce5_var

    quantidade_doce1_var = StringVar()
    quantidade_doce2_var = StringVar()
    quantidade_doce3_var = StringVar()
    quantidade_doce4_var = StringVar()
    quantidade_doce5_var = StringVar()

    # ---- Primeiro Doce ---- #
    frame_doces1 = Frame(doces, bg='white', width=900, height=450)
    frame_doces1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_doce1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\pizza_doce.png"
    doce_image1 = Image.open(imagem_doce1)
    doce_image1 = doce_image1.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image1_tk = ImageTk.PhotoImage(doce_image1)
    img_doce1 = Label(frame_doces1, image=doce_image1_tk, bg='white')
    img_doce1.image = doce_image1_tk
    img_doce1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces1, text="Pizza Doce", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces1, text="R$ 25,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces1, width=5, textvariable=quantidade_doce1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segundo Doce ---- #
    frame_doces2 = Frame(doces, bg='white', width=900, height=450)
    frame_doces2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_doce2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\sorvete_do_bao.png"
    doce_image2 = Image.open(imagem_doce2)
    doce_image2 = doce_image2.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image2_tk = ImageTk.PhotoImage(doce_image2)
    img_doce2 = Label(frame_doces2, image=doce_image2_tk, bg='white')
    img_doce2.image = doce_image2_tk
    img_doce2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces2, text="Sorvete", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces2, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces2, width=5, textvariable=quantidade_doce2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceiro Doce ---- #
    frame_doces3 = Frame(doces, bg='white', width=900, height=450)
    frame_doces3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_doce3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\torta_ma_num_e_reta.png"
    doce_image3 = Image.open(imagem_doce3)
    doce_image3 = doce_image3.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image3_tk = ImageTk.PhotoImage(doce_image3)
    img_doce3 = Label(frame_doces3, image=doce_image3_tk, bg='white')
    img_doce3.image = doce_image3_tk 
    img_doce3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces3, text="Torta de Chocolate", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces3, text="R$ 45,50", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces3, width=5, textvariable=quantidade_doce3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarto Doce ---- #
    frame_doces4 = Frame(doces, bg='white', width=900, height=450)
    frame_doces4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_doce4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\pudim-de-leite.png"
    doce_image4 = Image.open(imagem_doce4)
    doce_image4 = doce_image4.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image4_tk = ImageTk.PhotoImage(doce_image4)
    img_doce4 = Label(frame_doces4, image=doce_image4_tk, bg='white')
    img_doce4.image = doce_image4_tk 
    img_doce4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces4, text="Pudim de Leite", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces4, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces4, width=5, textvariable=quantidade_doce4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinto Doce ---- #
    frame_doces5 = Frame(doces, bg='white', width=900, height=450)
    frame_doces5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_doce5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\bolo_de_cenoura.jpg"
    doce_image5 = Image.open(imagem_doce5)
    doce_image5 = doce_image5.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image5_tk = ImageTk.PhotoImage(doce_image5)
    img_doce5 = Label(frame_doces5, image=doce_image5_tk, bg='white')
    img_doce5.image = doce_image5_tk 
    img_doce5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces5, text="Bolo de Cenoura", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces5, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces5, width=5, textvariable=quantidade_doce5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Confirmar ---- #
    button_confirmar = Button(doces, text="Validar Compra", command=validar_e_converter_doces)
    button_confirmar.place(relx=0.50, rely=0.85, anchor='center')

    # ---- Botão Fechar ---- #
    button_volta = Button(doces, fg="black", bg="white", text="Cancelar", command=doces.destroy)
    button_volta.place(relx=0.50, rely=0.90, anchor='center')

    doces.mainloop()
#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Principal  -------------------------------------------------------------------------------------------------------------#
def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return 0

def validar_e_converter_principais():
    global quantidade_principal1_var, quantidade_principal2_var, quantidade_principal3_var, quantidade_principal4_var, quantidade_principal5_var
    quantidade_principal1 = quantidade_principal1_var.get()
    quantidade_principal2 = quantidade_principal2_var.get()
    quantidade_principal3 = quantidade_principal3_var.get()
    quantidade_principal4 = quantidade_principal4_var.get()
    quantidade_principal5 = quantidade_principal5_var.get()

    numero_principal1 = converter_para_inteiro(quantidade_principal1)
    numero_principal2 = converter_para_inteiro(quantidade_principal2)
    numero_principal3 = converter_para_inteiro(quantidade_principal3)
    numero_principal4 = converter_para_inteiro(quantidade_principal4)
    numero_principal5 = converter_para_inteiro(quantidade_principal5)

    if not (numero_principal1 or numero_principal2 or numero_principal3 or numero_principal4 or numero_principal5):
        messagebox.showinfo("Aviso", "Todos os campos estão VAZIOS.")
        return

    if (numero_principal1 < 0 or numero_principal2 < 0 or numero_principal3 < 0 or
        numero_principal4 < 0 or numero_principal5 < 0):
        messagebox.showerror("Erro", "Por favor, insira apenas números maiores ou iguais a zero.")
        return

    comanda['Baião de Dois']['quantidade'] = numero_principal1
    comanda['Lasanha']['quantidade'] = numero_principal2
    comanda['Pastel']['quantidade'] = numero_principal3
    comanda['Frango a Parmegiana']['quantidade'] = numero_principal4
    comanda['Bife a Cavalo']['quantidade'] = numero_principal5

    total_principal1 = comanda['Baião de Dois']['quantidade'] * comanda['Baião de Dois']['preço_unitário']
    total_principal2 = comanda['Lasanha']['quantidade'] * comanda['Lasanha']['preço_unitário']
    total_principal3 = comanda['Pastel']['quantidade'] * comanda['Pastel']['preço_unitário']
    total_principal4 = comanda['Frango a Parmegiana']['quantidade'] * comanda['Frango a Parmegiana']['preço_unitário']
    total_principal5 = comanda['Bife a Cavalo']['quantidade'] * comanda['Bife a Cavalo']['preço_unitário']

    print(comanda)
    messagebox.showinfo("Compras Confirmadas - Pratos Principais",
f"""Baião de Dois: R$ {total_principal1:.2f} | Lasanha: R$ {total_principal2:.2f}
Pastel: R$ {total_principal3:.2f} | Frango a Parmegiana: R$ {total_principal4:.2f}
Bife a Cavalo: R$ {total_principal5:.2f}""")

def abrir_principal():
    global principal
    principal = Toplevel()
    principal.title("Restaurante do Ederson - Principal")
    principal.geometry('1400x900')

    # ---- Background ---- #
    imagem_bg7 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\feijoada.jpg"
    bg_imagem7 = Image.open(imagem_bg7)

    screen_width7 = principal.winfo_screenwidth()
    screen_height7 = principal.winfo_screenheight()
    bg_imagem7 = bg_imagem7.resize((screen_width7, screen_height7), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem7)

    bg_label7 = Label(principal, image=bg_image_tk)
    bg_label7.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_principal1_var, quantidade_principal2_var, quantidade_principal3_var, quantidade_principal4_var, quantidade_principal5_var

    quantidade_principal1_var = StringVar()
    quantidade_principal2_var = StringVar()
    quantidade_principal3_var = StringVar()
    quantidade_principal4_var = StringVar()
    quantidade_principal5_var = StringVar()

    # ---- Primeiro Principal ---- #
    frame_principal1 = Frame(principal, bg='white', width=900, height=450)
    frame_principal1.place(relx=0.25, rely=0.20, anchor='center')

    imagem_principal1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\principal\\baiao_do_bao.png"
    principal_image1 = Image.open(imagem_principal1)
    principal_image1 = principal_image1.resize((200, 200), Image.Resampling.LANCZOS)
    principal_image1_tk = ImageTk.PhotoImage(principal_image1)
    img_principal1 = Label(frame_principal1, image=principal_image1_tk, bg='white')
    img_principal1.image = principal_image1_tk
    img_principal1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_principal1, text="Baião de Dois", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal1, text="R$ 25,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_principal1, width=10, textvariable=quantidade_principal1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segundo Principal ---- #
    frame_principal2 = Frame(principal, bg='white', width=900, height=450)
    frame_principal2.place(relx=0.50, rely=0.20, anchor='center')

    imagem_principal2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\principal\\lasanha.png"
    principal_image2 = Image.open(imagem_principal2)
    principal_image2 = principal_image2.resize((200, 200), Image.Resampling.LANCZOS)
    principal_image2_tk = ImageTk.PhotoImage(principal_image2)
    img_principal2 = Label(frame_principal2, image=principal_image2_tk, bg='white')
    img_principal2.image = principal_image2_tk
    img_principal2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_principal2, text="Lasanha", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal2, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_principal2, width=10, textvariable=quantidade_principal2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceiro Principal ---- #
    frame_principal3 = Frame(principal, bg='white', width=900, height=450)
    frame_principal3.place(relx=0.75, rely=0.20, anchor='center')

    imagem_principal3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\principal\\pastel.png"
    principal_image3 = Image.open(imagem_principal3)
    principal_image3 = principal_image3.resize((200, 200), Image.Resampling.LANCZOS)
    principal_image3_tk = ImageTk.PhotoImage(principal_image3)
    img_principal3 = Label(frame_principal3, image=principal_image3_tk, bg='white')
    img_principal3.image = principal_image3_tk 
    img_principal3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_principal3, text="Pastel", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal3, text="R$ 18,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_principal3, width=10, textvariable=quantidade_principal3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quarto Principal ---- #
    frame_principal4 = Frame(principal, bg='white', width=900, height=450)
    frame_principal4.place(relx=0.37, rely=0.60, anchor='center')

    imagem_principal4 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\principal\\frango-a-parmegiana.jpg"
    principal_image4 = Image.open(imagem_principal4)
    principal_image4 = principal_image4.resize((200, 200), Image.Resampling.LANCZOS)
    principal_image4_tk = ImageTk.PhotoImage(principal_image4)
    img_principal4 = Label(frame_principal4, image=principal_image4_tk, bg='white')
    img_principal4.image = principal_image4_tk 
    img_principal4.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_principal4, text="Frango a Parmegiana", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal4, text="R$ 30,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal4, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_principal4, width=10, textvariable=quantidade_principal4_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Quinto Principal ---- #
    frame_principal5 = Frame(principal, bg='white', width=900, height=450)
    frame_principal5.place(relx=0.63, rely=0.60, anchor='center')

    imagem_principal5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\principal\\bife_a_cavalo.jpg"
    principal_image5 = Image.open(imagem_principal5)
    principal_image5 = principal_image5.resize((200, 200), Image.Resampling.LANCZOS)
    principal_image5_tk = ImageTk.PhotoImage(principal_image5)
    img_principal5 = Label(frame_principal5, image=principal_image5_tk, bg='white')
    img_principal5.image = principal_image5_tk 
    img_principal5.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_principal5, text="Bife a Cavalo", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal5, text="R$ 35,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_principal5, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_principal5, width=10, textvariable=quantidade_principal5_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Confirmar ---- #
    button_confirmar = Button(principal, text="Confirmar", command=validar_e_converter_principais)
    button_confirmar.place(relx=0.50, rely=0.90, anchor='center')

    # ---- Botão Fechar ---- #
    button_voltar1 = Button(principal, fg="black", bg="white", text="Cancelar", command=principal.destroy)
    button_voltar1.place(relx=0.50, rely=0.85, anchor='center')

    principal.mainloop()
#--------------------------------------------  Principal  -------------------------------------------------------------------------------------------------------------#


#--------------------------------------------  Carrinho  -------------------------------------------------------------------------------------------------------------#
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def calcular_total_comanda():
    total = 0
    for item, dados in comanda.items():
        total += dados['quantidade'] * dados['preço_unitário']
    return total

def resetar_comanda():
    for item in comanda:
        comanda[item]['quantidade'] = 0
    atualizar_interface()

def atualizar_interface():
    # Limpar o frame_buttons
    for widget in frame_buttons.winfo_children():
        widget.destroy()

    # Exibir dicionário e total no frame
    total = calcular_total_comanda()
    
    total_label = Label(frame_buttons, text=f"Total da Comanda: R$ {total:.2f}", bg='white', font=('Arial', 16))
    total_label.pack(pady=20)

    detalhes_label = Label(frame_buttons, text="Detalhes da Comanda:", bg='white', font=('Arial', 14))
    detalhes_label.pack(pady=10)

    for item, dados in comanda.items():
        item_info = f"{item}: {dados['quantidade']} x R$ {dados['preço_unitário']:.2f} = R$ {dados['quantidade'] * dados['preço_unitário']:.2f}"
        item_label = Label(frame_buttons, text=item_info, bg='white', font=('Arial', 12))
        item_label.pack()

    # Botão Fechar dentro do frame
    button_voltar = Button(frame_buttons, fg="white", bg="black", text="Fechar", command=carrinho.destroy)
    button_voltar.pack(pady=10)

    # Botão Resetar dentro do frame
    button_resetar = Button(frame_buttons, fg="white", bg="red", text="Resetar Comanda", command=resetar_comanda)
    button_resetar.pack(pady=5)

def abrir_carrinho():
    global carrinho, frame_buttons
    carrinho = Toplevel()
    carrinho.title("Restaurante do Ederson - Carrinho")
    carrinho.geometry('1400x900')

    # ---- Background ---- #
    imagem_bg6 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\maquina_registradora.jpg"
    bg_imagem6 = Image.open(imagem_bg6)

    screen_width6 = carrinho.winfo_screenwidth()
    screen_height6 = carrinho.winfo_screenheight()
    bg_imagem6 = bg_imagem6.resize((screen_width6, screen_height6), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem6)

    bg_label6 = Label(carrinho, image=bg_image_tk)
    bg_label6.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame_buttons = Frame(carrinho, bg='white', width=1000, height=600)
    frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

    atualizar_interface()

    carrinho.mainloop()

#--------------------------------------------  Carrinho  -------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Restaurante do Ederson  -----------------------------------------------------------------------------------------------#
def ver_bebidas():
    abrir_bebidas()

def ver_alcool():
    bebidas_alcool()

def ver_entrada():
    entradas()

def ver_escolha_da_casa():
    abrir_escolha_da_casa()

def ver_doces():
    abrir_doces()

def ver_carrinho():
    abrir_carrinho()

def ver_principal():
    abrir_principal()

def abrir_restaurante():
    global restaurante_do_ederson
    restaurante_do_ederson = Tk()
    restaurante_do_ederson.title("Restaurante do Ederson")
    restaurante_do_ederson.geometry('1600x1080')

#  ------- Background -------  #
    imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\Pantanal_em_Mato_Grosso_Brasil.jpg"
    bg_imagem = Image.open(imagem_bg)

    screen_width = restaurante_do_ederson.winfo_screenwidth()
    screen_height = restaurante_do_ederson.winfo_screenheight()
    bg_imagem = bg_imagem.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem)

    bg_label = Label(restaurante_do_ederson, image=bg_image_tk)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

#  ------- Frame -------  #
    frame_buttons = Frame(restaurante_do_ederson, bg='white', width=800, height=400)
    frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

#  ------- Logo+Texto -------  #
    logo= r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\imagens\logo\logotipo2.restaurante(bg).png.png"
    logo_image = Image.open(logo)
    logo_image_tk = ImageTk.PhotoImage(logo_image)
    img_label = Label(frame_buttons, image=logo_image_tk, bg='white')
    img_label.grid(row=0, column=0, columnspan=3, pady=10)

    texto = Label(frame_buttons, text=f"Bem Vindo {text_user}!", bg='white', font=('Arial', 16, 'bold'))
    texto.grid(row=1, column=0, columnspan=3, pady=(10, 5))

    opcoes_texto = Label(frame_buttons, text="Opções do Cardápio:", font=('Arial', 16), bg='white')
    opcoes_texto.grid(row=2, column=0, columnspan=3, pady=(5, 20))

#  ------- Botões -------  #
    button_beb = Button(frame_buttons, fg="white", bg="black", text="Bebidas", width=15, height=3, command=ver_bebidas)
    button_beb.grid(row=3, column=0, padx=10, pady=5)

    button_alco = Button(frame_buttons, fg="white", bg="black", text="Bebidas Alcoólicas", width=15, height=3, command=ver_alcool)
    button_alco.grid(row=3, column=1, padx=10, pady=5)

    button_ent = Button(frame_buttons, fg="white", bg="black", text="Entrada", width=15, height=3, command=ver_entrada)
    button_ent.grid(row=3, column=2, padx=10, pady=5)

    button_esc = Button(frame_buttons, fg="white", bg="black", text="Escolha da Casa", width=15, height=3, command=ver_escolha_da_casa)
    button_esc.grid(row=4, column=0, padx=10, pady=5)

    button_doc = Button(frame_buttons, fg="white", bg="black", text="Doces", width=15, height=3, command=ver_doces)
    button_doc.grid(row=4, column=1, padx=10, pady=5)
    
    button_pri = Button(frame_buttons, fg="white", bg="black", text="Principal", width=15, height=3, command=ver_principal)
    button_pri.grid(row=4, column=2, padx=10, pady=5)
    
    button_car = Button(frame_buttons, fg="white", bg="palegreen4", text="Carrinho", width=15, height=3, command=ver_carrinho)
    button_car.grid(row=5, column=1, padx=10, pady=5)

    restaurante_do_ederson.mainloop()
#--------------------------------------------  Restaurante do Ederson  ---------------------------------------------------------------------------------------------#

#--------------------------------------------  Login  --------------------------------------------------------------------------------------------------------------#
def verificar():
    global text_user
    if usuario_entry.get() == "" or senha_entry.get() == "":
        messagebox.showerror("Login Falho", "Campo não preenchido, confira os campos e tente novamente") 

    elif usuario_entry.get() == senha_entry.get():
        messagebox.showerror("Login Falho", "Usuário e Senha Não Podem Coincidir!")
    else:
        try:
            messagebox.showinfo("Login Bem Sucedido", "Login Realizado com Sucesso!")
            text_user = usuario_entry.get()
            root.destroy()
            abrir_restaurante()

        except:
            messagebox.showerror('Erro', f'Não foi possível executar o sistema')

root = Tk()
root.geometry("300x200")
root.title("Login")

usuario_label = Label(root, text="Usuário:")
usuario_label.pack()
usuario_label.place(x=100,y=15)
usuario_entry = Entry(root)
usuario_entry.pack()
usuario_entry.place(x=90,y=40)


senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_label.place(x=100,y=70)

senha_entry = Entry(root, show="*")
senha_entry.pack()
senha_entry.place(x=90,y=90)


cadastro_button = Button(root, text="Login", command=verificar)
cadastro_button.pack()
cadastro_button.place(x=120,y=120)
root.mainloop()
#----------------------
# ----------------------  Login  --------------------------------------------------------------------------------------------------------------#
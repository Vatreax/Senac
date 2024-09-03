from tkinter import *
from tkinter import StringVar, Label, Entry, Button, Toplevel, messagebox
from PIL import Image, ImageTk

def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return None

def validar_e_converter():
    global quantidade_bebidas1, quantidade_bebidas2, quantidade_bebidas3
    quantidade_bebidas1 = quantidade_bebidas1_var.get()
    quantidade_bebidas2 = quantidade_bebidas2_var.get()
    quantidade_bebidas3 = quantidade_bebidas3_var.get()

    # Verificar se os campos estão vazios
    if quantidade_bebidas1 == "" and quantidade_bebidas2 == "" and quantidade_bebidas3 == "":
        messagebox.showinfo("Aviso","Todos os campos estão VAZIOS.")
        return

    # Converter para inteiros e verificar erros
    numero_bebidas1 = converter_para_inteiro(quantidade_bebidas1)
    numero_bebidas2 = converter_para_inteiro(quantidade_bebidas2)
    numero_bebidas3 = converter_para_inteiro(quantidade_bebidas3)

    if numero_bebidas1 is None or numero_bebidas2 is None or numero_bebidas3 is None:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros válidos.")
    else:
        messagebox.showinfo("Conversão Bem-Sucedida", 
                            f"Quantidade Bebida 1: {numero_bebidas1}\n"
                            f"Quantidade Bebida 2: {numero_bebidas2}\n"
                            f"Quantidade Bebida 3: {numero_bebidas3}")

def voltar1():
    abrir_bebidas.withdraw()
    restaurante_do_ederson()

def abrir_bebidas():
    global bebidas
    bebidas = Toplevel()
    bebidas.title("Restaurante do Ederson - Bebidas")
    bebidas.geometry('1200x800')

    # ---- Background + Variáveis ---- #
    imagem_bg1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\refrescos.jpg"
    bg_imagem1 = Image.open(imagem_bg1)

    screen_width1 = bebidas.winfo_screenwidth()
    screen_height1 = bebidas.winfo_screenheight()
    bg_imagem1 = bg_imagem1.resize((screen_width1, screen_height1), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem1)

    bg_label1 = Label(bebidas, image=bg_image_tk)
    bg_label1.place(relx=0, rely=0, relwidth=1, relheight=1)

    global quantidade_bebidas1_var, quantidade_bebidas2_var, quantidade_bebidas3_var

    quantidade_bebidas1_var = StringVar()
    quantidade_bebidas2_var = StringVar()
    quantidade_bebidas3_var = StringVar()

    # ---- Primeira Bebida ---- #
    frame_bebida1 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida1.place(relx=0.25, rely=0.35, anchor='center')

    imagem_bebida1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\agua_de_coco.png"
    bebida_image1 = Image.open(imagem_bebida1)
    bebida_image1 = bebida_image1.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image1_tk = ImageTk.PhotoImage(bebida_image1)
    img_bebida1 = Label(frame_bebida1, image=bebida_image1_tk, bg='white')
    img_bebida1.image = bebida_image1_tk
    img_bebida1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida1, text="Água de Coco", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida1, text="R$ 10,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida1, width=10, textvariable=quantidade_bebidas1_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Bebida ---- #
    frame_bebida2 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida2.place(relx=0.50, rely=0.35, anchor='center')

    imagem_bebida2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\água_tônica.png"
    bebida_image2 = Image.open(imagem_bebida2)
    bebida_image2 = bebida_image2.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image2_tk = ImageTk.PhotoImage(bebida_image2)
    img_bebida2 = Label(frame_bebida2, image=bebida_image2_tk, bg='white')
    img_bebida2.image = bebida_image2_tk
    img_bebida2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida2, text="Água Tônica", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida2, text="R$ 8,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida2, width=10, textvariable=quantidade_bebidas2_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Bebida ---- #
    frame_bebida3 = Frame(bebidas, bg='white', width=900, height=450)
    frame_bebida3.place(relx=0.75, rely=0.35, anchor='center')

    imagem_bebida3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\bebidas\\suquinho.png"
    bebida_image3 = Image.open(imagem_bebida3)
    bebida_image3 = bebida_image3.resize((200, 200), Image.Resampling.LANCZOS)
    bebida_image3_tk = ImageTk.PhotoImage(bebida_image3)
    img_bebida3 = Label(frame_bebida3, image=bebida_image3_tk, bg='white')
    img_bebida3.image = bebida_image3_tk
    img_bebida3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_bebida3, text="Sucos", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida3, text="R$ 5,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_bebida3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_bebida3, width=10, textvariable=quantidade_bebidas3_var).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Botão Validar ---- #
    button_validar = Button(bebidas, text="Validar e Converter", command=validar_e_converter)
    button_validar.place(relx=0.50, rely=0.90, anchor='center')

    # ---- Fechar ---- #
    button_fechar = Button(bebidas, fg="black", bg="white", text="Fechar", command=bebidas.destroy)
    button_fechar.place(relx=0.50, rely=0.85, anchor='center')

    bebidas.mainloop()

# Função fictícia para abrir o restaurante
def restaurante_do_ederson():
    pass

# Exemplo de execução
abrir_bebidas()

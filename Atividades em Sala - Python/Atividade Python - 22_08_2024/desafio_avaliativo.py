from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#
def voltar1():
        abrir_bebidas.withdraw()
        restaurante_do_ederson()

def bebidas():
    global abrir_bebidas
    abrir_bebidas = Toplevel()
    abrir_bebidas.title("Restaurante do Ederson - Bebidas")
    abrir_bebidas.geometry('900x500')
    
    imagem_bg1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\refrescos.jpg"
    bg_imagem1 = Image.open(imagem_bg1)

    screen_width1= abrir_bebidas.winfo_screenwidth()
    screen_height1 = abrir_bebidas.winfo_screenheight()
    bg_imagem1 = bg_imagem1.resize((screen_width1, screen_height1), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem1)

    bg_label1 = Label(abrir_bebidas, image=bg_image_tk)
    bg_label1.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    frame_bebidas = Frame(abrir_bebidas, bg='white', width=500, height=400)
    frame_bebidas.place(relx=0.5, rely=0.5, anchor='center')

    abrir_bebidas.mainloop()
#--------------------------------------------  Bebidas  --------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Bebidas Alcoólicas  ---------------------------------------------------------------------------------------------------#
def voltar2():
    bebidas_alc.withdraw()
    restaurante_do_ederson()


def bebidas_alcool():
    global bebidas_alc
    bebidas_alc = Toplevel()
    bebidas_alc.title("Restaurante do Ederson - Bebidas Alcoólicas")
    bebidas_alc.geometry('900x500')

    imagem_bg2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\bebidas-refrescantes.jpg"
    bg_imagem2 = Image.open(imagem_bg2)

    screen_width2 = bebidas_alc.winfo_screenwidth()
    screen_height2 = bebidas_alc.winfo_screenheight()
    bg_imagem2 = bg_imagem2.resize((screen_width2, screen_height2), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem2)

    bg_label2 = Label(bebidas_alc, image=bg_image_tk)
    bg_label2.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame_alcool = Frame(bebidas_alc, bg='white', width=500, height=400)
    frame_alcool.place(relx=0.5, rely=0.5, anchor='center')

    button_vo = Button(bebidas_alc, fg="white", bg="black", text="Fechar",command=voltar2)
    button_vo.place(x=900,y=450)

    bebidas_alc.mainloop()
#--------------------------------------------  Bebidas Alcoólicas  ---------------------------------------------------------------------------------------------------#

#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#
def voltar3():
    entrada.withdraw()
    restaurante_do_ederson()

def entradas():
    global entrada
    entrada = Toplevel()
    entrada.title("Restaurante do Ederson - Entrada")
    entrada.geometry('1200x800')

    # ---- Background ---- #
    imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\entrada.jpg"
    bg_imagem = Image.open(imagem_bg)

    screen_width4 = entrada.winfo_screenwidth()
    screen_height4 = entrada.winfo_screenheight()
    bg_imagem = bg_imagem.resize((screen_width4, screen_height4), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem)

    bg_label = Label(entrada, image=bg_image_tk)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    quantidade_entrada1 = StringVar()
    quantidade_entrada2 = StringVar()
    quantidade_entrada3 = StringVar()

    # ---- Primeira Entrada ---- #
    frame_entrada1 = Frame(entrada, bg='white', width=900, height=450)
    frame_entrada1.place(relx=0.25, rely=0.35, anchor='center')

    imagem_entrada1 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\salada.png"
    entrada_image1 = Image.open(imagem_entrada1)
    entrada_image1 = entrada_image1.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image1_tk = ImageTk.PhotoImage(entrada_image1)
    img_entrada1 = Label(frame_entrada1, image=entrada_image1_tk, bg='white')
    img_entrada1.image = entrada_image1_tk
    img_entrada1.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada1, text="Salada", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada1, text="R$ 10,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada1, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada1, width=5, textvariable=quantidade_entrada1).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Entrada ---- #
    frame_entrada2 = Frame(entrada, bg='white', width=900, height=450)
    frame_entrada2.place(relx=0.50, rely=0.35, anchor='center')

    imagem_entrada2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\sopa.png"
    entrada_image2 = Image.open(imagem_entrada2)
    entrada_image2 = entrada_image2.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image2_tk = ImageTk.PhotoImage(entrada_image2)
    img_entrada2 = Label(frame_entrada2, image=entrada_image2_tk, bg='white')
    img_entrada2.image = entrada_image2_tk
    img_entrada2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada2, text="Sopa", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada2, text="R$ 12,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada2, width=5, textvariable=quantidade_entrada2).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Entrada ---- #
    frame_entrada3 = Frame(entrada, bg='white', width=900, height=450)
    frame_entrada3.place(relx=0.75, rely=0.35, anchor='center')

    imagem_entrada3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\entrada\\pasta.png"
    entrada_image3 = Image.open(imagem_entrada3)
    entrada_image3 = entrada_image3.resize((200, 200), Image.Resampling.LANCZOS)
    entrada_image3_tk = ImageTk.PhotoImage(entrada_image3)
    img_entrada3 = Label(frame_entrada3, image=entrada_image3_tk, bg='white')
    img_entrada3.image = entrada_image3_tk
    img_entrada3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_entrada3, text="Pasta", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada3, text="R$ 20,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_entrada3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_entrada3, width=5, textvariable=quantidade_entrada3).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Fechar ---- #
    def voltar4():
        entrada.destroy()

    button_voltar = Button(entrada, fg="black", bg="white", text="Fechar", command=voltar4)
    button_voltar.place(relx=0.50, rely=0.90, anchor='center')

    entrada.mainloop()
#--------------------------------------------  Entrada  --------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#
def voltar4():
    escolha_da_casa.destroy()
    restaurante_do_ederson()


def escolha():
    global escolha_da_casa
    escolha_da_casa = Toplevel()
    escolha_da_casa.title("Restaurante do Ederson - Escolha da Casa")
    escolha_da_casa.geometry('1200x800')

    # ---- Background ---- #
    imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\feijoada.jpg"
    bg_imagem = Image.open(imagem_bg)

    screen_width4 = escolha_da_casa.winfo_screenwidth()
    screen_height4 = escolha_da_casa.winfo_screenheight()
    bg_imagem = bg_imagem.resize((screen_width4, screen_height4), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem)

    bg_label = Label(escolha_da_casa, image=bg_image_tk)
    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    quantidade_casa1 = StringVar()
    quantidade_casa2 = StringVar()
    quantidade_casa3 = StringVar()

    # ---- Primeira Escolha ---- #
    frame_casa1 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa1.place(relx=0.25, rely=0.35, anchor='center')

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
    Entry(frame_casa1, width=5, textvariable=quantidade_casa1).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segunda Escolha ---- #
    frame_casa2 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa2.place(relx=0.50, rely=0.35, anchor='center')

    imagem_casa2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\feijoada_potente.png"
    casa_image2 = Image.open(imagem_casa2)
    casa_image2 = casa_image2.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image2_tk = ImageTk.PhotoImage(casa_image2)
    img_casa2 = Label(frame_casa2, image=casa_image2_tk, bg='white')
    img_casa2.image = casa_image2_tk
    img_casa2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa2, text="Feijoada", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa2, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa2, width=5, textvariable=quantidade_casa2).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceira Escolha ---- #
    frame_casa3 = Frame(escolha_da_casa, bg='white', width=900, height=450)
    frame_casa3.place(relx=0.75, rely=0.35, anchor='center')

    imagem_casa3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\escolha_da_casa\\hamburguer.png"
    casa_image3 = Image.open(imagem_casa3)
    casa_image3 = casa_image3.resize((200, 200), Image.Resampling.LANCZOS)
    casa_image3_tk = ImageTk.PhotoImage(casa_image3)
    img_casa3 = Label(frame_casa3, image=casa_image3_tk, bg='white')
    img_casa3.image = casa_image3_tk
    img_casa3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_casa3, text="Hambúrguer", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa3, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_casa3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_casa3, width=5, textvariable=quantidade_casa3).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Fechar ---- #
    button_voltar = Button(escolha_da_casa, fg="black", bg="white", text="Fechar", command=voltar4)
    button_voltar.place(relx=0.50, rely=0.90, anchor='center')

    escolha_da_casa.mainloop()

#--------------------------------------------  Escolha da Casa  ------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#
def voltar5():
    doces.destroy()
    restaurante_do_ederson()

def doce():
    global doces
    doces = Toplevel()
    doces.title("Restaurante do Ederson - Doces")
    doces.geometry('1200x800')

    # ---- Background ---- #
    imagem_bg5 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\balcao-de-padaria.png"
    bg_imagem5 = Image.open(imagem_bg5)

    screen_width5 = doces.winfo_screenwidth()
    screen_height5 = doces.winfo_screenheight()
    bg_imagem5 = bg_imagem5.resize((screen_width5, screen_height5), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem5)

    bg_label5 = Label(doces, image=bg_image_tk)
    bg_label5.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Variáveis para armazenar as quantidades inseridas
    quantidade_doce1 = StringVar()
    quantidade_doce2 = StringVar()
    quantidade_doce3 = StringVar()

    # ---- Primeiro Doce ---- #
    frame_doces1 = Frame(doces, bg='white', width=900, height=450)
    frame_doces1.place(relx=0.25, rely=0.35, anchor='center')

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
    Entry(frame_doces1, width=10, textvariable=quantidade_doce1).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Segundo Doce ---- #
    frame_doces2 = Frame(doces, bg='white', width=900, height=450)
    frame_doces2.place(relx=0.50, rely=0.35, anchor='center')

    imagem_doce2 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\sorvete_do_bao.png"
    doce_image2 = Image.open(imagem_doce2)
    doce_image2 = doce_image2.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image2_tk = ImageTk.PhotoImage(doce_image2)
    img_doce2 = Label(frame_doces2, image=doce_image2_tk, bg='white')
    img_doce2.image = doce_image2_tk  # Manter referência da imagem
    img_doce2.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces2, text="Sorvete", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces2, text="R$ 15,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces2, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces2, width=10, textvariable=quantidade_doce2).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Terceiro Doce ---- #
    frame_doces3 = Frame(doces, bg='white', width=900, height=450)
    frame_doces3.place(relx=0.75, rely=0.35, anchor='center')

    imagem_doce3 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\doces\\torta_ma_num_e_reta.png"
    doce_image3 = Image.open(imagem_doce3)
    doce_image3 = doce_image3.resize((200, 200), Image.Resampling.LANCZOS)
    doce_image3_tk = ImageTk.PhotoImage(doce_image3)
    img_doce3 = Label(frame_doces3, image=doce_image3_tk, bg='white')
    img_doce3.image = doce_image3_tk 
    img_doce3.grid(row=1, column=0, padx=10, pady=10)

    Label(frame_doces3, text="Bolo de Chocolate", bg='white', font=('Times New Roman', 20)).grid(row=0, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces3, text="R$ 50,00", bg='white', font=('Times New Roman', 16)).grid(row=2, column=0, padx=10, pady=5, sticky='n')
    Label(frame_doces3, text="Quantidade: ", bg='white').grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Entry(frame_doces3, width=10, textvariable=quantidade_doce3).grid(row=3, column=0, padx=10, pady=5, sticky='n')

    # ---- Fechar ---- #
    button_volta = Button(doces, fg="black", bg="white", text="Fechar", command=voltar5)
    button_volta.place(relx=0.50, rely=0.85, anchor='center')

    doces.mainloop()
#--------------------------------------------  Doces  ----------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Carrinho  -------------------------------------------------------------------------------------------------------------#
def voltar6():
    carrinho.destroy()

def carrinhos():
    global carrinho
    carrinho = Toplevel()
    carrinho.title("Restaurante do Ederson - Carrinho")
    carrinho.geometry('1200x800')

    imagem_bg6 = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\\imagens\\background\\maquina_registradora.jpg"
    bg_imagem6 = Image.open(imagem_bg6)

    screen_width6 = carrinho.winfo_screenwidth()
    screen_height6 = carrinho.winfo_screenheight()
    bg_imagem6 = bg_imagem6.resize((screen_width6, screen_height6), Image.Resampling.LANCZOS)

    bg_image_tk = ImageTk.PhotoImage(bg_imagem6)

    bg_label6 = Label(carrinho, image=bg_image_tk)
    bg_label6.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame_buttons = Frame(carrinho, bg='white', width=500, height=400)
    frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

    button_voltar = Button(carrinho, fg="white", bg="black", text="Fechar", command=voltar6)
    button_voltar.place(x=900,y=450)

    carrinho.mainloop()
#--------------------------------------------  Carrinho  -------------------------------------------------------------------------------------------------------------#

#--------------------------------------------  Restaurante do Ederson  -----------------------------------------------------------------------------------------------#
def ver_bebidas():
    bebidas()

def ver_alcool():
    bebidas_alcool()

def ver_entrada():
    entradas()

def ver_escolha_da_casa():
    escolha()

def ver_doces():
    doce()

def ver_carrinho():
    carrinhos()

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
    
    button_car = Button(frame_buttons, fg="white", bg="palegreen4", text="Carrinho", width=15, height=3, command=ver_carrinho)
    button_car.grid(row=4, column=2, padx=10, pady=5)

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
#--------------------------------------------  Login  --------------------------------------------------------------------------------------------------------------#
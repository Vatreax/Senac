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

def abrir_carrinho():
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

    

    button_voltar = Button(carrinho, fg="white", bg="black", text="Fechar", command=carrinho.destroy)
    button_voltar.place(relx=0.50, rely=0.85, anchor='center')

    carrinho.mainloop()
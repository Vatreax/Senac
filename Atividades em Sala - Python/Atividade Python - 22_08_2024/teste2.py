from tkinter import Tk, Frame, Label, Button
from PIL import Image, ImageTk

def ver_bebidas():
    pass  # Implementar a função

def ver_alcool():
    pass  # Implementar a função

def ver_entrada():
    pass  # Implementar a função

def ver_escolha_da_casa():
    pass  # Implementar a função

def ver_doces():
    pass  # Implementar a função

# Inicialização da janela principal
restaurante_do_ederson = Tk()
restaurante_do_ederson.title("Restaurante do Ederson")
restaurante_do_ederson.geometry('1600x1080')

# Carregar e redimensionar a imagem de fundo
imagem_bg = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\imagens\Pantanal_em_Mato_Grosso_Brasil.jpg"
bg_imagem = Image.open(imagem_bg)

# Redimensionar a imagem para o tamanho da tela
screen_width = restaurante_do_ederson.winfo_screenwidth()
screen_height = restaurante_do_ederson.winfo_screenheight()
bg_imagem = bg_imagem.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

bg_image_tk = ImageTk.PhotoImage(bg_imagem)

# Adicionar imagem de fundo à janela principal
bg_label = Label(restaurante_do_ederson, image=bg_image_tk)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Faz com que a imagem cubra toda a janela

# Criação do Frame para os botões com tamanho definido
frame_buttons = Frame(restaurante_do_ederson, bg='white', width=800, height=400)
frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

# Adicionar a imagem do logo ao Frame
logo_image_path = r"Atividades em Sala - Python\\Atividade Python - 22_08_2024\imagens\logo\logotipo2.restaurante(bg).png.png"
logo_image = Image.open(logo_image_path)
logo_image_tk = ImageTk.PhotoImage(logo_image)
img_label = Label(frame_buttons, image=logo_image_tk, bg='white')  # Adicione bg='white' para compatibilidade com o fundo branco do frame
img_label.pack(pady=10)

# Texto de boas-vindas
text_user = "Usuário"  # Substitua com o nome do usuário real
texto = Label(frame_buttons, text=f"Bem Vindo {text_user}, ao Restaurante do Ederson!", bg='white', font=('Arial', 16))
texto.pack(pady=(10, 5))

# Texto adicional "Opções do Cardápio"
opcoes_texto = Label(frame_buttons, text="Opções do Cardápio", font=('Arial', 16, 'bold'), bg='white')
opcoes_texto.pack(pady=(5, 20))

# Botões
button_beb = Button(frame_buttons, fg="white", bg="black", text="Bebidas", width=15, height=3, command=ver_bebidas)
button_beb.pack(pady=5)

button_alco = Button(frame_buttons, fg="white", bg="black", text="Bebidas Alcoólicas", width=15, height=3, command=ver_alcool)
button_alco.pack(pady=5)

button_ent = Button(frame_buttons, fg="white", bg="black", text="Entrada", width=15, height=3, command=ver_entrada)
button_ent.pack(pady=5)

button_esc = Button(frame_buttons, fg="white", bg="black", text="Escolha da Casa", width=15, height=3, command=ver_escolha_da_casa)
button_esc.pack(pady=5)

button_doc = Button(frame_buttons, fg="white", bg="black", text="Doces", width=15, height=3, command=ver_doces)
button_doc.pack(pady=5)

# Inicia o loop principal da aplicação
restaurante_do_ederson.mainloop()
from tkinter import Toplevel, Button, Label
from PIL import Image, ImageTk

def voltar1():
    # Função para o botão "Fechar"
    abrir_bebidas.destroy()

abrir_bebidas = Toplevel()
abrir_bebidas.title("Restaurante do Ederson - Bebidas")
abrir_bebidas.geometry('1920x1080')

button_v = Button(abrir_bebidas, fg="white", bg="black", text="Fechar", command=voltar1)
button_v.place(x=900, y=450)

# Função para redimensionar a imagem
def load_image(file_path, width, height):
    image = Image.open(file_path)
    image = image.resize((width, 50), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

# Carregar e redimensionar imagens
img_beb1 = load_image(r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\agua_de_coco.png", 100, 100)
imgb1_label = Label(abrir_bebidas, image=img_beb1)
imgb1_label.place(x=10, y=10)

img_beb2 = load_image(r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\água_tônica.png", 100, 100)
imgb2_label = Label(abrir_bebidas, image=img_beb2)
imgb2_label.place(x=120, y=10)

img_beb3 = load_image(r"c:\Users\RafaelMontiel\Documents\imagens\bebidas\suquinho.png", 100, 100)
imgb3_label = Label(abrir_bebidas, image=img_beb3)
imgb3_label.place(x=230, y=10)

abrir_bebidas.mainloop()

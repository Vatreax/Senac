import customtkinter as ctk
from PIL import Image


produtos = ctk.CTk()
produtos.title("Produtos")
produtos.geometry("1920x1080")


my_image = ctk.CTkImage(
    light_image=Image.open(r"c:\Users\RafaelMontiel\Downloads\Img.png"),
    dark_image=Image.open(r"c:\Users\RafaelMontiel\Downloads\Img.png"),
    size=(200, 200)  
)

frame_img = ctk.CTkFrame(master=produtos, width=800, height=400, corner_radius=5,bg_color="#000000", fg_color='black',)
frame_img.place(relx=0.5,rely=0.5,anchor='center')

image_label = ctk.CTkLabel(master=frame_img, image=my_image, text="",bg_color="#000000",fg_color='Black')
image_label.grid(row=0, column=0, padx=5, pady=5)

text_label = ctk.CTkLabel(master=frame_img, text="Bola de Petiscos",font=("Verdana",15, 'bold'), bg_color="#000000",fg_color='white')
text_label.grid(row=1,column=0,padx=5,pady=5)

produtos.mainloop()

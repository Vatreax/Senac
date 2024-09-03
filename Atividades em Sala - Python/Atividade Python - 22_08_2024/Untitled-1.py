import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, messagebox

def converter_para_inteiro(s):
    try:
        return int(s)
    except ValueError:
        return None

def validar_e_converter():
    quantidade_doce1 = quantidade_doce1_var.get()
    quantidade_doce2 = quantidade_doce2_var.get()

    # Verificar se os campos estão vazios
    if quantidade_doce1 == "" or quantidade_doce2 == "":
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    # Converter para inteiros e verificar erros
    numero_doce1 = converter_para_inteiro(quantidade_doce1)
    numero_doce2 = converter_para_inteiro(quantidade_doce2)

    if numero_doce1 is None or numero_doce2 is None:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros válidos.")
    else:
        messagebox.showinfo("Conversão Bem-Sucedida", f"Quantidade Doce 1: {numero_doce1}\nQuantidade Doce 2: {numero_doce2}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversão e Validação de Quantidade")

# Variáveis StringVar
quantidade_doce1_var = StringVar()
quantidade_doce2_var = StringVar()

# Layout
Label(root, text="Quantidade Doce 1:").pack(pady=5)
Entry(root, textvariable=quantidade_doce1_var).pack(pady=5)

Label(root, text="Quantidade Doce 2:").pack(pady=5)
Entry(root, textvariable=quantidade_doce2_var).pack(pady=5)

Button(root, text="Validar e Converter", command=validar_e_converter).pack(pady=20)

root.mainloop()

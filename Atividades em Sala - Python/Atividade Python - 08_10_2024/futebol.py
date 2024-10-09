import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"Atividades em Sala - Python\Atividade Python - 08_10_2024\tabelas\Tabela_Clubes.csv")

#print(df.head(1))

print("\n-------------\n",df.info())


def classificacao_2017():
    ano_2017 = df.query('Ano in [2017]').head(21)
    print(ano_2017['Pos.'].head(21))


    plt.figure(figsize=(12, 8))
    plt.barh(ano_2017['Clubes'], ano_2017['Pos.'], color='skyblue')
    plt.xlabel('Classificação final no campeonato brasileiro daquele ano')
    plt.title('')
    plt.gca().invert_yaxis()
    plt.show()


janela_grafico = ctk.CTk()
janela_grafico.title("Lista de Gráficos")
janela_grafico._set_appearance_mode("Dark")
janela_grafico.geometry('165x250')

grafico1 = ctk.CTkButton(master=janela_grafico, text="Classificação 2017", fg_color='blue', command=classificacao_2017)
grafico1.place(x=10,y=20)

grafico2 = ctk.CTkButton(master=janela_grafico, text="Grafico 2", fg_color='red', command=None)
grafico2.place(x=10,y=60)

grafico3 = ctk.CTkButton(master=janela_grafico, text="Grafico 3", fg_color='green', command=None)
grafico3.place(x=10,y=100)

grafico4 = ctk.CTkButton(master=janela_grafico, text="Grafico 4", fg_color='yellow', command=None)
grafico4.place(x=10,y=140)

grafico5 = ctk.CTkButton(master=janela_grafico, text="Grafico 5", fg_color='purple', command=None)
grafico5.place(x=10,y=180)

janela_grafico.mainloop()
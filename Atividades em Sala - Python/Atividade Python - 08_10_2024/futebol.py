import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"Atividades em Sala - Python\Atividade Python - 08_10_2024\tabelas\Tabela_Clubes.csv")

#print(df)
#print("\n-------------\n",df.info())


def classificacao_2017():
    plt.close()
    ano_2017 = df.query('Ano in [2017]').head(21)
    print(ano_2017, "\n-----------\n")

    plt.figure(figsize=(12, 8))
    plt.barh(ano_2017['Clubes'], ano_2017['Pos.'], color='green')
    plt.xlabel('Classificação Final no Campeonato Brasileiro do Ano 2017')
    plt.title('')
    plt.gca().invert_yaxis()
    plt.show()

def derrotas_10():
    plt.close()
    derrotas = df.query('Ano in [2015] & Derrotas > 10').head(21)
    print(derrotas, "\n-----------\n")

    plt.figure(figsize=(15, 15))
    plt.bar( derrotas['Clubes'], derrotas['Derrotas'], color='red')
    plt.yticks(fontsize=7)
    plt.xticks(fontsize=7)
    plt.ylabel('')
    plt.xlabel('')
    plt.title('Clubes com o Maior Número de Derrotas, na Temporada 2015')
    plt.show()

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

def idade_Media():
    converter = []
    plt.close()
    contar = df.query('Ano in [2009]').head(15)

    explode = [0.20] * len(contar)
    
    convert = contar['Idade_Media'].head(15)
    print(convert, "\n-----------\n")
    for x in convert:
        converter.append(float(x.replace(',','.')))
#    print(converter)

    
    plt.figure(figsize=(10, 10))
    plt.pie(x=converter, explode=explode,
    labels=df['Clubes'].head(15), rotatelabels=True, autopct = autopct_format(converter))
    plt.text(0, 1.55, 'Idade Média dos Jogadores por Clube \n   Na Temporada 2009', va='center', ha='center', fontsize=10, fontweight='bold')
    plt.show()

def quantidade():
    plt.close()
    Quantidade = df.query('Ano in [2010] & Qtd_Jogadores > 50').head(21)
    print(Quantidade, "\n-----------\n")

    plt.figure(figsize=(15, 15))
    plt.bar( Quantidade['Clubes'], Quantidade['Qtd_Jogadores'], color='skyblue')
    plt.yticks(fontsize=7)
    plt.xticks(fontsize=7)
    plt.ylabel('')
    plt.xlabel('')
    plt.title('Clubes com a Maior Quantidade de Jogadores, na Temporada 2010')
    plt.show()

def vitorias():
    plt.close()
    victory = df.query('Ano in [2011] & Vitorias > 12').head(30)
    print(victory, "\n-----------\n")

    plt.figure(figsize=(12, 8))
    plt.barh(victory['Clubes'], victory['Vitorias'], color='gold')
    plt.xlabel('Maior Número de Vitórias, na Temporada 2011', fontsize=10, fontweight='bold')
    plt.title('')
    plt.show()

janela_grafico = ctk.CTk()
janela_grafico.title("Lista de Gráficos")
janela_grafico._set_appearance_mode("Dark")
janela_grafico.geometry('165x225')

grafico1 = ctk.CTkButton(master=janela_grafico, text="Classificação 2017", fg_color='green', command=classificacao_2017)
grafico1.place(x=10,y=20)

grafico2 = ctk.CTkButton(master=janela_grafico, text="Mais Derrotas", fg_color='red', command=derrotas_10)
grafico2.place(x=10,y=60)

grafico3 = ctk.CTkButton(master=janela_grafico, text=("Idade Média"), text_color='white', fg_color='black', command=idade_Media)
grafico3.place(x=10,y=100)

grafico4 = ctk.CTkButton(master=janela_grafico, text="Qtd Jogadores", text_color='white', fg_color='skyblue', command=quantidade)
grafico4.place(x=10,y=140)

grafico5 = ctk.CTkButton(master=janela_grafico, text="Mais Vitórias", text_color='black', fg_color='gold', command=vitorias)
grafico5.place(x=10,y=180)

janela_grafico.mainloop()
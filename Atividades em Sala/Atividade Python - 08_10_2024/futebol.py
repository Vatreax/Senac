import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------- Classe para o Customtkinter ------------------------- #
class aplicar_tela():
    def __init__(self) -> None:
        super().__init__()
        
    def set_botoes(self, master, text, text_color, fg_color, command, x, y):
        self.button = ctk.CTkButton(master=master,
                                    text=text,
                                    text_color=text_color,
                                    fg_color=fg_color,
                                    command=command,
                                    font=('Arial', 12, 'bold'))
        self.button.place(x=x,
                          y=y)

    def set_text(self,master, text, font, num, intense, x, y, anchor):

        self.label = ctk.CTkLabel(master=master, 
                                        text=text,
#                                        fg_color=master.cget('bg'),  
                                        font=(font,num,intense), 
                                        )
        
        self.label.place(x=x,
                               y=y, 
                               anchor=anchor)
    
    def sete_text_box(self,text,master,width,height,font,num,index,state,x,y):
        self.texto = text
        self.textbox = ctk.CTkTextbox(master, 
                                width=width, 
                                height=height, 
                                font=(font, num))
        self.textbox.insert(index, text)
        self.textbox.configure(state=state) 
        self.textbox.place(x=x,y=y)

df = pd.read_csv(r"Atividades em Sala - Python\Atividade Python - 08_10_2024\tabelas\Tabela_Clubes.csv")

#print(df)
#print("\n-------------\n",df.info())

class graficos():
    def __init__(self) -> None:
        super().__init__()

# ------------------------- Gráficos ------------------------- #
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
    print(contar, "\n-----------\n")
    for x in convert:
        converter.append(float(x.replace(',','.')))

    plt.figure(figsize=(10, 10))
    plt.pie(x=converter, explode=explode,
    labels=contar['Clubes'].head(15), rotatelabels=True, autopct = autopct_format(converter))
    plt.text(0, 1.55, 'Média de Idade dos Jogadores por Clube \n   Na Temporada 2009', va='center', ha='center', fontsize=10, fontweight='bold')
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

# ------------------------- Customtkinter ------------------------- #
janela_grafico = ctk.CTk()
janela_grafico.title("Campeonato Brasileiro")
janela_grafico._set_appearance_mode("Dark")
janela_grafico.geometry('425x250')

tela = aplicar_tela()

# -- Titulo
tela.set_text(janela_grafico, 
              'Campeonato Brasileiro 2009-2018' + '\nAnálise dos dados dos times do campeonato brasileiro', 
              'Times New Roman', 18, 'bold', 212, 20, 'center')
# -- Botão 1
tela.set_botoes(janela_grafico, "Classificação 2017", 'white', 'green', classificacao_2017, 60, 65)
# -- Botão 2
tela.set_botoes(janela_grafico, "Mais Derrotas 2015", 'white', 'red', derrotas_10, 210, 65)
# -- Botão 3
tela.set_botoes(janela_grafico, "Média de Idade 2009", 'white', 'black', idade_Media, 60, 105)
# -- Botão 4
tela.set_botoes(janela_grafico, "Qtd Jogadores 2010", 'white', 'skyblue', quantidade, 210, 105)
# -- Botão 5
tela.set_botoes(janela_grafico, "Mais Vitórias 2011", 'black', 'gold', vitorias, 135, 145)
# -- link
tela.sete_text_box("Fonte: https://www.kaggle.com/datasets/andreifnmg/campeonato-braileiro-20092018",
                   janela_grafico, 415, 10, 'Arial', 10, "0.0", 'normal', 5, 200)

janela_grafico.mainloop()

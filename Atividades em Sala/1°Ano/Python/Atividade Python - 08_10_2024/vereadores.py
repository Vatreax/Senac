import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------- Vereadores -------------------------------------------------------------------------------- #
def vereadores():
    global verea
    plt.close()
    
    votos = [8567, 8128, 6912, 6409, 6371, 6314, 6271, 6131, 5355, 5050,
             5003, 4982, 4782, 4641, 4577, 4576, 4236, 4179, 4148, 4119,
             4063, 4030, 4022, 3922, 3877, 3859, 3768, 3693, 3648, 3636]

    porcentagem = [1.95, 1.85, 1.57, 1.46, 1.45, 1.44, 1.43, 1.39, 1.22, 1.15, 
                   1.14, 1.13, 1.09, 1.06, 1.04, 1.04, 0.96, 0.95, 0.94, 0.94, 
                   0.92, 0.92, 0.91, 0.89, 0.88, 0.88, 0.86, 0.84, 0.83, 0.83]

    nomes = [
        'Marquinhos Trad', 'Rafael Tavares', 'Carlão Comunitário Mesmo',
        'Silvio Pitu', 'Veterinário Francisco', 'Fabio Rocha',
        'Professor Riverton', 'Junior Coringa', 'Dr Victor Rocha',
        'Professor Juari', 'Flavio Cabo Almi', 'Luiza Ribeiro',
        'André Salineiro Agente Federal', 'Papy', 'Ana Portela',
        'Neto Santos', 'Maicon Nogueira', 'Delei Pinheiro',
        'Wilson Lands', 'Herculano Borges', 'Beto Avelar',
        'Dr Jamal', 'Landmark', 'Dr Sandro', 'Betinho',
        'Clodoilson Pires', 'Jean Ferreira', 'Professor João Rocha',
        'Valdir Gomes', 'Dr Lívio'
    ]

    verea = pd.DataFrame({
        'Nome': nomes,
        'Votos': votos,
        'Porcentagem': porcentagem
    })



    plt.figure(figsize=(12, 8))
    plt.barh(verea['Nome'], verea['Votos'], color='skyblue')
    plt.xlabel('Número de Votos')
    plt.title('Quantidade de Votos por Vereador - Campo Grande')
    plt.gca().invert_yaxis()
    plt.show()

def vereadores_banco():
    print(verea)
    verea.to_csv('vereadores.csv',sep=';',index=False,encoding='utf-8-sig')
# ------------------------------------------------- Vereadores -------------------------------------------------------------------------------- #

# ------------------------------------------------- Campo Grande -------------------------------------------------------------------------------- #
def campo_grande():
    global cg
    plt.close()    
    nomes = ['Adriane Lopes', 'Rose Modesto', 'Beto Pereira']
    votos = [140913, 131525, 115516]
    porcentagem = [31.67, 29.56, 25.96]

    cg = pd.DataFrame({
        'Nome': nomes,
        'Votos': votos,
        'Porcentagem': porcentagem
    })

    plt.figure(figsize=(12, 8))
    plt.barh(cg['Nome'], cg['Votos'], color='skyblue')
    plt.xlabel('Número de Votos')
    plt.title('Quantidade de Votos dos Candidatos a Prefeito - Campo Grande')
    plt.gca().invert_yaxis()
    plt.show()



def campo_banco():
    print(cg)
    cg.to_csv('cg.csv',sep=';',index=False,encoding='utf-8-sig')
# ------------------------------------------------- Campo Grande -------------------------------------------------------------------------------- #


# ------------------------------------------------- Corumbá -------------------------------------------------------------------------------- #
def corumba():
    global cmb
    plt.close()    
    nomes = ['Dr. Gabriel', 'Luiz Antonio Pardal', 'André Campos']
    votos = [28394, 10659, 5944]
    porcentagem = [56.74, 21.30, 11.88]

    cmb = pd.DataFrame({
        'Nome': nomes,
        'Votos': votos,
        'Porcentagem': porcentagem
    })

    plt.figure(figsize=(12, 8))
    plt.barh(cmb['Nome'], cmb['Votos'], color='skyblue')
    plt.xlabel('Número de Votos')
    plt.title('Quantidade de Votos dos Candidatos a Prefeito - Corumbá')
    plt.gca().invert_yaxis()
    plt.show()



def corumba_banco():
    print(cmb)
    cmb.to_csv('corumba.csv',sep=';',index=False,encoding='utf-8-sig')
# ------------------------------------------------- Corumbá -------------------------------------------------------------------------------- #

# ------------------------------------------------- Dourados -------------------------------------------------------------------------------- #
def dourados():
    global dd
    plt.close()    
    nomes = ['Marçal Filho', 'Alan Guedes', 'Tiago Botelho']
    votos = [60418, 34027, 17845]
    porcentagem = [50.05, 28.19, 14.78]

    dd = pd.DataFrame({
        'Nome': nomes,
        'Votos': votos,
        'Porcentagem': porcentagem
    })

    plt.figure(figsize=(12, 8))
    plt.barh(dd['Nome'], dd['Votos'], color='skyblue')
    plt.xlabel('Número de Votos')
    plt.title('Quantidade de Votos dos Candidatos a Prefeito - Dourados')
    plt.gca().invert_yaxis()
    plt.show()

    print(dd)

def dourados_banco():
    print(dd)
    dd.to_csv('dourados.csv',sep=';',index=False,encoding='utf-8-sig')    
# ------------------------------------------------- Dourados -------------------------------------------------------------------------------- #

def tres_lagoas():
    global tl
    plt.close()    
    nomes = ['Dr. Cassiano Maia', 'Dr. Ruy Costa', 'Professor Vitor']
    votos = [38076, 16027, 1392]
    porcentagem = [ 68.61, 28.88, 2.51]

    tl = pd.DataFrame({
        'Nome': nomes,
        'Votos': votos,
        'Porcentagem': porcentagem
    })

    plt.figure(figsize=(12, 8))
    plt.barh(tl['Nome'], tl['Votos'], color='skyblue')
    plt.xlabel('Número de Votos')
    plt.title('Quantidade de Votos dos Candidatos a Prefeito - Três Lagoas')
    plt.gca().invert_yaxis()
    plt.show()

def tres_banco():
    print(tl)
    tl.to_csv('tres_lagoas.csv',sep=';',index=False,encoding='utf-8-sig')    

janela_grafico = ctk.CTk()
janela_grafico.title("Lista de Gráficos")
janela_grafico._set_appearance_mode("Dark")
janela_grafico.geometry('310x250')

vereadore_campo_grande = ctk.CTkButton(master=janela_grafico, text="Vereadores", fg_color='blue', bg_color='white', command=vereadores)
vereadore_campo_grande.place(x=10,y=20)

campo = ctk.CTkButton(master=janela_grafico, text="Campo Grande", fg_color='red', bg_color='white', command=campo_grande)
campo.place(x=10,y=60)

corum = ctk.CTkButton(master=janela_grafico, text="Corumbá", fg_color='red', bg_color='white', command=corumba)
corum.place(x=10,y=100)

doura = ctk.CTkButton(master=janela_grafico, text="Dourados", fg_color='red', bg_color='white', command=dourados)
doura.place(x=10,y=140)

tres = ctk.CTkButton(master=janela_grafico, text="Três Lagoas", fg_color='red', bg_color='white', command=tres_lagoas)
tres.place(x=10,y=180)

vereadore_panda = ctk.CTkButton(master=janela_grafico, text="Exportar Vereadores", fg_color='blue', bg_color='white', command=vereadores_banco)
vereadore_panda.place(x=160,y=20)

campo_panda = ctk.CTkButton(master=janela_grafico, text="Exportar - CG", fg_color='green', bg_color='white', command=campo_banco)
campo_panda.place(x=160,y=60)

corum_panda = ctk.CTkButton(master=janela_grafico, text="Exportar - CMB", fg_color='green', bg_color='white', command=corumba_banco)
corum_panda.place(x=160,y=100)

doura_panda = ctk.CTkButton(master=janela_grafico, text="Exportar - DRD", fg_color='green', bg_color='white', command=dourados_banco)
doura_panda.place(x=160,y=140)

tres_panda = ctk.CTkButton(master=janela_grafico, text="Exportar - TRL", fg_color='green', bg_color='white', command=tres_banco)
tres_panda.place(x=160,y=180)

janela_grafico.mainloop()
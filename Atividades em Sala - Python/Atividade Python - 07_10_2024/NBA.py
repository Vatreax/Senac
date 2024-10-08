import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\RafaelMontiel\\documents\\senac\\Atividades em Sala - Python\\Atividade Python - 07_10_2024\\all_seasons.csv")

def graf1():
    plt.close()
    altura = df.loc[0:11145, ['player_height']]
    peso = df.loc[0:11145, ['player_weight']]

    plt.ylabel(u'Altura')
    plt.xlabel(u'Peso')
#    x = (1,2,3,4,5,6)
#    y = (1,2,3,4,5,6)
    plt.title('Meu Grafico')
#    plt.plot(x,y)
    plt.plot(altura,peso)
    plt.show()

def faz_o_L():
    plt.close()
    a = (100,1,1,1)
    b = (1,1,1,4)
    plt.plot(a,b)
    plt.show()



janela_grafico = ctk.CTk()
janela_grafico.title("Gráficos")
janela_grafico._set_appearance_mode("Dark")
janela_grafico.geometry('250x250')

graficozinho = ctk.CTkButton(master=janela_grafico, text="Grafico 1", fg_color='blue', bg_color='white', command=graf1)
graficozinho.place(x=50,y=50)

o_l = ctk.CTkButton(master=janela_grafico, text="Faz o L", fg_color='red', bg_color='white', command=faz_o_L)
o_l.place(x=50,y=100)



janela_grafico.mainloop()

















# --------------------------------------------- Explicação ------------------------------------------------------------- #
#a = (100,1,1,1)
#b = (1,1,1,4)

#a = (1,2,3,4,5)
#b = (1,2,3,4,5)

#plt.ylabel(u'Altura')
#plt.xlabel(u'Peso')
#plt.plot(a,b,'r')
#plt.show()

#x = (1,2,3,4,5,6)
#y = (1,2,3,4,5,6)

#plt.xlabel('Eixo X')
#plt.ylabel('Eixo Y')

#plt.plot((1,2,3,4), (1,4,9,16), 'mD:')
#plt.axis(0,6)

#x= np.linspace(0,1,num=100)
#y= x

#plt.plot(x,y,'r--')
#z = [t**2 for t in x]

#plt.plot(x,z,'bo')

#w = [t**3 for t in x]
#plt.title('Meu Grafito')
#plt.plot(x,w,'g^')
#plt.show()

#a = (1,2,3,4,5,6)
#b = (2,4,6,8,10,12)

#plt.scatter(a,b)
#plt.bar(a,b)
#plt.hist(a,b)
#plt.show()


#a = (10,20,30)
#explode = (0.1,0,0)
#labels = ['HB20', "Gol", "Fusca"]

#plt.pie(a, explode=explode,
#labels=labels, autopct='%.2f%%', shadow=True)
#plt.title("Meu Grafico")
#plt.grid(True)
#plt.show()
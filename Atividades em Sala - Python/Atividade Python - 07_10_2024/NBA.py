import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\RafaelMontiel\\documents\\senac\\Atividades em Sala - Python\\Atividade Python - 07_10_2024\\all_seasons.csv")

altura = df.loc[0:11145, ['player_height']]
peso = df.loc[0:11145, ['player_weight']]

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

x= np.linspace(0,1,num=100)
y= x

plt.plot(x,y,'r--')
z = [t**2 for t in x]

plt.plot(x,z,'bo')

w = [t**3 for t in x]
plt.title('Meu Grafito')
plt.plot(x,w,'g^')
plt.show()


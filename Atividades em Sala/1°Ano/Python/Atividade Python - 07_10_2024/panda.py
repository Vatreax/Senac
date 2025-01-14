import pandas as pd

#print(pd.__version__)

df= pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#print(df.head(11))

#print("\n-------------\n",df.info())

#df.set_index('PassengerId', inplace=True)
#print(df.head(12))

#print("\n------------------\n",df.columns)

#print("\n------------------\n",df.values)

#print("\n------------------\n",df.loc[1])

#print(df.loc[[1,2,],['Name','Sex','Age']])

#print(df.loc[0:30:5])

# Especificando as colunas a serem selecionadas
#print(df.loc[1:10, ['Name','Sex','Age']])

# Faz o tratamento de acordo com as especificações
#print(df.query('Age > 20').head(),'\n-------------\n')
#print(df.query('Age > 20'))

#print(df.query('Age > 20 & Sex=="female"').head())

#df.to_csv('dataset.csv',sep=';',index=False,encoding='utf-8-sig')



# ---------------------------------------- Atividade ------------------------------------------------------ #

# Quantas Crianças Abaixo de 10 Anos Sobreviveram
kid =  df.query('Age < 10')
print(" \n------ 1 ------- \n", "Crianças Menores de 10 Sobreviventes:", kid.count()['Survived'],"\n --------------- \n")
kid.to_csv('kid.csv',sep=';',index=False,encoding='utf-8-sig')

# Quantas Mulheres Sobreviveram
print(" \n------ 2 ------- \n", "Mulheres Sobreviventes:",df.query('Survived > 0 & Sex=="female"').count()['Survived'],"\n --------------- \n")

# Quantos Homens Sobreviveram
print(" \n------ 3 ------- \n", "Homens sobreviventes:",df.query('Survived > 0 & Sex=="male"').count()['Survived'],"\n --------------- \n")

# Quantos Idosos Acima de 50 anos sobreviveram?
print(" \n------ 4 ------- \n", "Idosos Sobreviventes:",df.query('Age >= 50').count()['Survived'],"\n --------------- \n")

# Quantas Crianças Sobreviveram
print(" \n------ 5 ------- \n", "Crianças Sobreviventes:",df.query('Age < 12 & Sex=="female"').count()['Survived'],"\n --------------- \n")
#    Crie um sistema de login utilizando o tkinter e importando um banco de dados.
#    A tarefa é criar 5 tipos diferentes de acesso (esses devem ser armazenados em banco), 
#    para cada acesso deve ser criada uma tela diferente de amostragem (uma imagem ou uma mensagem) 
#    quando o usuário colocar algum acesso que não existe no banco deve surgir uma mensagem avisando 
#    que este acesso não existe e perguntando se ele deseja criar um cadastro, 
#    se ele desejar deve ser feito o cadastro dele e enviado ao banco, caso o usuário digite a senha incorretamente deve surgir a mensagem de senha incorreta.
#    O cadastro deve conter: usuário, senha e um texto que ele deseje armazenar em seu cadastro (se voce quiser um desafio maior pode armazenar uma imagem)
#    Dica: https://acervolima.com/crie-uma-pagina-de-login-do-banco-de-dados-mysql-em-python-usando-tkinter/

import tkinter as tk
import mysql.connector
from tkinter import *

registros = Tk()
registros.geometry("400x400")
registros.config(bg='navy blue')
registros.title("cadastro")

def submitact():
     
    user = usuario_entry.get()
    passw = senha_entry.get()
  
    print(f"O nome inserido foi {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    
    
    if passw:
        db = mysql.connector.connect(host ="Um server ai",
                                     user = user,
                                     password = passw,
                                     db ="College")
        cursor = db.cursor()
         
    
    
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="College")
        cursor = db.cursor()
         
    
    savequery = "select * from STUDENT"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
       
      for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")

texto = Label(registros, text="Preencha os dados Abaixo", font=('arial',18,'bold'), bg='white')
texto.place(relx=0.50, rely=0.15, anchor='center')

usuario_label = Label(registros, text="Usuario:", font=('arial',15,'bold'), bg='white')
usuario_label.place(relx=0.50, rely=0.28, anchor='center')
usuario_entry = Entry(registros, font=('arial',15), bg='white')
usuario_entry.place(relx=0.50, rely=0.35, anchor='center')

senha_label = Label(registros, text="Senha:", font=('arial',15,'bold'), bg='white')
senha_label.place(relx=0.50, rely=0.43, anchor='center')
senha_entry = Entry(registros, show="*", font=('arial',15), bg='white')
senha_entry.place(relx=0.50, rely=0.50, anchor='center')

cadastro_button = Button(registros, text="Login",font=('arial',15,'bold'), bg='white', command=None)
cadastro_button.place(relx=0.50, rely=0.67, anchor='center')



registros.mainloop()
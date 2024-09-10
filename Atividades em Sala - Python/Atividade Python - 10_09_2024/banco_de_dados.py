#    Crie um sistema de login utilizando o tkinter e importando um banco de dados.
#    A tarefa é criar 5 tipos diferentes de acesso (esses devem ser armazenados em banco), 
#    para cada acesso deve ser criada uma tela diferente de amostragem (uma imagem ou uma mensagem) 
#    quando o usuário colocar algum acesso que não existe no banco deve surgir uma mensagem avisando 
#    que este acesso não existe e perguntando se ele deseja criar um cadastro, 
#    se ele desejar deve ser feito o cadastro dele e enviado ao banco, caso o usuário digite a senha incorretamente deve surgir a mensagem de senha incorreta.
#    O cadastro deve conter: usuário, senha e um texto que ele deseje armazenar em seu cadastro (se voce quiser um desafio maior pode armazenar uma imagem)
#    Dica: https://acervolima.com/crie-uma-pagina-de-login-do-banco-de-dados-mysql-em-python-usando-tkinter/


import mysql.connector
from tkinter import *
from tkinter import messagebox



def cadastrar():
    registros.destroy()
    def Destruir():
        messagebox.showwarning("Atenção","Abra novamente o sistema")
        cadastro.destroy()



    cadastro = Tk()
    cadastro.geometry("400x400")

    voltar_button = Button(cadastro, text="Registrar",font=('arial',15,'bold'), bg='white', command= Destruir)
    voltar_button.place(relx=0.46, rely=0.85, anchor='center')
    cadastro.mainloop()


def submitact():
     
    usuario = usuario_entry.get()
    senha = senha_entry.get()
  
    print(f"O nome inserido foi {usuario} {senha}")
  
    logintodb(usuario, senha)
  
 
def logintodb(usuario, senha):
    
    if senha:
        dataBase = mysql.connector.connect( 
                            host = "10.28.2.39", 
                            user = "suporte", 
                            password = "suporte", 
                            database = "registros")

        savequery = "select * from registros.login"

        cursor = dataBase.cursor()
        

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
    
        for x in myresult:
            print(x)

        print("Query Excecuted successfully")

    except:
        dataBase.rollback()
        print("Error occured")

registros = Tk()
registros.geometry("400x400")
registros.config(bg='navy blue')
registros.title("Banco de Dados")

texto = Label(registros, text="MySQL Teste", font=('arial',18,'bold'), bg='white')
texto.place(relx=0.50, rely=0.15, anchor='center')

usuario_label = Label(registros, text="Usuario:", font=('arial',15,'bold'), bg='white')
usuario_label.place(relx=0.50, rely=0.28, anchor='center')
usuario_entry = Entry(registros, font=('arial',15), bg='white')
usuario_entry.place(relx=0.50, rely=0.35, anchor='center')

senha_label = Label(registros, text="Senha:", font=('arial',15,'bold'), bg='white')
senha_label.place(relx=0.50, rely=0.43, anchor='center')
senha_entry = Entry(registros, show="*", font=('arial',15), bg='white')
senha_entry.place(relx=0.50, rely=0.50, anchor='center')

texto_label = Label(registros, text="Texto", font=('arial',15,'bold'), bg='white')
texto_label.place(relx=0.50, rely=0.59, anchor='center')
texto_entry = Entry(registros, show="*", font=('arial',15), bg='white')
texto_entry.place(relx=0.50, rely=0.65, anchor='center')

submeter_button = Button(registros, text="Inserir",font=('arial',15,'bold'), bg='white', command=submitact)
submeter_button.place(relx=0.35, rely=0.85, anchor='center')

cadastro_button = Button(registros, text="Cadastrar",font=('arial',15,'bold'), bg='white', command=cadastrar)
cadastro_button.place(relx=0.65, rely=0.85, anchor='center')


registros.mainloop()


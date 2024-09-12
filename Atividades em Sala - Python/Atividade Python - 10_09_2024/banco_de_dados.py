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

global usuario,senha,cursor,dataBase

def logar():
    global usuario, senha
    usuario = usuario_entry.get()
    senha = senha_entry.get()


    
    if usuario and senha:
        if verificar_login(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            inserir_texto = Toplevel()
            inserir_texto.title("Inserir Texto")
            inserir_texto.geometry('300x300')

            def escrever():
                escreva = texto_entry.get()
                sql = f"UPDATE login SET texto = '{escreva}' WHERE usuario = '{usuario} and senha = {senha}'"

                cursor.execute(sql)
                dataBase.commit()
                

                myresult = cursor.fetchall()

                for x in myresult:
                    print(x)
                    
                print("Query Excecuted successfully")
                dataBase.close()

            texto_label = Label(inserir_texto, text="Texto", font=('arial',15,'bold'), bg='white')
            texto_label.place(relx=0.50, rely=0.25, anchor='center')
            texto_entry = Entry(inserir_texto, font=('arial',15), bg='white')
            texto_entry.place(relx=0.50, rely=0.35, anchor='center')

            escreve_button = Button(inserir_texto, text="Escrever", font=('arial',15,'bold'), bg='white', command=escrever)
            escreve_button.place(relx=0.50, rely=0.48, anchor='center')



            inserir_texto.mainloop()
        else:
            messagebox.showerror("Login", "Usuário ou senha inválidos.")
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

def verificar_login(usuario, senha):
    try:
        
        dataBase = mysql.connector.connect(
            host="10.28.2.39",
            user="suporte",
            password="suporte",
            database="registros"
        )
        cursor = dataBase.cursor()

        sql = "SELECT * FROM login WHERE usuario = %s AND senha = %s"
        cursor.execute(sql, (usuario, senha))
        
        resultado = cursor.fetchone()
        
        cursor.close()
        
        return resultado is not None

    except mysql.connector.Error:
        print(f"Erro","Login Fracassado")


registros = Tk()
registros.geometry("400x400")
registros.config(bg='navy blue')
registros.title("Banco de Dados")

texto = Label(registros, text="MySQL Teste", font=('arial',18,'bold'), bg='white')
texto.place(relx=0.50, rely=0.15, anchor='center')

usuario_label = Label(registros, text="Usuário:", font=('arial',15,'bold'), bg='white')
usuario_label.place(relx=0.50, rely=0.28, anchor='center')
usuario_entry = Entry(registros, font=('arial',15), bg='white')
usuario_entry.place(relx=0.50, rely=0.35, anchor='center')

senha_label = Label(registros, text="Senha:", font=('arial',15,'bold'), bg='white')
senha_label.place(relx=0.50, rely=0.43, anchor='center')
senha_entry = Entry(registros, font=('arial',15), bg='white')
senha_entry.place(relx=0.50, rely=0.50, anchor='center')

submeter_button = Button(registros, text="Inserir", font=('arial',15,'bold'), bg='white', command=logar)
submeter_button.place(relx=0.35, rely=0.85, anchor='center')

cadastro_button = Button(registros, text="Cadastrar", font=('arial',15,'bold'), bg='white', command=None)
cadastro_button.place(relx=0.65, rely=0.85, anchor='center')

registros.mainloop()

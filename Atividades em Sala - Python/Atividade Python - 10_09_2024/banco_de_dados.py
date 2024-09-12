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

global usuario,senha,cursor,dataBase,registros


# ------------------------------------------- TEXTO ---------------------------------------------------------------------------------------- #
def logar():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    if usuario and senha:
        if verificar_login(usuario, senha):
            messagebox.showinfo("Login", f"Login bem-sucedido!\nUsuário: {usuario}\nSenha: {senha}")
            inserir_texto = Toplevel()
            inserir_texto.title("Inserir Texto")
            inserir_texto.geometry('300x200')
            inserir_texto.config(bg='deepskyblue4')
            def escrever():
                escreva = texto_entry.get().strip()

                if escreva == '':
                    messagebox.showwarning("Aviso","Campo Vazio")
                
                else:
                    sql = "UPDATE login SET texto = %s WHERE usuario = %s and senha = %s"

                    dataBase = mysql.connector.connect(
                    host="10.28.2.39",
                    user="suporte",
                    password="suporte",
                    database="registros")

                    try:
                        cursor = dataBase.cursor()
                        cursor.execute(sql, (escreva,usuario,senha))
                        dataBase.commit()
                        dataBase.close()
                        messagebox.showinfo("Texto Inserido",f"Operação Realizada com Sucesso.\nTexto Inserido: {escreva}")
                        inserir_texto.destroy()
                        registros.destroy()

                    except mysql.connector.Error as n1:
                        messagebox.showerror("Erro ",f"Erro: {n1}")

            texto_label = Label(inserir_texto, text="Texto", font=('arial',15,'bold'), fg='white', bg='deepskyblue4')
            texto_label.place(relx=0.50, rely=0.20, anchor='center')
            texto_entry = Entry(inserir_texto, font=('arial',15), bg='white')
            texto_entry.place(relx=0.50, rely=0.35, anchor='center')

            escreve_button = Button(inserir_texto, text="Escrever", font=('arial',15,'bold'), fg='white',bg='deepskyblue4', command=escrever)
            escreve_button.place(relx=0.50, rely=0.60, anchor='center')




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
        
        
        return resultado is not None

    except mysql.connector.Error:
        print(f"Erro","Login Fracassado")
# ------------------------------------------- TEXTO ------------------------------------------------------------------------------------------- #

# ---------------------------------- CADASTRO ------------------------------------------------------------------------------------------------- #

def cadastrar():
    global novo_entry, nova_senha_entry, confirmar_senha_entry, abrir_cadastro
    registros.destroy()

    abrir_cadastro = Tk()
    abrir_cadastro.title("Cadastro")
    abrir_cadastro.geometry("425x425")
    abrir_cadastro.config(bg='floralwhite')

    frame_cad = Frame(abrir_cadastro, bg='deepskyblue4', width=350, height=350)
    frame_cad.place(relx=0.50, rely=0.50, anchor='center')

    
    titulo = Label(frame_cad, text="Cadastrar", font=('Times New Roman',18,'bold'), fg='white',bg='deepskyblue4')
    titulo.place(relx=0.50, rely=0.15, anchor='center')

    novo_label = Label(frame_cad, text="Usuário:", font=('arial',12,'bold'),  fg='white',bg='deepskyblue4')
    novo_label.place(relx=0.29, rely=0.28, anchor='center')
    novo_entry = Entry(frame_cad, font=('arial',15))
    novo_entry.place(relx=0.50, rely=0.35, anchor='center')

    nova_senha_label = Label(frame_cad, text="Senha:", font=('arial',12,'bold'),  fg='white',bg='deepskyblue4')
    nova_senha_label.place(relx=0.27, rely=0.45, anchor='center')
    nova_senha_entry = Entry(frame_cad, font=('arial',15), show='*')
    nova_senha_entry.place(relx=0.50, rely=0.52, anchor='center')

    confirmar_senha_label = Label(frame_cad, text="Confirmar Senha:", font=('arial',12,'bold'), fg='white',bg='deepskyblue4')
    confirmar_senha_label.place(relx=0.38, rely=0.63, anchor='center')
    confirmar_senha_entry = Entry(frame_cad, font=('arial',15), show='*')
    confirmar_senha_entry.place(relx=0.50, rely=0.70, anchor='center')

    voltar_button = Button(frame_cad, text="Voltar", font=('arial',12,'bold'),  width=8, height=1, fg='white',bg='deepskyblue4', command=lambda: (abrir_cadastro.destroy(),abrir_registros()))
    voltar_button.place(relx=0.32, rely=0.85, anchor='center')

    confirm_button = Button(frame_cad, text="Confirmar", font=('arial',12,'bold'), width=8, height=1, fg='white', bg='deepskyblue4', command=novo_usuario)
    confirm_button.place(relx=0.68, rely=0.85, anchor='center')



def novo_usuario():

    user = novo_entry.get().strip()
    passw = nova_senha_entry.get().strip()
    passw_conf = confirmar_senha_entry.get().strip()

    if user == '' or passw == '' or passw_conf == '':
        messagebox.showerror("Erro","Todos os campos devem ser preenchidos!")
    
    elif passw != passw_conf:
        messagebox.showerror("Erro","As senhas devem ser iguais")

    elif passw == user:
        messagebox.showerror("Erro","Usuário e senha não podem ser iguais")
    
    else:
        try:

            dataBase = mysql.connector.connect(
            host="10.28.2.39",
            user="suporte",
            password="suporte",
            database="registros"
        )
            cursor = dataBase.cursor()
            
            select_usuario = "SELECT * FROM login WHERE usuario = %s"
            cursor.execute(select_usuario, (user,))
            result = cursor.fetchone()

            if result:
                messagebox.showerror("Erro","Usuario já existe!")

            else:
                insertando = "INSERT INTO login (usuario,senha) VALUES (%s,%s)"
                cursor.execute(insertando,(user,passw))
                dataBase.commit()
                messagebox.showinfo("Sucesso","Novo Usuario Registrado")
                abrir_cadastro.destroy()
                abrir_registros()

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Deu Erro. {err}")
            

        finally:
            cursor.close()
            dataBase.close()
        


# ----------------------------------- CADASTRO ------------------------------------------------------------------------------------------------- #

# ------------------------------------------- PRINCIPAL ---------------------------------------------------------------------------------------- #

def abrir_registros():
    global usuario_entry,senha_entry, registros
    registros = Tk()
    registros.geometry("425x425")
    registros.config(bg='floralwhite')
    registros.title("Banco de Dados")

    frame = Frame(registros, bg='deepskyblue4', width=350, height=350)
    frame.place(relx=0.50, rely=0.50, anchor='center')

    texto = Label(frame, text="MySQL", font=('Times New Roman',18,'bold'), fg='white', bg='deepskyblue4')
    texto.place(relx=0.50, rely=0.15, anchor='center')

    usuario_label = Label(frame, text="Usuário:", font=('arial',12,'bold'), fg='white', bg='deepskyblue4')
    usuario_label.place(relx=0.30, rely=0.28, anchor='center')
    usuario_entry = Entry(frame, font=('arial',15), fg='black')
    usuario_entry.place(relx=0.50, rely=0.35, anchor='center')

    senha_label = Label(frame, text="Senha:", font=('arial',12,'bold'), fg='white', bg='deepskyblue4')
    senha_label.place(relx=0.28, rely=0.45, anchor='center')
    senha_entry = Entry(frame, font=('arial',15), fg='black', show='*')
    senha_entry.place(relx=0.50, rely=0.52, anchor='center')

    submeter_button = Button(frame, text="Inserir", font=('arial',15,'bold'), width=8, height=1, fg='white', bg='deepskyblue4', command=logar)
    submeter_button.place(relx=0.30, rely=0.85, anchor='center')

    cadastro_button = Button(frame, text="Cadastrar", font=('arial',15,'bold'), width=8, height=1,fg='white', bg='deepskyblue4', command=cadastrar)
    cadastro_button.place(relx=0.67, rely=0.85, anchor='center')

    texto1 = Label(frame, text="Clique para\n Inserir Texto", font=('arial',8,'bold'), fg='white', bg='deepskyblue4')
    texto1.place(relx=0.30, rely=0.72, anchor='center')

    texto2 = Label(frame, text="Caso não tenha uma conta\nClique para Cadastrar", font=('arial',8,'bold'), fg='white', bg='deepskyblue4')
    texto2.place(relx=0.67, rely=0.72, anchor='center')

    registros.mainloop()

abrir_registros()
# ------------------------------------------- PRINCIPAL ---------------------------------------------------------------------------------------- #
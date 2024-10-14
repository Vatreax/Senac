import mysql.connector 
dataBase = mysql.connector.connect( 
                     host = "10.28.2.39", 
                     user = "suporte", 
                     password = "suporte", 
                     database = "registros")  
cursor = dataBase.cursor()
def algumacoisa():
# sql = f"UPDATE login SET texto = '{n1}' WHERE usuario = '{n2}'"
   
    sql = f"INSERT INTO login (usuario,senha) VALUES ('{n1}','{n2}')"
    cursor.execute(sql)
    dataBase.commit()

savequery = "select * from registros.login"

n1 = input("Usuário: ")
n2 = input("Senha: ")

algumacoisa()


# try:
cursor.execute(savequery)
if n1 in cursor:
    myresult = cursor.fetchall()

for x in myresult:
    print(x)

print("Query Excecuted successfully")

# except:
#     dataBase.rollback()
#     print("Error occured")

dataBase.close()
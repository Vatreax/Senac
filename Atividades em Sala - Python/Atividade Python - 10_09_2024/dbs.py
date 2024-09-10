import mysql.connector 
dataBase = mysql.connector.connect( 
                     host = "10.28.2.39", 
                     user = "suporte", 
                     password = "suporte", 
                     database = "registros")  

savequery = "select * from login"

n1 = input("Escreve algo: ")
n2 = input("Usuario: ")

cursor = dataBase.cursor()

sql = f"UPDATE login SET texto = '{n1}' WHERE usuario = '{n2}'"

cursor.execute(sql)

dataBase.commit()

try:
    cursor.execute(savequery)
    myresult = cursor.fetchall()
    
    for x in myresult:
        print(x)

    print("Query Excecuted successfully")

except:
    dataBase.rollback()
    print("Error occured")

cursorObject = dataBase.cursor()  
dataBase.close()
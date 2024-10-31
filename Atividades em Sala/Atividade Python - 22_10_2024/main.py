from livros import Livro
from tarefa import Usuario
from biblioteca import Biblioteca
import mysql.connector

conexao = mysql.connector.connect(
    host ='10.28.2.39',
    user='suporte',
    password='suporte',
    database='biblioteca'
)

cursor = conexao.cursor()

cursor.execute("insert into livro(titulo, autor, genero, status,codigo) values ('o pequeno principe', 'Enzo','fantasia', 'disponivel',1)")
cursor.execute("insert into usuario(nome,cpf,telefone) values ('Rafaela','1234567891011','67912378666')")
cursor.execute("update livro set usuario = 1 where id_livro = 1")
# cursor.execute("delete from livro where id_livro = 1")

conexao.commit()
print(dir(conexao))
from models.livros import Livro
from models.usuario import Usuario

livrin = Livro('auto','titulo','','')
usando = Usuario('Tafarel','123456789','6799132323')

print(vars(livrin))
print(vars(usando))
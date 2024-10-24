from livros import Livro
from tarefa import Usuario
from biblioteca import Biblioteca

rafaela = Usuario('Rafaela','tafarela123@gmail.com','rafarilda321')

dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", "Romance","1")
incidente_antares = Livro("Incidente em Antares", "Érico Verissimo", "Ficção Cientifica","2")
turma_da_monica = Livro("Turma da Mônica", "Mauricio de Souza", "Literatura Infantil","3")
poliana = Livro("Poliana", "Harry", "Romance","4")


Biblioteca.Acervo.append(dom_casmurro)
Biblioteca.Acervo.append(incidente_antares)


rafaela.pegar_emprestado(dom_casmurro)
rafaela.pegar_emprestado(incidente_antares)

dom_casmurro.emprestimo_livro(rafaela)
incidente_antares.emprestimo_livro(rafaela)
# print(vars(rafaela))
# print(vars(dom_casmurro))

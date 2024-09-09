#    6. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
#    Você vai criar uma tabela para armazenar os dados de revistas (como por ex: Veja, Isto é,
#    Epoca, Quatro Rodas, Claudia, etc).
#    Escreva e execute os comandos para:
#    • Criar a tabela chamada Revista para conter os campos: idRevista (int e chave
#    primária da tabela), nome (varchar, tamanho 40), categoria (varchar, tamanho 30). Os
#    valores de idRevista devem iniciar com o valor 1 e ser incrementado automaticamente
#    pelo sistema.
#    • Inserir 4 registros na tabela, mas sem informar a categoria.
#    Escreva e execute os comandos para:
#    • Exibir todos os dados da tabela.
#    • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
#    novamente para verificar se atualizou corretamente.
#    • Insira mais 3 registros completos.
#    • Exibir novamente os dados da tabela.
#    • Exibir a descrição da estrutura da tabela.
#    • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
#    • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o
#    tamanho da coluna categoria
#    • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
#    • Exibir os dados da tabela.
#    • Excluir a coluna periodicidade da tabela.

drop database if exists sprint;
create database sprint;
use sprint;

create table Revista(
idRevista int auto-increment primary key,
nome varchar(40),
categoria varchar(30)
);


INSERT INTO Revista (nome) VALUES
    ('Veja'),
    ('Isto é'),
    ('Época'),
    ('Quatro Rodas'),
    ('Claudia');

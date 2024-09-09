#    6. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
#    Você vai criar uma tabela para armazenar os dados de revistas (como por ex: Veja, Isto é,
#    Epoca, Quatro Rodas, Claudia, etc).
#    Escreva e execute os comandos para:

drop database if exists sprint;
create database sprint;
use sprint;

#    • Criar a tabela chamada Revista para conter os campos: idRevista (int e chave
#    primária da tabela), nome (varchar, tamanho 40), categoria (varchar, tamanho 30). Os
#    valores de idRevista devem iniciar com o valor 1 e ser incrementado automaticamente
#    pelo sistema.
create table Revista(
idRevista int auto_increment primary key,
nome varchar(40),
categoria varchar(30)
);


#    • Inserir 4 registros na tabela, mas sem informar a categoria.
#    Escreva e execute os comandos para:
insert into Revista (nome) VALUES
    ('Veja'),
    ('Isto é'),
    ('Época'),
    ('Quatro Rodas'),
    ('Claudia');

#    • Exibir todos os dados da tabela.
select * from Revista;

#    • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
#    novamente para verificar se atualizou corretamente.
update Revista set categoria = 'Fake News' where idRevista =1;
update Revista set categoria = 'Política' where idRevista=2;
update Revista set categoria = 'Automobilistica' where idRevista=3;
select * from Revista where idRevista <= 3;

#    • Insira mais 3 registros completos.
create table Revista(
idRevista int auto_increment primary key,
nome varchar(40),
categoria varchar(30)
);


#    • Inserir 4 registros na tabela, mas sem informar a categoria.
#    Escreva e execute os comandos para:
insert into Revista (nome) VALUES
    ('Veja'),
    ('Isto é'),
    ('Época'),
    ('Quatro Rodas'),
    ('Claudia');

#    • Exibir todos os dados da tabela.
select * from Revista;

#    • Atualize os dados das categorias das 3 revistas inseridas. Exibir os dados da tabela
#    novamente para verificar se atualizou corretamente.
update Revista set categoria = 'Fake News' where idRevista =1;
update Revista set categoria = 'Política' where idRevista=2;
update Revista set categoria = 'Polêmicas' where idRevista=3;
select * from Revista where idRevista <= 3;

#    • Insira mais 3 registros completos.
insert into Revista (nome, categoria) values
    ('Superinteressante', 'Ciência'),
    ('Caras', 'Celebridades'),
    ('National Geographic', 'Natureza');
    
#    • Exibir novamente os dados da tabela.
select * from Revista;

#    • Exibir a descrição da estrutura da tabela.
describe Revista;

#    • Alterar a tabela para que a coluna categoria possa ter no máximo 40 caracteres.
alter table Revista modify categoria varchar (40);

#    • Exibir novamente a descrição da estrutura da tabela, para verificar se alterou o
#    tamanho da coluna categoria
describe Revista;

#    • Acrescentar a coluna periodicidade à tabela, que é varchar(15).
alter table Revista add column periodicidade varchar(15);

#    • Exibir os dados da tabela.
select * from Revista;

#    • Excluir a coluna periodicidade da tabela.
alter table Revista drop column periodicidade;
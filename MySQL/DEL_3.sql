#	3. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
#	Criar a tabela chamada Filme para conter os dados: idFilme, título (tamanho 50), genero
#	(tamanho 40), diretor (tamanho 40), sendo que idFilme é a chave primária da tabela.
#	Inserir dados na tabela, procurando colocar um gênero de filme que tenha mais de um
#	filme, e um diretor, que tenha mais de um filme cadastrado. Procure inserir pelo menos
#	uns 7 filmes.
#	Execute os comandos para:

drop database if exists sprint;
create database sprint;
use sprint;

create table Filme(
idFilme int auto_increment primary key,
titulo varchar (50),
genero varchar (40),
diretor varchar (40)
);

SET SQL_SAFE_UPDATES = 0;

insert into Filme(idFilme,titulo,genero,diretor) values
	(null,'De Volta Para o Futuro','Aventura','Robert Zemeckis'),
    (null,'ET, o Extraterreste', 'Aventura','Steven Spillberg'),
    (null,'Exterminador do Futuro','Ação','James Cameron'),
    (null,'As Branquelas','Comédia','Keenen Ivory'),
    (null,'Alien','Terror','Ridley Scott'),
    (null,'A Teia','Suspense','Adam Cooper'),
    (null,'Manchester á Beira-Mar','Drama','Kenneth Lonergan');
    
#	• Exibir todos os dados da tabela.
select * from Filme;

#	• Adicionar o campo protagonista do tipo varchar(50) na tabela;
alter table Filme add column protagonista varchar(50);

#	• Atualizar o campo protagonista de todas os filmes inseridos;
update Filme set protagonista = 'John Connor' where titulo = 'Exterminador do Futuro';
update Filme set protagonista = 'Jovem Elliot' where titulo = 'ET, o Extraterreste';
update Filme set protagonista = 'Marty McFly' where titulo = 'De Volta Para o Futuro';
update Filme set protagonista = 'Shawn Wayans/Marlon Wayans' where titulo = 'Exterminador do Futuro';
update Filme set protagonista = 'Ellen Ripley' where titulo = 'Alien';
update Filme set protagonista = 'Roy Freeman' where titulo = 'A Teia';
update Filme set protagonista = 'Lee Chandler' where titulo = 'Manchester á Beira-Mar';

#	• Atualizar o campo protagonista de todas os filmes inseridos;
UPDATE Filme SET protagonista = 'Alex Johnson' WHERE titulo = 'Exterminador do Futuro';
UPDATE Filme SET protagonista = 'Samantha Green' WHERE titulo = 'ET, o Extraterrestre';
UPDATE Filme SET protagonista = 'Chris Miller' WHERE titulo = 'De Volta Para o Futuro';
UPDATE Filme SET protagonista = 'Jordan Smith' WHERE titulo = 'As Branquelas';
UPDATE Filme SET protagonista = 'Taylor Brown' WHERE titulo = 'Alien';
UPDATE Filme SET protagonista = 'Morgan Lee' WHERE titulo = 'A Teia';
UPDATE Filme SET protagonista = 'Jamie Parker' WHERE titulo = 'Manchester à Beira-Mar';

#	• Modificar o campo diretor do tamanho 40 para o tamanho 150;
alter table Filme modify diretor varchar(150);

#	• Atualizar o diretor do filme com id=5;
update Filme set diretor = 'Robert' where idFilme = 5;

#	• Atualizar o diretor dos filmes com id=2 e com o id=7;
update Filme set diretor = 'Cabeça de Gelo' where idFilme in (2,7);

#	• Atualizar o título do filme com o id=6;
update Filme set titulo = 'Jeba' where idFilme = 6;

#	• Excluir o filme com o id=3;
delete from Filme where idFilme = 3;

#	• Exibir os filmes em que o gênero é diferente de drama;
select * from Filme where genero = 'Drama';

#	• Exibir os dados dos filmes que o gênero é igual ‘suspense’;
select * from Filme where genero = 'Suspense';

#	• Descrever os campos da tabela mostrando a atualização do campo protagonista e
#	diretor;
describe Filme;

#	• Limpar os dados da tabela;
truncate Filme;
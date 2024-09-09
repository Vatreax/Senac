#	2. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
#	Criar a tabela chamada Musica para conter os dados: idMusica, titulo (tamanho 40), artista
#	(tamanho 40), genero (tamanho 40), sendo que idMusica é a chave primária da tabela.
#	Inserir dados na tabela, procurando colocar um gênero de música que tenha mais de uma
#	música, e um artista, que tenha mais de uma música cadastrada. Procure inserir pelo
#	menos umas 7 músicas.
#	Execute os comandos para:

drop database if exists sprint;
create database sprint;
use sprint;

create table Musica(
idMusica int auto_increment primary key,
titulo varchar(40),
artista varchar(40),
genero varchar(40)
);

insert into Musica (idMusica,titulo,artista,genero) values
	(null,'Hackearam Meu Site','DJ Rogerinho','Todos'),
    (null,'Cabeça de Gelo','Cleito Rasta','Eletrônica'),
    (null,'Suavão','DJ Rolinha','Funk'),
    (null,'Bunker','Uma Banda Ai','Rock'),
    (null,'In My Head','Queens of The Stone Age','Rock'),
    (null,'Opressão','Poeta','Rap'),
    (null,'Money','Lil Pimp','Hip-Hop');

#	a) Exibir todos os dados da tabela.
select * from Musica;

#	b) Adicionar o campo curtidas do tipo int na tabela;
alter table Musica add column curtidas int;

#	c) Atualizar o campo curtidas de todas as músicas inseridas;
update Musica set curtidas = 171 where idMusica = 1;
update Musica set curtidas = 1500 where idMusica = 2;
update Musica set curtidas = 1 where idMusica = 3;
update Musica set curtidas = 2 where idMusica = 4;
update Musica set curtidas = 100000 where idMusica = 5;
update Musica set curtidas = 6 where idMusica = 6;
update Musica set curtidas = 5 where idMusica = 7;

#	d) Modificar o campo artista do tamanho 40 para o tamanho 80;
alter table Musica modify artista varchar(80);

#	e) Atualizar a quantidade de curtidas da música com id=1;
update Musica set curtidas = 8000 where idMusica = 1;

#	f) Atualizar a quantidade de curtidas das músicas com id=2 e com o id=3;
update Musica set curtidas = 800 where idMusica >= 2 and idMusica <= 3;

#	g) Atualizar o nome da música com o id=5;
update Musica set titulo = 'Podre de Xique' where idMusica = 5;

#	i) Exibir as músicas onde o gênero é diferente de funk;
select * from Musica where genero != 'Funk';

#	j) Exibir os dados das músicas que tem curtidas maior ou igual a 20;
select * from Musica where curtidas >= 20;

#	k) Descrever os campos da tabela mostrando a atualização do campo artista;
describe Musica;

#	l) Limpar os dados da tabela;
truncate Musica;
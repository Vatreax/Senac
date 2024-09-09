# 1. No MySQL Workbench, crie o banco de dados ‘sprint’:
# Escreva e execute os comandos para:
# • Criar a tabela chamada Atleta para conter os dados:(
# idAtleta int e chave primária da tabela,
# nome varchar tamanho 40, 
# varchar tamanho 40, 
# qtdMedalha int, representando a quantidade de medalhas que o atleta possui
# );
# • Inserir dados na tabela, procurando colocar mais de um atleta para cada modalidade
# e pelo menos 5 atletas.
# Escreva e execute os comandos para:
# • Exibir todos os dados da tabela.
# • Atualizar a quantidade de medalhas do atleta com id=1;
# • Atualizar a quantidade de medalhas do atleta com id=2 e com o id=3;
# • Atualizar o nome do atleta com o id=4;
# • Adicionar o campo dtNasc na tabela, com a data de nascimento dos atletas, tipo date;
# • Atualizar a data de nascimento de todos os atletas;
# • Excluir o atleta com o id=5;
# • Exibir os atletas onde a modalidade é diferente de natação;
# • Exibir os dados dos atletas que tem a quantidade de medalhas maior ou igual a 3;
# • Modificar o campo modalidade do tamanho 40 para o tamanho 60;
# • Descrever os campos da tabela mostrando a atualização do campo modalidade;
# • Limpar os dados da tabela;

drop database if exists sprint;
create database sprint;
use sprint;

create table Atleta (
idAtleta int primary key,
nome varchar(40),
modalidade varchar(40),
qtdMedalha int
);

insert into Atleta (idAtleta,nome,modalidade,qtdMedalha) values
	(1,'Roberto','Atletismo',10),
	(2,'Josilda','Salto com Vara',2),
	(3,'Marcus','Natação',3),
    (4,'Bianca','Nado Sincronizado', 20),
    (5,'Vanildo','Judô',7);
    
-- 1.  
SELECT * FROM sprint.Atleta;

-- 2.
update Atleta set qtdMedalha = 100 where idAtleta = 1;

-- 3.
update Atleta set qtdMedalha = 50 where idAtleta >= 2 and idAtleta <= 3;

-- 4.
update Atleta set nome = 'Alex' where idAtleta = 4;

-- 5.
alter table Atleta add column dtNasc date;

-- 6.
update Atleta set dtNasc = '1998-10-02' where idAtleta = 1;
update Atleta set dtNasc = '1990-03-03' where idAtleta = 2;
update Atleta set dtNasc = '2000-02-09' where idAtleta = 3;
update Atleta set dtNasc = '1991-05-08' where idAtleta = 4;
update Atleta set dtNasc = '2005-06-20' where idAtleta = 5;


-- 7.
delete from Atleta where idAtleta = 5;

-- 8.
select * from Atleta where modalidade != 'natação';

-- 9.
select * from Atleta where qtdMedalha >= 3;

-- 10.
alter table Atleta modify modalidade varchar (60);

-- 11.
describe Atleta;

-- 12.
truncate Atleta;
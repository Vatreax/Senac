drop database escola;
create database escola;
use escola;
create table alunos(
matricula int(4) auto_increment,
nome varchar (30) not null,
email varchar (50),
primary key (matricula)
);

insert into alunos (matricula,nome,email) values (null,"Tafarel","tafarindonson@gmail.com");
select * from alunos;
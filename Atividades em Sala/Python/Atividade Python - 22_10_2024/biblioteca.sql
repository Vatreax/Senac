drop database if exists biblioteca;
create database biblioteca;
use biblioteca;

create table usuario(
	id_usuario int auto_increment primary key,
    nome varchar(50),
    cpf varchar(13) unique,
    telefone varchar(20)
);

create table livro(
	id_livro int auto_increment primary key,
	titulo varchar(50),
    autor varchar(50),
    genero varchar(50),
    status varchar(50),
    codigo int,
    usuario int,
    foreign key (usuario) references usuario(id_usuario)
);

create table emprestimo(
	id_emprestimo int auto_increment primary key,
	id_livro int,
    id_usuario int,
    foreign key (id_livro) references livro(id_livro),
    foreign key (id_usuario) references usuario(id_usuario)
);

SELECT * from livro;
SELECT * from usuario;
SELECT * from emprestimo;

select * from livro join usuario where livro.usuario = usuario.id_usuario;
describe livro;
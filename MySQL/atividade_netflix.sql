create database netflix;
-- drop database netflix;
use netflix;

create table usuario(
id int auto_increment primary key,
nome varchar(255) not null,
email varchar(255) not null,
senha varchar(100) not null ,
cpf varchar(9) not null,
endereco_de_cobranca varchar(255) not null,
numero_do_cartao_de_credito int(25) not null,
telefone int(13) not null
);
-----------------------------------------------------------------------------------
create table servico(
id int auto_increment primary key,
assinatura int not null,
mensalidade float not null);

-----------------------------------------------------------------------------------
create table catalogo(
id int auto_increment primary key,
id_serie int not null,
id_filme int not null,
id_ator int not null,
id_documentario int not null);

-----------------------------------------------------------------------------------
create table serie(
id int auto_increment primary key,
titulo varchar(255),
duracao int not null,
ano_de_producao date not null,
temporada int not null,
numero_de_episodios int not null
);
-----------------------------------------------------------------------------------
create table episodio(
id int auto_increment primary key,
titulo varchar(255) not null,
numero_do_episodio int not null,
duracao_em_minutos int not null,
temporada int not null
);

alter table episodio add column id_serie int first;
alter table episodio add foreign key(id_serie) references serie(id);
-----------------------------------------------------------------------------------
create table proximo_episodio(
id int auto_increment primary key,
titulo varchar(255) not null,
duracao_em_minutos int not null,
temporada int not null,
numero_do_episodio int not null,
proximo_episodio int not null
);

alter table proximo_episodio add column id_episodio int first;
alter table proximo_episodio add foreign key(id_episodio) references episodio(id);

alter table proximo_episodio add column id_serie int first;
alter table proximo_episodio add foreign key(id_serie) references serie(id);
-----------------------------------------------------------------------------------
create table filme(
id int auto_increment primary key,
titulo varchar(255) not null,
ano_de_producao date not null,
duracao_em_minutos int not null
);
-----------------------------------------------------------------------------------
create table ator(
id int auto_increment primary key,
nome varchar(255) not null,
local_de_nascimento varchar(255) not null,
data_de_nascimento date not null
);
-----------------------------------------------------------------------------------
create table documentario(
id int auto_increment primary key,
titulo varchar(255) not null,
ano_de_producao date not null,
produtora varchar(255) not null,
duracao_em_minutos int not null
);
-----------------------------------------------------------------------------------
alter table catalogo add foreign key (id_serie) references serie(id);
alter table catalogo add foreign key (id_filme) references filme(id);
alter table catalogo add foreign key (id_ator) references ator(id);
alter table catalogo add foreign key (id_documentario) references documentario(id);
-----------------------------------------------------------------------------------
alter table servico add column id_usuario int first;
alter table servico add foreign key (id_usuario) references usuario(id);
alter table servico add column id_catalogo int first;
alter table servico add foreign key (id_catalogo) references catalogo(id);
-----------------------------------------------------------------------------------
alter table usuario add column id_servico int first;
alter table usuario add foreign key (id_servico) references servico(id);



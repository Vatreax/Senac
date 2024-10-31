drop database if exists teste_testando;
create database if not exists teste_testando;
use teste_testando;

CREATE TABLE sexos(
	id_sexo int auto_increment primary key ,
	sexo enum('Masculino','Feminino', 'Outro') not null
);

create table estados(
	id_estado int auto_increment primary key,
	estado varchar(100)
);

create table cidades(
	id_cidade int auto_increment primary key,
	id_estado int,
	cidade varchar(100),
	foreign key fk_estado(id_estado) references estados(id_estado)
);

CREATE TABLE enderecos (
		id_endereco int auto_increment primary key,
		id_cidade int,
		cep varchar(8),    
		endereco varchar(100),
		bairro varchar(100),
		complemento varchar(100),
		foreign key fk_cidade(id_cidade) references cidades(id_cidade)
);

CREATE TABLE clientes (
    id_cliente int auto_increment primary key,
    nome varchar(20) not null,
    sobrenome VARCHAR(60) NOT NULL,
    nascimento DATE NOT NULL,
    cpf varchar(11) not null,
    numero_telefone VARCHAR(12) not null,
    email varchar(100) unique not null,
    senha varchar(50) not null,
    id_endereco int,
    id_sexo int,
    foreign key fk_endereco(id_endereco) references enderecos(id_endereco),
    foreign key fk_sexo(id_sexo) references sexos(id_sexo)
);


-- Inserindo dados na tabela sexos
INSERT INTO sexos (sexo) VALUES ('Masculino');
INSERT INTO sexos (sexo) VALUES ('Feminino');
INSERT INTO sexos (sexo) VALUES ('Outro');

-- Inserindo dados na tabela estados
INSERT INTO estados (estado) VALUES ('São Paulo');
INSERT INTO estados (estado) VALUES ('Rio de Janeiro');
INSERT INTO estados (estado) VALUES ('Minas Gerais');

-- Inserindo dados na tabela cidades
INSERT INTO cidades (id_estado, cidade) VALUES (1, 'São Paulo');
INSERT INTO cidades (id_estado, cidade) VALUES (2, 'Rio de Janeiro');
INSERT INTO cidades (id_estado, cidade) VALUES (3, 'Belo Horizonte');

-- Inserindo dados na tabela enderecos
INSERT INTO enderecos (id_cidade, cep, endereco, bairro, complemento) VALUES (1, '01001000', 'Rua A', 'Centro', 'Apto 1');
INSERT INTO enderecos (id_cidade, cep, endereco, bairro, complemento) VALUES (2, '20040002', 'Rua B', 'Copacabana', 'Apto 2');
INSERT INTO enderecos (id_cidade, cep, endereco, bairro, complemento) VALUES (3, '30130010', 'Rua C', 'Savassi', 'Apto 3');

-- Inserindo dados na tabela clientes
INSERT INTO clientes (nome, sobrenome, nascimento, cpf, numero_telefone, email, senha, id_endereco, id_sexo) VALUES ('João', 'Silva', '1990-01-01', '12345678901', '11999999999', 'joao.silva@example.com', 'senha123', 1, 1);
INSERT INTO clientes (nome, sobrenome, nascimento, cpf, numero_telefone, email, senha, id_endereco, id_sexo) VALUES ('Maria', 'Oliveira', '1985-05-05', '23456789012', '21988888888', 'maria.oliveira@example.com', 'senha456', 2, 2);
INSERT INTO clientes (nome, sobrenome, nascimento, cpf, numero_telefone, email, senha, id_endereco, id_sexo) VALUES ('Alex', 'Santos', '2000-10-10', '34567890123', '31977777777', 'alex.santos@example.com', 'senha789', 3, 3);

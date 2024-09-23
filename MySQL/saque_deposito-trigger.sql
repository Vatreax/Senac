drop database if exists banco;
create database if not exists banco;
use banco;

create table estado(
id_estado int auto_increment primary key,
nome varchar (50) not null
);

create table cidade(
id_cidade int auto_increment primary key,
nome varchar (50) not null,
id_estado int,
foreign key (id_estado) references estado (id_estado)
);

create table genero(
id_gen int auto_increment primary key,
tipo enum("Masculino","Feminino","Outro") not null
);

create table raca(
id_raca int auto_increment primary key,
tipo enum("Branco","Negro","Amarelo","Indígena") not null
);

create table religiao(
id_religiao int auto_increment primary key,
tipo enum("Protestante","Católico","Islâmico","Budismo","Umbanda","Judeu") not null
);

create table agencia(
numero_da_agencia int auto_increment primary key,
endereco varchar(100) not null,
id_cidade int,
id_estado int,
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_estado) references estado(id_estado)
);

create table cliente(
numero_da_conta varchar(15) primary key not null,
cpf varchar(11) not null,
nome varchar(100) not null,
rg varchar(12) not null,
data_de_nascimento date not null,
estado_civil enum("Casado","Solteiro","Separado","Divorciado","Viúvo"),
religiao int,
genero int,
saldo float,
numero_da_agencia int,
id_cidade int,
id_estado int,
foreign key (religiao) references religiao (id_religiao),
foreign key (genero) references genero(id_gen),
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_estado) references estado(id_estado),
foreign key (numero_da_agencia) references agencia (numero_da_agencia)
);

create table saque(
id_operecao int auto_increment primary key,
id_agencia int,
id_conta_cliente varchar(15),
valor_saque float,
foreign key (id_agencia) references agencia(numero_da_agencia),
foreign key (id_conta_cliente) references cliente(numero_da_conta)
);

create table deposito(
id_operecao int auto_increment primary key,
id_agencia int,
id_conta_cliente varchar(15),
valor_deposito float,
foreign key (id_agencia) references agencia(numero_da_agencia),
foreign key (id_conta_cliente) references cliente(numero_da_conta)
);

DELIMITER %
CREATE TRIGGER tgr_saque BEFORE INSERT
ON saque
FOR EACH ROW
BEGIN
	declare saldo_atual float;
    
    select saldo into saldo_atual from cliente where numero_da_conta = new.id_conta_cliente;


	if saldo_atual >= 0 then
	UPDATE cliente Set saldo = saldo - NEW.valor_saque
    WHERE numero_da_conta = NEW.id_conta_cliente;
    else
		signal sqlstate '45000' set message_text = 'Você foi Taxadd' ;
	end if;

END%

CREATE TRIGGER tgr_deposito BEFORE INSERT
ON deposito
FOR EACH ROW
BEGIN
	UPDATE cliente Set saldo = saldo + NEW.valor_deposito
WHERE numero_da_conta = NEW.id_conta_cliente;
END%
DELIMITER ;	

-- Estados
insert into estado (nome) values
	('São Paulo'),
	('Rio de Janeiro'),
	('Minas Gerais');

-- Cidades
insert into cidade (nome, id_estado) values 
	('São Paulo', 1),
	('Rio de Janeiro', 2),
	('Belo Horizonte', 3);

-- Gêneros
insert into genero (tipo) values 
	('Masculino'),
	('Feminino'),
	('Outro');

-- Inserindo raças
insert into raca (tipo) values 
	('Branco'),
	('Negro'),
	('Indígena');

-- Inserindo religiões
insert into religiao (tipo) values 
	('Católico'),
	('Protestante'),
	('Budismo');

-- Agências
insert into agencia (endereco, id_cidade, id_estado) values 
	('Rua A, 123', 1, 1),
	('Avenida B, 456', 2, 2),
	('Praça C, 789', 3, 3);

-- Clientes
insert into cliente (numero_da_conta, cpf, nome, rg, data_de_nascimento, estado_civil, religiao, genero, saldo, numero_da_agencia, id_cidade, id_estado) values 
	('123456789012345', '12345678901', 'João Silva', 'MG1234567', '1980-01-01', 'Solteiro', 1, 1, 0, 1, 1, 1),
	('987654321098765', '10987654321', 'Maria Oliveira', 'MG7654321', '1990-05-15', 'Casado', 2, 2, 1500.0, 2, 2, 2),
	('456123789012345', '45612378900', 'Ana Souza', 'MG1122334', '1995-07-20', 'Divorciado', 3, 1, 500.0, 3, 3, 3);

-- Saque
insert into saque (id_agencia, id_conta_cliente, valor_saque) values 
	(1, '123456789012345', 200.0),
	(2, '987654321098765', 150.0),
	(3, '456123789012345', 100.0);

-- Depósito
insert into deposito (id_agencia, id_conta_cliente, valor_deposito) values 
	(1, '123456789012345', 300.0),
	(2, '987654321098765', 500.0),
	(3, '456123789012345', 700.0);
    
select * from cliente join religiao on cliente.religiao = religiao.id_religiao;
select * from cliente join genero on cliente.genero = genero.id_gen;
select saldo from cliente;
select valor_saque from saque;
select valor_deposito from deposito;



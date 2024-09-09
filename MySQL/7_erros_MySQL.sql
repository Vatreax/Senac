-- criar o BD ecommerce
-- o create database possui um erro de digitação. ERRADO: |create datbase ecommerce| - CERTO |create database ecommerce|
-- use ecommerce também possui um erro de digitação. ERRADO: |user ecommerce| - CERTO |use ecommerce|
create database ecommerce;
use ecommerce;

---------------------------------------------
-- 'create table produtos' não esta abrindo um parênteses, para poder colocar as atribuições. ERRADO |create table produtos ...);| - CERTO |create table produtos (...);|
-- Continuando na mesma tabela, esta faltando virgulas e existe uma virgula na atribuição final, além de um erro de digitação.
-- Existe também o erro de não definir uma primary key 
create table  produtos (
    id_prod int(5) primary key auto_increment,
    nome_prod varchar(100) not null,
    descricao text,
    modelo varchar(50),
    id_categoria int(5),
    id_fabricante int(5)
    );

-- drop database ecommerce;
-- drop table pedidos;

-- 'create table clientes' começa com um erro de digitação. ERRADO |create tabela clientes| - CERTO |create table clientes|
-- Dentro da tabela, possui erros de digitação e falta de virgulas
-- Existe também o erro de não definir uma primary key 
create table clientes (
    id_cli int(5) primary key auto_increment,
    nome varchar(100) not null,
    cpf int(11),
    telefone varchar(50),
    sexo enum('F','M'),
    cadastro datetime
    );

-- dentro da 'create table pedidos' existe um erro de indentação e digitação.
create table pedidos(
    num_pedido int(5) primary key auto_increment,
    data_ datetime,
    status varchar(50),
   id_cli int(5),
   constraint foreign key (id_cli) references clientes(id_cli)
    );

-- a 'create table pedido_item', possui diversos erros de digitação, e erros de indentação. ERROS |create tabe pedido_item| |foregn key| - CERTO |create table pedido_item| |foreign key|
create table pedido_item (
    idtem_pedido int(5) primary key auto_increment,
    num_pedido int(5) not null,
    qtde int(5) not null,
    valor_unit decimal(10,2),
    total decimal(10,2),
    id_prod int(5),
    constraint foreign key (num_pedido) references pedidos(num_pedido),
    constraint foreign key (id_prod) references produtos(id_prod)
    );

-- a 'create table estoque_produtos' possui erros de digitação, falta de parentêses e erros de indentação.
    create table estoque_produtos(
	id_estoque int(5) primary key auto_increment,
	quantidade int(5),
	quant_min int(5),
	id_prod int(5),
    constraint foreign key (id_prod) references produtos(id_prod)
	);

-- nos 'insert into cliente' e 'insert into produtos', existem erros de indentação e digitação,falta de aspas e virgulas.
insert into clientes values (null,'João','02102202324','6799999999','M',now());
insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now());
insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());

insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);
   
insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null, null);


insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null, null);

-- erros de digitação no 'select * from produtos;' e 'describe estoque_produtos'.
select * from produtos;
describe estoque_produtos;

-- erros de digitação nos 'insert into estoque_produtos'.
insert into estoque_produtos values (null,80,10,1);
insert into estoque_produtos values (null,44,5,9);
insert into estoque_produtos values (null,55,5,8);
insert into estoque_produtos values (null,36,5,7);
insert into estoque_produtos values (null,49,5,6);
insert into estoque_produtos values (null,100,5,1);
insert into estoque_produtos values (null,100,5,2);
insert into estoque_produtos values (null,100,5,3);
insert into estoque_produtos values (null,100,5,4);
insert into estoque_produtos values (null,100,5,5);
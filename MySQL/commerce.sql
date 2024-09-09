create database commerce;
-- drop database commerce;
use commerce;

create table EX2_CLIENTE(
codcliente int auto_increment primary key,
nome varchar(255) not null,
data_nascimento date not null,
cpf varchar(255) not null
);
-----------------------------------------------------------------------
create table EX2_PEDIDO(
codpedido int auto_increment primary key,
codcliente int not null,
datapedido date not null,
nf varchar(100) not null,
valortotal float not null,
foreign key (codcliente) references EX2_CLIENTE(codcliente)
);
-----------------------------------------------------------------------
create table EX2_ITEMPEDIDO(
codpedido int not null,
numeroitem int auto_increment primary key,
valorunitario float not null,
quantidade int not null,
codproduto int not null,
foreign key (codpedido) references EX2_PEDIDO(codpedido)
);
-----------------------------------------------------------------------
create table EX2_PRODUTO(
codproduto int auto_increment primary key,
descricao varchar(255) not null,
quantidade int not null
);

alter table EX2_ITEMPEDIDO add foreign key (codproduto) references EX2_PRODUTO(codproduto);
-----------------------------------------------------------------------
create table EX2_LOG(
codlog int auto_increment primary key,
data_ date not null,
descricao varchar(255) not null
);
-----------------------------------------------------------------------
create table EX2_REQUISICAO_COMPRA(
codrequisicaocompra int auto_increment primary key,
codproduto int not null,
data_ date not null,
quantidade int not null,
foreign key (codproduto) references EX2_PRODUTO(codproduto)
);

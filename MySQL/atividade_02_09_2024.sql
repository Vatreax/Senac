drop database if exists atividade_02_09_2024;
create database atividade_02_09_2024;
use atividade_02_09_2024;

create table fornecedores(
cod_forne varchar(15) primary key not null,
nome varchar(125) not null,
cidade_sede varchar(125) not null,
grupo_cod_fornecedor varchar(125)
);

create table material(
cod_material varchar(15)primary key not null,
cod_fornecedor varchar(15),
nome varchar(125) not null,
descricao varchar(250),
foreign key (cod_fornecedor) references fornecedores(cod_forne)
);

insert into fornecedores (cod_forne,nome,cidade_sede,grupo_cod_fornecedor) values
	('ABC','ABC Materias Eletricos','Vitoria',null),
    ('XYZ','XYZ Materias de Escritorio','Rio de Janeiro','HiX'),
	('Hidra','Hidra Materiais Hidraulicos','Sao Paulo','HiX'),
    ('Hix','HidraX Materiais Elétricos e Hidraulicos','Sao Paulo',null);
    
insert into material (cod_material,cod_fornecedor,nome,descricao) values
	('123','ABC','Tomada eletrica 10A Nova','Tomada eletrica 10A padrao novo'),
	('234','ABC','Disjuntor 25A','Disjuntor eletrico 25A'),
	('345','XYZ','Resma Papel A4','Resma papel branco A4'),
	('456','XYZ','Toner Imp HR5522','Toner impressora HR5522'),
	('678','Hidra','Cano PVC 1/2','Cano PVC 1/2 pol'),
	('679','Hidra','Cano PVC 3/4','Cano PVC 3/4 pol'),
	('680','Hidra','Medidor hidr 1/2','Medidor hidraulico 1/2 pol'),
	('681','Hidra','Joelho 1/2','Conector Joelho 1/2 pol'),
	('682','Hidra','Junta 1/2','Cano PVC 1/2 pol'),
	('1234','ABC','Tomada eletrica 20A Nova','Tomada eletrica 20A padrao novo'),
	('2345','XYZ','Caneta Azul','Caneta esferografica azul'),
	('4567','XYZ','Grapeador','Grampeador mesa pequeno'),
	('4568','XYZ','Caneta Marca Texto Amarela','Caneta Marca Texto Amarela'),
	('4569','XYZ','Lapis HB','Lapis Preto HB');

-- Quantos materiais possuem o Fornecedor ABC:
select * from material where cod_fornecedor like 'ABC%';
select count(cod_fornecedor) from material where cod_fornecedor like 'ABC%';

-- Quantos materiais possuem o Fornecedor XYZ:
select * from material where cod_fornecedor like 'XYZ%';
select count(cod_fornecedor) from material where cod_fornecedor like 'XYZ%';

-- Quantos materiais possuem o Fornecedor HIDRA:
select * from material where cod_fornecedor like 'HIDRA';
select count(cod_fornecedor) from material where cod_fornecedor like 'HIDRA';

-- Join entre as duas tables:
select * from fornecedores join material on material.cod_fornecedor = fornecedores.cod_forne;
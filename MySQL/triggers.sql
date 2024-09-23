drop database if exists mercadinho;
create database if not exists mercadinho;
use mercadinho;

create table produto(
referencia varchar(3) primary key,
descricao varchar(50) unique,
estoque int not null default 0
);

create table item_venda(
venda int,
produto varchar(3),
quantidade int
);

DELIMITER %
CREATE TRIGGER tgr_item_venda_insert AFTER INSERT
ON item_venda
FOR EACH ROW
BEGIN
	UPDATE produto Set estoque = estoque - NEW.quantidade
WHERE referencia = NEW.produto;
END%

CREATE TRIGGER Tgr_item_venda_delete AFTER DELETE
ON item_venda
FOR EACH ROW
begin Update produto SET estoque = estoque + OLD.quantidade
WHERE referencia = OLD.produto;
END%
DELIMITER ;	

insert into produto values 
	('001', 'Feijão', 10),
	('002','Arroz', 5),
	('003','Farinha', 15);

insert into item_venda values 
	(1,'001',3),
    (2,'002',1),
    (3,'003',5);

SET SQL_SAFE_UPDATES = 0;
# delete from item_venda where produto like '001'; 

SELECT * FROM mercadinho.produto;
SELECT * FROM mercadinho.item_venda;
SELECT * FROM item_venda join produto on produto=referencia;
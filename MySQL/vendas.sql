DROP DATABASE IF EXISTS vendas;

CREATE DATABASE vendas;

USE vendas;
 
-- Criação da tabela CIDADE

CREATE TABLE CIDADE (

    CODCID   INTEGER NOT NULL AUTO_INCREMENT,

    NOMECID  VARCHAR(60),

    UF       CHAR(2),

    PRIMARY KEY (CODCID)

);
 
-- Criação da tabela SETOR

CREATE TABLE SETOR (

    CODSETOR   INTEGER NOT NULL AUTO_INCREMENT,

    NOMESETOR  VARCHAR(50),

    PRIMARY KEY (CODSETOR)

);
 
-- Criação da tabela VENDEDOR

CREATE TABLE VENDEDOR (

    CODVEND   INTEGER NOT NULL AUTO_INCREMENT,

    NOMEVEND  VARCHAR(60),

    CODSETOR  INTEGER,

    SALARIO   NUMERIC(10,2),

    PRIMARY KEY (CODVEND),

    FOREIGN KEY (CODSETOR) REFERENCES SETOR (CODSETOR)

);
 
-- Criação da tabela CLIENTE

CREATE TABLE CLIENTE (

    CODCLI    INTEGER NOT NULL AUTO_INCREMENT,

    NOME      VARCHAR(60),

    ENDERECO  VARCHAR(60),

    CODCID    INTEGER NOT NULL,

    CEP       CHAR(10),

    CPF       CHAR(20),

    PRIMARY KEY (CODCLI),

    FOREIGN KEY (CODCID) REFERENCES CIDADE (CODCID)

);
 
-- Criação da tabela PEDIDO

CREATE TABLE PEDIDO (

    NUMPED   INTEGER NOT NULL AUTO_INCREMENT,

    ENTREGA  SMALLINT,

    CODCLI   INTEGER NOT NULL,

    CODVEND  INTEGER NOT NULL,

    PRIMARY KEY (NUMPED),

    FOREIGN KEY (CODCLI) REFERENCES CLIENTE (CODCLI),

    FOREIGN KEY (CODVEND) REFERENCES VENDEDOR (CODVEND)

);
 
-- Criação da tabela PRODUTO

CREATE TABLE PRODUTO (

    CODPROD    INTEGER NOT NULL AUTO_INCREMENT,

    DESCRICAO  VARCHAR(25),

    UNIDADE    CHAR(3),

    VALOR_UN   NUMERIC(10,2),

    PRIMARY KEY (CODPROD)

);
 
-- Criação da tabela ITEMPEDIDO

CREATE TABLE ITEMPEDIDO (

    NUMPED   INTEGER NOT NULL,

    CODPROD  INTEGER NOT NULL,

    QTDADE   SMALLINT

);

ALTER TABLE ITEMPEDIDO ADD CONSTRAINT FOREIGN KEY (NUMPED) REFERENCES PEDIDO (NUMPED);

ALTER TABLE ITEMPEDIDO ADD CONSTRAINT FOREIGN KEY (CODPROD) REFERENCES PRODUTO (CODPROD);

-- Inserções de Dados

INSERT INTO CIDADE (NOMECID, UF) VALUES

('DOURADOS', 'MS'),

('CAMPO GRANDE', 'MS'),

('SÃO PAULO', 'SP'),

('CUIABA', 'MT'),

('FLORIANÓPOLIS', 'SC'),

('SÃO SEBASTIÃO', 'SC'),

('CAARAPÓ', 'MS'),

('BRASÍLIA', 'DF'),

('TUPÃ', 'SP'),

('SÃO JOSÉ DO RIO PRETO', 'SP'),

('APUCARANA', 'PR'),

('JARDIM', 'MS'),

('JATEI', 'MS'),

('AMAMBAI', 'MS');
 
COMMIT WORK;
 
INSERT INTO CLIENTE (NOME, ENDERECO, CODCID, CEP, CPF) VALUES

('Nicolash Pereira Rodrigues', 'Rua José Germano, 1456', 1, '13971-150', '13971-150'),

('Cauã Oliveira Azevedo', 'Rua Luís Squilace, 175', 3, '05326-010', '855.498.901-51'),

('Martim Melo Araujo', 'Rua de Mizar, 429', 2, '32550-220', '421.837.827-49'),

('Matheus Pinto Almeida', 'Travessa Getúlio Vargas, 1426', 4, '54250-382', NULL),

('Estevan Pereira Cardoso', 'Travessa Maria da Penha Costa, 692', 5, '29707-190', '231.416.173-41'),

('Rebeca Sousa Fernandes', 'Avenida da Saudade, 1899', 3, '09030-030', NULL),

('Thaís Melo Rodrigues', 'Rua N, 1379', 11, '35900-626', '884.501.839-36'),

('Matheus Martins Ribeiro', 'Rua Ubaldo Damiano, 1006', 1, '17204-281', NULL),

('Leonardo Barros Melo', 'Rua Treze de Maio, 808', 2, '65900-220', '735.643.235-89'),

('Emilly Rocha Ribeiro', 'Passagem Santa Luzia, 221', 1, '66117-060', '613.666.706-12'),

('Luan Goncalves Melo', 'Rua Chapada Velha, 944', 3, '05728-070', '656.106.888-25'),

('Júlia Gomes Araujo', 'Rua Alamanda, 751', 3, '06728-320', '184.206.138-00'),

('Camila Rodrigues Barbosa', 'Rua dos Cumarus, 1977', 2, '38703-678', '973.600.869-06'),

('Melissa Araujo Almeida', 'Rua 104A, 1820', 1, '74083-310', '677.324.633-40'),

('Laura Barros Rodrigues', 'Rua Doutor Muraí, 697', 3, '03159-080', '670.936.770-37');
 
COMMIT WORK;
 
INSERT INTO SETOR (NOMESETOR) VALUES

('JARDIM'),

('VENENOS'),

('PEÇAS'),

('FERRAMENTAS'),

('VACINAS'),

('VESTUÁRIO');
 
COMMIT WORK;
 
INSERT INTO VENDEDOR (NOMEVEND, CODSETOR, SALARIO) VALUES

('ANTONIO CARLOS DA SILVA', 1, 500),

('ROGERIO SANTOS AMADO', 1, 550),

('JOÃO FLORISVALDO JESUS', 2, 800),

('PEDRO CELESTINO VENÂNCIO', 3, 1000),

('JAIR COSTA', 3, 1000),

('ELIZA DOS ANJOS', 4, 700),

('DENIS OTTANO', 5, 600),

('RONEI ARAÚJO BATISTA', 6, 400),

('JAMES CHEN VILAREAL', 6, 400),

('FABIO BENDITO REIS', 4, 700),

('EDILSON NOGUEIRA', 2, 800),

('RODOLFO DOS SANTOS', 4, 450),

('CRISTIANE ANTUNES ROCHA', 3, 450),

('CRISLAINE RUBENS AZEVEDO', 1, 500),

('JADER DE AMARO', 4, 1500);
 
COMMIT WORK;
 
INSERT INTO PEDIDO (ENTREGA, CODCLI, CODVEND) VALUES

(5, 1, 3),

(2, 2, 5),

(10, 4, 1),

(20, 1, 2),

(2, 8, 9),

(2, 2, 4),

(10, 5, 7),

(2, 14, 11),

(5, 15, 15),

(5, 15, 4),

(20, 9, 10),

(10, 9, 11),

(1, 5, 6),

(1, 13, 9),

(20, 12, 5);
 
COMMIT WORK;
 
INSERT INTO PRODUTO (DESCRICAO, UNIDADE, VALOR_UN) VALUES

('MATA CUPIM', 'UN', 25),

('GLIFOSSATO', 'UN', 12),

('RANDAP', 'UN', 33),

('ESCOVA DE AÇO', 'UN', 22),

('MAÇA', 'KG', 7),

('BANANA', 'KG', 6),

('ESCOVA P', 'UN', 1),

('CANETA AZUL', 'UN', 0.5),

('CADERNO', 'UN', 2.5),

('LIVRO', 'UN', 10),

('AEROSSOL', 'UN', 6),

('LIXA', 'UN', 3),

('PERFUME', 'UN', 18),

('ÓLEO DE COZINHA', 'UN', 7.5),

('LEITE', 'UN', 4);

COMMIT WORK;

INSERT INTO ITEMPEDIDO (NUMPED, CODPROD, QTDADE) VALUES 
	(1, 1, 1),
	(1, 3, 1),
	(1, 10, 2),
	(2, 4, 1),
	(3, 2, 1),
	(3, 3, 1),
	(4, 9, 5),
	(4, 11, 2),
	(4, 12, 2),
	(5, 2, 2),
	(5, 11, 2),
	(5, 18, 1),
	(5, 20, 2),
	(6, 5, 1),
	(7, 7, 1),
	(8, 8, 1),
	(10, 2, 2),
	(10, 12, 3),
	(10, 17, 1),
	(10, 18, 1),
	(10, 19, 1),
	(13, 8, 1),
	(13, 19, 1),
	(13, 20, 1),
	(14, 13, 1),
	(14, 17, 1),
	(15, 15, 20),
	(15, 16, 1);
 
 COMMIT WORK;
 
 SELECT * FROM vendas.vendedor;
 
-- 01. Quantas cidades tem cadastradas no banco? 
select count(*) as Total_Cidades from CIDADE;
 
-- 02. Quantos Clientes tem cadastrado no banco? 
select count(*) as Total_Clientes from CLIENTE;
 
-- 03. Quantos produtos tem no banco? 
select count(*) as Total_Produtos from PRODUTO;
 
-- 04. Quantos setores tem no banco? 
select count(*) as Total_Setores from VENDEDOR;
 
-- 05. Quantos pedidos tem no banco? 
select count(*) as Total_Pedidos from PEDIDO;

-- 06. Qual o maior salário dos vendedores? 
select max(SALARIO) as Maiores_Salário from VENDEDOR;

-- 07. Quem possui o maior salário?  
select NOMEVEND as Maior_Salário from VENDEDOR order by SALARIO desc limit 1;
 
-- 08. Qual o menor salário dos vendedores? 
select min(SALARIO) as Menor_Salário from VENDEDOR;

-- 09. Quem possui o menor salário? 
select NOMEVEND as Menor_Salário from VENDEDOR order by SALARIO asc limit 1;

-- 10. Qual pedido teve a maior venda em quantidade? 
select max;

-- 11. Qual pedido teve a menor venda em quantidade? 

-- 12. Qual o produto mais barato? 

-- 13. Qual o produto mais caro? 

-- 14. Quantos vendedores existem no setor de ferramentas? 

-- 15. Quantos pedidos o cliente Estevan Pereira Cardoso fez? 
SELECT count(*) from pedido join cliente on pedido.CODCLI = cliente.CODCLI where cliente 'Estevan Pereira Cardoso'

 
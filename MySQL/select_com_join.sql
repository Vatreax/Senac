drop database if exists atividade_do_ederson;
create database atividade_do_ederson;
use atividade_do_ederson;

-- ------------------------- 1°Parte ----------------------------------------------------------------------------------------------------------------------------------
create table estado(
id_estado int auto_increment primary key,
estado varchar(100));

create table cidade(
id_cidade int auto_increment primary key,
cidade varchar(100),
id_estado int,
foreign key (id_estado) references estado(id_estado));

create table sexo(
id_sexo int auto_increment primary key,
sexo varchar(20));

create table nacionalidade(
id_nacionalidade int auto_increment primary key,
nacionalidade varchar(100));

create table raca(
id_raca int auto_increment primary key,
raca varchar(25) not null);

create table escolaridade(
id_escolaridade int auto_increment primary key,
escolaridade varchar(50));

create table clientes(
cpf varchar(11) primary key not null,
rg varchar(7) not null,
nome varchar(255),
id_cidade int,
id_sexo int,
id_nacionalidade int,
id_raca int,
id_escolaridade int,
fone varchar(15),
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_sexo) references sexo(id_sexo),
foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
foreign key (id_raca) references raca(id_raca),
foreign key (id_escolaridade) references escolaridade(id_escolaridade)
);

-- ------------------------- 2°Parte ----------------------------------------------------------------------------------------------------------------------------------

insert into estado (id_estado,estado) values
(null, 'Acre'),
(null, 'Alagoas'),
(null, 'Amapá'),
(null, 'Amazonas'),
(null, 'Bahia'),
(null, 'Ceará'),
(null, 'Distrito Federal'),
(null, 'Espírito Santo'),
(null, 'Goiás'),
(null, 'Maranhão'),
(null, 'Mato Grosso'),
(null, 'Mato Grosso do Sul'),
(null, 'Minas Gerais'),
(null, 'Pará'),
(null, 'Paraíba'),
(null, 'Paraná'),
(null, 'Pernambuco'),
(null, 'Piauí'),
(null, 'Rio de Janeiro'),
(null, 'Rio Grande do Norte'),
(null, 'Rio Grande do Sul'),
(null, 'Rondônia'),
(null, 'Roraima'),
(null, 'Santa Catarina'),
(null, 'São Paulo'),
(null, 'Sergipe'),
(null, 'Tocantins');

insert into cidade (id_cidade,cidade,id_estado) values
-- Acre
(1, 'Rio Branco', 1),
(2, 'Cruzeiro do Sul', 1),
(3, 'Sena Madureira', 1),
(4, 'Tarauacá', 1),
(5, 'Feijó', 1),

-- Alagoas
(6, 'Maceió', 2),
(7, 'Arapiraca', 2),
(8, 'Palmeira dos Índios', 2),
(9, 'Rio Largo', 2),
(10, 'Penedo', 2),

-- Amapá
(11, 'Macapá', 3),
(12, 'Santana', 3),
(13, 'Laranjal do Jari', 3),
(14, 'Oiapoque', 3),
(15, 'Mazagão', 3),

-- Amazonas
(16, 'Manaus', 4),
(17, 'Parintins', 4),
(18, 'Itacoatiara', 4),
(19, 'Manacapuru', 4),
(20, 'Coari', 4),

-- Bahia
(21, 'Salvador', 5),
(22, 'Feira de Santana', 5),
(23, 'Vitória da Conquista', 5),
(24, 'Camaçari', 5),
(25, 'Juazeiro', 5),

-- Ceará
(26, 'Fortaleza', 6),
(27, 'Caucaia', 6),
(28, 'Juazeiro do Norte', 6),
(29, 'Maracanaú', 6),
(30, 'Sobral', 6),

-- Distrito Federal
(31, 'Brasília', 7),
(32, 'Taguatinga', 7),
(33, 'Ceilândia', 7),
(34, 'Samambaia', 7),
(35, 'Planaltina', 7),

-- Espírito Santo
(36, 'Vitória', 8),
(37, 'Vila Velha', 8),
(38, 'Serra', 8),
(39, 'Cariacica', 8),
(40, 'Linhares', 8),

-- Goiás
(41, 'Goiânia', 9),
(42, 'Aparecida de Goiânia', 9),
(43, 'Anápolis', 9),
(44, 'Rio Verde', 9),
(45, 'Luziânia', 9),

-- Maranhão
(46, 'São Luís', 10),
(47, 'Imperatriz', 10),
(48, 'Caxias', 10),
(49, 'Timon', 10),
(50, 'Codó', 10),

-- Mato Grosso
(51, 'Cuiabá', 11),
(52, 'Várzea Grande', 11),
(53, 'Rondonópolis', 11),
(54, 'Sinop', 11),
(55, 'Tangará da Serra', 11),

-- Mato Grosso do Sul
(56, 'Campo Grande', 12),
(57, 'Dourados', 12),
(58, 'Três Lagoas', 12),
(59, 'Corumbá', 12),
(60, 'Ponta Porã', 12),

-- Minas Gerais
(61, 'Belo Horizonte', 13),
(62, 'Uberlândia', 13),
(63, 'Contagem', 13),
(64, 'Juiz de Fora', 13),
(65, 'Betim', 13),

-- Pará
(66, 'Belém', 14),
(67, 'Ananindeua', 14),
(68, 'Santarém', 14),
(69, 'Marabá', 14),
(70, 'Parauapebas', 14),

-- Paraíba
(71, 'João Pessoa', 15),
(72, 'Campina Grande', 15),
(73, 'Santa Rita', 15),
(74, 'Patos', 15),
(75, 'Bayeux', 15),

-- Paraná
(76, 'Curitiba', 16),
(77, 'Londrina', 16),
(78, 'Maringá', 16),
(79, 'Ponta Grossa', 16),
(80, 'Cascavel', 16),

-- Pernambuco
(81, 'Recife', 17),
(82, 'Jaboatão dos Guararapes', 17),
(83, 'Olinda', 17),
(84, 'Caruaru', 17),
(85, 'Petrolina', 17),

-- Piauí
(86, 'Teresina', 18),
(87, 'Parnaíba', 18),
(88, 'Picos', 18),
(89, 'Piripiri', 18),
(90, 'Floriano', 18),

-- Rio de Janeiro
(91, 'Rio de Janeiro', 19),
(92, 'São Gonçalo', 19),
(93, 'Duque de Caxias', 19),
(94, 'Nova Iguaçu', 19),
(95, 'Niterói', 19),

-- Rio Grande do Norte
(96, 'Natal', 20),
(97, 'Mossoró', 20),
(98, 'Parnamirim', 20),
(99, 'São Gonçalo do Amarante', 20),
(100, 'Macau', 20),

-- Rio Grande do Sul
(101, 'Porto Alegre', 21),
(102, 'Caxias do Sul', 21),
(103, 'Pelotas', 21),
(104, 'Canoas', 21),
(105, 'Santa Maria', 21),

-- Rondônia
(106, 'Porto Velho', 22),
(107, 'Ji-Paraná', 22),
(108, 'Ariquemes', 22),
(109, 'Vilhena', 22),
(110, 'Cacoal', 22),

-- Roraima
(111, 'Boa Vista', 23),
(112, 'Rorainópolis', 23),
(113, 'Caracaraí', 23),
(114, 'Mucajaí', 23),
(115, 'Pacaraima', 23),

-- Santa Catarina
(116, 'Florianópolis', 24),
(117, 'Joinville', 24),
(118, 'Blumenau', 24),
(119, 'São José', 24),
(120, 'Chapecó', 24),

-- São Paulo
(121, 'São Paulo', 25),
(122, 'Guarulhos', 25),
(123, 'Campinas', 25),
(124, 'São Bernardo do Campo', 25),
(125, 'Santo André', 25),

-- Sergipe
(126, 'Aracaju', 26),
(127, 'Nossa Senhora do Socorro', 26),
(128, 'Lagarto', 26),
(129, 'Itabaiana', 26),
(130, 'Estância', 26),

-- Tocantins
(131, 'Palmas', 27),
(132, 'Araguaína', 27),
(133, 'Gurupi', 27),
(134, 'Porto Nacional', 27),
(135, 'Paraíso do Tocantins', 27);

insert into sexo (id_sexo,sexo) values
(null,'Mulher'),
(null,'Homen'),
(null,'Outros');

insert into nacionalidade (id_nacionalidade,nacionalidade) values
(null,'Brasileira'),
(null,'Estrangeira');

insert into raca(id_raca,raca) values
(null,'Negro'),
(null,'Branco'),
(null,'Pardo'),
(null,'Amarelo'),
(null,'Indígena');

insert into escolaridade(id_escolaridade,escolaridade) values
(null, 'Educação Infantil'),
(null, 'Ensino Fundamental I'),
(null, 'Ensino Fundamental II'),
(null, 'Ensino Médio'),
(null, 'Ensino Técnico'),
(null, 'Ensino Superior'),
(null, 'Pós-Graduação'),
(null, 'Mestrado');

insert into clientes (cpf, rg, nome, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, fone) values
('21345678901', '2134567', 'Eduardo Lima', 21, 1, 1, 1, 1, '899999999'),
('22345678901', '2234567', 'Sofia Almeida',22, 2, 1, 2, 2, '888888888'),
('23345678901', '2334567', 'Miguel Santos', 23, 1, 1, 3, 3, '877777777'),
('24345678901', '2434567', 'Alice Oliveira', 24, 2, 1, 4, 4, '866666666'),
('25345678901', '2534567', 'Arthur Costa', 25, 1, 2, 5, 5, '855555555'),
('26345678901', '2634567', 'Helena Pereira', 26, 2, 1, 2, 6, '844444444'),
('27345678901', '2734567', 'Bernardo Souza', 27, 1, 1, 5, 7, '833333333'),
('28345678901', '2834567', 'Laura Fernandes', 28, 2, 1, 3, 8, '822222222'),
('29345678901', '2934567', 'Gabriel Rodrigues', 29, 1, 1, 4, 1, '811111111'),
('30345678901', '3034567', 'Manuela Martins', 30, 2, 1, 1, 2, '800000000'),
('31345678901', '3134567', 'Lucas Barbosa', 31, 1, 1, 3, 3, '799999999'),
('32345678901', '3234567', 'Valentina Lima', 32, 2, 1, 5, 4, '788888888'),
('33345678901', '3334567', 'Joaquim Silva', 33, 1, 1, 1, 5, '777777777'),
('34345678901', '3434567', 'Isabella Souza', 34, 2, 1, 3, 6, '766666666'),
('35345678901', '3534567', 'Henrique Costa', 35, 1, 1, 2, 7, '755555555'),
('36345678901', '3634567', 'Mariana Oliveira', 36, 2, 1, 3, 8, '744444444'),
('37345678901', '3734567', 'Theo Pereira', 37, 1, 1, 5, 1, '733333333'),
('38345678901', '3834567', 'Lara Fernandes', 38, 2, 2, 1, 2, '722222222'),
('39345678901', '3934567', 'Davi Rodrigues', 39, 1, 1, 2, 3, '711111111'),
('40345678901', '4034567', 'Beatriz Martins', 40, 2, 2, 2, 4, '700000000');

-- ---------------------------- 3°Parte -------------------------------------------------------------------------------------------------------------------------------

-- 1. Apresentar um select apenas com o nome e a cidade.
select clientes.nome,cidade.cidade from clientes join cidade on clientes.id_cidade = cidade.id_cidade;

-- 2. Apresensentar um select apenas com o nome e o estado.
select clientes.nome,estado.estado from clientes join estado on estado.id_estado;

-- 3. Apresentar um select apenas com o nome, cpf e a raça
select clientes.nome,clientes.cpf,raca.raca from clientes join raca on clientes.id_raca = raca.id_raca;

-- 4. Apresentar um select apenas com o nome a nacionalidade;
select clientes.nome,nacionalidade.nacionalidade from clientes join nacionalidade on clientes.id_nacionalidade = nacionalidade.id_nacionalidade;

-- 5. Apresentar um select apenas com o nome e a escolaridade;
select clientes.nome,escolaridade.escolaridade from clientes join escolaridade on clientes.id_escolaridade = escolaridade.id_escolaridade;

-- 6. Apresentar um select com o nome, cidade e estado;
select clientes.nome,cidade.cidade,estado.estado from clientes join cidade on clientes.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado;

-- 7 Apresentar um select com o nome, cidade, estado, fone, rg, sexo, nacionalidade, raça, escolaridade;
select nome, cidade.cidade, estado.estado, fone, rg, sexo.sexo, nacionalidade.nacionalidade, raca.raca, escolaridade.escolaridade from clientes 
join cidade on clientes.id_cidade = cidade.id_cidade
join estado on cidade.id_estado = estado.id_estado 
join sexo on clientes.id_sexo = sexo.id_sexo
join nacionalidade on clientes.id_nacionalidade = nacionalidade.id_nacionalidade
join raca on clientes.id_raca = raca.id_raca
join escolaridade on clientes.id_escolaridade = escolaridade.id_escolaridade;

-- Verificando se as cidades são dos respectivos estados.
select cidade,estado.estado from cidade join estado on cidade.id_estado = estado.id_estado; 
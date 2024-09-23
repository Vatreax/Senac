use dia1309;

# ----------------- Cliente Relacionado ----------------- #
select cliente_relacionado.*, dados_cadastrais.nomecliente from cliente_relacionado join dados_cadastrais on cliente_relacionado.idcliente = dados_cadastrais.idcliente;
describe cliente_relacionado; 

INSERT INTO cliente_relacionado (
    idcliente,
    cliente_vinculado,
    relacionamento,
    data_relacionamento,
    descricao_relacionamento,
    importancia_relacionamento
) VALUES (
    1,                  -- Substitua por um valor válido para idcliente
    'João Silva',         -- Nome do cliente vinculado
    'Familia',           -- Tipo de relacionamento
    '2024-09-15',        -- Data do relacionamento
    'Cliente de longa data, é um primo distante.', -- Descrição do relacionamento
    'Alta'               -- Importância do relacionamento
);

alter table cliente_relacionado modify cliente_vinculado varchar(255) not null;
alter table cliente_relacionado modify relacionamento enum('Familia','Negocios') not null;
alter table cliente_relacionado modify data_relacionamento date not null;
alter table cliente_relacionado modify importancia_relacionamento enum('Alta','Media','Baixa') not null;
# ----------------- Cliente Relacionado ----------------- #

# ----------------- Comunicação ----------------- #
rename table comunicação to comunicacao;
select * from comunicacao;
describe comunicacao;

INSERT INTO comunicacao (
    idcomunicacao,
    idcliente,
    whatsapp1,
    whatsapp2,
    email_login,
    contate_nos
) VALUES (
    1,                       
    1,                     
    '+551199999999',         
    '+551188888888',         
    'carlos.silva@gmail.com',
    'Favor contatar via email para mais detalhes.' 
);

alter table comunicacao change emaillogin email_login varchar(50);


# ----------------- Comunicação ----------------- #

# ----------------- Contatos ----------------- #
select * from contatos;
describe contatos;
select contatos.*, dados_cadastrais.nomecliente from contatos join dados_cadastrais on contatos.idcliente = dados_cadastrais.idcliente;

INSERT INTO `contatos` (
    `idcliente`,
    `nome_contato`,
    `email_contato`,
    `cargo`,
    `tipo_contato`
) VALUES (
    2,                          -- idcliente, deve corresponder a um id existente na tabela dadoscadastrais
    'Maria Oliveira',             -- nome_contato
    'maria.oliveira@example.com', -- email_contato
    'Gerente de Vendas',          -- cargo
    'Comercial'                   -- tipo_contato
);

alter table contatos modify email_contato varchar(255) not null;
# ----------------- Contatos ----------------- #

# ----------------- Dados Adicionais ----------------- #
select * from dados_adicionais;
describe dados_adicionais;
select dados_adicionais.*, dados_cadastrais.nomecliente from dados_adicionais join dados_cadastrais on dados_adicionais.idcliente = dados_cadastrais.idcliente;

INSERT INTO dados_adicionais (
    idcliente,
    observacoes,
    tipo_relacionamento,
    data_cadastro,
    status_cliente,
    codigo_promocional
) VALUES (
    2,                           -- idcliente, deve corresponder a um id existente na tabela dadoscadastrais
    'Cliente com interesse em novos produtos.', -- observacoes
    'Parceria',                    -- tipo_relacionamento
    '2024-09-15',                 -- data_cadastro
    'Ativo',                       -- status_cliente
    'PROMO2024'                    -- codigo_promocional
);

alter table dados_adicionais modify data_cadastro date not null;
alter table dados_adicionais modify tipo_relacionamento enum("Familia","Negocios","Parceria") not null DEFAULT "Parceria";
alter table dados_adicionais modify status_cliente enum("Ativo","Inativo") not null DEFAULT "Inativo";
# ----------------- Dados Adicionais ----------------- #

# ----------------- Dados Cadastrais ----------------- #
rename table dadoscadastrais to dados_cadastrais;
select * from dados_cadastrais;
describe dados_cadastrais;


alter table dados_cadastrais drop column sexo;
alter table dados_cadastrais modify rg varchar(15);
alter table dados_cadastrais change emaillogin1 email_login varchar(50);
alter table dados_cadastrais modify foto mediumblob;
alter table dados_cadastrais add column sexo enum("Homem","Mulher","Outro");
alter table dados_cadastrais modify aliquota float;
alter table dados_cadastrais modify ICMS float;


update dados_cadastrais set sexo = 'Homem' where idcliente = 1 ;
update dados_cadastrais set sexo = 'Homem' where idcliente = 3 ;
update dados_cadastrais set sexo = 'Mulher' where idcliente = 2;
update dados_cadastrais set sexo = 'Mulher' where idcliente = 4;
# ----------------- Dados Cadastrais ----------------- #

# ----------------- Endereço ----------------- #
select * from enderecos;
describe enderecos;

INSERT INTO enderecos (idcliente, endereco, numero, cidade, estado, cep)
VALUES (1, 'Rua das Flores', '100', 'Campo Grande', 'Mato Grosso do Sul', '79000-000');


alter table enderecos drop column cpf;
alter table enderecos modify cidade varchar(100) not null;
alter table enderecos modify estado varchar(100) not null;
alter table enderecos modify cep varchar(10) not null;
# ----------------- Endereço ----------------- #

# ----------------- Extra ----------------- #
select * from extra;
describe extra;

alter table extra modify facebook varchar(100);
alter table extra modify instagram varchar(100);
alter table extra modify linkedin varchar(100);
alter table extra modify X varchar(100);
# ----------------- Extra ----------------- #

# ----------------- Financeiro ----------------- #
select * from financeiro;
describe financeiro;

alter table financeiro modify valor float;
alter table financeiro modify limite_credito float;
# ----------------- Financeiro ----------------- #

# ----------------- login ----------------- #
select * from login;
describe login;

alter table login change emaillogin email_login varchar(20) not null;
# ----------------- login ----------------- #

# ----------------- NFVendapeças ----------------- #
rename table NFVendapeças to NFVendapecas;
select * from NFVendapecas;
describe NFVendapecas;


alter table NFVendapecas modify docto varchar(50);
alter table NFVendapecas modify numeropedido int;
alter table NFVendapecas modify prazoent date;
# ----------------- NFVendapeças ----------------- #

# ----------------- Ordem Serviço ----------------- #
select * from ordemservico;
describe ordemservico;

alter table ordemservico modify documento varchar(30);
alter table ordemservico change valorserviço valor_servico decimal;
# ----------------- Ordem Serviço ----------------- #

# ----------------- Peças ----------------- #
select * from pecas;
describe pecas;
alter table pecas modify PS varchar(20);

# -------------- Tela Cadastro --------------#
select * from telacadastro;
describe telacadastro;
alter table telacadastro modify telcomercial varchar(18);
# -------------- Tela Cadastro --------------#

# ------------------------ Vendedores ------------------------#
select * from vendedores;
describe vendedores;
alter table vendedores modify telefonevend varchar(18);
# ------------------------ Vendedores ------------------------#
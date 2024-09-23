drop database if exists tela_de_login;
create database tela_de_login;
use tela_de_login;

# Tela Cadastro
create table tela_cadastro (
id_cliente int auto_increment primary key,
nome varchar(50),
razao_social varchar(50),
data_nasc date,
tel_comercial varchar(50),
tel_resid varchar(50),
cpf_or_cnpj varchar(30),
indicou varchar(250),
regime_de_tributação enum('Pessoa Fisica','Pessoa Juridica'),
email varchar(100),
email_cobranca varchar(100),
email_danfe varchar(100),
email_loja varchar(100),
rg varchar(19),
ramal varchar(10),
fax varchar(10),
situacao_icms varchar(30),
insc_suframa varchar(50),
sexo enum('Homem','Mulher','Outro'),
insc_estadual varchar(50),
insc_municipal varchar(50),
transportadora_1 varchar(50),
transportadora_2 varchar(50),
tabela_de_preco varchar(250),
frete enum('Frete Rodoviário', 'Frete Aéreo', 'Frete Marítimo', 'Frete Ferroviário', 'Frete Expresso', 'Frete Courier'),
sit_cad enum('Aprovado','Reprovado'),
linha_do_pef varchar (50),
aliquota$ float,
icms_st_carga_tributaria_media boolean,
e_fornecedor boolean,
enviar_email_cadastramento boolean,
enviar_email_loja boolean
);

INSERT INTO tela_cadastro (
    nome, 
    razao_social, 
    data_nasc, 
    tel_comercial, 
    tel_resid, 
    cpf_or_cnpj, 
    indicou, 
    regime_de_tributação, 
    email, 
    email_cobranca, 
    email_danfe, 
    email_loja, 
    rg, 
    ramal, 
    fax, 
    situacao_icms, 
    insc_suframa, 
    sexo, 
    insc_estadual, 
    insc_municipal, 
    transportadora_1, 
    transportadora_2, 
    tabela_de_preco, 
    frete, 
    sit_cad, 
    linha_do_pef, 
    aliquota$, 
    icms_st_carga_tributaria_media, 
    e_fornecedor, 
    enviar_email_cadastramento, 
    enviar_email_loja
) VALUES (
    'Ana Costa', 
    'Comércio em Geral', 
    '1990-04-12', 
    '21 98765-4321', 
    '21 91234-5678', 
    '123.456.789-01', 
    'Carlos Silva', 
    'Pessoa Fisica', 
    'ana.costa@example.com', 
    'cobranca@exemplo.com', 
    'danfe@exemplo.com', 
    'loja@exemplo.com', 
    '12.345.678', 
    '789', 
    '101', 
    'Normal', 
    '1234567891', 
    'Mulher', 
    'RJ-12345678', 
    '654321', 
    'Transportadora X', 
    'Transportadora Y', 
    'Tabela B', 
    'Frete Aéreo', 
    'Aprovado', 
    'Linha 2', 
    15.50, 
    TRUE, 
    FALSE, 
    TRUE, 
    FALSE
);

# Mostar
select * from tela_cadastro;

# Comando Editar
UPDATE tela_cadastro
SET 
    nome = 'Ana Costa', 
    razao_social = 'Loja de Roupas Ana Costa', 
    data_nasc = '1990-04-12', 
    tel_comercial = '21 98765-4321', 
    tel_resid = '21 91234-5678', 
    cpf_or_cnpj = '123.456.789-01', 
    indicou = 'Carlos Silva', 
    regime_de_tributação = 'Pessoa Fisica', 
    email = 'ana.costa@example.com', 
    email_cobranca = 'cobranca@exemplo.com', 
    email_danfe = 'danfe@exemplo.com', 
    email_loja = 'loja@exemplo.com', 
    rg = '12.345.678', 
    ramal = '789', 
    fax = '101', 
    situacao_icms = 'Normal', 
    insc_suframa = '1234567891', 
    sexo = 'Mulher', 
    insc_estadual = 'RJ-12345678', 
    insc_municipal = '654321', 
    transportadora_1 = 'Transportadora X', 
    transportadora_2 = 'Transportadora Y', 
    tabela_de_preco = 'Tabela B', 
    frete = 'Frete Aéreo', 
    sit_cad = 'Aprovado', 
    linha_do_pef = 'Linha 2', 
    aliquota$ = 15.50, 
    icms_st_carga_tributaria_media = TRUE, 
    e_fornecedor = FALSE, 
    enviar_email_cadastramento = TRUE, 
    enviar_email_loja = FALSE
WHERE id_cliente = 1;

# Deletar Usuário
#delete from tela_cadastro where id_cliente = 1;

# Cadastro Ordem de Serviço
create table ordem_servico (
documento varchar(50) primary key unique,
emissao date,
id_cliente int,
foreign key (id_cliente) references tela_cadastro (id_cliente),
previsao date,
descricao varchar(100),
execucao varchar(50),
servico varchar(50),
variante varchar(50),
quantidade integer,
valor float
);

INSERT INTO ordem_servico (documento, emissao, id_cliente, previsao, descricao, execucao, servico, variante, quantidade, valor)
VALUES ('DOC006', '2024-09-20', 1, '2024-10-05', 'Substituição de peças', 'Pendente', 'Manutenção', 'Premium', 4, 3200.00);

# Deletar Documento
#delete from ordem_servico where documento = "DOC006";

# Mostrar
select ordem_servico.*, tela_cadastro.nome from ordem_servico join tela_cadastro on ordem_servico.id_cliente = tela_cadastro.id_cliente;

# Editar Documento
UPDATE ordem_servico
SET 
    emissao = '2024-09-21',
    id_cliente = 1,
    previsao = '2024-10-10',
    descricao = 'Troca de componentes eletrônicos',
    execucao = 'Em andamento',
    servico = 'Reparo',
    variante = 'Especial',
    quantidade = 5,
    valor = 4000.00
WHERE documento = 'DOC006';

# Peças
create table pecas(
codigo varchar(50) primary key unique,
descricao varchar(100),
variante varchar(50),
pBARRAs float,
quantidade_base integer,
quantidade integer,
unidade_medida varchar(50),
custo_unitario float,
custo_total float,
quantidade_fixa float,
ordem varchar(50),
CI varchar(50),
origem integer,
status_peca enum('Ativado','Desligado')
);


INSERT INTO pecas (
    codigo, descricao, variante, pBARRAs, quantidade_base, quantidade, 
    unidade_medida, custo_unitario, custo_total, quantidade_fixa, 
    ordem, CI, origem, status_peca
) VALUES
('PE001', 'Parafuso A', 'Standard', 1234567890123, 100, 50, 
 'unidade', 0.25, 12.50, 10.0, 
 'ORD001', 'CI001', 1, 'Ativado'),
 
('PE002', 'Engrenagem B', 'Premium', 1234567890124, 200, 120, 
 'unidade', 1.50, 180.00, 15.0, 
 'ORD002', 'CI002', 2, 'Desligado'),
 
('PE003', 'Rolamento C', 'Deluxe', 1234567890125, 150, 80, 
 'unidade', 2.75, 220.00, 20.0, 
 'ORD003', 'CI003', 3, 'Ativado'),
 
('PE004', 'Mola D', 'Basic', 1234567890126, 300, 200, 
 'unidade', 0.90, 180.00, 25.0, 
 'ORD004', 'CI004', 1, 'Ativado'),
 
('PE005', 'Cabo E', 'Standard', 1234567890127, 500, 350, 
 'metro', 0.45, 157.50, 30.0, 
 'ORD005', 'CI005', 2, 'Desligado');

# Delete
#Delete from pecas where codigo = '';

# Mostar
select * from pecas;

# Editar Peças
UPDATE pecas
SET 
    descricao = 'Rolamento C - Atualizado',
    variante = 'Deluxe Plus',
    pBARRAs = 1234567890128,
    quantidade_base = 160,
    quantidade = 90,
    unidade_medida = 'unidade',
    custo_unitario = 3.00,
    custo_total = 270.00,
    quantidade_fixa = 25.0,
    ordem = 'ORD006',
    CI = 'CI006',
    origem = 4,
    status_peca = 'Ativado'
WHERE codigo = 'PE003';

# Nota Fiscal
create table nota_fiscal(
documento varchar(50) primary key unique,
sequencia int,
emissao date,
hora time,
vencimento date,
previsao_faturamento date,
aprovacao_cliente date,
hora_aprovacao time,
embarques integer,
prazo_entrega_dias integer,
n°pedido integer,
vendedor varchar(50),
id_cliente int,
foreign key (id_cliente) references tela_cadastro (id_cliente),
endereco_entrega float(50),
tabela_preco enum("Vendedor","Revendedor"),
transportadora1 varchar(50),
transportadora2 varchar(50),
frete enum('Frete Rodoviário', 'Frete Aéreo', 'Frete Marítimo', 'Frete Ferroviário', 'Frete Expresso', 'Frete Courier'),
valor_frete float,
desconto float,
valor_desconto_rateado float,
contato enum('Telefone', 'Email', 'WhatsApp', 'Outro'),
historico varchar(50),
faturamentos float,
doc_pecas varchar(50),
foreign key (doc_pecas) references pecas (codigo)
);

INSERT INTO nota_fiscal (
    documento, sequencia, emissao, hora, vencimento, previsao_faturamento, 
    aprovacao_cliente, hora_aprovacao, embarques, prazo_entrega_dias, 
    n°pedido, vendedor, id_cliente, endereco_entrega, tabela_preco, 
    transportadora1, transportadora2, frete, valor_frete, desconto, 
    valor_desconto_rateado, contato, historico, faturamentos, doc_pecas
) VALUES
('NF001', 1, '2024-09-10', '09:00:00', '2024-09-20', '2024-09-15', 
 '2024-09-12', '10:30:00', 2, 7, 
 12345, 'Luiz Oliveira', 1, 123.45, 'Vendedor', 
 'Transportadora A', 'Transportadora B', 'Frete Rodoviário', 100.00, 15.00, 
 5.00, 'Telefone', 'Primeira compra do cliente', 3500.00, 'PE001');

INSERT INTO nota_fiscal (
    documento, sequencia, emissao, hora, vencimento, previsao_faturamento, 
    aprovacao_cliente, hora_aprovacao, embarques, prazo_entrega_dias, 
    n°pedido, vendedor, id_cliente, endereco_entrega, tabela_preco, 
    transportadora1, transportadora2, frete, valor_frete, desconto, 
    valor_desconto_rateado, contato, historico, faturamentos, doc_pecas
) VALUES
('NF002', 2, '2024-09-15', '14:00:00', '2024-09-25', '2024-09-20', 
 '2024-09-17', '15:00:00', 3, 10, 
 67890, 'Ana Souza', 1, 456.78, 'Revendedor', 
 'Transportadora C', 'Transportadora D', 'Frete Aéreo', 200.00, 25.00, 
 10.00, 'Email', 'Pedido urgente', 5000.00, 'PE005');


# Mostrar
select nota_fiscal.*, tela_cadastro.nome from nota_fiscal join tela_cadastro on nota_fiscal.id_cliente = tela_cadastro.id_cliente;

# Editar Nota Fiscal
UPDATE nota_fiscal
SET 
    emissao = '2024-09-11',
    hora = '10:15:00',
    vencimento = '2024-09-22',
    previsao_faturamento = '2024-09-18',
    aprovacao_cliente = '2024-09-13',
    hora_aprovacao = '11:00:00',
    embarques = 3,
    prazo_entrega_dias = 8,
    n°pedido = 54321,
    vendedor = 'Luiz Oliveira Atualizado',
    endereco_entrega = 125.75,
    tabela_preco = 'Revendedor',
    transportadora1 = 'Transportadora X',
    transportadora2 = 'Transportadora Y',
    frete = 'Frete Expresso',
    valor_frete = 130.00,
    desconto = 12.00,
    valor_desconto_rateado = 6.00,
    contato = 'WhatsApp',
    historico = 'Compra revisada e atualizada',
    faturamentos = 3600.00,
    doc_pecas = 'PE002'
WHERE documento = 'NF001';

UPDATE nota_fiscal
SET 
    emissao = '2024-09-16',
    hora = '15:45:00',
    vencimento = '2024-09-30',
    previsao_faturamento = '2024-09-25',
    aprovacao_cliente = '2024-09-18',
    hora_aprovacao = '16:30:00',
    embarques = 4,
    prazo_entrega_dias = 12,
    n°pedido = 67891,
    vendedor = 'Ana Souza Atualizada',
    endereco_entrega = 460.90,
    tabela_preco = 'Vendedor',
    transportadora1 = 'Transportadora Z',
    transportadora2 = 'Transportadora W',
    frete = 'Frete Marítimo',
    valor_frete = 220.00,
    desconto = 20.00,
    valor_desconto_rateado = 12.00,
    contato = 'Email',
    historico = 'Pedido urgente revisado',
    faturamentos = 5200.00,
    doc_pecas = 'PE004'
WHERE documento = 'NF002';


# Deletar Nota Fiscal
delete from nota_fiscal where documento = "";




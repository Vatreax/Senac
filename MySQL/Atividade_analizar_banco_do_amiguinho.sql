use dia1309;

# --- Sobre o Banco de Dados ---
# Somente algumas descrições deveriam ser NULL.
# Outros dados são obrigatórios, sendo necessário o uso do NOT NULL.

select * from cliente_relacionado;
describe cliente_relacionado; 
# 0 - Não a reclamação, ta dboas <3 (^-^)

select * from comunicação;
describe comunicação;
# 1 - Nome com ç.
# 2 - emaillogin não esta conectado com os dados cadastrais.
  

select * from contatos;
describe contatos;
# 0 - Não a reclamação, ta dboas <3 (^-^).

select * from dados_adicionais;
describe dados_adicionais;
# 0 - Não a reclamação, ta dboas <3 (^-^).

select * from dadoscadastrais;
describe dadoscadastrais;
# 1 - Rg não pode ser integer, pode começar com 0.
# 2 - Por favor, não coloquem email e login juntos, um l duplo fica confuso. Nesse caso deveria ter seguido o padrão de email_loja e ter colocado email_login1.
# 3 - Longblob ocupa 4gb, podendo ser utilizado Mediumblob ao invés.
# 4 - Sexo deveria ser Enum.
# 5 - Aliquota deveriam ser float, por serem porcentagem.
# 6 - Não abreviar palavras, isso dificulta a interpretação e compreeensão dos dados.
# 7 - ICMS deveria ser uma opção em booleano.
# 8 - O emaillogin1 esta desconectado com a table login, onde possui uma outra variável emailogin.

select * from enderecos;
describe enderecos;
# 1 - Cpf no endereço.
# 2 - Cpf não pode ser integer, pois pode começar com zero. Na dúvida varchar.
# 3 - Cidade, Estado e Cep deveriam ser não nulos.

select * from extra;
describe extra;
# 1 - Poderiam aumentar o valor dos varchar para 50, pois existem nomes nessas redes maiores que 20.

select * from financeiro;
describe financeiro;
# 1 - Valor deveria ser float.
# 2 - Limite de crédito deveria ser float.

select * from login;
describe login;
# 1 - Senha não pode ser nulo.

select * from NFVendapeças;
describe NFVendapeças;
# 1 - (Docto) Documento pode começar com 0, não pode ser int. Na Dúvida varchar.
# 2 - Nome da tabela deveria sempre ser tudo em minusculo, para manter consistência.
# 3 - Sem caracteres brasileiros no nome da tabela, sem usar ç.
# 4 - Separar palavras no nome por _.
# 5 - Não abrevie as palavras em nomes, Ao invéz de NF, use Nota Fiscal. Ao invéz de Docto use Documento.
# 6 - Porcentagens não precisam ser precisas, pode usar float nelas.
# 7 - 'prazoent' deveria ser date ao invés de int.
# 8 - numeropedido deveria ser int ao invés de varchar.

select * from ordemservico;
describe ordemservico;
# 1 - Documento pode começar com 0, não pode ser int. Na Dúvida varchar.
# 2 - Não usar caracteres brasileiros nas variaveis da tabela. Não use ç.

select * from pecas;
describe pecas;
# 1 - Mantenha consistência, se vai separar espaço por _, faça isso com todas as variaveis. Ex : qntdbase vs custo_unitario.
# 2 - Não abrevie as palavras.
# 3 - Não tenha letras maiusculas.
# 4 - PS não é varchar(1), Price per Sale costuma ser um pouco maior.
# 5 - peças deveria ser conectado obrigatoriamente com a NFV.

select * from perfil;
describe perfil;
# 0 - Não a reclamação, ta dboas <3 (^-^).

select * from telacadastro;
describe telacadastro;
# 1 - Um telefone comercial e residencial ambos tem a mesma quantia de numeros.

select * from vendedores;
describe vendedores;
# 1 - Decida a quantia de numeros que um telefone tem antes de colocar essa variavel na db, a tabela de tela cadastro tem dois com 16 e 18, essa tem um com 15.
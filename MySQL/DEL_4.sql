#    4. No MySQL Workbench, utilizando o banco de dados ‘sprint’:
#    Criar a tabela chamada Professor para conter os dados: idProfessor, nome (tamanho 50),
#    especialidade (tamanho 40), dtNasc (date), sendo que idProfessor é a chave primária da
#    tabela.
#    Exemplo do campo data: ‘AAAA-MM-DD’, ‘1983-10-13’.
#    Inserir dados na tabela, procurando colocar uma especialista para mais de um professor.
#    Procure inserir pelo menos uns 6 professores.
#    Execute os comandos para:

drop database if exists sprint;
create database sprint;
use sprint;

create table Professor(
idProfessor int auto_increment primary key,
nome varchar(50),
especialidade varchar(40),
dtNasc date
);

# SET_SQL_SAFE_UPDATES = 0;

insert into Professor (nome, especialidade, dtNasc) values
    ('Ana Costa', 'Matemática', '1985-06-15'),
    ('Carlos Silva', 'Física', '1978-11-23'),
    ('Maria Oliveira', 'Química', '1980-03-30'),
    ('Pedro Almeida', 'História', '1990-05-12'),
    ('Joana Martins', 'Geografia', '1987-09-08'),
    ('Lucas Pereira', 'Literatura', '1983-12-01');

#    a) Exibir todos os dados da tabela.
select * from Professor;

#    b) Adicionar o campo funcao do tipo varchar(50), onde a função só pode ser ‘monitor’,
#    ‘assistente’ ou ‘titular’;
alter table Professor add column funcao varchar(50);
alter table Professor modify funcao enum('monitor','assistente','titular');
describe Professor;

#    c) Atualizar os professores inseridos e suas respectivas funções;
update Professor set funcao = 'monitor' where idProfessor = 1;
update Professor set funcao = 'assistente' where idProfessor = 2;
update Professor set funcao = 'assistente' where idProfessor = 3;
update Professor set funcao = 'titular' where idProfessor = 4;
update Professor set funcao = 'assistente' where idProfessor = 5;
update Professor set funcao = 'monitor' where idProfessor = 6;

#    d) Inserir um novo professor;
insert into Professor (nome, especialidade, dtNasc, funcao) values
    ('João Pedro','Filosofia','1990-04-01','titular');

#    e) Excluir o professor onde o idProfessor é igual a 5;
delete from Professor where idProfessor = 5;

#    f) Exibir apenas os nomes dos professores titulares;
select nome from Professor where funcao = 'titular';

#    g) Exibir apenas as especialidades e as datas de nascimento dos professores monitores;
select especialidade,dtNasc from Professor where funcao = 'monitor';

#    h) Atualizar a data de nascimento do idProfessor igual a 3;
update Professor set dtNasc = '2000-04-01' where idProfessor = 3;

#    i) Limpar a tabela Professor;
truncate Professor;
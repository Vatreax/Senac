use ibge;
select * from senso where estado = 'Mato Grosso do Sul';
select * from senso where nome_mun like 'C%';
select * from senso where nome_mun = 'Campo Grande' or nome_mun = 'Terenos';
select * from senso where populacao < 1000;
select * from senso where estado = 'Mato Grosso do Sul' and populacao > 100000; 
select estado,nome_mun from senso; 
select nome_mun,pib from senso order by pib desc limit 1;
select nome_mun,pib_per_cap from senso order by pib_per_cap desc limit 1;
select nome_mun,populacao from senso order by populacao desc limit 1;
select nome_mun,populacao from senso order by populacao asc limit 1;
select estado,nome_mun,populacao from senso;
select count(*) from senso;
select avg(pib) from senso;
select avg(populacao) from senso;
select avg(pib_per_cap) from senso;
select estado from senso where estado like '_A%';
select estado from senso where estado like 'B%';
select * from senso where cod_meso_reg = 5003;

 
select * from senso cross join uf on uf.cod_uf = senso.cod_uf;
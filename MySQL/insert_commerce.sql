use commerce;



-- insert into EX2_PRODUTO (codproduto,descricao,quantidade) value
-- 	     	(null,"Gelado",1),
--  	 	(null,"Macio",2),
--          (null,"Impolgante",5),
--          (null,"Jubilante",15),
--          (null,"Vazio",2),
--         (null,"Triste",1),
--         (null,"Esperança",60),
--         (null,"Felicidade",4);

drop table EX2_PEDIDO;
insert into EX2_PEDIDO (codpedido,codcliente,datapedido,nf,valortotal) value
		(1,6,"2015-11-02","2216643311223341044",199.99),
        (2,7,"2012-12-01","1111333399557722122",10000.10),
        (3,8,"2020-08-01","1244448832001199222",2440.150),
        (4,9,"2021-07-21","2222299111882220011",200.00),
        (5,10,"2010-03-04","0001119922881117722",1220.91);

insert into EX2_ITEMPEDIDO (codpedido,numeroitem,valorunitario,quantidade,codproduto) value
		(1,null,1225.00,20,5),
        (2,null,1225.00,20,6),
        (3,null,1225.00,20,7),
        (4,null,1225.00,20,8),
        (5,null,1225.00,20,9);
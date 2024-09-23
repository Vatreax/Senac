DROP DATABASE IF EXISTS registros;
CREATE DATABASE registros;
USE registros;

CREATE TABLE login(
id_user int auto_increment primary key,
usuario varchar(50),
senha varchar(50),
texto varchar(50)
);

INSERT INTO login (usuario,senha) VALUES
	('Rafael Montiel','raf123'),
    ('Alan','alano23'),
    ('Varin','var23'),
    ('Jubileu','jub123'),
    ('Cleito Rasta','gelo'),
    ('L','13');	

SELECT * FROM registros.login;

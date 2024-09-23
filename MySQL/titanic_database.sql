create database if not exists titanicos;
use titanicos;

# drop table titanic_base;
create table titanic_base(
PassengerId int primary key,
Survived int,
Pclass int,
Nome varchar(100),
Sex varchar(20),
Age varchar(20),
SibSp int,
Parch int,
Ticket varchar(50),
Fare float,
Cabin varchar(50),
Embarked varchar(10)
);

select * from titanic_base;
select count(*) from titanic_base;

# --- Quantos Sobreviveram/Morreram
select count(*) from titanic_base where Survived = 0;
select count(*) from titanic_base where Survived = 1;

# --- Quantas Crianças Abaixo dos 12 Anos Sobreviveram/Morreram
select count(*) from titanic_base where Age < 12 and  age <> '' and Survived = 1;
select * from titanic_base where Age < 12 and  age <> '' and Survived = 1;
select * from titanic_base where Age < 12 and  age <> '' and Survived = 0;

# --- Quantas Mulheres Sobreviveram/Morreram
select count(*) from titanic_base where Sex = 'female' and Survived = 1;
select count(*) from titanic_base where Sex = 'female' and Survived = 0;
select * from titanic_base where Sex = 'female' and Survived = 1;

# --- Quantos Homens Sobreviveram/Morreram
select count(*) from titanic_base where Sex = 'Male' and Survived = 1;
select count(*) from titanic_base where Sex = 'Male' and Survived = 0;
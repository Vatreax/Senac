drop database if exists  Fofoca;
create database Fofoca;
use Fofoca;

create table administrador(
id_admin int auto_increment primary key,
nome varchar(50),
senha varchar(50),

);

create table cliente(
id_user int auto_increment primary key,
nome varchar(50),
senha varchar(50)
);

create table famoso(
id_famoso int auto_increment primary key,
nome varchar(50),
senha varchar(50)
);
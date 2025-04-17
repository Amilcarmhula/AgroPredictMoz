create database agropredictmoz;

use agropredictmoz;

create table previsoes(
	id integer primary key auto_increment,
    localizacao varchar(100) not null,
    temperatura decimal(5,3) not null,
    chuva decimal(5,3) not null,
    recomendacoes varchar(300) not null,
    data_registo timestamp default current_timestamp
);

desc previsoes;
   drop database agropredictmoz;
create database agropredictmoz;

use agropredictmoz;

create table previsao(
	id integer primary key auto_increment,
    localizacao varchar(100) not null,
    temperatura decimal(5,3) not null,
    umidade  decimal(5,3) not null,
    precipitacao decimal(5,3) not null,
    luz_solar integer not null,
    data_registo timestamp default current_timestamp
);

create table recomendacao(
	id integer primary key auto_increment,
    recomendacoes varchar(300) not null,
    fk_id_previsao integer not null,
    foreign key (fk_id_previsao) references previsao(id)
);

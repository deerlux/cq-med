CREATE TABLE IF NOT EXISTS jianchazhibiao (
    zhibiao_id bigserial not null,
    zhibiao_code varchar(8),
    zhibiao_name varchar(32) not null,
    zhibiao_name_eng varchar(16),
    zhibiao_unit varchar(16),
    zhibiao_ref1 float,
    zhibiao_ref2 float,
    PRIMARY KEY(zhibiao_id)
);

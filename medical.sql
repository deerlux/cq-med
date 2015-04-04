-- this script is for PostgreSQL 9.4

CREATE TABLE IF NOT EXISTS jianchazhibiao (
    zhibiao_id bigserial not null,
    zhibiao_code varchar(8),
    zhibiao_name varchar(32) not null,
    zhibiao_name_eng varchar(16),
    zhibiao_unit varchar(16),
    zhibiao_ref1 float,
    zhibiao_ref2 float,
    PRIMARY KEY(zhibiao_id),
    UNIQUE (zhibiao_name, zhibiao_name_eng)
);
CREATE INDEX ON jianchazhibiao(zhibiao_name);
CREATE INDEX ON jianchazhibiao(zhibiao_name_eng);

CREATE TABLE IF NOT EXISTS jiancha_image_store(
    image_id bigserial not null,
    image_path varchar(128),
    primary key(image_id)
);

CREATE TABLE IF NOT EXISTS user_info(
    user_id varchar(16) not null,
    user_name varchar(32),
    email varchar(64),
    address varchar(64),
    --- flase is female, true is male ---
    gender boolean,
    birthday date,
    register_time timestamp with time zone,
    primary key(user_id)
);

CREATE INDEX ON user_info(user_id);
CREATE INDEX ON user_info(user_name);

CREATE TABLE IF NOT EXISTS user_test_value(
    user_test_id bigserial not null,
    test_time timestamp with time zone,
    test_value float,
    zhibiao bigint REFERENCES jianchazhibiao (zhibiao_id),
    test_image bigint REFERENCES jiancha_image_store (image_id),
    user_id varchar(16) REFERENCES user_info (user_id),
    primary key(user_test_id)
);

CREATE INDEX ON user_test_value(test_time);




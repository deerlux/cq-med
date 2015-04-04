
CREATE TABLE IF NOT EXISTS jianchazhibiao (
    zhibiao_id bigint not null auto_increment,
    zhibiao_code varchar(8),
    zhibiao_name varchar(32) not null,
    zhibiao_name_eng varchar(16),
    zhibiao_unit varchar(16),
    zhibiao_ref1 float,
    zhibiao_ref2 float,
    PRIMARY KEY(zhibiao_id),
    UNIQUE (zhibiao_name, zhibiao_name_eng)
);
CREATE INDEX zhibiao_name_idx ON jianchazhibiao(zhibiao_name);
CREATE INDEX zhibiao_name_eng_idx ON jianchazhibiao(zhibiao_name_eng);

CREATE TABLE IF NOT EXISTS jiancha_image_store(
    image_id bigint not null auto_increment,
    image_path varchar(128),
    primary key(image_id)
);

CREATE TABLE IF NOT EXISTS user_info(
    user_id varchar(16) not null,
    user_name varchar(32),
    email varchar(64),
    address varchar(64),
    gender boolean,
    birthday date,
    register_time timestamp,
    primary key(user_id)
);

CREATE INDEX user_id_idx ON user_info(user_id);
CREATE INDEX user_name_idx ON user_info(user_name);

CREATE TABLE IF NOT EXISTS user_test_value(
    user_test_id bigint not null auto_increment,
    test_time timestamp,
    test_value float,
    zhibiao bigint,
    index (zhibiao),
    constraint foreign key (zhibiao) REFERENCES jianchazhibiao (zhibiao_id),
    test_image bigint,
    index (test_image),
    constraint foreign key (test_image) REFERENCES jiancha_image_store (image_id),
    user_id varchar(16),
    index (user_id),
    constraint foreign key (user_id) REFERENCES user_info (user_id),
    primary key(user_test_id)
);

CREATE INDEX test_time_idx ON user_test_value(test_time);




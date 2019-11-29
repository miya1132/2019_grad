-- データベース作成
create database 2019_grad_db;

-- DB選択
use 2019_grad_db;

-- テーブル作成
CREATE TABLE users (
  id int(11) NOT NULL AUTO_INCREMENT,
  created_by int(11) DEFAULT NULL,
  updated_by int(11) DEFAULT NULL,
  name varchar(64) NOT NULL,
  kana varchar(64) DEFAULT NULL,
  login_id varchar(64) NOT NULL,
  password varchar(64) NOT NULL,
  created_at datetime NOT NULL,
  updated_at datetime NOT NULL,
  PRIMARY KEY (id),
  KEY index_users_on_name (name)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4;

insert into users(name,login_id,password,created_at,updated_at) values('テスト01','dev','dev',now(),now());

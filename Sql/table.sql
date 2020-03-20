CREATE TABLE stock_list (
  id int(11) unsigned NOT NULL AUTO_INCREMENT,
  name varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (id),
  UNIQUE KEY unique_stock (name)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8;


CREATE TABLE user_trade (
  id int(11) unsigned NOT NULL AUTO_INCREMENT,
  date date NOT NULL,
  rate int(11) NOT NULL,
  stock_id int(11) unsigned NOT NULL,
  trade char(4) NOT NULL DEFAULT '',
  quantity int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY user_trade_stock_id_foreign (stock_id),
  CONSTRAINT user_trade_stock_id_foreign FOREIGN KEY (stock_id) REFERENCES stock_list (id)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
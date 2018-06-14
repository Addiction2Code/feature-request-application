-- Need to setup relationships.

drop table if exists feature_requests;
create table feature_requests (
  id integer primary key autoincrement,
  title string not null,
  description string not null,
  client integer,
  client_priority integer,
  target_date date,
  product_area string null,
  created_at datetime
);

drop table if exists clients;
create table clients (
  id integer primary key autoincrement,
  name string not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username string not null,
  password string not null
);

CREATE DATABASE IF NOT EXISTS `Users`;
GRANT ALL ON Users.* TO 'user'@'%';

USE Users;

create table Users(
  user_id int,
  user_name varchar(7),
  user_pass varchar(11),
  primary key(user_id)
)DEFAULT CHARACTER SET=utf8;

insert into Users(user_id,user_name,user_pass) 
values(5191028,'5191028','51910282020'),
      (5191059,'5191059','51910592020'),
      (5191037,'5191037','51910372020'),
      (5191032,'5191032','51910322020')

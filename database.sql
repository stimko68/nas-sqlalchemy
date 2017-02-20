DROP DATABASE IF EXISTS star_trek;
CREATE DATABASE IF NOT EXISTS star_trek;
USE star_trek;

CREATE TABLE IF NOT EXISTS captain (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  metadata JSON DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB, CHARSET='utf8mb4';

CREATE TABLE IF NOT EXISTS ship (
  id INT AUTO_INCREMENT,
  captain_fk INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  reg_number VARCHAR(20) NOT NULL,
  max_warp_speed FLOAT DEFAULT 1,
  PRIMARY KEY (id),
  FOREIGN KEY (captain_fk) REFERENCES captain (id)
) ENGINE=InnoDB, CHARSET='utf8mb4';

/* Seed data */
INSERT INTO captain SET first_name = 'Jonathan', last_name = 'Archer';
INSERT INTO captain SET first_name = 'James', last_name = 'Kirk';
INSERT INTO captain SET first_name = 'Jean Luc', last_name = 'Picard';

INSERT INTO ship SET name = 'Enterprise', reg_number = 'NX-01', max_warp_speed = 5.0, captain_fk = 1;
INSERT INTO ship SET name = 'Enterprise', reg_number = 'NCC-1701', max_warp_speed = 9.9, captain_fk = 2;
INSERT INTO ship SET name = 'Enterprise', reg_number = 'NCC-1701-A', max_warp_speed = 9.9, captain_fk = 2;
INSERT INTO ship SET name = 'Enterprise', reg_number = 'NCC-1701-D', max_warp_speed = 9.9, captain_fk = 3;

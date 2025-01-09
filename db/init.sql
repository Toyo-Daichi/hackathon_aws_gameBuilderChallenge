CREATE DATABASE gameday;

\c gameday;

REVOKE ALL ON DATABASE gameday FROM public;

CREATE USER appuser WITH
LOGIN
PASSWORD  'password';

GRANT CONNECT ON DATABASE gameday TO appuser;
GRANT USAGE ON SCHEMA public TO appuser;

GRANT pg_read_all_data TO appuser;
GRANT pg_write_all_data TO appuser;

CREATE TYPE public.roletype AS ENUM('Player', 'Enemy'); 
CREATE TYPE public.gamemode AS ENUM('Normal', 'DoS', 'DDoS'); 

DROP TABLE IF EXISTS characters CASCADE;
CREATE TABLE characters (
  id            SERIAL PRIMARY KEY,
  name          VARCHAR(64),
  role          ROLETYPE,
  x_coord       INT,
  y_coord       INT,
  create_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
  id            SERIAL PRIMARY KEY,
  name          VARCHAR(64),
  character_id  INT REFERENCES characters(id) ON DELETE SET NULL,
  create_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  update_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS scores CASCADE;
CREATE TABLE scores (
  id            SERIAL PRIMARY KEY,
  user_id       INT REFERENCES users(id) ON DELETE CASCADE,
  gamemode      GAMEMODE,
  value         INT NOT NULL,
  create_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data;
INSERT INTO characters (name, role, x_coord, y_coord, create_at, update_at)
values ('Mario', 'Player', 80, 32, NOW(), NOW()),
   ('Luigi', 'Player', 96, 32, NOW(), NOW()),
   ('Basic1', 'Player',  0,  0, NOW(), NOW()),
   ('Basic2',  'Enemy', 16,  0, NOW(), NOW()),
   ('Cat',     'Enemy', 32,  0, NOW(), NOW()),
   ('Slime',   'Enemy', 48,  0, NOW(), NOW()),
   ('Ghost',   'Enemy', 64,  0, NOW(), NOW()),
   ('Mash',    'Enemy', 80,  0, NOW(), NOW()),
   ('Packen1', 'Enemy',  0, 32, NOW(), NOW()),
   ('Basic3',  'Enemy', 32, 32, NOW(), NOW()),
   ('Basic4',  'Enemy', 48, 32, NOW(), NOW()),
   ('Fish',    'Enemy', 64, 32, NOW(), NOW()),
   ('Basic5',  'Enemy',  0, 64, NOW(), NOW()),
   ('Basic6',  'Enemy', 16, 64, NOW(), NOW()),
   ('Packen2', 'Enemy', 48, 64, NOW(), NOW()),
   ('Killer',  'Enemy', 64, 64, NOW(), NOW());

INSERT INTO users (name, character_id, create_at, update_at)
values ('anoymous', 1, NOW(), NOW());

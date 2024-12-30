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

DROP TABLE IF EXISTS characters CASCADE;
CREATE TABLE characters (
  id            SERIAL PRIMARY KEY,
  name          VARCHAR(64),
  role          ROLETYPE,
  path          VARCHAR(64),
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
  value         INT NOT NULL,
  create_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data;
INSERT INTO characters (name, role, path, create_at, update_at)
values ('Ship', 'Player', './', NOW(), NOW());

INSERT INTO users (name, character_id, create_at, update_at)
values ('anoymous', 1, NOW(), NOW());

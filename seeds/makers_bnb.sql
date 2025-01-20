DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS homes;
DROP SEQUENCE IF EXISTS homes_id_seq;
DROP TABLE IF EXISTS available_dates;
DROP SEQUENCE IF EXISTS available_dates_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS homes_id_seq;

CREATE TABLE homes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    location VARCHAR(255),
    price_per_night int,
    users_id int
);

CREATE SEQUENCE IF NOT EXISTS available_dates_id_seq;

CREATE TABLE available_dates ( 
    id SERIAL PRIMARY KEY, 
    home_id INT NOT NULL, 
    date_available DATE NOT NULL, 
    FOREIGN KEY (home_id) REFERENCES homes(id) ON DELETE CASCADE, 
    UNIQUE (home_id, date_available) 
);




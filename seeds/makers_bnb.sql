DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
DROP TABLE IF EXISTS homes;
DROP SEQUENCE IF EXISTS homes_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

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
    user_id int,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;

CREATE TABLE requests ( 
    id SERIAL PRIMARY KEY, 
    status VARCHAR(255),
    date_submitted DATE NOT NULL,
    home_id INT NOT NULL, 
    user_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (home_id) REFERENCES homes (id) ON DELETE CASCADE
    
    --UNIQUE (home_id, date_available) 
);

INSERT INTO users (username, email, password) VALUES ('test_username', 'test@email.com', 'test_password');
INSERT INTO users (username, email, password) VALUES ('test_username2', 'test2@email.com', 'test_password2');

INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('test_title', 'test_description', 'test_location', 100, 1);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('test_title2', 'test_description2', 'test_location2', 100, 2);

INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2000-01-01', '1', '1', '2000-02-05', '2000-02-07');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2000-01-01', '1', '1', '2000-02-05', '2000-02-07');
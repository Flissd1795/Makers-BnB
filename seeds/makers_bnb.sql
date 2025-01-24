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
    price_per_night float, 
    user_id int,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS requests_id_seq;

CREATE TABLE requests ( 
    id SERIAL PRIMARY KEY, 
    status VARCHAR(255) DEFAULT 'unseen',
    date_submitted DATE,
    home_id INT, 
    user_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (home_id) REFERENCES homes (id) ON DELETE CASCADE
    --UNIQUE (home_id, date_available) 
);

INSERT INTO users (username, email, password) VALUES ('Ducky', 'ducky@email.com', 'duck');
INSERT INTO users (username, email, password) VALUES ('test_username2', 'test2@email.com', 'test_password2');

INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Hotel room I found the key for', 'This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in.', 'Central London (most of the time)', 100, 1);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('The cave', 'Damp and smelly', 'Wales', 100, 1);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Gary''s garage', 'Room for more than a car', 'Front of Garys house', 1000, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Steve''s shed', 'Better than Garys garage', 'Back of Steves house', 100, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Barry''s basement', 'Dark and dingy', 'At the bottom', 50, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Carl''s climbingframe', 'Lots of fun to be had', 'Outside somewhere', 100, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Andy''s attic', 'Large and lofty', 'At the top', 100, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Graham''s garden', 'Lots of room for activities', 'The back of Grahams house', 10, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Tony''s toilet', 'Fragrant', 'The bog', 3000, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Freddie''s fruitbowl', 'Small and cosy', 'Kitchen counter', 200, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Penelope''s plane', 'Cosy stay in the cockpit', 'In the air', 30, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Alana''s allotment', 'Lovely fruit and veg', 'In a field', 100, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Love island villa', 'Great spot for a fireside chat', 'Spain', 100, 2);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Ilona''s igloo', 'Bit chilly', 'North Pole', 70, 1);
INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('Tory''s treehouse', 'Dont visit if scared of heights', 'In a tree', 500, 2);

INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2025-01-01', '1', '2', '2025-02-09', '2025-02-13');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2024-11-25', '1', '2', '2025-01-05', '2025-01-07');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2025-01-03', '1', '2', '2025-02-09', '2025-02-13');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2025-01-20', '1', '2', '2025-02-03', '2025-02-07');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2025-01-01', '2', '2', '2025-02-09', '2025-02-13');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2024-11-25', '2', '2', '2025-01-05', '2025-01-07');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2025-01-03', '2', '2', '2025-02-09', '2025-02-13');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2025-01-20', '2', '2', '2025-02-03', '2025-02-07');

INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('unseen', '2025-01-11', '9', '1', '2025-02-13', '2025-02-14');
INSERT INTO requests (status, date_submitted, home_id, user_id, start_date, end_date) VALUES ('confirmed', '2024-10-05', '11', '1', '2025-03-02', '2025-03-13');
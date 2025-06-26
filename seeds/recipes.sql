DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    avg_time INT,
    rating FLOAT 
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, avg_time, rating) VALUES ('Spaghetti Bolognese', 45, 4.5);
INSERT INTO recipes (name, avg_time, rating) VALUES ('Chicken Curry', 60, 4.7);
INSERT INTO recipes (name, avg_time, rating) VALUES ('Vegetable Stir Fry', 25, 4.2);
INSERT INTO recipes (name, avg_time, rating) VALUES ('Beef Tacos', 30, 4.6);
INSERT INTO recipes (name, avg_time, rating) VALUES ('Lemon Cheesecake', 90, 4.9);

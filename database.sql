CREATE DATABASE todoDB; 

CREATE TABLE todo(
    todo_id SERIAL PRIMARY KEY, 
    description VARCHAR(255)
);
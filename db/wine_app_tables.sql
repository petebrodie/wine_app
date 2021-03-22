DROP TABLE IF EXISTS wines;
DROP TABLE IF EXISTS producers;

CREATE TABLE producers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number INT,
    email VARCHAR(255),
    country VARCHAR(255),
    region VARCHAR(255)

);


CREATE TABLE wines(
    id SERIAL PRIMARY KEY,
    grape_variety VARCHAR(255),
    description VARCHAR(255),
    cost_price FLOAT,
    retail_price FLOAT,
    stock INT,
    producer VARCHAR(255)
);
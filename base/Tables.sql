create database seucurity_application_test_db;
\c seucurity_application_test_db

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password text NOT NULL
);
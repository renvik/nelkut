CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE inproceedings (
    id SERIAL PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    year INTEGER,
    booktitle TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE article (
    id SERIAL PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume INTEGER,
    start_page INTEGER,
    end_page INTEGER,
    user_id INTEGER REFERENCES users
);

CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    year INTEGER,
    publisher TEXT,
    user_id INTEGER REFERENCES users
);

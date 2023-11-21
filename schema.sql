CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE inproceedings (
    id INTEGER PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    year INTEGER,
    booktitle TEXT
    user_id INTEGER REFERENCES users
);

CREATE TABLE article (
    id INTEGER PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    journal TEXT,
    year INTEGER,
    volume INTEGER,
    pages TEXT
    user_id INTEGER REFERENCES users
);

CREATE TABLE book (
    id INTEGER PRIMARY KEY,
    cite_id TEXT UNIQUE,
    author TEXT,
    title TEXT,
    year INTEGER,
    publisher TEXT,
    user_id INTEGER REFERENCES users
);

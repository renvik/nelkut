DROP DATABASE IF EXISTS nelkut;
DROP DATABASE IF EXISTS nelkut_tests;

CREATE DATABASE nelkut;
CREATE DATABASE nelkut_tests;
\c nelkut;

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
	start_page INTEGER,
	end_page INTEGER,
	user_id INTEGER REFERENCES users
);

CREATE TABLE articles (
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

CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	cite_id TEXT UNIQUE,
	author TEXT,
	title TEXT,
	year INTEGER,
	publisher TEXT,
	start_page INTEGER,
	end_page INTEGER,
	user_id INTEGER REFERENCES users
);

\c nelkut_tests;

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
	start_page INTEGER,
	end_page INTEGER,
	user_id INTEGER REFERENCES users
);

CREATE TABLE articles (
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

CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	cite_id TEXT UNIQUE,
	author TEXT,
	title TEXT,
	year INTEGER,
	publisher TEXT,
	start_page INTEGER,
	end_page INTEGER,
	user_id INTEGER REFERENCES users
);


INSERT INTO inproceedings (cite_id, author, title, year, booktitle, start_page, end_page)  VALUES ('test_id_1', 'test_1_author', 'test_1_title', 1, 'test_1_booktitle', 1, 2);
INSERT INTO inproceedings (cite_id, author, title, year, booktitle, start_page, end_page)  VALUES ('test_id_2', 'test_2_author', 'test_2_title', 1, 'test_2_booktitle', 1, 2);
INSERT INTO articles (cite_id, author, title, journal, year, volume, start_page, end_page)  VALUES ('test_id_3', 'test_3_author', 'test_3_title', 'test_3_journal', 1, 2, 1, 2);
INSERT INTO articles (cite_id, author, title, journal, year, volume, start_page, end_page)  VALUES ('test_id_4', 'test_4_author', 'test_4_title', 'test_4_journal', 1, 2, 1, 2);
INSERT INTO books (cite_id, author, title, year, publisher, start_page, end_page)  VALUES ('test_id_5', 'test_5_author', 'test_5_title', 1, 'test_5_publisher', 1, 2);
INSERT INTO books (cite_id, author, title, year, publisher, start_page, end_page)  VALUES ('test_id_6', 'test_6_author', 'test_6_title', 1, 'test_6_publisher', 1, 2);
import unittest
import refservice
from flask import Flask
from db import db
from os import getenv
from sqlalchemy.sql import text
import subprocess
import platform

class MockupRequest:
    def __init__(self, form):
        self.form = form

initSQL = """
INSERT INTO inproceedings (cite_id, author, title, year, booktitle, start_page, end_page)  VALUES ('test_id_1', 'test_1_author', 'test_1_title', 1, 'test_1_booktitle', 1, 2);
INSERT INTO inproceedings (cite_id, author, title, year, booktitle, start_page, end_page)  VALUES ('test_id_2', 'test_2_author', 'test_2_title', 1, 'test_2_booktitle', 1, 2);
INSERT INTO articles (cite_id, author, title, journal, year, volume, start_page, end_page)  VALUES ('test_id_3', 'test_3_author', 'test_3_title', 'test_3_journal', 1, 2, 1, 2);
INSERT INTO articles (cite_id, author, title, journal, year, volume, start_page, end_page)  VALUES ('test_id_4', 'test_4_author', 'test_4_title', 'test_4_journal', 1, 2, 1, 2);
INSERT INTO books (cite_id, author, title, year, publisher, start_page, end_page)  VALUES ('test_id_5', 'test_5_author', 'test_5_title', 1, 'test_5_publisher', 1, 2);
INSERT INTO books (cite_id, author, title, year, publisher, start_page, end_page)  VALUES ('test_id_6', 'test_6_author', 'test_6_title', 1, 'test_6_publisher', 1, 2);
"""

class RefServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE")
        self.db = db

        if platform.system() == "Windows":
            subprocess.call("bash reset_test_db.bash")
        else:
            subprocess.call("./reset_test_db.bash")

        with self.app.app_context():
            self.db.init_app(self.app)
            self.db.session.execute(text(initSQL))
            self.db.session.commit()

    def test_add_book_to_database(self):
        
        with self.app.app_context():
            initial_amount = len(refservice.list_books(self.db))
            request = MockupRequest({"cite_id": "abcdefghijk", 
                                     "author": "Some Author", 
                                     "title": "Some Title", 
                                     "year": 1, 
                                     "publisher": "Some Publisher", 
                                     "start_page": 1, 
                                     "end_page": 2,
                                     "user_id": 1})
            refservice.add_book_to_database(self.db, request)
            books = refservice.list_books(self.db)
            self.assertEqual(len(books), initial_amount + 1)

    def test_add_article_to_database(self):
        
        with self.app.app_context():
            initial_amount = len(refservice.list_articles(self.db))
            request = MockupRequest({"cite_id": "smfokmsc", 
                                    "author": "jfpapoksad", 
                                    "title": "adslkjasldk", 
                                    "journal": "lafdsjajds", 
                                    "year": 1, 
                                    "volume": 2, 
                                    "start_page": 3, 
                                    "end_page": 4,
                                    "user_id": 1})
            refservice.add_article_to_database(self.db, request)
            articles = refservice.list_articles(self.db)
            self.assertEqual(len(articles), initial_amount + 1)

    def test_add_inproceeding_to_database(self):
        
        with self.app.app_context():
            initial_amount = len(refservice.list_inproceedings(self.db))
            request = MockupRequest({"cite_id": "ldjfajsja", 
                                    "author": "lasjdljsadk", 
                                    "title": "lajdsjaslkdjö", 
                                    "year": 1, 
                                    "booktitle": "sapjdajd", 
                                    "start_page": 2, 
                                    "end_page": 3,
                                    "user_id": 1})
            refservice.add_inproceeding_to_database(self.db, request)
            inproceedings = refservice.list_inproceedings(self.db)
            self.assertEqual(len(inproceedings), initial_amount + 1)

    def test_lists_length(self):

        with self.app.app_context():
            books, articles, inproceedings = refservice.list_references(self.db)
            self.assertEqual(len(books), 2)
            self.assertEqual(len(articles), 2)
            self.assertEqual(len(inproceedings), 2)

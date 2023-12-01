import unittest
import refservice
from flask import Flask
from db import db
from os import getenv
from sqlalchemy.sql import text

class MockupRequest:
    def __init__(self, form):
        self.form = form

class RefServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE")
        self.db = db
    
    def test_add_book_to_database(self):
        
        with self.app.app_context():
            self.db.init_app(self.app)
            initial_amount = len(refservice.list_books(self.db))
            request = MockupRequest({"cite_id": "abcdefghijk", 
                                     "author": "Some Author", 
                                     "title": "Some Title", 
                                     "year": 1, 
                                     "publisher": "Some Publisher", 
                                     "start_page": 1, 
                                     "end_page": 2})
            refservice.add_book_to_database(self.db, request)
            books = refservice.list_books(self.db)
            self.assertEqual(len(books), initial_amount + 1)

    def test_add_article_to_database(self):
        
        with self.app.app_context():
            self.db.init_app(self.app)
            initial_amount = len(refservice.list_articles(self.db))
            request = MockupRequest({"cite_id": "smfokmsc", 
                                    "author": "jfpapoksad", 
                                    "title": "adslkjasldk", 
                                    "journal": "lafdsjajds", 
                                    "year": 1, 
                                    "volume": 2, 
                                    "start_page": 3, 
                                    "end_page": 4})
            refservice.add_article_to_database(self.db, request)
            articles = refservice.list_articles(self.db)
            self.assertEqual(len(articles), initial_amount + 1)

    def test_add_inproceeding_to_database(self):
        
        with self.app.app_context():
            self.db.init_app(self.app)
            initial_amount = len(refservice.list_inproceedings(self.db))
            request = MockupRequest({"cite_id": "ldjfajsja", 
                                    "author": "lasjdljsadk", 
                                    "title": "lajdsjaslkdjö", 
                                    "year": 1, 
                                    "booktitle": "sapjdajd", 
                                    "start_page": 2, 
                                    "end_page": 3})
            refservice.add_inproceeding_to_database(self.db, request)
            inproceedings = refservice.list_inproceedings(self.db)
            self.assertEqual(len(inproceedings), initial_amount + 1)

    def test_lists_length(self):

        with self.app.app_context():
            self.db.init_app(self.app)
            books, articles, inproceedings = refservice.list_references(self.db)
            self.assertEqual(len(books), 3)
            self.assertEqual(len(articles), 3)
            self.assertEqual(len(inproceedings), 3)

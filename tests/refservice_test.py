import unittest
import refservice
from flask import Flask
from db import db
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class MockupRequest:
    def __init__(self, form):
        self.form = form

class RefServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE")
#        print("Tämän alla pitäisi olla jotian")
#        print(self.app.config["SQLALCHEMY_DATABASE_URI"])
#        print("tämän yllä pitisi olla jotain")
        self.db = db
    
    def test_add_book_to_database(self):
        
        with self.app.app_context():
            self.db.init_app(self.app)
            request = MockupRequest({"cite_id": "Some Cite id", 
                                     "author": "Some Author", 
                                     "title": "Some Title", 
                                     "year": 1, 
                                     "publisher": "Some Publisher", 
                                     "start_page": 1, 
                                     "end_page": 2})
            refservice.add_book_to_database(self.db, request)
            books = self.db.session.execute(text("SELECT * FROM books")).fetchall()
            self.assertEqual(books, 1)

    def test_lists_length(self):

        with self.app.app_context():
            self.db.init_app(self.app)
            books, articles, inproceedings = refservice.list_references(self.db)
            self.assertEqual(len(books)+len(articles)+len(inproceedings), 6)

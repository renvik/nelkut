import unittest
import refservice
from flask import Flask
from db import db
from os import getenv
from flask_sqlalchemy import SQLAlchemy

class RefServiceTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE")
        self.db = db

    def test_lists_length(self):

        with self.app.app_context():
            self.db.init_app(self.app)
            books, articles, inproceedings = refservice.list_references(self.db)
            self.assertEqual(len(books)+len(articles)+len(inproceedings), 6)
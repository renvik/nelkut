import unittest
from reference_list import list_references
from flask import Flask
from db import db
from flask_sqlalchemy import SQLAlchemy

class TestReferenceList(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///nelkut_tests"
        self.db = db

    def test_lists_length(self):

        with self.app.app_context():
            self.db.init_app(self.app)
            books, articles, inproceedings = list_references(self.db)
            self.assertEqual(len(books)+len(articles)+len(inproceedings), 6)
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///nelkut"
db = SQLAlchemy(app)

def list_references():
    sql = "SELECT * FROM book"
    books = db.session.execute(text(sql)).fetchall()
    sql = "SELECT * FROM article"
    articles = db.session.execute(text(sql)).fetchall()
    sql = "SELECT * FROM inproceedings"
    inproceedings = db.session.execute(text(sql)).fetchall()
    return books, articles, inproceedings
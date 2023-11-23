from db import db
from sqlalchemy.sql import text

def list_references():
    references = []
    books = list_books()
    for i in books:
        references.append(i)
    articles = list_articles()
    for i in articles:
        references.append(i)
    inproceedings = list_inproceedings()
    for i in inproceedings:
        references.append(i)
    return references

def list_books():
    sql = "SELECT * FROM books"
    books = db.session.execute(text(sql)).fetchall()
    return books

def list_articles():
    sql = "SELECT * FROM articles"
    articles = db.session.execute(text(sql)).fetchall()
    return articles

def list_inproceedings():
    sql = "SELECT * FROM inproceedings"
    inproceedings = db.session.execute(text(sql)).fetchall()
    return inproceedings
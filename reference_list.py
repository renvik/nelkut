
from sqlalchemy.sql import text

def list_references(books, articles, inproceedings):
    references = []
    for i in books:
        references.append(i)
    for i in articles:
        references.append(i)
    for i in inproceedings:
        references.append(i)
    return references

def list_books(db):
    sql = "SELECT * FROM books"
    books = db.session.execute(text(sql)).fetchall()
    return books

def list_articles(db):
    sql = "SELECT * FROM articles"
    articles = db.session.execute(text(sql)).fetchall()
    return articles

def list_inproceedings(db):
    sql = "SELECT * FROM inproceedings"
    inproceedings = db.session.execute(text(sql)).fetchall()
    return inproceedings
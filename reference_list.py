
from sqlalchemy.sql import text


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

def list_references(db):
	books = list_books(db)
	articles = list_articles(db)
	inproceedings = list_inproceedings(db)
	return books, articles, inproceedings
from db import db
from sqlalchemy.sql import text

def list_references():
    references = []
    sql = "SELECT * FROM books"
    books = db.session.execute(text(sql)).fetchall()
    for i in books:
        references.append(i)
    sql = "SELECT * FROM articles"
    articles = db.session.execute(text(sql)).fetchall()
    for i in articles:
        references.append(i)
    sql = "SELECT * FROM inproceedings"
    inproceedings = db.session.execute(text(sql)).fetchall()
    for i in inproceedings:
        references.append(i)
    return references
from db import db
from sqlalchemy.sql import text

def add_book_to_database(request):
    title = request["title"]
    author = request["author"]
    year = request["year"]
    publisher = request["publisher"]
    start_page = request["start_page"]
    end_page = request["end_page"]
    cite_id = request["cite_id"]
    sql = text("INSERT INTO books (cite_id, title, author, year, publisher, start_page, end_page) VALUES (:cite_id, :title, :author, :year, :publisher, :start_page, :end_page)")
    db.session.execute(sql, {"books"})
        

#    def validate_reference(self, reference):
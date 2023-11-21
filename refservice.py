from db import db
from sqlalchemy.sql import text

def __insert(table_name, keys, request):
	colon = ':'
	sql = text(f"INSERT INTO {table_name} ({', '.join(__keys)}) VALUES ({', '.join(colon + key for key in __keys)})")
	db.session.execute(sql, {key: request.form[key] for key in __keys})
	db.session.commit()

def add_inproceeding_to_database(request):
	keys = ["cite_id", "title", "author", "year", "publisher", "start_page", "end_page"]

	__insert("inproceedings", keys, request)

def add_article_to_database(request):
	keys = ["cite_id", "author", "title", "journal", "year", "volume", "start_page", "end_page"]

	__insert("articles", keys, request)

def add_book_to_database(request):
	keys = ["cite_id", "author", "title", "year", "publisher", "start_page", "end_page"]

	__insert("books", keys, request)

#    def validate_reference(self, reference):
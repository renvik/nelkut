from db import db
from sqlalchemy.sql import text

def __insert(table_name, keys, request):
	colon = ':'
	sql = text(f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(colon + key for key in keys)})")
	db.session.execute(sql, {key: request.form[key] for key in keys})
	db.session.commit()

def add_inproceeding_to_database(request):
	keys = ["cite_id", "author", "title", "year", "booktitle", "start_page", "end_page"]

	__insert("inproceedings", keys, request)

def add_article_to_database(request):
	keys = ["cite_id", "author", "title", "journal", "year", "volume", "start_page", "end_page"]

	__insert("articles", keys, request)

def add_book_to_database(request):
	keys = ["cite_id", "author", "title", "year", "publisher", "start_page", "end_page"]

	__insert("books", keys, request)

def validate_reference(keys, table_name, request):
	new = tuple([request.form[key] for key in keys])
	all = db.session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
	for reference in all:
		if new == reference:
			pass
	pagecheck(request)
	
def pagecheck(request):
	start_page = request.form["start_page"]
	end_page = request.form["end_page"]
	if end_page < start_page:
		pass
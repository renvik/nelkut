from sqlalchemy.sql import text
from flask import session

def __insert(db, table_name, keys, request, user_id):
	colon = ':'
	sql = text(f"INSERT INTO {table_name} ({', '.join(keys)}, user_id) VALUES ({', '.join(colon + key for key in keys)}, :user_id)")
	keys_dict = {key: request.form[key] for key in keys}
	keys_dict["user_id"] = user_id
	db.session.execute(sql, keys_dict)
	db.session.commit()

def add_inproceeding_to_database(db, request, user_name):
	keys = ["cite_id", "author", "title", "year", "booktitle", "start_page", "end_page"]
	user_id = check_and_fetch_users_cite_id_duplicate(request.form["cite_id"], user_name, db)
	if user_id:
		__insert(db, "inproceedings", keys, request, user_id)
	# TODO error handling

def add_article_to_database(db, request, user_name):
	keys = ["cite_id", "author", "title", "journal", "year", "volume", "start_page", "end_page"]
	user_id = check_and_fetch_users_cite_id_duplicate(request.form["cite_id"], user_name, db)
	if user_id:
		__insert(db, "articles", keys, request, user_id)
	# TODO error handling

def add_book_to_database(db, request, user_name):
	keys = ["cite_id", "author", "title", "year", "publisher", "start_page", "end_page"]
	user_id = check_and_fetch_users_cite_id_duplicate(request.form["cite_id"], user_name, db)
	if user_id:
		__insert(db, "books", keys, request, user_id)
	# TODO error handling

def check_and_fetch_users_cite_id_duplicate(cite_id, username, db):
	sql = "SELECT id FROM users WHERE username=:username"
	user_id = db.session.execute(text(sql), {"username":username}).fetchone()[0]
	for i in ["books", "articles", "inproceedings"]:
		sql = f"SELECT * FROM {i} WHERE cite_id=:cite_id AND user_id=:user_id"
		check = db.session.execute(text(sql), {"cite_id":cite_id,"user_id":user_id}).fetchall()
		if check:
			return False
	return user_id

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
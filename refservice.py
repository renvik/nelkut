from sqlalchemy.sql import text

def __insert(db, table_name, keys, request):
	colon = ':'
	sql = text(f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(colon + key for key in keys)})")
	db.session.execute(sql, {key: request.form[key] for key in keys})
	db.session.commit()

def add_inproceeding_to_database(db, request):
	keys = ["cite_id", "author", "title", "year", "booktitle", "start_page", "end_page", "user_id"]
	check_users_cite_id_duplicate(request.form["cite_id"], request.form["user_id"], db)

	__insert(db, "inproceedings", keys, request)

def add_article_to_database(db, request):
	keys = ["cite_id", "author", "title", "journal", "year", "volume", "start_page", "end_page", "user_id"]
	check_users_cite_id_duplicate(request.form["cite_id"], request.form["user_id"], db)

	__insert(db, "articles", keys, request)

def add_book_to_database(db, request):
	keys = ["cite_id", "author", "title", "year", "publisher", "start_page", "end_page", "user_id"]
	check_users_cite_id_duplicate(request.form["cite_id"], request.form["user_id"], db)

	__insert(db, "books", keys, request)

def check_users_cite_id_duplicate(cite_id, user_id, db):
	for i in ["books", "articles", "inproceedings"]:
		sql = f"SELECT * FROM {i} WHERE cite_id=:cite_id AND user_id=:user_id"
		check = db.session.execute(text(sql), {"cite_id":cite_id,"user_id":user_id}).fetchall()
		if not check:
			return False
	return True

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
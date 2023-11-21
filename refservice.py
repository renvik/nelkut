from db import db
from sqlalchemy.sql import text


def add_book_to_database(request):
	__keys = ["cite_id", "title", "author", "year", "publisher", "start_page", "end_page"]

	colon = ':'
	sql = text(f"INSERT INTO books ({', '.join(__keys)}) VALUES ({', '.join(colon + key for key in __keys)})")
	db.session.execute(sql, {key: request.form[key] for key in __keys})
	db.session.commit()

#    def validate_reference(self, reference):
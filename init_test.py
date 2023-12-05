from os import getenv
from flask import Flask
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
import subprocess
import platform

def init_test(init_sql=None):
	app = Flask(__name__)
	app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE")
	db = SQLAlchemy()

	if platform.system() == "Windows":
		subprocess.call("bash reset_test_db.bash")
	else:
		subprocess.call("./reset_test_db.bash")

	with app.app_context():
		db.init_app(app)
		if init_sql:
			db.session.execute(text(init_sql))
			db.session.commit()

	return app, db

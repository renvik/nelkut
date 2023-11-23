from flask import Flask
from db import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///nelkut"
db.init_app(app)

import routes
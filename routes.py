from flask import render_template
from app import app
from os import getenv
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add")
def add():
	return render_template("add_reference.html")

@app.route("/list")
def list():
	pass

from flask import request, redirect, render_template
from app import app
import db
import refservice

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add", methods=["GET"])
def add():
	return render_template("add_reference.html")

@app.route("/add_inproceedings", methods=["GET", "POST"])
def add_inproceedings():
	if request.method == "GET":
		return render_template("add_inproceedings_reference.html")

	# todo: add the stuff from request to the database

	return redirect("/")

@app.route("/add_article", methods=["GET", "POST"])
def add_article():
	if request.method == "GET":
		return render_template("add_article_reference.html")

	# todo: add the stuff from request to the database

	return redirect("/")

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
	if request.method == "GET":
		return render_template("add_book_reference.html")

	# todo: add the stuff from request to the database
	refservice.add_book_to_database(request)

	return redirect("/")

@app.route("/list")
def list():
	references = db.list_references()
	return render_template("list_references.html")
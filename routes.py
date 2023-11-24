from flask import request, redirect, render_template
from app import app
from reference_list import list_references, list_articles, list_books, list_inproceedings
import refservice
from db import db

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add", methods=["GET"])
def add():
	return render_template("add_reference.html")

@app.route("/add_inproceeding", methods=["GET", "POST"])
def add_inproceeding():
	if request.method == "GET":
		return render_template("add_inproceeding_reference.html")

	# todo: add the stuff from request to the database
	refservice.add_inproceeding_to_database(request)

	return redirect("/")

@app.route("/add_article", methods=["GET", "POST"])
def add_article():
	if request.method == "GET":
		return render_template("add_article_reference.html")

	# todo: add the stuff from request to the database
	refservice.add_article_to_database(request)

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
	books = list_books(db)
	articles = list_articles(db)
	inproceedings = list_inproceedings(db)
	references = list_references(books, articles, inproceedings)
	return render_template("list_references.html" , references = references)
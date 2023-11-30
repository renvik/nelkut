from flask import request, redirect, render_template
from app import app
import refservice
from db import db
from bibtex_creator import write_bibtex_file, sort_entries

@app.route("/")
def index():
	books, articles, inproceedings = refservice.list_references(db)
	return render_template("index.html", books = books, articles = articles, inproceedings = inproceedings)


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

@app.route("/bibtex")
def bibtex():
	write_bibtex_file(sort_entries(), "bibtex.bib")
	return redirect("/")


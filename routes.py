from flask import request, redirect, render_template
from app import app
import db

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
	if request.method == "GET":
		return render_template("add_reference.html")

	# todo: add the stuff from request to the database

	return redirect(f"/")

@app.route("/list")
def list():
	references = db.list_references()
	return render_template("list_references.html")
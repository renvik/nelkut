from flask import request, redirect, render_template
from app import app

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

	return render_template("list_references.html")

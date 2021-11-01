from flask import render_template
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
	print("JJJJJJJJJJJJJJJAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
	return render_template("index.html")

@main.route('/mesec/<m>', methods=['GET', 'POST'])
def mesec(m):
	print("JANUAR")
	return render_template("mesec.html", m=m)
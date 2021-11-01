from flask import render_template
from . import main
from .. import db
from ..models import Dan

@main.route('/', methods=['GET', 'POST'])
def index():
	print("JJJJJJJJJJJJJJJAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
	return render_template("index.html")

@main.route('/mesec/<m>', methods=['GET', 'POST'])
def mesec(m):
	print("JANUAR")
	dnevi = Dan.query.filter_by(mesec=m.lower())
	return render_template("mesec.html", m=m, dnevi=dnevi)
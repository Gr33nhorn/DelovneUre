from . import db
from datetime import datetime

class Dan(db.Model):
	__tablename__='dnevi'
	id = db.Column(db.Integer, primary_key=True)
	datum = db.Column(db.DateTime, default=datetime.utcnow)
	zacetek = db.Column(db.DateTime, default=datetime.utcnow)
	konec = db.Column(db.DateTime, default=datetime.utcnow)
	stevilo_ur = db.Column(db.Integer)
	mesec = db.Column(db.String(64))

	def __repr__(self):
		return '<Dan %r>' % self.id
from . import db
from datetime import datetime

class Liuyan(db.Model):
	__tablename__ ='liuyans'
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
	title = db.Column(db.String(64))
	body = db.Column(db.Text)
	comments = db.relationship('Comment',backref='liuyan',lazy='dynamic')

class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key = True)
	author = db.Column(db.String(64))
	timestamp = db.Column(db.DateTime,default=datetime.utcnow)
	body = db.Column(db.Text)
	liuyan_id = db.Column(db.Integer,db.ForeignKey('liuyans.id'))
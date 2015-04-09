from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from .. import db
from ..models import Liuyan, Comment
from . import main
from .forms import PostLiuyanForm,CommentForm

@main.route('/',methods=['GET','POST'])
def index():
	form = PostLiuyanForm()
	if form.validate_on_submit():
		liuyan = Liuyan(author=form.author.data,title=form.title.data,body=form.body.data)
		db.session.add(liuyan)
		return redirect(url_for('main.index'))
	liuyans = Liuyan.query.order_by(Liuyan.timestamp.desc()).all()
	return render_template('index.html',form=form,liuyans=liuyans)

@main.route('/liuyan/<int:id>',methods=['GET','POST'])
def liuyan(id):
	liuyan = Liuyan.query.get_or_404(id)
	form = CommentForm()
	if form.validate_on_submit():
		comment = Comment(author=form.author.data,body=form.body.data,
			liuyan=liuyan)
		db.session.add(comment)
		return redirect(url_for('main.liuyan',id=liuyan.id))
	comments = liuyan.comments.order_by(Comment.timestamp.asc()).all()
	return render_template('liuyan.html',liuyan=liuyan,comments=comments,form=form)
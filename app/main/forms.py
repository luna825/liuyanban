from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import Liuyan,Comment

class PostLiuyanForm(Form):
	author = StringField('Author',validators=[Length(0,64)])
	title = StringField('Title',validators=[Length(0,255)])
	body = TextAreaField('Body',validators=[DataRequired()])

class CommentForm(Form):
	author = StringField('Author',validators=[Length(0,64)])
	body = TextAreaField('Body',validators=[DataRequired()])
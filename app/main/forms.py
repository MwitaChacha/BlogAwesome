from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField, BooleanField
from wtforms.widgets import TextArea
from datetime import datetime


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email')])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')

class PostForm(FlaskForm):
    author = StringField('Author', validators=[InputRequired()])
    title = StringField("Title", validators=[InputRequired()])
    content = StringField("Blog", validators=[InputRequired()], widget=TextArea())
 
class CommentForm(FlaskForm):
    description = StringField("Comment") 
 
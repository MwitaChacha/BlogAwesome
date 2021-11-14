from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, PasswordField, BooleanField
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user



app = Flask(__name__)

app.config['SECRET_KEY'] = 'This_is_my_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:6775@localhost/sunday'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# MODELS
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15),unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String())
    # posts = db.relationship('Post', backref='poster')
    # comments = db.relationship('Comment', backref='commentor')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)
    # poster_id = db.Column(db.Integer, db.ForeignKey(user.id))

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    # commentor_id = db.Column(db.Integer, db.ForeignKey(user.id))
     



# FORMS
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
    
# VIEWS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
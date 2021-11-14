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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  

# MODELS
class User(UserMixin, db.Model):
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
       
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
         
        return redirect('failure')
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required

def dashboard():
    form = CommentForm()
    post = Post.query.all()
    comment = Comment.query.all()
    if form.validate_on_submit():
        comment = Comment(description=form.description.data)
        form.description.data = ''
        
        
        
        db.session.add(comment)
        db.session.commit()
    
    return render_template('dashboard.html', name=current_user.username, post=post, form=form, comment=comment)

@app.route('/success')
def success():
   
    return render_template('success.html')

@app.route('/profile')
def profile():
   
    return render_template('profile.html', name=current_user.username, email=current_user.email )

@app.route('/failure')
def failure():
    
    return render_template('failure.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(author=form.author.data, title=form.title.data, content=form.content.data)
        form.author.data = ''
        form.title.data = ''
        form.content.data = ''
        
        
        db.session.add(post)
        db.session.commit()
    return render_template('blog.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
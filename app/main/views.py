from flask import render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from .forms import LoginForm, RegisterForm, PostForm, CommentForm
from ..models import User, Post, Comment
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from . import main
from .. import db




@main.route('/')
def index():
    return render_template('index.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
       
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    
        db.session.add(new_user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))
         
        return redirect('failure')
    return render_template('login.html', form=form)

@main.route('/dashboard', methods=['GET', 'POST'])
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
    
    return render_template('dashboard.html', name=current_user.username, post=post, form=form, description=form.description.data)

@main.route('/success')
def success():
   
    return render_template('success.html')

@main.route('/profile')
def profile():
   
    return render_template('profile.html', name=current_user.username, email=current_user.email )

@main.route('/failure')
def failure():
    
    return render_template('failure.html')

@main.route('/blog', methods=['GET', 'POST'])
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

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
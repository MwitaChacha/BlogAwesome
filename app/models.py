from flask_login import UserMixin
from . import db
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15),unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String())
    # posts = db.relationship('Post', backref='poster')
    # comments = db.relationship('Comment', backref='commentor')
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    
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
     

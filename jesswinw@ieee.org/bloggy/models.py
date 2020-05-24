from datetime import datetime
from bloggy import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_img = db.Column(
        db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.profile_img}')"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

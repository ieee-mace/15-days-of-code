from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '29d4eb262b1a49af7daed3ca77ed1b7f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Users(db.Model):
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


posts = [{
    'author': 'Bob Vance',
    'title': 'Refridgerators affecting my Life',
    'content': 'asdhaskdhaskjhd daskjdhkjash kdjsah kdjhaskjdh kash dkjash dkjash k',
    'date': 'April 23,2020'
}, {
    'author': 'John Doe',
    'title': 'Everyody uses my name!!',
    'content': 'asdhaskdhaskjhd daskjdhkjash kdjsah kdjhaskjdh kash dkjash dkjash k',
    'date': 'April 22,2020'
}]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if(form.validate_on_submit()):
        flash(
            f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        if(form.email.data == 'admin@bloggy.com' and form.password.data == 'password'):
            flash('You have been logged In', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect Password or Email ID', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

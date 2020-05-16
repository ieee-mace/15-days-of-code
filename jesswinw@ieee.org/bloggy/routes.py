from flask import render_template, url_for, redirect, flash
from bloggy import app
from bloggy.forms import RegistrationForm, LoginForm
from datetime import datetime
from bloggy.models import Users, Posts


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

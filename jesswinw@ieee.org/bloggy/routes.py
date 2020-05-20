from flask import render_template, url_for, redirect, flash,request
from bloggy import app, bcrypt, db
from bloggy.forms import RegistrationForm, LoginForm, UserupdateForm
from datetime import datetime
from bloggy.models import Users, Posts
from flask_login import login_user,logout_user,current_user,login_required
import os 
import secrets
from PIL import Image

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
        hashed_pass = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = Users(username=form.username.data,
                    email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(
            f'Account has been successfully created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        user = Users.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Incorrect Password or Email ID', 'danger')

    return render_template('login.html', title='Login', form=form)

def save_picture(form_picture):
    rand_hex = secrets.token_hex(8)
    _,extension = os.path.splitext(form_picture.filename)
    pic_fname = rand_hex + extension
    # pic_path = os.path.join(app.root_path,'static/profile_pics',pic_fname)
    pic_path = os.path.join(app.root_path,'static/profile-pics',pic_fname)

    req_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(req_size)

    i.save(pic_path)
    return pic_fname

@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UserupdateForm()
    image = url_for('static',filename="profile-pics/"+current_user.profile_img)
    if(form.validate_on_submit()):
        if(form.picture.data):
            picture_file = save_picture(form.picture.data)
            current_user.profile_img = picture_file
        current_user.username = form.username.data    
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated','success')
        return redirect(url_for('account'))
    elif(request.method == 'GET'): 
        form.username.data = current_user.username   
        form.email.data = current_user.email   
    return render_template('account.html',title='Account',profile_img = image,form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

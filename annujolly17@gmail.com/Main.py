from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'the random string'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
  


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    shortdescription = db.Column(db.String(200))
    description = db.Column(db.String(200))
    # tag = db.Column(db.String(200))
    img = db.Column(db.String(200))
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)
    createdby_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Inbox(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    sharedto_email = db.Column(db.String(200))
    sharedby_email = db.Column(db.Integer, db.ForeignKey('user.id'))


################################################ FUNCTIONS ##############################


################################## REGISTER  LOGIN  LOGOUT ROUTES ###################################
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        data = User.query.filter_by(email=email,
                                    password=password).first()

        if data is not None:
            session['user'] = data.id
            print session['user']
            return redirect(url_for('home'))
        return render_template('incorrect_login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(name=request.form['name'], email=request.form['email'],
                        password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


################################## OTHER ROUTES#########################################



@app.route('/addPost', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = session['user']
        print(user_id)
        new_question = Post(title=request.form['title'], shortdescription=request.form['shortdescription'],
                            description=request.form['description'], img=request.form['img'],
                            createdby_id=user_id)
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('home'))
    else:

        return render_template('addPost.html')


@app.route('/ParticularPost', methods=['GET', 'POST'])
def ParticularPost():
    id = request.args
    print("inside particular q id is", id)
    p = Post.query.get(id)
    user = p.createdby_id
    name = User.query.get(user).name
    img = "https://unsplash.com/photos/fJQamCZIZf8"
    print("name is", name)
    # response=Post.query.filter_by(postID=p.id).all()
    # print("response is",response)
    return render_template('ParticularPost.html', post=p, name=name, img=img)


@app.route('/likedislike', methods=['GET', 'POST'])
def likedislike():
    url = request.args
    id = int(url['id'])
    likedislike = int(url['likedislike'])
    print("ds", likedislike)
    post = Post.query.get(id)
    if likedislike == 0:
        post.dislike += 1
        db.session.commit()
    if likedislike == 1:
        post.like += 1
        db.session.commit()

    return render_template('likedislike.html')


@app.route('/share', methods=['GET', 'POST'])
def share():
    details = request.args
    print("details shared is", details)
    user_id = session['user']
    my_Emailid = User.query.get(user_id).email
    new_share = Inbox(post_id=request.form['post_id'], sharedto_email=request.form['email'], sharedby_email=my_Emailid)
    db.session.add(new_share)
    db.session.commit()

    i = Inbox.query.all()
    return render_template('share.html', inbox_shared=i)


@app.route('/inbox')
def inbox():
    user_id = session['user']
    my_Emailid = User.query.get(user_id).email
    print("inside inbox", my_Emailid)
    myInbox = Inbox.query.filter_by(sharedto_email=my_Emailid).all()
    print("name is", myInbox)

    return render_template('myInbox.html', myInbox=myInbox)


@app.route('/myPost')
def myPost():
    user_id = session['user']
    myPost = Post.query.filter_by(createdby_id=user_id).all()
    print(myPost)
    return render_template('myPost.html', myPost=myPost)



@app.route('/follower')
def follower():
    show_user = User.query.order_by(desc(User.id))

    return render_template('followers.html', followers=show_user)
################################ DISPLAY #############################################


@app.route('/home')
def home():
    showPost = Post.query.order_by(desc(Post.id))
    return render_template('home.html', showPost=showPost)


@app.route('/show')
def show():
    show_user = User.query.all()
    return render_template('show.html', show_user=show_user)


@app.route('/showPost')
def showPost():
    show_post = Post.query.all()
    return render_template('showPost.html', show_post=show_post)


@app.route('/sharedPost')
def sharedPost():
    i = Inbox.query.all()
    return render_template('share.html', inbox_shared=i)


@app.route('/profile')
def profile():
    user = User.query.get(session['user'])
    return render_template('profile.html', user=user)


#############################################################################


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

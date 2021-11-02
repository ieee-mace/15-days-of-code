from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from bloggy.models import Users, Posts
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Regexp('^\w+$',message="Username should only contain alphanumeric characters and _s"), Length(min=2, max=16)])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    con_password = PasswordField('Confirm Password', validators=[
                                 DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account with the same email is present')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])

    password = PasswordField('password', validators=[DataRequired()])

    remember = BooleanField('Remember Me!')
    submit = SubmitField('Log In')

class UserupdateForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=16)])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Change')

    def validate_username(self, username):
        if(current_user.username != username.data):
            print(current_user.username,username)
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken')
                    



    def validate_email(self, email):
        if(current_user.email != email.data):
            print(current_user.email,email)
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('An account with the same email is present')
        
class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')
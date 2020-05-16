from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=16)])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    con_password = PasswordField('Confirm Password', validators=[
                                 DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])

    password = PasswordField('password', validators=[DataRequired()])

    remember = BooleanField('Remember Me!')
    submit = SubmitField('Log In')

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SignInForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[ DataRequired() ])
    email = StringField('Email', validators= [ DataRequired(), Email()])
    password = PasswordField('Password', validators = [ DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
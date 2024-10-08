from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField,PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Register')

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log in')

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Comment')
    
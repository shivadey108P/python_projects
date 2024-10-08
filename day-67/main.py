from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
current_dir = os.path.abspath(os.path.dirname(__file__))
# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(current_dir,'posts.db')}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ckeditor = CKEditor(app)

class NewBlog(FlaskForm):
    title = StringField(label='Blog Title', validators=[DataRequired(message="You can't leave this field empty")])
    subtitle = StringField(label='Blog Subtitle', validators=[DataRequired(message="You can't leave this field empty")])
    author= StringField(label='Your name', validators=[DataRequired(message="You can't leave this field empty")])
    img_url = StringField(label='Your blog background image', validators=[DataRequired(message="You can't leave this field empty"), URL(message='Enter a valid URL')])
    body = CKEditorField(label='Blog Content', validators=[DataRequired(message="You can't leave this field empty")], )
    submit = SubmitField(label='Submit Post')
    
# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# with app.app_context():
#     db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    blog_post = db.session.execute(db.select(BlogPost)).scalars().all()
    posts = blog_post
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods = ['GET','POST'])
def add_new_post():
    add_blog = NewBlog()
    if add_blog.validate_on_submit():
        new_blog = BlogPost(
            title = add_blog.title.data,
            subtitle = add_blog.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            author = add_blog.author.data,
            img_url = add_blog.img_url.data,
            body = add_blog.body.data
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form = add_blog)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:blog_id>', methods=['GET', 'POST'])
def edit_post(blog_id):
    post_data = db.get_or_404(BlogPost, blog_id)
    edit_post = NewBlog(obj = post_data)
    if edit_post.validate_on_submit():
        post_data.title = edit_post.title.data
        post_data.subtitle = edit_post.subtitle.data
        post_data.author = edit_post.author.data
        post_data.date = date.today().strftime("%B %d, %Y")
        post_data.img_url = edit_post.img_url.data
        post_data.body = edit_post.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', editing = True, form = edit_post)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

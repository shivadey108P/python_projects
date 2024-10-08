from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegistrationForm, LoginForm, CommentForm
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
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)

# gravatar = Gravatar(app,
#                     size=100,
#                     rating='g',
#                     default='retro',
#                     force_default=False,
#                     force_lower=False,
#                     use_ssl=False,
#                     base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
this_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(this_dir, 'posts.db')}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    author: Mapped[str] = relationship('Users', back_populates='posts')
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
    comments = relationship('Comments', back_populates='parent_post')
    

# TODO: Create a User table for all your registered users. 
class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email : Mapped[str] = mapped_column(String(100), unique=True)
    password : Mapped[str] = mapped_column(String(100), nullable=False)
    
    posts = relationship('BlogPost', back_populates='author')
    comments = relationship('Comments', back_populates='comment_author')
    
class Comments(db.Model):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    comment_author: Mapped[str] = relationship('Users', back_populates='comments')
    
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('blog_posts.id'))
    parent_post: Mapped[str] = relationship('BlogPost', back_populates='comments')
    
with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods = ['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        email_entered = register_form.email.data
        user = db.session.execute(db.select(Users).where(Users.email == email_entered)).scalar()
        if user:
            flash("You've already registered with this email, please try login instead!")
            return redirect(url_for('login'))
        new_user = Users(email = email_entered,
                        password = generate_password_hash(password=register_form.password.data,
                                                        method='pbkdf2:sha256',
                                                        salt_length=8),
                        name = register_form.name.data
                        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts')) 
    return render_template("register.html", form=register_form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        existing_user = db.session.execute(db.select(Users).where(Users.email==email)).scalar()
        if existing_user:
            if check_password_hash(password=password, pwhash=existing_user.password):
                login_user(existing_user)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Password you have entered is incorrect, please try again!')
                return redirect(url_for('login'))
        else:
            flash("The email you have entered doesn't exist, please try again!")
            return redirect(url_for('login'))
    return render_template("login.html",  form = login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/', methods = ['GET', 'POST'])
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()

    # Handle comment submission
    if comment_form.validate_on_submit():
        user_comment = comment_form.comment.data
        if current_user.is_authenticated:
            new_comment = Comments(
                text=user_comment,
                comment_author=current_user,
                parent_post=requested_post
            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id = post_id))
        else:
            flash("You need to be logged in to comment.")
            return redirect(url_for('login'))

    return render_template("post.html", post=requested_post, form=comment_form, logged_in=current_user.is_authenticated)



# admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorator_function(*agrs, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*agrs, **kwargs)
    return decorator_function

# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True )


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)

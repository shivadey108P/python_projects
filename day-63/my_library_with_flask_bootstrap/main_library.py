from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

load_dotenv()

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

class AddBook(FlaskForm):
    title = StringField(label='Book Title', validators=[DataRequired(message="You can't leave this field empty")])
    author = StringField(label='Author Name', validators=[DataRequired(message="You can't leave this field empty")])
    rating = DecimalField(label='Rating', validators=[DataRequired(message="You can't leave this field empty")])
    submit = SubmitField(label='Add')
    
class EditBook(FlaskForm):
    title = StringField(label='Book Title', validators=[DataRequired(message="You can't leave this field empty")])
    author = StringField(label='Author Name', validators=[DataRequired(message="You can't leave this field empty")])
    rating = DecimalField(label='Rating', validators=[DataRequired(message="You can't leave this field empty")])
    submit = SubmitField(label='Edit Details')
    
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.secret_key = os.environ['SECRET_KEY']
bootstrap = Bootstrap5(app=app)
db = SQLAlchemy(model_class=Base)

db.init_app(app)

all_books = []

class Book(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    
    def __repr__(self):
        return f"<Book {self.title}>"
    
with app.app_context():
    db.create_all()
    
def add_data(title, author, rating):    
    with app.app_context():
        new_book = Book(title= title, author = author, rating = rating)
        db.session.add(new_book)
        db.session.commit()

# with app.app_context():
#     book_title_to_update = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter')).scalar()
#     book_title_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

def delete_data(id):
    with app.app_context():
        delete_data = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(delete_data)
        db.session.commit()

def update_data(id, title, author, rating):
    with app.app_context():
        update_data = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        update_data.title = title
        update_data.author = author
        update_data.rating = rating
        db.session.commit()

def send_data():
    with app.app_context():
        global all_books
        result = db.session.execute(db.select(Book).order_by(Book.title))
        books = result.scalars()
        all_books.clear()
        for book in books:
            new_book ={
                    'id' : book.id,
                    'title': book.title,
                    'author': book.author,
                    'rating': book.rating
                }
            all_books.append(new_book)
        
        
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    delete_data(id=book_id)
    return redirect(url_for('home'))
    
@app.route("/", methods = ['GET', 'POST'])
def home():
    global all_books
    send_data()
    return render_template('index.html', books= all_books)

@app.route("/add", methods = ['GET','POST'])
def add():
    add_book = AddBook()
    if add_book.validate_on_submit():
        global all_books
        book_name = add_book.title.data
        author_name = add_book.author.data
        rating = add_book.rating.data
        add_data(title=book_name, author=author_name, rating=rating)
        send_data()
        return redirect(url_for('home'))
    return render_template('add.html', form = add_book)

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    
    book_id = request.args.get('id')
    book_data = db.session.execute(db.select(Book).where(Book.id==book_id)).scalar()
    edit_book = EditBook(obj=book_data)
    
    if edit_book.validate_on_submit():
        
        book_title = edit_book.title.data
        book_author = edit_book.author.data
        book_rating = edit_book.rating.data
        update_data(id=book_id,author=book_author, rating=book_rating, title=book_title)
    return render_template('edit.html', form = edit_book)

if __name__ == "__main__":
    app.run(debug=True)
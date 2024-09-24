from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField, IntegerField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
Bootstrap5(app)
base_dir = os.path.abspath(os.path.dirname(__file__))

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'movie.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app=app)

# CREATE TABLE
class Movie(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String(5000), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    ranking : Mapped[int] = mapped_column(Integer, nullable=False)
    review : Mapped[str] = mapped_column(String(1000), nullable=False)
    image_url : Mapped[str] = mapped_column(String(3000), nullable=False) 
    
    def __repr__(self) -> str:
        return f"<Movie {self.title}-{self.year}>"

# with app.app_context():
#     db.create_all()
    
def add_data(title, year, description, rating, ranking, review, image_url):
    with app.app_context():
        new_movie = Movie(title=title,
                        year=year,
                        description= description,
                        rating=rating,
                        ranking=ranking,
                        review= review,
                        image_url=image_url)
        db.session.add(new_movie)
        db.session.commit()
        
def read_data():
    with app.app_context():
        movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
        return movies
    
class AddMovie(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired(message="You can't leave this field empty")])
    year = DateField(label='Movie Release Date', validators=[DataRequired(message="You can't leave this field empty")])
    review = StringField(label='Movie Review', validators=[DataRequired(message="You can't leave this field empty")])
    description = StringField(label='Movie Review Description', validators=[DataRequired(message="You can't leave this field empty")])
    ranking = IntegerField(label='Movie Ranking', validators=[DataRequired(message="You can't leave this field empty")])
    rating = DecimalField(label='Rating', validators=[DataRequired(message="You can't leave this field empty")])
    image_url = StringField(label='Movie Image or Poster link', validators=[DataRequired(message="You can't leave this field empty")])
    submit = SubmitField(label='Add')

@app.route("/", methods = ['GET', 'POST'])
def home():
    all_movies = read_data()
    return render_template("index.html", movies = all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    add_movie = AddMovie()
    if add_movie.validate_on_submit():
        title = add_movie.title.data
        year = add_movie.year.data
        review = add_movie.review.data
        description = add_movie.description.data
        ranking = add_movie.ranking.data
        rating = add_movie.rating.data
        image_url = add_movie.image_url.data
        
        add_data(title=title,
                year=year,
                review=review,
                description=description,
                rating=rating,
                ranking=ranking,
                image_url=image_url)
        return redirect(url_for('add', saved = True))
    return render_template('add.html', form = add_movie)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
current_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(current_dir,'cafes.db')}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        return { column.name : getattr(self,column.name) for column in self.__table__.columns}


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route('/random')
def get_random_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    print(f'Total cafes in the database: {len(all_cafes)}')  # Debugging line

    # Handle the case where there are no cafes
    if not all_cafes:
        return jsonify(error="No cafes found"), 404

    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(cafe={
    #     'id': random_cafe.id,
    #     'name': random_cafe.name,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'amenities': {
    #         'has_sockets': random_cafe.has_sockets,
    #         'has_toilets': random_cafe.has_toilet,
    #         'has_wifi': random_cafe.has_wifi,
    #         'can_take_calls': random_cafe.can_take_calls,
    #         'seats': random_cafe.seats,
    #         'coffee_price': random_cafe.coffee_price,
    #     }
    # })
    
@app.route('/all')
def all():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    
    if not all_cafes:
        return jsonify(error='No cafes found'), 404
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def get_cafe_at_location():
    query_loc = request.args.get('loc').title()
    requested_data = db.session.execute(db.select(Cafe).where(Cafe.location == query_loc)).scalars().all()
    
    if not requested_data:
        return jsonify(error='No data found based on your request')
    else:
        return jsonify(cafe = [data.to_dict() for data in requested_data])
    
@app.route('/add', methods = ['POST'])    
def add_new_cafe():
    try:
        if request.method == 'POST':
            new_cafe = Cafe(
                name = request.form.get('name'),
                map_url = request.form.get('map_url'),
                img_url = request.form.get('img_url'),
                location = request.form.get('location'),
                has_sockets = request.form.get('has_sockets'),
                has_toilet = request.form.get('has_toilet'),
                has_wifi = request.form.get('has_wifi'),
                can_take_calls = request.form.get('can_take_calls'),
                seats = request.form.get('seats'),
                coffee_price = request.form.get('coffee_price')        
            )
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response ={
                "success": "Successfully added the data"
                })
    except Exception as e:
        return jsonify(error= {'message': f'An error occurred- {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

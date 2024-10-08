from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

def get_gender(name_of_person):
    param = {
        'name': name_of_person
    }
    response = requests.get(url='https://api.genderize.io/', params=param)
    gender_of_person = response.json()['gender']
    return gender_of_person

def get_guess_age(name_of_person):
    param = {
        'name': name_of_person
    }
    response = requests.get(url='https://api.agify.io/', params=param)
    age_of_person = response.json()['age']
    return age_of_person

@app.route('/guess/<name>')
def home(name):
    name = name.title()
    gender = get_gender(name)
    age = get_guess_age(name)
    year = dt.datetime.now().year
    
    return render_template('index.html', year=year, gender=gender, name=name, age=age)


if "__main__" in __name__:
    app.run(debug=True)
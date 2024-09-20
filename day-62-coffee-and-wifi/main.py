from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', 
                        validators=[DataRequired(message='You cannot leave this field empty!')])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', 
                                validators=[DataRequired(message='You cannot leave this field empty!'),
                                            URL(message="Please enter a valid URL")])
    opening_time = StringField('Opening Time e.g. 8 AM',
                                validators=[DataRequired(message='You cannot leave this field empty!'),])
    closing_time = StringField('Closing Time e.g. 5:30 PM',
                                validators=[DataRequired(message='You cannot leave this field empty!')])
    coffee_rating = SelectField('Coffee Rating', choices=['☕','☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                default=None,
                                validators=[DataRequired(message='You cannot leave this field empty!')])
    wifi_strength = SelectField('Wifi Strength Rating', choices=['✖','💪','💪💪','💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], 
                                default=None,
                                validators=[DataRequired(message='You cannot leave this field empty!')])
    power_socket = SelectField('Power Socket Rating', choices=['✖','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                                default=None,
                                validators=[DataRequired(message='You cannot leave this field empty!')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_coffee_cafe = [form.cafe.data,
                    form.cafe_location.data,
                    form.opening_time.data,
                    form.closing_time.data,
                    form.coffee_rating.data,
                    form.wifi_strength.data,
                    form.power_socket.data]
        write_csv(new_coffee_cafe)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./day-62-coffee-and-wifi/static/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

def write_csv(data):
    with open('./day-62-coffee-and-wifi/static/cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data)
        


if __name__ == '__main__':
    app.run(debug=True)

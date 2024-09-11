from flask import Flask
import random

app = Flask(__name__)

def make_bold(func):
    def wrap_bold():
        return f"<h1>{func()}</h1>"
    return wrap_bold

def make_too_low(func):
    def wrap_too_low_design():
        return f"<h1 style='color:red'> {func()}</h1>"
    return wrap_too_low_design

def make_too_high(func):
    def wrap_too_high_design():
        return f"<h1 style='color:purple'> {func()}</h1>"
    return wrap_too_high_design

def make_correct(func):
    def wrap_correct_design():
        return f"<h1 style='color:green'> {func()}</h1>"
    return wrap_correct_design

def generate_random_num():
    return random.randint(0,10)

@app.route('/')
@make_bold
def guess_number_homepage():
    return 'Guess the number between 0 to 9<br>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess the number image" width=500px>'
correct_num = generate_random_num()
@app.route('/<int:num>')
def guess_correct_number(num):
    
    print(correct_num)
    if num == correct_num:
        return correct_guess()
    elif num < correct_num:
        return too_low_guess()
    elif num > correct_num:
        return too_high_guess()

@make_correct        
def correct_guess():
    return 'You found me!<br>' \
            '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500px>'
            
@make_too_high
def too_high_guess():
    return 'Too High, try again!<br>'\
            '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500px>'

@make_too_low
def too_low_guess():
    return 'Too low, try again!<br>'\
            '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500px>'

if '__main__' in __name__:
    app.run(debug=True)
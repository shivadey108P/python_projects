from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def make_bold(func):
    def wrap_bold():
        value = func()
        return f"<b>{value}</b>"
    return wrap_bold

def make_emphasis(func):
    def wrap_emphasis():
        value = func()
        return f"<em>{value}</em>"
    return wrap_emphasis

def make_underline(func):
    def wrap_underline():
        value = func()
        return f"<u>{value}</u>"
    return wrap_underline

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye!'

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

if '__main__' in __name__:
    app.run(debug=True)
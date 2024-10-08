from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def sign_up():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def receive_data():
    if request.method == 'POST':
        return render_template('login.html', user_email = request.form['user_email'], password = request.form['password'])

if '__main__' in __name__:
    app.run(debug=True)
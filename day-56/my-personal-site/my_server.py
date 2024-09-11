from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_site():
    return render_template("site.html")

if '__main__' in __name__:
    app.run(debug=True)
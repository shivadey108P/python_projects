from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

print(random.__name__)
print(__name__)
# if '__main__' in __name__:
#     app.run()
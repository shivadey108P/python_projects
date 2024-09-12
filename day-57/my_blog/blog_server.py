from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_blog_posts():
    blog_url = 'https://api.npoint.io/8baa67ea23f6cf42dbb3'
    response = requests.get(url=blog_url)
    response.raise_for_status()
    return response.json()

@app.route('/')
def home():
    return render_template('index_default.html')

@app.route('/blog')
def get_blog():
    all_posts = get_blog_posts()
    return render_template('blog.html', posts = all_posts)

if '__main__' in __name__:
    app.run(debug=True)
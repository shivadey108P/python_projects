from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

post_object = []

def get_blog_posts():
    blog_url = 'https://api.npoint.io/8baa67ea23f6cf42dbb3'
    response = requests.get(url=blog_url)
    response.raise_for_status()
    return response.json()

def get_posts():
    global post_object
    all_posts = get_blog_posts()
    for post in all_posts:
        post_obj = Post(id=post['id'],
                           title=post['title'],
                           subtitle=post['subtitle'],
                           body=post['body'])
        post_object.append(post_obj)
    return post_object

@app.route('/')
def home():
    all_posts = get_posts()
    return render_template("index.html", posts = all_posts)

@app.route('/post/<int:post_id>')
def get_post_link(post_id):
    render_post = None
    for post in post_object:
        if post.id == post_id:
            render_post = post
    return render_template("post.html", post=render_post)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import datetime as dt
import requests
from post import Post
from send_email import SendEmail

app = Flask(__name__)

post_objects = []

def get_blog_posts():
    blog_url = 'https://api.npoint.io/566c6288b258ba8ab69e'
    response = requests.get(url=blog_url)
    response.raise_for_status()
    return response.json()

def get_posts():
    global post_objects
    post_objects.clear()
    if not post_objects:  # Check if post_objects is empty
        all_posts = get_blog_posts()
        for post in all_posts:
            post_obj = Post(id=post['id'],
                            title=post['title'],
                            subtitle=post['subtitle'],
                            body=post['body'],
                            image=post['image_url'],
                            author=post['author'],
                            time_stamp=post['time_stamp'])
            post_objects.append(post_obj)
    return post_objects

@app.route("/home")
def home():
    all_posts = get_posts()
    current_year = dt.datetime.now().year
    return render_template('index.html',year=current_year, posts = all_posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        send_email(name=request.form['name_of_user'],
                          email=request.form['user_email'],
                          phone_number=request.form['user_phone_number'],
                          message_body=request.form['message_body'])
        return render_template('contact.html', update = True)
    return render_template('contact.html', update = False)

@app.route('/post/<int:post_id>')
def get_post_link(post_id):
    render_post =  None
    for post in post_objects:
        if post.id == post_id:
            render_post = post
    return render_template('post.html', post = render_post)

def send_email(name, email, phone_number, message_body):
    email = SendEmail(name=name,
                      email=email,
                      phone_number=phone_number,
                      message=message_body)
    email.send_email_notification()

if "__main__" in __name__:
    app.run(debug=True)
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass

current_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(current_dir,'users.db')}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        check_existing_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if check_existing_user:
            flash("You've already registered with this email, try login instead!", 'info')
            return redirect(url_for('login'))
        
        new_user = User(email = email,
                        password = generate_password_hash(password=password,
                                                        method='pbkdf2:sha256',
                                                        salt_length=8),
                        name = name)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("User registered successfully!", 'success')
        return redirect(url_for('secrets'))
    return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        exiting_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        print(exiting_user)
        if exiting_user:
            if check_password_hash(password=password,pwhash=exiting_user.password): 
                login_user(exiting_user)
                flash("User logged in successfully!", 'success')
                return redirect(url_for('secrets'))
            else:
                flash("You've entered wrong password, please try again!", 'error')
                return redirect(url_for('login'))
        else:
            flash("That email doesn't exist, please try again or try registering!", 'info')
            return redirect(url_for('login'))
    return render_template("login.html", logged_in = current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name = current_user.name, logged_in = True)


@app.route('/logout')
def logout():
    flash("User logged out successfully!")
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods = ['POST'])
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)

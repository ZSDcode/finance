from flask import Flask, render_template, url_for, request, flash, redirect
from forms import Registration, Login
import mysql.connector

app = Flask(__name__)

app.config['SECRET_KEY'] = '814f48134cc9273ff0b89b83bc06b308'

posts = [
    {
        'author': 'Dylan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 25, 2024'
    },
    
    {
        'author': 'Clarence',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 1, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=["POST", "GET"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'Success')
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = Login()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
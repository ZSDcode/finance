from flask import Flask, render_template, url_for, request
import mysql.connector

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)
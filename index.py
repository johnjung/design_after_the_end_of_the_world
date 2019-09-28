import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route("/about/")
def about():
    return render_template(
        'about.html'
    )

@app.route("/")
def home():
    return render_template(
        'home.html'
    )

@app.route("/program/")
def program():
    return render_template(
        'program.html'
    )

@app.route("/users/user/")
def user():
    return render_template(
        'user.html'
    )

@app.route("/program/video/")
def video():
    return render_template(
        'video.html'
    )

if __name__=="__main__":
    app.run()

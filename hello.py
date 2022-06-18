from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')

def index():
    return render_template("index.html")

# localhost:5000/user/Manish
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

# Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

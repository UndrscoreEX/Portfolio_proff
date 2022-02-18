from flask import Flask, url_for, redirect,render_template 
from flask_bootstrap import Bootstrap
# from flask.templating import render_template

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template("portfolio.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/design')
def design():
    return render_template('graphicD.html')

@app.route('/ITbackend')
def it():
    return render_template('IT.html')

@app.route('/proff')
def proff():
    return render_template('personalCoach.html')
if __name__ == "__main__":
    app.run(debug=True)
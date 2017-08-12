from flask import render_template, request
from showtweet import app

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def id_posted():
    return request.form['tweet_id']
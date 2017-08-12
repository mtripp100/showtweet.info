from flask import render_template
from showtweet import app

@app.route('/')
def hello():
    return render_template('base.html')

from flask import Flask
from flask import request
from flask import render_template
import pprint
import tweet

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def id_posted():
    return "<pre>{}</pre>".format(pprint.pformat(tweet.get_json(request.form['tweet_id'])))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import request
from flask import render_template
import json
import tweet

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/', methods=['POST'])
def id_posted():
    return render_template('base.html', tweet_text=json.dumps(tweet.get_json(**request.form), indent=2, sort_keys=True))

if __name__ == '__main__':
    app.run(debug=True)

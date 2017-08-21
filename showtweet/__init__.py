from showtweet import twitter
from flask import Flask, request, render_template, redirect, url_for, abort
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/", methods=["POST"])
def id_posted():
    return redirect(url_for("show_tweet", **request.form.to_dict()))

@app.route("/<tweet_id>")
def show_tweet(tweet_id):
    try:
        int(tweet_id)
    except ValueError:
        return abort(404)
    return render_template(
        "base.html", tweet_text=json.dumps(
            twitter.get_json(tweet_id, **request.args), indent=2, sort_keys=True
        )
    )

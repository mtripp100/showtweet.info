from showtweet import twitter, form
from flask import Flask, request, render_template, redirect, url_for, abort
import json

app = Flask(__name__, static_url_path="")


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/", methods=["POST"])
def id_posted():
    return redirect(url_for("show_tweet", **form.generate_tweet_options(request.form)))


@app.route("/t/")
def base():
    return redirect(url_for("hello"))


@app.route("/t/<tweet_id>")
def show_tweet(tweet_id):
    try:
        int(tweet_id)
    except ValueError:
        return abort(400)
    return render_template(
        "base.html", tweet_text=json.dumps(
            twitter.get_json(tweet_id, **request.args), indent=2, sort_keys=True
        )
    )

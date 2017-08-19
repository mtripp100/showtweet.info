from showtweet import twitter
from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/", methods=["POST"])
def id_posted():
    try:
        int(request.form["tweet_id"])
    except ValueError:
        return redirect(url_for("hello"))
    return render_template(
        "base.html", tweet_text=json.dumps(
            twitter.get_json(**request.form), indent=2, sort_keys=True
        )
    )

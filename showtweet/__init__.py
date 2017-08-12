from flask import Flask

app = Flask(__name__)
from showtweet import views  # noqa

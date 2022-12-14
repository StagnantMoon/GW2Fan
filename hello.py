from flask_bootstrap import Bootstrap5
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

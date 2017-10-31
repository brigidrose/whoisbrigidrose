from flask import Flask, render_template, request, flash, redirect, session, jsonify, json
from jinja2 import StrictUndefined


app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def index():
    """Homepage."""

    return render_template("home.html")


@app.route('/about')
def about():
    """About page."""

    return render_template("about.html")


@app.route('/work')
def work():
    """Portfolio/work page."""

    return render_template("work.html")















if __name__ == "__main__":
    #Set debug to true to invoke the DebugToolbarExtension
    app.debug = True

    # connect_to_db(app)

    app.run(host="0.0.0.0")
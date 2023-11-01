#!/usr/bin/env python3
"""Module that does a locale setup using request
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class that defines languages available in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/', strict_slashes=False)
def index():
    """Displays welcome message as titles and greeting as header
    """
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """Gets the locale of app user
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

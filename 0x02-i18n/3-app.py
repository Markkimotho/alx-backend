#!/usr/bin/env python3
"""Module that performs parametrization of templates
"""

from flask import Flask, render_template, requests
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route
def index():
    """Displays welcome message as titles and greeting as header
    """
    return render_template("3-index.html")


def gettext:
    """Parametrizes templates
    """
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

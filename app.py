from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

APP = os.environ.get('APP') or "localhost"

color_codes = {
    "store": "#e9c46a",
    "conference": "#f4a261",
    "delivery": "#e76f51",
    "pay": "#5c5a70",
    "404": "#ffffff"
}

images = {
    "store": "https://raw.githubusercontent.com/rotoro-cloud/rotoro-cloud.github.io/master/images/CKA/shop.jpg",
    "conference": "https://raw.githubusercontent.com/rotoro-cloud/rotoro-cloud.github.io/master/images/CKA/conference.jpg",
    "delivery": "https://raw.githubusercontent.com/rotoro-cloud/rotoro-cloud.github.io/master/images/CKA/delivery.jpg",
    "pay": "https://raw.githubusercontent.com/rotoro-cloud/rotoro-cloud.github.io/master/images/CKA/pay.jpg",
    "404": "https://raw.githubusercontent.com/rotoro-cloud/rotoro-cloud.github.io/master/images/CKA/404.jpg"
}


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('hello.html', COLOR=color_codes[APP], IMAGE=images["404"])


@app.route('/')
def main():
    return render_template('hello.html', COLOR=color_codes[APP], IMAGE=images[APP])


if __name__ == "__main__":

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)

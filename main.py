import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ghost")
def ghost():
    return render_template("ghost.html")


@app.route("/item")
def item():
    return render_template("item.html")


# https://docs-python.ru/packages/veb-frejmvork-flask-python/funktsija-url-for-modulja-flask/

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

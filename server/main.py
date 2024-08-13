from flask import Flask, url_for
from api import api_blueprint
import flask

app = Flask(__name__, static_folder="./web/static", template_folder="./web/templates")
app.register_blueprint(api_blueprint)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return flask.redirect("/")

@app.route("/regression")
def regression():
    return flask.render_template("regression.html")

if __name__ == "__main__":
    app.run(debug=True)
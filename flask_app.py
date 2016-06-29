
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="oisinroblc",
    password="1Tonaknuck",
    hostname="oisinroblc.mysql.pythonanywhere-services.com",
    databasename="oisinroblc$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

comments = []

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))


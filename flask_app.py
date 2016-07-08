
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import pandas as pd
import dictfile as dkt


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


# Model for database
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class Points(db.Model):
    __tablename__ = "POINTS"
    id = db.Column(db.Integer, primary_key=True)
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    IRISH = db.Column(db.Integer)
    ENGLISH = db.Column(db.Integer)
    MATHS = db.Column(db.Integer)
    HISTORY = db.Column(db.Integer)
    GEOGRAPHY = db.Column(db.Integer)
    LATIN = db.Column(db.Integer)
    ANCIENT_GREEK = db.Column(db.Integer)
    CLASSICAL_STUDIES = db.Column(db.Integer)
    FRENCH = db.Column(db.Integer)
    GERMAN = db.Column(db.Integer)
    SPANISH = db.Column(db.Integer)
    ITALIAN = db.Column(db.Integer)
    ART = db.Column(db.Integer)
    APPLIED_MATHS = db.Column(db.Integer)
    PHYSICS = db.Column(db.Integer)
    CHEMISTRY = db.Column(db.Integer)
    PHYSICS_AND_CHEMISTRY = db.Column(db.Integer)
    AG_SCIENCE = db.Column(db.Integer)
    BIOLOGY = db.Column(db.Integer)
    AGRICULTURAL_ECONOMICS = db.Column(db.Integer)
    ENGINEERING = db.Column(db.Integer)
    CONSTRUCTION_STUDIES = db.Column(db.Integer)
    ACCOUNTING = db.Column(db.Integer)
    BUSINESS = db.Column(db.Integer)
    ECONOMICS = db.Column(db.Integer)
    FINNISH = db.Column(db.Integer)
    JAPANESE = db.Column(db.Integer)
    ARABIC = db.Column(db.Integer)
    TECHNOLOGY = db.Column(db.Integer)
    MUSIC = db.Column(db.Integer)
    HOME_EC = db.Column(db.Integer)
    RUSSIAN = db.Column(db.Integer)
    RELIGIOUS_EDUCATION = db.Column(db.Integer)
    LINK_MODULE = db.Column(db.Integer)
    POLISH = db.Column(db.Integer)
    HUNGARIAN = db.Column(db.Integer)
    ROMANIAN = db.Column(db.Integer)
    DESIGN_AND_COMM_GRAPHICS = db.Column(db.Integer)
    TOTALS = db.Column(db.Integer)
    CUTOFF = db.Column(db.Integer)

class Grades(db.Model):
    __tablename__ = "GRADES"
    id = db.Column(db.Integer, primary_key=True)
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    IRISH = db.Column(db.String(4), nullable=True)
    ENGLISH = db.Column(db.String(4), nullable=True)
    MATHS = db.Column(db.String(4), nullable=True)
    HISTORY = db.Column(db.String(4), nullable=True)
    GEOGRAPHY = db.Column(db.String(4), nullable=True)
    LATIN = db.Column(db.String(4), nullable=True)
    ANCIENT_GREEK = db.Column(db.String(4), nullable=True)
    CLASSICAL_STUDIES = db.Column(db.String(4), nullable=True)
    FRENCH = db.Column(db.String(4), nullable=True)
    GERMAN = db.Column(db.String(4), nullable=True)
    SPANISH = db.Column(db.String(4), nullable=True)
    ITALIAN = db.Column(db.String(4), nullable=True)
    ART = db.Column(db.String(4), nullable=True)
    APPLIED_MATHS = db.Column(db.String(4), nullable=True)
    PHYSICS = db.Column(db.String(4), nullable=True)
    CHEMISTRY = db.Column(db.String(4), nullable=True)
    PHYSICS_AND_CHEMISTRY = db.Column(db.String(4), nullable=True)
    AG_SCIENCE = db.Column(db.String(4), nullable=True)
    BIOLOGY = db.Column(db.String(4), nullable=True)
    AGRICULTURAL_ECONOMICS = db.Column(db.String(4), nullable=True)
    ENGINEERING = db.Column(db.String(4), nullable=True)
    CONSTRUCTION_STUDIES = db.Column(db.String(4), nullable=True)
    ACCOUNTING = db.Column(db.String(4), nullable=True)
    BUSINESS = db.Column(db.String(4), nullable=True)
    ECONOMICS = db.Column(db.String(4), nullable=True)
    FINNISH = db.Column(db.String(4), nullable=True)
    JAPANESE = db.Column(db.String(4), nullable=True)
    ARABIC = db.Column(db.String(4), nullable=True)
    TECHNOLOGY = db.Column(db.String(4), nullable=True)
    MUSIC = db.Column(db.String(4), nullable=True)
    HOME_EC = db.Column(db.String(4), nullable=True)
    RUSSIAN = db.Column(db.String(4), nullable=True)
    RELIGIOUS_EDUCATION = db.Column(db.String(4), nullable=True)
    LINK_MODULE = db.Column(db.String(4), nullable=True)
    POLISH = db.Column(db.String(4), nullable=True)
    HUNGARIAN = db.Column(db.String(4), nullable=True)
    ROMANIAN = db.Column(db.String(4), nullable=True)
    DESIGN_AND_COMM_GRAPHICS = db.Column(db.String(4), nullable=True)


# Begining of directors
@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        data = pd.read_csv(file)
        # Here go transforms
        clean_data = dkt.dataAlign(data)
        clean_data = clean_data.astype(object).where(pd.notnull(clean_data), None)
        clean_data.to_sql(name='GRADES', con=db.engine, if_exists = 'append', index=False)
        # Points Table
        clean_points = dkt.dataPoints(clean_data)
        clean_points = clean_points.astype(object).where(pd.notnull(clean_points), None)
        clean_points.to_sql(name='POINTS', con=db.engine, if_exists = 'append', index=False)
        return redirect(url_for('index'))

@app.route('/points')
def points():
    points = db.engine.execute("SELECT * FROM POINTS;")
    return render_template("points_table.html", points=points)
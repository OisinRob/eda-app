
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
    __tablename__ = "points"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096), nullable=False)
    Irish = db.Column(db.Integer)
    English = db.Column(db.Integer)
    Maths = db.Column(db.Integer)
    History = db.Column(db.Integer)
    Geography = db.Column(db.Integer)
    Latin = db.Column(db.Integer)
    Ancient_Greek = db.Column(db.Integer)
    Classical_studies = db.Column(db.Integer)
    French = db.Column(db.Integer)
    German = db.Column(db.Integer)
    Spanish = db.Column(db.Integer)
    Italian = db.Column(db.Integer)
    Art = db.Column(db.Integer)
    Applied_Maths = db.Column(db.Integer)
    Physics = db.Column(db.Integer)
    Chemistry = db.Column(db.Integer)
    Physics_and_Chemistry = db.Column(db.Integer)
    Ag_Science = db.Column(db.Integer)
    Biology = db.Column(db.Integer)
    Agricultural_Economics = db.Column(db.Integer)
    Engineering = db.Column(db.Integer)
    Construction_Studies = db.Column(db.Integer)
    Accounting = db.Column(db.Integer)
    Business = db.Column(db.Integer)
    Economics = db.Column(db.Integer)
    Finnish = db.Column(db.Integer)
    Japanese = db.Column(db.Integer)
    Arabic = db.Column(db.Integer)
    Technology = db.Column(db.Integer)
    Music = db.Column(db.Integer)
    Home_Ec = db.Column(db.Integer)
    Russian = db.Column(db.Integer)
    Religious_Education = db.Column(db.Integer)
    Link_Module = db.Column(db.Integer)
    Polish = db.Column(db.Integer)
    Hungarian = db.Column(db.Integer)
    Romanian = db.Column(db.Integer)
    Design_and_Comm_Graphics = db.Column(db.Integer)

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

        return redirect(url_for('index'))


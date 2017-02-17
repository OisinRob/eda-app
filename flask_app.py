
# A very simple Flask Hello World app for you to get started with...

from flask import (Flask, redirect, render_template, request, url_for, session,
                    abort, Response, flash)
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            AnonymousUserMixin, confirm_login,
                            fresh_login_required)
import pandas as pd
import dictfile as dkt
import hashlib
import time
import pygal
from pygal.style import Style
import datetime
import os
import numpy as np
import random

# Things that should not be here
colour = ['red', 'blue', 'green', 'orange']
def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))

custom_style = Style(
  background='transparent',
  plot_background='transparent',
#   plot_background = 'rgba(240, 240, 240, 0.7)',
#   font_size = '20',
#   value_font_size = '40',
  foreground='#53E89B',
#   foreground_strong='#53A0E8',
#   foreground_subtle='#630C0D',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in',
  colors = ('rgb(12,55,149)', 'rgb(117,38,65)', 'rgb(228,127,0)', 'rgb(159,170,0)', 'rgb(149,12,12)'))

def data_frame(query, columns):
    """
    Takes a sqlalchemy query and a list of columns, returns a dataframe.
    """
    def make_row(x):
        return dict([(c, getattr(x, c)) for c in columns])
    return pd.DataFrame([make_row(x) for x in query])


app = Flask(__name__)


app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'secret'



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

class Uploads(db.Model):
    __tablename__ = "UPLOADS"
    id = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(4096))
    FILENAME = db.Column(db.String(4096))
    STUCOUNT = db.Column(db.Integer)
    CREATED = db.Column(db.Date, default=time.strftime('%Y-%m-%d %H:%M:%S'))

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class Points(db.Model):
    __tablename__ = "POINTS"
    id = db.Column(db.Integer, primary_key=True)
    # UPLOADER = db.Column(db.String(4096))
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    GENDER = db.Column(db.String(1), nullable=True, default="F")
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
    USER = db.Column(db.String(25))
    FILE = db.Column(db.String(4096))

class Grades(db.Model):
    __tablename__ = "GRADES"
    id = db.Column(db.Integer, primary_key=True)
    # UPLOADER = db.Column(db.String(4096))
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    GENDER = db.Column(db.String(1), nullable=True, default="F")
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
    USER = db.Column(db.String(25))
    FILE = db.Column(db.String(4096))

class national(db.Model):
    __tablename__ = "NATIONAL"
    id = db.Column(db.Integer, primary_key=True)
    LABEL = db.Column(db.String(4096), nullable=True)
    YEAR = db.Column(db.String(4096), nullable=True)
    EXAM = db.Column(db.String(4096), nullable=True)
    LEVEL = db.Column(db.String(4096), nullable=True)
    SUBJECT = db.Column(db.String(4096), nullable=True)
    A1 = db.Column(db.Float, nullable=True)
    A2 = db.Column(db.Float, nullable=True)
    B1 = db.Column(db.Float, nullable=True)
    B2 = db.Column(db.Float, nullable=True)
    B3 = db.Column(db.Float, nullable=True)
    C1 = db.Column(db.Float, nullable=True)
    C2 = db.Column(db.Float, nullable=True)
    C3 = db.Column(db.Float, nullable=True)
    D1 = db.Column(db.Float, nullable=True)
    D2 = db.Column(db.Float, nullable=True)
    D3 = db.Column(db.Float, nullable=True)
    E = db.Column(db.Float, nullable=True)
    F = db.Column(db.Float, nullable=True)
    NG = db.Column(db.Float, nullable=True)
    TOTALS = db.Column(db.Float, nullable=True)


class User(db.Model):
    __tablename__ = "USERS"
    id = db.Column(db.Integer, primary_key=True)
    USERNAME = db.Column(db.String(4096))
    HPSAUCE = db.Column(db.String(4096))
    ACTIVE = db.Column(db.Boolean, default=False, nullable=False)
    AUTHENTICATED = db.Column(db.Boolean, default=False, nullable=False)

    def is_active(self):
        """True, as all users are active."""
        return self.ACTIVE

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.USERNAME

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.AUTHENTICATED

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.USERNAME = 'Guest'
    self.name = 'Guest'

# USERS = {
#     1: User(u"Notch", 1),
#     2: User(u"Steve", 2),
#     3: User(u"Creeper", 3, False),
# }

# USER_NAMES = dict((u[1].name, u[1]) for u in USERS.items())

login_manager = LoginManager()
# login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.anonymous_user = Anonymous


# @login_manager.user_loader
# def load_user(id):
#     return USERS.get(int(id))
@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object."""
    return User.query.filter_by(USERNAME=user_id).one()

login_manager.setup_app(app)


# Begining of directors
@app.route('/', methods = ["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def stu_upload():
    username = current_user.USERNAME
    file = request.files['file']
    if file:
        filename = os.path.splitext(os.path.basename(file.filename))[0]

        query = db.session.query(Uploads).filter_by(USERNAME=username)
        df_uploads = data_frame(query, [c.name for c in Uploads.__table__.columns])
        if filename in df_uploads.FILENAME.values:
            filename = filename + '{:%Y-%b-%d_%H:%M:%S}'.format(datetime.datetime.now())

        data = pd.read_csv(file)
        # Here go transforms
        clean_data = dkt.dataAlign(data)
        clean_data = clean_data.astype(object).where(pd.notnull(clean_data), None)
        clean_data["USER"] = username
        clean_data["FILE"] = filename

        # Add Gender

        # Upload File
        upload_dic = {'USERNAME': [username], 'FILENAME': [filename],
            'STUCOUNT' : [len(clean_data)], 'CREATED' : ['{:%Y-%m-%d}'.format(datetime.datetime.now())]}
        upload_data = pd.DataFrame(upload_dic, columns=['USERNAME', 'FILENAME', 'STUCOUNT', 'CREATED'])
        # Points Table
        clean_points = dkt.dataPoints(clean_data)
        clean_points = clean_points.astype(object).where(pd.notnull(clean_points), None)
        clean_data["USER"] = username
        clean_data["FILE"] = filename

        # Upload tables
        clean_data.to_sql(name='GRADES', con=db.engine, if_exists = 'append', index=False)
        upload_data.to_sql(name='UPLOADS', con=db.engine, if_exists = 'append', index=False)
        clean_points.to_sql(name='POINTS', con=db.engine, if_exists = 'append', index=False)

        return redirect(url_for('index'))


@app.route('/national_upload', methods=['POST'])
def nat_upload():
    file = request.files['file']
    if file:
        # Here go transforms
        nat_data = dkt.natAlign(file)
        nat_data.to_sql(name='NATIONAL', con=db.engine, if_exists = 'append', index=False)
        return redirect(url_for('index'))

@app.route('/points')
def points():
    points = db.engine.execute("SELECT * FROM POINTS;")
    return render_template("points_table.html", points=points)


@app.route('/chart_ui')
@login_required
def chart_home_ui():
    username = current_user.USERNAME
    uploads = db.session.query(Uploads).filter_by(USERNAME=username)
    return render_template("charting.html", uploads=uploads)


@app.route('/chart')
@login_required
def chart_home():
    username = current_user.USERNAME
    uploads = db.session.query(Uploads).filter_by(USERNAME=username)
    return render_template("user_page.html", uploads=uploads)


@app.route('/chart/<file>')
@login_required
def file_page(file):
    username = current_user.USERNAME
    uploads = db.session.query(Uploads).filter_by(USERNAME=username)
    sanitized_file = file
    query = db.session.query(Grades).filter_by(USER=username, FILE=sanitized_file)
    df = data_frame(query, [c.name for c in Grades.__table__.columns])
    df = df.dropna(axis=1, how='all')
    subject_tuples = zip(df.columns, [df[x].count() for x in df.columns])
    return render_template("file_page.html", file=sanitized_file, uploads=uploads, subject_tuples=subject_tuples)


@app.route('/chart/<file>/<subject>')
@login_required
def chart_subject(file,subject):
    username = current_user.USERNAME
    uploads = db.session.query(Uploads).filter_by(USERNAME=username)
    # Need to fix this
    sanitized_subject = subject
    sanitized_file = file
# Get Grades
    query = db.session.query(Grades).filter_by(USER=username, FILE=sanitized_file)
    df = data_frame(query, [c.name for c in Grades.__table__.columns])
    df = df.dropna(axis=1, how='all')

# Get Points
    query = db.session.query(Points).filter_by(USER=username)
    df_points = data_frame(query, [c.name for c in Points.__table__.columns])

# Get subject names
    subjects = [x for x in list(df.columns) if not x in ['USER', 'id', 'FILE']]

# Chart 1
    pie_chart = pygal.Pie(style=custom_style, value_font_size=25, legend_font_size=25)
    pie_chart.title = 'Honors vs pass'
    pie_chart.add('Honors', [str(i)[0] for i in df[sanitized_subject]].count('A'))
    pie_chart.add('Pass', [str(i)[0] for i in df[sanitized_subject]].count('G'))
    pie_chart.add('Foundation', [str(i)[0] for i in df[sanitized_subject]].count('B'))
    chart_pie = pie_chart.render(is_unicode=True)

# Chart 2
    line_chart = pygal.Bar(style=custom_style, value_font_size=25, legend_font_size=25)
    line_chart.add('Honors A', [str(i)[:2] for i in df[sanitized_subject]].count('AA'))
    line_chart.add('Honors B', [str(i)[:2] for i in df[sanitized_subject]].count('AB'))
    line_chart.add('Honors C', [str(i)[:2] for i in df[sanitized_subject]].count('AC'))
    line_chart.add('Honors D', [str(i)[:2] for i in df[sanitized_subject]].count('AD'))
    chart_line = line_chart.render(is_unicode=True)

# Table
    grades = df[["NAME", sanitized_subject]].dropna()
    points = df_points[["NAME", sanitized_subject, "CUTOFF", "TOTALS"]].dropna()
    points["CUTOFF"] = points[sanitized_subject] <= points["CUTOFF"]
    table_data = pd.merge(grades,points, on=['NAME'])

    return render_template("basic_chart.html", uploads=uploads, subjects=subjects,
    sanitized_file=sanitized_file, sanitized_subject=sanitized_subject,
    chart_pie=chart_pie, chart_line=chart_line, table_data=table_data)



# @app.route('/chart/<subject>')
# @login_required
# def chart_subject(dataset):
#     username = current_user.USERNAME
#     uploads = db.session.query(Uploads).filter_by(USERNAME=username)
#     # box_plot = pygal.Box(mode='extremes')
#     bar_chart = pygal.HorizontalStackedBar()
#     bar_chart.title = "Remarquable sequences"
#     bar_chart.x_labels = map(str, range(11))
#     bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
#     bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
#     chart = bar_chart.render(is_unicode=True)
#     # for i in
#     # box_chart.add(
#     # chart = box_chart.render(is_unicode=True)
#     return render_template("charting.html", uploads=uploads, chart=chart)

@app.route("/login", methods=["GET", "POST"])
def login():
    username = current_user.USERNAME
    # if current_user.is_authenticated():
    #     return redirect(request.args.get("next") or url_for("index"))
    # else:
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = hashlib.md5((app.config["SECRET_KEY"] + request.form["password"]).encode('utf-8')).hexdigest()
        # user = User.query.get(username)
        try:
            auth = db.session.query(User).filter_by(USERNAME=username).filter_by(HPSAUCE=password).one()
        except:
            class fakeObject(object):
                pass
            auth = fakeObject()
            auth.ACTIVE = False
        if auth.ACTIVE:
            # remember = request.form.get("remember", "no") == "yes"
            login_user(auth)
            flash("Logged in!")
            return redirect(request.args.get("next") or url_for("index"))
        else:
            flash("Sorry, but you could not log in.")
    return render_template("login.html", username=username)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))



@app.route('/test/<file>')
def test(file):
    username = current_user.USERNAME
    sanitized_file = file
    # Santitized file is the file name so maybe the path is /sanitized_file/threecompare or something
    query = db.session.query(Grades).filter_by(USER=username, FILE=sanitized_file)
    df = data_frame(query, [c.name for c in Grades.__table__.columns])
    df.drop(["NAME", "USER", "id", "FILE" ], axis=1, inplace=True)
    firster = lambda x: x[:1] if x is not None else None
    df = df.applymap(firster)
    df_female = df[df.GENDER == 'F'].drop(["GENDER"], axis=1)
    df_male = df[df.GENDER == 'M'].drop(["GENDER"], axis=1)
    male_count = len(df_male.index)
    female_count = len(df_female.index)
    # create dummy table to join on
    data_m = {'dummy_m': [0,0,0]}
    grouped_db_m = pd.DataFrame(data_m, index=['A','G','B'])
    for subject in df_male.columns:
        sub_grouped = pd.DataFrame(df_male.groupby([subject]).size(), columns=[subject + '_MALE'])*100/male_count
        grouped_db_m = pd.merge(grouped_db_m, sub_grouped, right_index=True, left_index=True, how='outer')
        grouped_db_m["AVG_MALE"] = grouped_db_m.sum(axis=1)*100/(grouped_db_m.sum(axis=1).sum(axis=0))

    data_f = {'dummy_f': [0,0,0]}
    grouped_db_f = pd.DataFrame(data_f, index=['A','G','B'])
    for subject in df_female.columns:
        sub_grouped = pd.DataFrame(df_female.groupby([subject]).size(), columns=[subject + '_FEMALE'])*100/female_count
        grouped_db_f = pd.merge(grouped_db_f, sub_grouped, right_index=True, left_index=True, how='outer')
        grouped_db_f["AVG_FEMALE"] = grouped_db_f.sum(axis=1)*100/(grouped_db_f.sum(axis=1).sum(axis=0))

    grouped_db = pd.merge(grouped_db_f, grouped_db_m, right_index=True, left_index=True, how='outer')

    # data = {'dummy_f': [0,0,0]}
    # for subject in df_female.columns:
    #     sub_grouped = pd.DataFrame(df_female.groupby([subject]).size(), columns=[subject + '_FEMALE'])*100/female_count
    #     grouped_db = pd.merge(grouped_db, sub_grouped, right_index=True, left_index=True, how='outer')

    df_html = grouped_db.dropna(axis=1,how='all').fillna(0).drop(["dummy_m", "dummy_f"], axis=1).to_html()
    grouped_db = np.round(grouped_db.dropna(axis=1,how='all').fillna(0).drop(["dummy_m", "dummy_f"], axis=1).reindex(["A", "G", "B"]))

    outstring_start = "var dataset_start = ["
    for num, subject in enumerate(grouped_db[["AVG_FEMALE", "AVG_MALE"]].columns):
        outstring_start = outstring_start + "{ label: '" + subject.replace('_',' ').title().replace('Female','F').replace('Male','M') + "', backgroundColor: '" + colour[num % 3] + "', data:[" + ','.join(map(str, grouped_db[subject].values)) + "] },"
    outstring_start = outstring_start + "]"
# This is where the full data set is made
    outstring = "var dataset = ["
    for num, subject in enumerate(grouped_db.columns):
        outstring = outstring + "{ label: '" + subject.replace('_',' ').title().replace('Female','F').replace('Male','M') + "', backgroundColor: 'rgb" + str(random_color()) + "', data:[" + ','.join(map(str, grouped_db[subject].values)) + "] },"
    outstring = outstring + "]"
    return render_template("test.html", table=df_html, outstring=outstring, outstring_start=outstring_start)


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
    UPLOADER = db.Column(db.String(4096))
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    GENDER = db.Column(db.String(10), nullable=True)
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
    UPLOADER = db.Column(db.String(4096))
    EXAM_NUM = db.Column(db.String(4096), nullable=True)
    NAME = db.Column(db.String(4096), nullable=True)
    GENDER = db.Column(db.String(10), nullable=True)
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
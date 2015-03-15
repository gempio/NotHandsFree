from NotHandsFree import db


class Speeddial(db.Model):
    gesture = db.Column(db.String, primary_key=True)
    number = db.Column(db.String, unique=True)
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(512))
    last_name = db.Column(db.String(512))
    nickname = db.Column(db.String(512))
    created = db.Column(db.Boolean, default=False)
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.Boolean)


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(512))
    last_name = db.Column(db.String(512))
    nickname = db.Column(db.String(512))

    user = db.relationship('User', backref='name')
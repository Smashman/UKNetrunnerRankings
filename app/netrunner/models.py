from app import db


class Identity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faction_id = db.Column(db.Integer, db.ForeignKey('faction.id'))
    name = db.Column(db.String(256), nullable=False)

    faction = db.relationship('Faction', backref='identity')


class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    side_id = db.Column(db.Integer, db.ForeignKey('side.id'))
    name = db.Column(db.String(64), nullable=False)

    side = db.relationship('Side', backref='faction')


class Side(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
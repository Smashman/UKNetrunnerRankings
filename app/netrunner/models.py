from app import db
from ..tournament.models import Participant
from sqlalchemy import or_


class Identity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(16), nullable=False)
    faction_id = db.Column(db.Integer, db.ForeignKey('faction.id'))
    name = db.Column(db.String(256), nullable=False)
    image_url = db.Column(db.String(256))

    faction = db.relationship('Faction', backref='identity')
    participants = db.relationship('Participant', primaryjoin=or_(Participant.runner_ident_id == id,
                                                                  Participant.corp_ident_id == id)) # Thanks agronholm!


class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    side_id = db.Column(db.Integer, db.ForeignKey('side.id'))
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(32), nullable=False)

    side = db.relationship('Side', backref='faction')


class Side(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class Pack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycle.id'))
    code = db.Column(db.String(16), nullable=False)
    num_in_cycle = db.Column(db.Integer)
    name = db.Column(db.String(128), nullable=False)


class Cycle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(128), nullable=False)
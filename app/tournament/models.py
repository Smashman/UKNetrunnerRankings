import datetime
from app import db


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    uploaded = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date = db.Column(db.Date)
    type = db.Column(db.Enum('sc', 'regi', 'nati'))
    location = db.Column(db.String(1024))
    mwl = db.Column(db.Boolean)
    filename = db.Column(db.String(256))
    file_type = db.Column(db.Enum('txt', 'json'))

    participants = db.relationship('Participant', backref=db.backref('tournament'))
    upload_user = db.relationship('User', backref='tournament')

    def __init__(self, filename):
        self.filename = filename
        self.file_type = filename.split('.')[-1]


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    runner_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))
    corp_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))

    user = db.relationship('User', backref='participant')
    runner_ident = db.relationship('Identity', foreign_keys=runner_ident_id)
    corp_ident = db.relationship('Identity', foreign_keys=corp_ident_id)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    position = db.Column(db.Integer)
    points = db.Column(db.Integer)
    strength_of_schedule = db.Column(db.Float)
    extended_sos = db.Column(db.Float)

    participant = db.relationship('Participant', backref='result')
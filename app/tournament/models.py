from app import db


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    type = db.Column(db.Enum('sc', 'regi', 'nati'))
    location = db.Column(db.String(1024))
    mwl = db.Column(db.Boolean)

    upload_user = db.relationship('User', backref='tournament')


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    runner_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))
    corp_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))

    user = db.relationship('User', backref='participant')
    tournament = db.relationship('Tournament', backref='participant')
    # runner_ident = db.relationship('Identity', backref='participant', foreign_keys=runner_ident_id)
    # corp_ident = db.relationship('Identity', backref='participant', foreign_keys=corp_ident_id)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    position = db.Column(db.Integer)
    points = db.Column(db.Integer)
    strength_of_schedule = db.Column(db.Integer)

    participant = db.relationship('Participant', backref='result')
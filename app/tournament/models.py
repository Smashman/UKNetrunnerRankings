from app import db


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    upload_user = db.relationship('User', backref='tournament')


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    runner_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))
    corp_ident_id = db.Column(db.Integer, db.ForeignKey('identity.id'))
    name = db.Column(db.String(512))

    user = db.relationship('User', backref='player')
    tournament = db.relationship('Tournament', backref='player')
    # runner_ident = db.relationship('Identity', backref='player')
    # corp_ident = db.relationship('Identity', backref='player')

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    position = db.Column(db.Integer)
    points = db.Column(db.Integer)
    strength_of_schedule = db.Column(db.Integer)
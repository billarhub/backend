from .BaseModel import BaseModel
from app import db

class Enrollment(BaseModel):

    __tablename__ = 'Enrollment'

    # Tournament ID
    tournament_id = db.Column(db.Integer, db.ForeignKey('Tournament.id'), nullable=False)
    tournament = db.relationship('Tournament', backref = db.backref('Enrollment', lazy=True))

    # User ID
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User', backref = db.backref('Enrollment', lazy=True))
    enrollment_status = db.Column(db.Integer,  nullable=False)

    # New instance instantiation procedure
    def __init__(self, tournament_id, user_id):
        self.tournament_id = tournament_id
        self.user_id = user_id

    #def __repr__(self):
    #    return '<enrollments %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
            "tournament_id": self.tournament_id,
            "user_id": self.user_id
        }

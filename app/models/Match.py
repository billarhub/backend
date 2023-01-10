from .BaseModel import BaseModel
from app import db

class Match(BaseModel):

    __tablename__ = 'Match'
    
    # Tor id 
    tournament_id = db.Column(db.Integer, db.ForeignKey('Tournament.id'), nullable=False)
    tournament = db.relationship('Tournament', backref = db.backref('Match', lazy=True))
    
    # User_1
    user_1_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user_1 = db.relationship('User', backref = db.backref('Match', lazy=True))
    
    # User_2
    user_2_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user_2 = db.relationship('User', backref = db.backref('Match', lazy=True))
    
    # Score_1 
    score_1 = db.Column(db.Integer, nullable=False)
    
    # Score_2 
    score_2 = db.Column(db.Integer, nullable=False)
    
    # Number_Table 
    number_table = db.Column(db.Integer, nullable=False)
    
    # Time
    time = db.Column(db.String(10), nullable=False)
    
    # Matchkey 
    matchkey = db.Column(db.Integer, nullable=False)
    
    # Winner
    winner_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    winner = db.relationship('User', backref = db.backref('Match', lazy=True))
    
    # Loser
    loser_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    loser = db.relationship('User', backref = db.backref('Match', lazy=True))
    
    # Operator
    operator_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    operator = db.relationship('User', backref = db.backref('Match', lazy=True))
    
    # New instance instantiation procedure
    def __init__(self,tournament_id, user_1_id, user_2_id,score_1,score_2,number_table,time,matchkey,winner_id,loser_id,operator_id):
        self.tournament_id = tournament_id
        self.user_1_id = user_1_id
        self.user_2_id = user_2_id     
        self.score_1 = score_1
        self.score_2 = score_2
        self.number_table = number_table
        self.time = time
        self.matchkey = matchkey
        self.winner_id = winner_id
        self.loser_id = loser_id
        self.operator_id = operator_id
        
    def __repr__(self):
        return '<User %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
           # PENDIENTE
        }

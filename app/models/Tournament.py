from .BaseModel import BaseModel
from app import db

class Tournament(BaseModel):

    __tablename__ = 'Tournament'
    
    # Tournament name 
    name = db.Column(db.String(100), nullable=False)
    
    # Start Date
    date_start = db.Column(db.DateTime, nullable=False)
    
    # End Date
    date_end = db.Column(db.DateTime, nullable=False)
    
    # Max Users
    max_user = db.Column(db.Integer, nullable=False)
    
    # Venue
    venue = db.Column(db.String(100), nullable=False)
    
    # Race_To
    race_to = db.Column(db.Integer, nullable=False)
    
    # price
    price = db.Column(db.Float,  nullable=False)

    # minimum prize
    minimum_prize = db.Column(db.Float,  nullable=False)

    # Par_tor_id
    tournament_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    tournament = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
    # Par_mod_id
    modality_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    modality = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
    # Par_Style_id
    style_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    style = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
    
    # Par_table_id
    table_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    table = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
        
    # Par_eli_id
    elimination_type_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    eliminattion_type = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
    # Par_organizer_id
    organizer_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    organizer = db.relationship('User', backref = db.backref('Tournament', lazy=True))
    
    # Par_Broadcast_id
    broadcast_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    broadcast = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
    # Par_Status_id
    status_id = db.Column(db.Integer, db.ForeignKey('Parameter.id'), nullable=False)
    status = db.relationship('Parameter', backref = db.backref('Tournament', lazy=True))
    
  
    # New instance instantiation procedure
    def __init__(self,name,date_start, date_end, max_user, venue, race_to, price, minimum_prize, tournament_id, modality_id, table_id, elimination_type_id, organizer_id, broadcast_id, status_id):
        self.name = name
        self.date_start = date_start
        self.date_end = date_end     
        self.max_user = max_user
        self.venue = venue
        self.race_to = race_to  
        self.price = price
        self.minimum_prize = minimum_prize
        self.tournamentr_id = tournament_id        
        self.modality_id = modality_id   
        self.table_id = table_id   
        self.elimination_type_id = elimination_type_id   
        self.organizer_id = organizer_id   
        self.broadcast_id = broadcast_id   
        self.status_id = status_id
        
    def __repr__(self):
        return '<Tournament %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
            PENDIENTE
        }

from .BaseModel import BaseModel
from app import db

class Parameter(BaseModel):

    __tablename__ = 'Parameter'
    
    # Entity name 
    name = db.Column(db.String(50), nullable=False)
    
    # Description Entity 
    description = db.Column(db.String(50), nullable=False)
    
    # Sport
    sport_id = db.Column(db.Integer, db.ForeignKey('Sport.id'), nullable=False)
    sport = db.relationship('Sport', backref = db.backref('Parameter', lazy=True))

    # New instance instantiation procedure
    def __init__(self,entity, description, sport_id):
        self.entity = entity
        self.description = description
        self.sport_id = sport_id        

    def __repr__(self):
        return '<Parameters %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
            #PENDIENTE
        }
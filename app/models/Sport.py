from .BaseModel import BaseModel
from app import db

class Sport(BaseModel):

    __tablename__ = 'Sport'
    
    # Sport name 
    name = db.Column(db.String(50), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Sport %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
            "id": self.id,
            "name": self.name
        }
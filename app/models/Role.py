from .BaseModel import BaseModel
from app import db

class Role(BaseModel):

    __tablename__ = 'Role'

    # Role name or type
    name = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % (self.name)

    def serialize(self):
        """
        Return as dict
        """
        return {
            "id": self.id,
            "name": self.name
        }
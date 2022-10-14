from .BaseModel import BaseModel
from app import db

class PasswordRecovery(BaseModel):

    __tablename__ = 'PasswordRecovery'

    # Discount name
    token = db.Column(db.String(500), nullable=False)

    # Customer
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User', foreign_keys='PasswordRecovery.user_id')
     
    # New instance instantiation procedure
    def __init__(self, token, user_id ):
        self.token     = token
        self.user_id = user_id

    def __repr__(self):
        return '<PasswordRecovery %r>' % (self.id)

    def serialize(self):
        """
        Return as dict
        """
        return {
            "id": self.id,
            "date_created": self.date_created.strftime("%d/%m/%Y %X"),
        }
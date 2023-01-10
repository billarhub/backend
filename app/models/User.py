from .BaseModel import BaseModel
from app import db
from .Role import Role

class User(BaseModel):

    __tablename__ = 'User'

    # Identification Type
    identification_type = db.Column(db.String(1), nullable=False)

    # Identification Number
    identification_number = db.Column(db.String(9), nullable=False, unique=True)
 
    # User Name
    name    = db.Column(db.String(128),  nullable=False)

    # User Lastname
    lastname    = db.Column(db.String(128),  nullable=False)

    # User Cellphone
    cellphone = db.Column(db.String(128),  nullable=False, unique=True)

    # Status
    status = db.Column(db.Integer,  nullable=False)

    # Identification Data: username, email & password
    username    = db.Column(db.String(128),  nullable=False, unique=True)
    email    = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    # Role
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'), nullable=False)
    role = db.relationship('Role', backref = db.backref('User', lazy=True))

    # New instance instantiation procedure
    def __init__(self, identification_type, identification_number, cellphone, role_id, name, lastname, username, email, password, status):

        self.name     = name
        self.lastname = lastname
        self.identification_type = identification_type
        self.identification_number = identification_number
        self.cellphone = cellphone
        self.username = username
        self.email    = email
        self.password = password
        self.role_id = role_id
        self.status = status

    def __repr__(self):
        return '<User %r>' % (self.name)

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False  

    def get_id(self):
        return self.id  
        
    def serialize(self):
        """
        Return as dict
        """

        return {
            "id": self.id,
            "date_created": self.date_created,
            "name": self.name,
            "lastname": self.lastname,
            "identification_type": self.identification_type,
            "identification_number": self.identification_number,
            "cellphone": self.cellphone,
            "username": self.username,
            "email": self.email,
            "status": self.status,
            "role_id": self.role_id,
            "date_created": self.date_created,
        }


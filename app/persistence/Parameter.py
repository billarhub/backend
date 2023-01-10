from inspect import Traceback, trace
from .DAO import DAO
from ..models import Parameter as ParameterModel, Role as RoleModel
from app import db
import bcrypt
import traceback

class Parameter(DAO):
    """
    User Data Access Object Abstract Class.
    """

    def __init__(self):
        pass

    def add(self, data):
        """ 
        Adds to the Database
        """
        try:
            parameter = ParameterModel(data["name"], data["description"], data["sport_id"])
            db.session.add(parameter)
            db.session.commit()

            return parameter.id
        except Exception as ex:
            traceback.print_exc()
            return 0

    def get(self):
        """
        Gets alll records from the Database
        """
        # users = UserModel.query.all()

        return 

    def find(self, id):
        """
        Find a single record from the Database by id
        """
        # users = UserModel.query.filter_by(role_id = 1, id = id).first()

        return 

    def update(self, data):
        """
        Updates a Record on the Database 
        """
        try:
            user = UserModel.query.filter_by(id = data['id']).first()

            user.name = data['name']
            user.lastname = data['last_name']
            user.email = data['email']
            user.cellphone = data['cellphone']
            user.username = data['username']
            user.identification_type = data['identification_type']
            user.identification_number = data['identification_number']

            if data['password'] != '':
                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                user.password = hashed_password.decode('utf-8')

            db.session.commit()

            return user.id
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def delete(self, id):
        """

        Deletes a record on the Database
        """
        pass


    def find_by_username(self, username):
        """
        Find an Operator by username
        """ 
        user = UserModel.query.filter_by(username=username).first()


        return user

    def get_admins(self):
        """
        Find an Operator by username
        """ 
        users = UserModel.query.filter_by(role_id=1).all()


        return users

    def get_companys(self):
        """
        Find an Operator by username
        """ 
        users = UserModel.query.filter_by(role_id=4).all()


        return users


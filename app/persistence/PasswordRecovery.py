from .DAO import DAO
from ..models import PasswordRecovery as RecoveryModel, User as UserModel
from app import db
from flask_login import current_user
import bcrypt
import traceback
from secrets import token_urlsafe
import bcrypt

class PasswordRecovery(DAO):
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
            token = token_urlsafe(100)
            user = UserModel.query.filter_by(email = data['email']).first()
            recovery = RecoveryModel.query.filter_by(user_id = user.id).first()
            hashed_token = bcrypt.hashpw(token.encode('utf-8'), bcrypt.gensalt())

            if recovery:
                recovery.token = hashed_token.decode()
                db.session.commit()
            else:
                recovery = RecoveryModel(hashed_token.decode(), user.id)
                db.session.add(recovery)
                db.session.commit()

            return {"recovery_id":recovery.id, "token":token}
        except Exception as ex:
            traceback.print_exc()
            raise ex

    def get(self):
        """
        Gets alll records from the Database
        """
        pass

    def find(self, id):
        """
        Find a single record from the Database by id
        """
        pass

    def update(self, data):
        """
        Updates a Record on the Database 
        """
        pass

    def delete(self, id):
        """

        Deletes a record on the Database
        """
        pass


    def confirm(self, data):
        """Confirm and updates password

        Args:
            data (dict): Dictionary with relevant data

        """
        try:
            user = UserModel.query.filter_by(email = data['email']).first()
            recovery = RecoveryModel.query.filter_by(user_id = user.id).first()
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode()

            user.password = hashed_password
            db.session.commit()

            db.session.delete(recovery)
            db.session.commit()

            return user.id
        except Exception as ex:
            traceback.print_exc()
            raise ex

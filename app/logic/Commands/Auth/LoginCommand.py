from ..Command import Command
from ....persistence.User import User as UserDao
from flask_login import login_user
import bcrypt

class LoginCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        dao = UserDao()

        user = dao.find_by_username(self._payload['username'])

        #If the user exist
        if user:
            if user.status == 2:
                return {
                    "logged":False,
                    "message":"El usuario no puede hacer uso del sistema porque atenta contra las políticas de Wellness"
                }                
            #This should be changed to a hash comparison
            if bcrypt.checkpw(bytes(self._payload["password"],'utf-8'), bytes(user.password, 'utf-8')):
                login_user(user, remember=True)
                return {
                    "logged": True,
                    "user": user.serialize()
                }
            else:
                return {
                "logged":False,
                "message":"Contraseña incorrecta"
            }

        else:
            return {
                "logged":False,
                "message":"El usuario no existe"
            }
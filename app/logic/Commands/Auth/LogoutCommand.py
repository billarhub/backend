from ..Command import Command
from flask_login import logout_user
import bcrypt

class LogoutCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def execute(self):
        logout_user()
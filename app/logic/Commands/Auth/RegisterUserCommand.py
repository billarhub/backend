from ..Command import Command
from ....persistence.User import User as UserDao

class RegisterUserCommand(Command):
    """
    Add operator command
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        dao = UserDao()

        response = dao.add(self._payload)
        return response
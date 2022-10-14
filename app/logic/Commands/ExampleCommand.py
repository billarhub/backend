from .Command import Command
from ...persistence.User import User as UserDao

class ExampleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self):
        pass

    def execute(self):
        dao = UserDao()

        response = [i.serialize() for i in dao.get()]
        return response
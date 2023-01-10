from ..Command import Command
from ....persistence.Parameter import Parameter as ParameterDao

class AddParameterCommand(Command):
    """
    Add operator command
    """

    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        dao = ParameterDao()

        response = dao.add(self._payload)
        return response
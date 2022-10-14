from ..Command import Command
from ....persistence.PasswordRecovery import PasswordRecovery as RecoveryDao
from flask_login import current_user
from flask_mail import Message

class ConfirmPasswordCommand(Command):
    """
    Add operator command
    """
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        dao = RecoveryDao()

        response = dao.confirm(self._payload)

        return response
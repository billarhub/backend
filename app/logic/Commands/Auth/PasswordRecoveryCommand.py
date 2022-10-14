from ..Command import Command
from ....persistence.PasswordRecovery import PasswordRecovery as RecoveryDao
from flask_login import current_user
from flask_mail import Message

class PasswordRecoveryCommand(Command):
    """
    Add operator command
    """
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        dao = RecoveryDao()

        response = dao.add(self._payload)

        # Sent email with the password recovery token
        import app
        
        if response:
            message = """
                Si desea recuperar su contraseña, por favor dirigirse al siguiente enlace:
                    {0}PasswordRecovery?token={1}&email={2}

            """.format(app.config.get("FRONTEND_URL"),response['token'], self._payload['email'])

            msg = Message(subject="Recuperar Contraseña - Wellness.com ",
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=[self._payload['email']], # replace with your email for testing
                        body=message)
            app.mail.send(msg) 

        return response
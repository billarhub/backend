from cerberus import Validator
from ....common.Exceptions import *
from ....models import User as UserModel, PasswordRecovery as RecoveryModel
import bcrypt

class ConfirmPasswordValidator():
    """
    Validation for Operator Login
    """
    
    def __init__(self, data):
        self.data = data

    def __translate(self, field):

        if field == 'email':
            return 'correo electrónico'

        if field == 'password':
            return 'contraseña'

        if field == 'repeat_password':
            return 'repetir contraseña'

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'email': {'type': 'string', 'empty': False, 'required': True},
            'password': {'type': 'string', 'empty': False, 'required': True},
            'repeat_password': {'type': 'string', 'empty': False, 'required': True},
            'token': {'type': 'string', 'empty': False, 'required': True},
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors.keys())[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        user = UserModel.query.filter_by(email = self.data['email']).first()
        recovery = RecoveryModel.query.filter_by(user_id = user.id).first()

        if self.data['repeat_password'] != self.data['password']:
            raise ValidationException("La contraseña no coincide")

        if not user:
            raise ValidationException("El correo electrónico no existe")

        if not recovery or not bcrypt.checkpw(bytes(self.data["token"],'utf-8'), bytes(recovery.token, 'utf-8')):
            raise ValidationException("URL invalido o expirado")

from cerberus import Validator
from ....common.Exceptions import *
from ....models import User as UserModel

class LoginValidator():
    """
    Validation for Operator Login
    """
    
    def __init__(self, data):
        self.data = data

    def __translate(self, field):

        if field == 'password':
            return 'contraseña'

        if field == 'username':
            return 'nombre de usuario'

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'username': {'type': 'string', 'empty': False, 'required': True},
            'password': {'type': 'string', 'empty': False, 'required': True},
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors.keys())[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))
        

from cerberus import Validator
from ....common.Exceptions import *
from ....models import User as UserModel

class RecoveryValidator():
    """
    Validation for Operator Login
    """
    
    def __init__(self, data):
        self.data = data

    def __translate(self, field):

        if field == 'email':
            return 'correo electrónico'

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'email': {'type': 'string', 'empty': False, 'required': True},
            }

        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors.keys())[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        user = UserModel.query.filter_by(email = self.data['email']).first()

        if not user:
            raise ValidationException("El correo electrónico no existe")
        

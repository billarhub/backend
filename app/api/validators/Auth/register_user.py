from sqlalchemy.sql.expression import null
from cerberus import Validator
from ....common.Exceptions import *
from ....models import User as UserModel

class RegisterUserValidator():
    """
    Validation for Operator Login
    """
    
    def __init__(self, data):
        self.data = data

    def __translate(self, field):
        if field == 'name':
            return 'nombre'

        if field == 'last_name':
            return 'apellido'

        if field == 'identification_type':
            return 'tipo de documento'

        if field == 'identification_number':
            return 'número de identidad'

        if field == 'password':
            return 'contraseña'

        if field == 'repeat_password':
            return 'repetir contraseña'

        if field == 'cellphone':
            return 'teléfono'

        if field == 'username':
            return 'nombre de usuario'

        if field == 'email':
            return 'correo electrónico'

        return field

    def validate(self):
        """
        Validate fields
        """
        schema = {
            'name': {'type': 'string', 'nullable': True},
            'last_name': {'type': 'string', 'nullable': True},
            'identification_type': {'type': 'string', 'empty': False, 'required': True},
            'identification_number': {'type': 'string', 'empty': False, 'required': True},
            'cellphone': {'type': 'string', 'empty': False, 'required': True},
            'username': {'type': 'string', 'empty': False, 'required': True},
            'email': {'type': 'string', 'empty': False, 'required': True},
            'password': {'type': 'string', 'empty': False, 'required': True},
            'repeat_password': {'type': 'string', 'empty': False, 'required': True},
            }
        v = Validator(schema)

        if not v.validate(self.data):
            field = list(v.errors.keys())[0]
            raise ValidationException("El campo {} es obligatorio".format(self.__translate(field)))

        if self.data['repeat_password'] != self.data['password']:
            raise ValidationException("La contraseña no coincide")

        if UserModel.query.filter_by(username = self.data['username']).first():
            raise ValidationException("El nombre de usuario ya existe")

        if UserModel.query.filter_by(cellphone = self.data['cellphone']).first():
            raise ValidationException("Ya existe un usuario con ese teléfono")

        if UserModel.query.filter_by(email = self.data['email']).first():
            raise ValidationException("El correo electrónico ya existe")

        if UserModel.query.filter_by(identification_number = self.data['identification_number']).first():
            raise ValidationException("Ya existe un usuario con ese número de identificación")


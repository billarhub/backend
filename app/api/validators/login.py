from ...common.Exceptions import *

class LoginValidator():
    """
    Validation for Operator Login
    """
    
    def __init__(self, data):
        self.data = data

    def validate(self):
        """
        Validate fields
        """
        try:
            self.data['username']
        except KeyError as ex:
            raise ValidationException(message="El campo username debe existir")

        try:
            self.data['password']
        except KeyError as ex:
            raise ValidationException(message="El campo password debe existir")

        if self.data['username'] == '':
            raise ValidationException(message="El campo nombre de usuario no debe estar vacio")

        if self.data['password'] == '':
            raise ValidationException(message="El campo constraseña no debe estar vacio")

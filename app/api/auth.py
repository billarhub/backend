# Import flask dependencies
from app.logic.Commands.Auth.RegisterStoreCommand import RegisterStoreCommand
from cerberus import validator
from flask import Blueprint, request
from .validators import *
from ..common.Exceptions import ValidationException
import traceback
import json

from ..logic.Commands import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth/')

# Set the route and accepted methods
@auth.route('/login', methods=['POST'])
def login():
    try:
        data = json.loads(request.data)

        validator = LoginValidator(data)
        validator.validate()

        command = LoginCommand(data)
        response = command.execute()

        if response['logged']:
            # User logged successfully
            return {"status":1, "message":"Inicio de sesión exitoso","data": { "user":response["user"] } }, 200
        else:
            return {"status":0, "message":response["message"] }, 202
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = json.loads(request.data)

        validator = RegisterUserValidator(data)
        validator.validate()
        
        data['status'] = 1
        data['role_id'] = 2

        command = RegisterUserCommand(data)
        response = command.execute()

        if response > 0:
            # Admin registered succesfully
            return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
        else:
            return {"status":0, "message":"Hubo un error interno" }, 400
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/register_store', methods=['POST'])
def register_store():
    try:
        data = json.loads(request.data)

        validator = RegisterUserValidator(data)
        validator.validate()

        data['status'] = 0
        data['role_id'] = 3

        command = RegisterStoreCommand(data)
        response = command.execute()

        if response > 0:
            # Admin registered succesfully
            return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
        else:
            return {"status":0, "message":"Hubo un error interno" }, 400
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/register_company', methods=['POST'])
def register_company():
    try:
        data = json.loads(request.data)

        validator = RegisterUserValidator(data)
        validator.validate()

        data['status'] = 1
        data['role_id'] = 4

        command = RegisterStoreCommand(data)
        response = command.execute()

        if response > 0:
            # Admin registered succesfully
            return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
        else:
            return {"status":0, "message":"Hubo un error interno" }, 400
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/register_rider', methods=['POST'])
def register_rider():
    try:
        data = json.loads(request.data)

        validator = RegisterUserValidator(data)
        validator.validate()

        data['status'] = 1
        data['role_id'] = 5

        command = RegisterUserCommand(data)
        response = command.execute()

        if response > 0:
            # Admin registered succesfully
            return {"status":1, "message":"Registro exitoso","data": { "id":response } }, 200
        else:
            return {"status":0, "message":"Hubo un error interno" }, 400
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/logout', methods=['POST'])
def logout():
    try:

        command = LogoutCommand()
        response = command.execute()
    # Logged out successfully
        return {"status":1, "message":"Cierre de sesion exitoso" }, 200
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/recover_password', methods=['POST'])
def password_recovery():
    try:
        data = json.loads(request.data)

        validator = RecoveryValidator(data)
        validator.validate()

        command = PasswordRecoveryCommand(data)
        response = command.execute()
    # Logged out successfully
        return {"status":1, "message":"Correo enviado", "data": response }, 200
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400

@auth.route('/confirm_password', methods=['POST'])
def confirm_password():
    try:
        data = json.loads(request.data)

        validator = ConfirmPasswordValidator(data)
        validator.validate()

        command = ConfirmPasswordCommand(data)
        response = command.execute()
    # Logged out successfully
        return {"status":1, "message":"Contraseña cambiada con éxito", "data": response }, 200
    except ValidationException as ex:
        return {"status":0, "message":ex.message }, 202
    except Exception as ex:
        traceback.print_exc()
        # There was an error adding the admin
        return {"status":0, "message":"Hubo un error interno" }, 400
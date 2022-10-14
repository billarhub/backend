# Import flask and template operators
from itertools import count
from flask import Flask, render_template
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

config = app.config

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)


login_manager = LoginManager()
login_manager.init_app(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return {"error":"Endpoint not found"}, 404

#If the user is not authorizewd to use the endpoint
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return {
        "status":0,
        "message":"User not authorized"
    }, 202

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(user_id)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.api.auth import auth as auth_module

# Register blueprint(s)
# app.register_blueprint(company_module)
app.register_blueprint(auth_module)
# ..


CORS(app, origins=app.config['ALLOWED_ORIGINS'], supports_credentials= True)
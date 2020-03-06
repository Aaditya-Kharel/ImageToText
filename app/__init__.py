#must initialize all extensions here before using

#creates object of class Flask
from flask import Flask
from config import Config
from flask_login import LoginManager

#name py variable set to name of module using it
app = Flask(__name__)
#lowercase config is py module, uppercse is Class
app.config.from_object(Config)
login = LoginManager(app)

#refers to app package: app directory and this script
from app import routes
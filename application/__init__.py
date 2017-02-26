import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir

application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)

from application import views, models

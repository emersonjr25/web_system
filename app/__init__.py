from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os.path

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
from app.models import tables
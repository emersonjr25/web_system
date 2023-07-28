from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os.path

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('app/storage.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
from app.models import tables, form
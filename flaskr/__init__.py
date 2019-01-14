from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
#↑はエラーがでる
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

import flaskr.views
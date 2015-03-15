import os
import redis
from flask import Flask
from flask_sockets import Sockets
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['REDIS_URL'] = os.environ['REDISTOGO_URL']
app.config['REDIS_CHAN'] = "nothandsfree"

sentry = Sentry(app)
redis = redis.from_url(app.config['REDIS_URL'])
db = SQLAlchemy(app)
sockets = Sockets(app)

from NotHandsFree.ws import Backend
backend = Backend()
backend.start()

from NotHandsFree import views
import os
import redis
from flask import Flask
from flask.ext.heroku import Heroku
from flask_sockets import Sockets
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config['REDIS_URL'] = os.environ['REDISTOGO_URL']
app.config['REDIS_CHAN'] = "howmany"

sentry = Sentry(app)
redis = redis.from_url(app.config['REDIS_URL'])
sockets = Sockets(app)
from NotHandsFree import app, backend, sockets, redis, db
from NotHandsFree.models import Speeddial

from flask import render_template, jsonify, request

import gevent

import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/train", methods=['GET', 'POST'])
def train():
    if request.method == "POST":
        # We're creating a new speeddial
        newdial = Speeddial(
            gesture=request.form['gesture'],
            number=request.form['number']
        )

        db.session.add(newdial)
        db.session.commit()
    return render_template("train.html")

@app.route("/speed")
def get_all_speeddial():
    dials = []
    for assoc in Speeddial.query.all():
        dials.append({'gesture': assoc.gesture, 'number': assoc.number})
    return jsonify(speeddial=dials)

@app.route("/input", methods=['POST'])
def recv_input():
    json = request.get_json(force=True)
    for key in json:
        val = json[key]
        del json[key]
        json[str(key)] = str(val)
    redis.publish(app.config['REDIS_CHAN'], json)
    return jsonify(status="OK")

@sockets.route('/ws')
def ws_receive(ws):
    backend.register(ws)
    while not ws.closed:
        gevent.sleep()
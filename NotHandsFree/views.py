from NotHandsFree import app, backend, sockets, redis

from flask import render_template, jsonify, request

import gevent

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/train")
def train():
    return render_template("train.html")

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
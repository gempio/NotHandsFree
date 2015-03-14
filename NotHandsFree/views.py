from NotHandsFree import app, backend, sockets

from flask import render_template, jsonify

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input", methods=['POST'])
def recv_input():
    return jsonify(ok="ok")

@sockets.route('/ws')
def ws_receive(ws):
    backend.register(ws)
    while not ws.closed:
        gevent.sleep()
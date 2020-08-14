from flask import Flask, jsonify
from threading import Thread
from flask_restful import Resource, Api
from gevent.pywsgi import WSGIServer

import random_exc as exc

app = Flask('')
api = Api(app)

class Home(Resource):
    def get(self):
        return "<h1>Random Book Excerpts</h1><p>A prototype API for Random Excerpts.</p>"

class Info(Resource):
    def get(self):
        random = exc.runner()
        return jsonify(random)

#creating api endpoint
api.add_resource(Home, '/')
api.add_resource(Info, '/api/restful')

def run():
    http_server = WSGIServer(('', 7210), app)
    http_server.serve_forever()

t = Thread(target=run)
t.start()
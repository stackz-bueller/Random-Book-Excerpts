from flask import Flask, jsonify
from threading import Thread
from flask_restful import Resource, Api
import random_exc as exc

app = Flask('')
api = Api(app)

class Info(Resource):
    def get(self):
        random = exc.runner()
        return jsonify(random)

class Home(Resource):
    def get(self):
        return "<h1>Random Book Excerpts</h1><p>A prototype API for Random Excerpts.</p>"

#creating api endpoint
api.add_resource(Home, '/')
api.add_resource(Info, '/api/restful')

def run():
    app.run(host='0.0.0.0',port=7210)

t = Thread(target=run)
t.start()
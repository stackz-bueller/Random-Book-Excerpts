from flask import Flask, jsonify, render_template
from gevent.pywsgi import WSGIServer
from threading import Thread
import random_exc as exc

app = Flask(__name__,template_folder='template')

# Routing to Home Page
@app.route('/')
def Home():
    return '''<h1>Random Book Excerpts</h1><p>A prototype API for Random Excerpts.</p>'''

# Routing to json of Info
@app.route('/base')
def Info():
  random = exc.runner()
  return jsonify(random)

# Routing to Nice HTML Layout, Test3.html
@app.route('/pretty')
def New_Info():
  random = exc.runner()
  return render_template('test3.html',book_title=random['title'],book_author=random['author'],book_text=random['text'])

# Routing to Nice HTML Layout, Test4.html
@app.route('/new_pretty')
def Hype_Info():
  random = exc.runner()
  return render_template('test4.html',book_title=random['title'],book_author=random['author'],book_text=random['text'])

# Forbidden Access Error Handling
@app.errorhandler(403)
def forbidden_access(e):
  return Home()

# Not Found Error Handling
@app.errorhandler(404)
def not_found(e):
  return Home()

# Server Problems Error Handling
@app.errorhandler(500)
def server_error(e):
  return Home()

# Runner for Server
def run():
    http_server = WSGIServer(('', 7210), app)
    http_server.serve_forever()

# Threading for Server
t = Thread(target=run)
t.start()
from flask import Flask, jsonify, render_template
from gevent.pywsgi import WSGIServer
from threading import Thread
import random_exc as exc

app = Flask(__name__,template_folder='template')

@app.route('/')
def Home():
    return '''<h1>Random Book Excerpts</h1><p>A prototype API for Random Excerpts.</p>'''

@app.route('/base')
def Info():
  random = exc.runner()
  return jsonify(random)

@app.route('/pretty')
def New_Info():
  random = exc.runner()
  return render_template('test3.html',book_title=random['title'],book_author=random['author'],book_text=random['text'])

@app.route('/new_pretty')
def Hype_Info():
  random = exc.runner()
  return render_template('test4.html',book_title=random['title'],book_author=random['author'],book_text=random['text'])

def run():
    http_server = WSGIServer(('', 7210), app)
    http_server.serve_forever()

t = Thread(target=run)
t.start()
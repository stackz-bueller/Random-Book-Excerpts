from flask import Flask, jsonify, render_template
from gevent.pywsgi import WSGIServer
from threading import Thread
import random_exc as exc
'''
App Creation & Routing
'''
# App Init
app = Flask(__name__, template_folder='template')


# Routing to Home Page
@app.route('/')
def Home():
    return render_template('index.html')


# Routing to json of Info
@app.route('/base')
def Base_Info():
    random = exc.runner()
    return jsonify(random)


# Routing to Nice HTML Layout, excerpt.html
@app.route('/pretty-dep')
def Old_Pretty():
    random = exc.runner()
    return render_template(
        'excerpt.html',
        book_title=random['title'],
        book_author=random['author'],
        book_text=random['text'],
        book_link=random['link'])


# Routing to Nice HTML Layout, excerpt-v2.html
@app.route('/pretty')
def New_Pretty():
    random = exc.runner()
    return render_template(
        'excerpt-v2.html',
        book_title=random['title'],
        book_author=random['author'],
        book_text=random['text'],
        book_link=random['link'])


'''
Error Handling
'''


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


'''
App Service
'''


# Runner for Server
def run():
    http_server = WSGIServer(('', 7210), app)
    http_server.serve_forever()


# Threading for Server
t = Thread(target=run)
t.start()

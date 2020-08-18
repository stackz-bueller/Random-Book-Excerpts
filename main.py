from flask import Flask, request, jsonify, render_template, session
import httpagentparser
import urllib.request
import datetime
import hashlib
import json
from gevent.pywsgi import WSGIServer
from threading import Thread
import engine_ as exc
import webhook

# Initialize Session Inf
userOS, userBrowser, userIP, userContinent, userCity, userCountry, SessionID = None
'''
App Creation & Routing
'''
# App Init
app = Flask(__name__, template_folder='template')


# Routing to Home Page
@app.route('/')
def Home():
    return render_template('pagefiles/index.html')


# Routing to json of Info
@app.route('/base')
def Base_Info():
    random = exc.runner()
    return jsonify(random)


# Routing to Nice HTML Layout, excerpt.html
@app.route('/pretty-tester')
def Old_Pretty():
    random = exc.runner()
    return render_template(
        'pagefiles/excerpt_tester.html',
        book_title=random['title'],
        book_author=random['author'],
        book_text=random['text'],
        book_link=random['link'])


# Routing to Nice HTML Layout, excerpt-v2.html
@app.route('/pretty')
def New_Pretty():
    random = exc.runner()
    return render_template(
        'pagefiles/excerpt-v2.html',
        book_title=random['title'],
        book_author=random['author'],
        book_text=random['text'],
        book_link=random['link'])


@app.before_request
def getAnalyticsOnVisitor():
    global userOS, userBrowser, userIP, userContinent, userCity, userCountry, SessionID
    userInfo = httpagentparser.detect(request.headers.get('User-Agent'))
    userOS = userInfo['platform']['name']
    userBrowser = userInfo['browser']['name']
    userIP = "172.18.0.1" if request.remote_addr == '127.0.0.1' else request.remote_addr
    api = "https://www.iplocate.io/api/lookup/" + userIP

    try:
        resp = urllib.request.urlopen(api)
        result = resp.read()
        result = json.loads(result.decode("utf-8"))

        userCountry = result["country"]
        userContinent = result["continent"]
        userCity = result["city"]

    except:
        print("Could not find: ", userIP)
        userCountry = " "
        userContinent = " "
        userCity = " "

    finally:
        get_session()
        webhook.noft_visitor(sessionID, userIP, userCity, userCountry,
                             userContinent, userBrowser, userOS)


def get_session():
    global sessionID
    time = datetime.now().replace(microsecond=0)
    if 'user' not in session:
        lines = (str(time) + userIP).encode('utf-8')
        session['user'] = hashlib.md5(lines).hexdigest()
        sessionID = session['user']
    else:
        sessionID = session['user']


'''
Error Handling
'''


# Forbidden Access Error Handling
@app.errorhandler(403)
def forbidden_access(e):
    return render_template('errorhandles/403.html'), 403


# Not Found Error Handling
@app.errorhandler(404)
def not_found(e):
    return render_template('errorhandles/404.html'), 404


# Page No Longer Exists
@app.errorhandler(410)
def no_longer_exist(e):
    return render_template('errorhandles/410.html'), 410


# Server Problems Error Handling
@app.errorhandler(500)
def server_error(e):
    return render_template('errorhandles/500.html'), 500


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

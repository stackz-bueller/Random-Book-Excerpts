import requests as req
import settings as codes

# Capture API Key without Echo
apiKey = codes.IFTTT_API_KEY

# Set Trigger Name according to IFTTT Applet
trigger = 'repl_trigger'

# Visitor Notification Method (Static Method, no returned value)
def noft_visitor(sessionID, userIP, city, country, contin, browser, userOS):
    report = {'value1' : 'Repl, engine-3; {}'.format(sessionID),
              'value2' :  'IP Address: {}'.format(userIP) if city==" " else 'IP Address: {}, {},{},{}'.format(userIP, city, country, contin),
              'value3' : 'Browser: {}, OS: {}'.format(browser,userOS)}

    req.post('https://maker.ifttt.com/trigger/'+trigger+'/with/key/'+apiKey,data=report)
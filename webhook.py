import requests as req

# Set Trigger Name according to IFTTT Applet
trigger = 'web_traffic_trigger'

class iffft():
  def __init__(self, key):
    self.KEY = key

  # Visitor Notification Method (Static Method, no returned value)
  def noft_visitor(self, userIP, city, zipcode, country, contin, browser, userOS):
      report = {'value1' : 'Repl, engine-3',
                'value2' :  'IP Address: {}'.format(userIP) if city==" " else 'IP Address: {}, {}, {}, {}, {}'.format(userIP, city, zipcode, country, contin),
                'value3' : 'Browser: {}, OS: {}'.format(browser,userOS)}

      req.post('https://maker.ifttt.com/trigger/'+trigger+'/with/key/'+self.KEY,data=report)
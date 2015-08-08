import jinja2
import webapp2
from twilio.rest import TwilioRestClient
import random

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('main.html')
        self.response.write(template.render())
    def post(self):
        account_sid = "ACb332643db3e9450c8831d380bd722a3c"
        auth_token  = "3b80f0c5f9fc9ec030afe69149de8e49"
        client = TwilioRestClient(account_sid, auth_token)
        recipient= self.request.get("recipient")
        textmessage= self.request.get("textmessage")
        sender= self.request.get("sender")
        images=["http://media.giphy.com/media/Un8RpWaTkAOLm/giphy.gif","http://media.giphy.com/media/giGMSOQKUi2QM/giphy.gif","http://media.giphy.com/media/13bjQGtqxnZxxm/giphy.gif","http://media.giphy.com/media/oDDs67mo76beM/giphy.gif","http://media.giphy.com/media/drwkO7nxYwaJi/giphy.gif","http://media.giphy.com/media/EA4ZexjGOnfP2/giphy.gif","http://media.giphy.com/media/FB7yASVBqPiFy/giphy.gif","http://media.giphy.com/media/biJpWkEdgitMs/giphy.gif","http://media.giphy.com/media/qugzlUdW5CkeI/giphy.gif","http://media.giphy.com/media/xZx7ht7MH8Wqs/giphy.gif","http://media.giphy.com/media/PxfJk0LKktjdS/giphy.gif","http://media.giphy.com/media/oobNzX5ICcRZC/giphy.gif","http://media.giphy.com/media/osMIREQbo3s2c/giphy.gif","http://media.giphy.com/media/8cryeowqTlIs0/giphy.gif","http://media.giphy.com/media/DfzVdbj45WcU0/giphy.gif"]
        media_url=random.choice(images)
        message = client.messages.create(
          to= recipient,
          from_="+15712508532",
          body= textmessage+ "<3 "+ sender+ " powered by: http://ow.ly/QjpAn",
          media_url=media_url,
          )
        print message.sid
        results = env.get_template('results.html')
        template_variables= {'recipient':recipient,'textmessage':textmessage, 'sender':sender, 'media_url':media_url}
        self.response.write(results.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

import os

from twilio.rest import TwilioRestClient

import jinja2
import webapp2
    

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


account = "ACb25ca21f061784336f896f03dc8d5bc0"
token = "ec3c8c702590b4b63c2592817c378540"
client = TwilioRestClient(account, token)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('homelayout.html')
        self.response.write(template.render())

    def post(self):
        msg_body = "Thinking of You"
        trim_typed_msg = self.request.get('message').lstrip()
        if len(trim_typed_msg) > 0:
            msg_body = trim_typed_msg
        send_to_num = self.request.get('number')
        template = JINJA_ENVIRONMENT.get_template('sentlayout.html')
        if len(send_to_num) == 10:
            message = client.sms.messages.create(to="+1" + send_to_num, from_="+12487825626",
                                             body=msg_body)
            message = 'Message sent!'
            template_values = {
                'message_line1': message,
                'message_line2': ""
                }
            self.response.write(template.render(template_values))
        else:
            message_line1 = "Invalid phone number."
            message_line2 = "Please try again!"
            template_values = {
                'message_line1': message_line1,
                'message_line2': message_line2
                }
            self.response.write(template.render(template_values))
    
    
class Funnel2(webapp2.RequestHandler):
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('funnel2.html')
        self.response.write(template.render())
 
 
class Funnel3(webapp2.RequestHandler):
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('funnel3.html')
        self.response.write(template.render())


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/funnel2', Funnel2),
    ('/funnel3', Funnel3),
], debug=True)








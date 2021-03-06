import json

import webapp2


class ErrorHandler(webapp2.RequestHandler):
    """Show an "offline" error message."""
    def post(self):
        self.get()

    def get(self):
        msg = "Due to problems with third-party services, the API is not"
        msg += " available at this moment. We apologize for any inconvenience."

        resp = {
            "status": "offline",
            "message": msg
        }

        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(resp)+"\n")

error_handler = webapp2.WSGIApplication([('/.*', ErrorHandler)], debug=True)

#-- DEPENDENCES --# g = global
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager


import models  

DEBUG = True
PORT = 8000


#-- INITIALIZATION OF FLASK --#
app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response





# Default route ends in / 
@app.route('/')
def index():
  return 'hi'







# @app.route('/json')
# def dog():
#     return jsonify(name="Frankie", age=8)

# Run the application 
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)



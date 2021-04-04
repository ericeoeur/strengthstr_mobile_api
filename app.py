#-- DEPENDENCES --# g = global
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager


import models 
from resources.users import lifter
 

DEBUG = True
PORT = 8000

login_manager = LoginManager()


#-- INITIALIZATION OF FLASK --#
app = Flask(__name__)

app.secret_key = 'TOPSECRETDONOTSTEAL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(lifter_id):
    try:
        return models.Lifter.get(models.Lifter.id == lifter_id)
    except:
        print(f'Lifter not found: {lifter_id}')
        return None


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


CORS(lifter, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(lifter, url_prefix='/lifter')


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



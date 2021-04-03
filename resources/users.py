import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

# BluePrint for the Particular User 
# blueprints is that they record operations to execute when registered on an application. Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another.
user = Blueprint('users', 'user', url_prefix='/user')

# Route to Return a User 
@user.route('/', methods=['GET'])
def get_users():
    return 'here is a user'
  # This route is funcitonal 
  
@user.route('/test')
def test():
    return jsonify('test')
  # This one is too
  
# Register a User  
@user.route('/register', methods=['POST'])
def register():
    payload = request.get_json()

    payload['email'] = payload['email'].lower()

    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={'code': 401, 'message': 'A user with that email already exists'})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)

        login_user(user)

        user_dict = model_to_dict(user)
        del user_dict['password']

        return jsonify(data=user_dict, status={'code': 201, 'message': 'Successfully created a user'})
# registration works... i think 
      
# Login
@user.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()

    try:
        user = models.User.get(models.User.email == payload['email'])
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Email does not exist'})


    if user:
        user_dict = model_to_dict(user)

        if (check_password_hash(user_dict['password'], payload['password'])):
            login_user(user)
            del user_dict['password']

            return jsonify(data=user_dict, status={'code': 200, 'message': 'Login Successful'})
        else:
            return jsonify(data={}, status={'code': 401, 'message': 'Incorrect username or pasword'})
#  OK Login apparently works too lmao
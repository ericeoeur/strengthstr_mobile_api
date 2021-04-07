import models
import json

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

# BluePrint for the Particular User 
# blueprints is that they record operations to execute when registered on an application. Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another.
lifter = Blueprint('users', 'lifter', url_prefix='/lifter')

# Route to Return a User 
@lifter.route('/', methods=['GET'])
def get_lifters():
    return 'here is a lifter'
  # This route is funcitonal 
  
@lifter.route('/test')
def test():
    return jsonify('test')
  # This one is too
  
# Register a User  
@lifter.route('/register', methods=['POST'])
def register():
    
    # payload = request.get_json()
    print(request);
    payload = request.get_json()
    
    
    print('sneepsnoop')
    print(payload)
    # print(payload['email'])
    
    # looks like the registion is sending a string instead of an object? how to convert it into an object? 
    

    payload['email'] = payload['email'].lower()
    
    


    try:
        models.Lifter.get(models.Lifter.email == payload['email'])
        return jsonify(data={}, status={'code': 401, 'message': 'A user with that email already exists'})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        lifter = models.Lifter.create(**payload)

        login_user(lifter)

        lifter_dict = model_to_dict(lifter)
        del lifter_dict['password']

        return jsonify(data=lifter_dict, status={'code': 201, 'message': 'Successfully created a lifter'})
# registration works... i think 
      
# Login
@lifter.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()

# When i come back, need to change the validation to username not email
    try:
        lifter = models.Lifter.get(models.Lifter.email == payload['email'])
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Email does not exist'})


    if lifter:
        lifter_dict = model_to_dict(lifter)

        if (check_password_hash(lifter_dict['password'], payload['password'])):
            login_user(lifter)
            del lifter_dict['password']

            return jsonify(data=lifter_dict, status={'code': 200, 'message': 'Login Successful'})
        else:
            return jsonify(data={}, status={'code': 401, 'message': 'Incorrect username or pasword'})
#  OK Login apparently works too lmao

@lifter.route('/logout', methods=['GET'])
def logout(): 
  logout_user()
  return jsonify(data={}, status={'code':200, 'message': 'you logged out woo hoo'})
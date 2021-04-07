import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict

workout = Blueprint('workouts', 'workout', url_prefix='/workouts')


@workout.route('/', methods=['GET'])
def get_all_workouts():
  try:
    workouts = [model_to_dict(workout) for workout in current_user.workouts]

    return jsonify(data=workouts, status={'code': 200, 'message': 'Success'})
  
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 401, 'message' :'Error getting the resources'})
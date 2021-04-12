import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict

workout = Blueprint('workouts', 'workout', url_prefix='/workouts')

# GET ALL WORKOUTS FROM CURRENT USER 
@workout.route('/', methods=['GET'])
def get_all_workouts():
  try:
    workouts = [model_to_dict(workout) for workout in current_user.workouts]

    return jsonify(data=workouts, status={'code': 200, 'message': 'Success'})
  
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 401, 'message' :'Error getting the resources'})
  
# COUNT ALL WORKOUTS FROM CURRENT USER 
@workout.route('/<lifter_id>/count', methods=['GET'])
def count_all_workouts(lifter_id):
  
  # countedWorkouts = models.Workout.select().count().where(models.Workout.lifter_id == lifter_id)
  try:
    countedWorkouts = models.Workout.select().where(models.Workout.lifter_id == lifter_id).count()
    return jsonify(data=countedWorkouts, status={'code': 200, 'message': 'Success'})
  
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 401, 'message' :'Error getting the resources'})
  
  
  
# CREATE A WORKOUT FOR A CURRENT USER  
@workout.route('/', methods=['POST'])
def create_workouts():
  payload = request.get_json()

  workout = models.Workout.create(note=payload['note'], image=payload['image'], lifter=current_user.id)

  workout_dict = model_to_dict(workout)

  return jsonify(data=workout_dict, status={"code": 201, "message": "Successful workout creation"})

# GET ONE WORKOUT FOR THE USER 
@workout.route('/<workout_id>', methods=['GET'])
def get_one_workout(workout_id):
  """
  - We have a route param that is the ID we want to search
  - Search PSQL for that ID
    - What do we do when the database doesn't have the id?
  - Return that value in the response
  """
  print(f'Searching for workout_id: {workout_id}')
  try:
    workout = models.Workout.get_by_id(workout_id)
    print('test')
    print(workout)

    return jsonify(data=model_to_dict(workout), status={'code': 200, 'message': 'Success'})
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 404, 'message' : f'workout resource {workout_id} does not exist'})
  
# DELETE A WORKOUT
@workout.route('/<workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
  query = models.Workout.delete().where(models.Workout.id == workout_id)
  del_rows = query.execute()
  # del_rows = models.Dog.delete_by_id(dog_id)

  print(f'deleted rows: {del_rows}')

  # 0 is a falsy value. If del_rows is anything other than 0 we know the operation worked
  if del_rows:
    return jsonify(data=f'Deleted {del_rows} successfully', status={'code': 200, 'message':'resource successfully deleted'})
  else:
    return jsonify(data='No resource to delete', status={'code': 404, 'message': f'Dog resource {dog_id} does not exist'})
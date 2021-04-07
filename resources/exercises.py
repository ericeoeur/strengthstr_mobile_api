import models

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from playhouse.shortcuts import model_to_dict

exercise = Blueprint('exercises', 'exercise', url_prefix='/workouts')


# GET ALL EXERCISES FROM CURRENT WORKOUT 
@exercise.route('/<workout_id>/exercises', methods=['GET'])
def get_all_exercises(workout_id):
  try:    
    exercises = models.Exercise.select().where(models.Exercise.workout == workout_id)
    output = []
      
    for row in exercises:
      output.append(model_to_dict(row))
    

    return jsonify(data=(output), status={'code': 200, 'message': 'Success'})
  
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 401, 'message' :'Error getting the resources'})
  

# CREATE AN EXERCISE FOR CURRENT WORKOUT   
@exercise.route('/<workout_id>/exercises', methods=['POST'])
def create_exercise(workout_id):
  payload = request.get_json()
  print("test")

  exercise = models.Exercise.create(lift_name=payload['lift_name'], weight=payload['weight'], sets=payload['sets'], reps=payload['reps'], note=payload['note'], completed=payload['completed'], workout=workout_id)

  exercise_dict = model_to_dict(exercise)

  return jsonify(data=exercise_dict, status={"code": 201, "message": "Successful exercise creation"})


# GET ONE EXERCISE  
@exercise.route('/<workout_id>/exercises/<exercise_id>', methods=['GET'])
def get_one_exercise(workout_id, exercise_id):
  print(f'Searching for exercise_id: {exercise_id}')
  
  try:
    exercise = models.Exercise.get_by_id(exercise_id)

    return jsonify(data=model_to_dict(exercise), status={'code': 200, 'message': 'Succesful update'})
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 404, 'message' : f'Exercise {exercise_id} does not exist'})

# UPDATE A WORKOUT 
@exercise.route('/<workout_id>/exercises/<exercise_id>', methods=['PUT'])
def update_exercise(workout_id, exercise_id):
  payload = request.get_json()

  query = models.Exercise.update(**payload).where(models.Exercise.id == exercise_id)
  
  try:
    query.execute()

    exercise = models.Exercise.get_by_id(exercise_id)

    return jsonify(data=model_to_dict(exercise), status={'code': 200, 'message': 'Succesful update'})
  except models.DoesNotExist:
    return jsonify(data={}, status={'code': 404, 'message' : f'Exercise {exercise_id} does not exist'})



# DELETE A WORKOUT
@exercise.route('/<workout_id>/exercises/<exercise_id>', methods=['DELETE'])
def delete_workout(workout_id, exercise_id):
  query = models.Exercise.delete().where(models.Exercise.id == exercise_id)
  del_rows = query.execute()

  print(f'deleted rows: {del_rows}')

  # 0 is a falsy value. If del_rows is anything other than 0 we know the operation worked
  if del_rows:
    return jsonify(data=f'Deleted {del_rows} successfully', status={'code': 200, 'message':'resource successfully deleted'})
  else:
    return jsonify(data='No resource to delete', status={'code': 404, 'message': f'Dog resource {dog_id} does not exist'})
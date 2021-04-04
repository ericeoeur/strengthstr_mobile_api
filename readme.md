test


## One Rep Max
INSERT INTO one_rep_max (lift_name, max_weight, lifter_id) VALUES ('press', 175, 2);

# Show One Rep Maxes with user by id 
SELECT * FROM lifter JOIN one_rep_max on one_rep_max.lifter_id = lifter.id WHERE lifter.id = 2;

# Show One Lift Maxes for all users for squat:
SELECT * FROM lifter JOIN one_rep_max on one_rep_max.lifter_id = lifter.id WHERE lift_name = 'squat';

# Timestamp 
2021-04-03 19:52:34.441873


# Insert an Exercise into a Workout
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('Bench', 50, 3, 5, 'this was hard!', True,  1); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('squat', 150, 1, 5, 'this was easy!', True,  1); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('deadlift', 250, 5, 1, 'this was bad!', False,  1); 

## Note: Need to check how to make items that can be null nulled 

# Find the exercises in each particular workout 
SELECT * FROM lifter JOIN workout on workout.lifter_id = lifter.id WHERE workout.id = 1; //no this just finds the exercise that is asscoiated with the user 

SELECT * FROM workout JOIN exercise on exercise.workout_id = workout.id WHERE workout.id = 1; 

SELECT * FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1; //works

SELECT lifter.username, workout.id, exercise.lift_name, exercise.weight, exercise.sets, exercise.reps FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1;
SELECT lifter.username, workout.id as workout_id, exercise.lift_name, exercise.weight, exercise.sets, exercise.reps FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1; //with alias 






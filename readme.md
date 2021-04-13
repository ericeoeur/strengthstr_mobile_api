# Starting Strength Mobile API 

Below is a list of all the SQL lines of code that assisted in the production of StrengthStr Mobile. 


## One Rep Max
INSERT INTO one_rep_max (lift_name, max_weight, lifter_id) VALUES ('press', 175, 2);

# Show One Rep Maxes with user by id 
SELECT * FROM lifter JOIN one_rep_max on one_rep_max.lifter_id = lifter.id WHERE lifter.id = 2;

# Show One Lift Maxes for all users for squat:
SELECT * FROM lifter JOIN one_rep_max on one_rep_max.lifter_id = lifter.id WHERE lift_name = 'squat';

# Timestamp 
2021-04-03 19:52:34.441873


# Create a workout for a user 
INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-03 19:52:34.441873', 'test', 'test.jpg', 1);

INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-04 19:52:34.441873', 'test2', 'test2.jpg', 1);

INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-05 19:52:34.441873', 'test3', 'test3.jpg', 1);

INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-03 19:52:34.441873', 'siena1', 'siena.jpg', 2);

INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-04 19:52:34.441873', 'siena2', 'siena2.jpg', 2);

INSERT INTO workout (created_at, note, image, lifter_id) VALUES ('2021-04-05 19:52:34.441873', 'siena3', 'siena3.jpg', 2);




# Insert an Exercise into a Workout
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('Bench', 50, 3, 5, 'this was hard!', True,  1); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('squat', 150, 1, 5, 'this was easy!', True,  1); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('deadlift', 250, 5, 1, 'this was bad!', False,  1); 


INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('Bench', 100, 1, 5, 'this was ok!', True,  2); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('squat', 250, 3, 5, 'this was hard!', True,  2); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('deadlift', 550, 5, 5, 'this was easy!', False,  2); 


INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('Bench', 50, 1, 5, 'this was ok!', True,  4); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('squat', 20, 3, 5, 'this was hard!', True,  4); 
INSERT INTO exercise (lift_name, weight, sets, reps, note, completed, workout_id) VALUES('deadlift', 50, 5, 5, 'this was easy!', False,  4); 


## Note: Need to check how to make items that can be null nulled 

# Find the exercises in each particular workout 
SELECT * FROM lifter JOIN workout on workout.lifter_id = lifter.id WHERE workout.id = 1; //no this just finds the exercise that is asscoiated with the user 

SELECT * FROM workout JOIN exercise on exercise.workout_id = workout.id WHERE workout.id = 1; 

SELECT * FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1; //works

SELECT lifter.username, workout.id, exercise.lift_name, exercise.weight, exercise.sets, exercise.reps FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1;

SELECT lifter.username, workout.id as workout_id, exercise.lift_name, exercise.weight, exercise.sets, exercise.reps FROM workout JOIN exercise on exercise.workout_id = workout.id JOIN lifter on lifter.id = workout.lifter_id WHERE workout.id = 1; //with alias 


# Count Number of Workouts by Lifter ID
SELECT COUNT(*) FROM workout  where lifter_id = 1;




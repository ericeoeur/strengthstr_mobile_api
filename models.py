# DEPENDENCIES 
from peewee import *
from datetime import datetime
from flask_login import UserMixin

# Call the database here, but make it manually first in terminal 
DATABASE = PostgresqlDatabase('strengthstr')

class User (UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()
  age = IntegerField()
  weight = IntegerField()
  created_at = DateTimeField(default=datetime.now)

  class Meta:
    database = DATABASE


class OneRepMax(Model):
  maxBench = IntegerField()
  maxPress = IntegerField()
  maxDeadlift = IntegerField()
  maxSquat = IntegerField()
  user = ForeignKeyField(User, backref='oneRepMaxes')
  
  class Meta: 
    database = DATABASE 
    
    
class WorkoutExercises(Model):
  created_at = DateTimeField(default=datetime.now)
  note = TextField()
  image = CharField()
  # Insert Something there to hold an array of OneExcercises? ForeignKeyField(s)????
  # exercises = ForeignKeyField(OneExercise, backref='exercises') 
  user = ForeignKeyField(User, backref='Workouts')
  
  class Meta: 
    database = DATABASE
    

class OneExercise(Model):
  liftName = CharField()
  weight = IntegerField()
  sets = IntegerField()
  reps = IntegerField()
  note = TextField()
  completed = BooleanField()
  workoutID = ForeignKeyField(WorkoutExercises, backref='OneExercise')
  # Do I even need to reference the user in the oneexercise model when it is only connected to each particular workout....? 
  user = ForeignKeyField(User, backref='OneExercise') 
  
  class Meta: 
    database = DATABASE
  
    
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, OneRepMax, WorkoutExercises, OneExercise], safe=True)
  print('TABLES created')
  DATABASE.close()  

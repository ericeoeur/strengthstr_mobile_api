# DEPENDENCIES 
from peewee import *
from datetime import datetime
from flask_login import UserMixin
import os

from playhouse.db_url import connect


if 'ON_HEROKU' in os.environ:                         
  DATABASE = connect(os.environ.get('DATABASE_URL'))                                                   
else:
  DATABASE = PostgresqlDatabase('strengthstr')

class Lifter (UserMixin, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()
  age = IntegerField()
  weight = IntegerField()
  created_at = DateTimeField(default=datetime.now)

  class Meta:
    database = DATABASE
    legacy_table_names=False


class OneRepMax(Model):
  lift_name = CharField()
  max_weight = IntegerField()
  lifter = ForeignKeyField(Lifter, backref='one_rep_maxes')
  # By default this is a one to many relationship 
  # if you want to do ONE to ONE (aka (only ONE) ONE REP MAX for the lifter) example:   lifter = ForeignKeyField(Lifter, backref='one_rep_maxes', unique=True)

  
  class Meta: 
    database = DATABASE 
    legacy_table_names=False
    
    
class Workout(Model):
  created_at = DateTimeField(default=datetime.now)
  note = TextField(null=True)
  image = CharField(null=True)
  # Insert Something there to hold an array of OneExcercises? ForeignKeyField(s)????
  # exercises = ForeignKeyField(OneExercise, backref='exercises') 
  lifter = ForeignKeyField(Lifter, backref='workouts')
  
  class Meta: 
    database = DATABASE
    legacy_table_names=False

class Exercise(Model):
  lift_name = CharField()
  weight = IntegerField()
  sets = IntegerField()
  reps = IntegerField()
  note = TextField(null=True)
  completed = BooleanField()
  workout = ForeignKeyField(Workout, backref='exercises')
  # Do I even need to reference the user in the oneexercise model when it is only connected to each particular workout....? 
  
  class Meta: 
    database = DATABASE
    legacy_table_names=False
    
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Lifter, OneRepMax, Workout, Exercise], safe=True)
  print('TABLES created')
  DATABASE.close()  

import datetime

from peewee import *

DATABASE = SqliteDatabase("todo.db")

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Board(BaseModel):
    board_name = CharField(max_length=100)
    created_at = DateTimeField(default=datetime.datetime.now)
    is_starred = BooleanField(default=False)
    board_color = CharField(max_length=6)
    class Meta:
        order_by = ('-created_at',)

class List(BaseModel):
    belongs_to_board = ForeignKeyField(Board)
    name = CharField(max_length=64)
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        order_by = ('-created_at',)

class Task(BaseModel):
    belongs_to_list = ForeignKeyField(List)
    task_name = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.datetime.now)
    task_description = TextField()
    task_order = IntegerField()
    class Meta:
        order_by = ('belongs_to_list', 'task_order')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Board, List, Task], safe=True)
    DATABASE.close()

initialize()

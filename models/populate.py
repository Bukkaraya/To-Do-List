import datetime

from models import Board, List, Task

highest_order= Task.select().where(Task.belongs_to_list == 1).order_by(Task.task_order.desc()).get()

new_task = Task(belongs_to_list=List.select().where(List.name == "Important List"),
                task_name="Learn Rails",
                task_description="I am trying to learn rails so I can build complex apps in the future and also my own api someday.",
                task_order=(highest_order.task_order+1))
new_task.save()

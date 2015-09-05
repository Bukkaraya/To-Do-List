from models import *

boards = Board.select()

lists = List.select(List, Board).join(Board).where(Board.board_name == "Important Things")

tasks = []
i = 0
for l in lists:
    tasks.append(Task.select(List, Task).join(List).where(List.name == l.name))
    print " %s: \n" % (l.name)
    for t in tasks[i]:
        if t.belongs_to_list.name == l.name:
            print " \t %s \n " % (t.task_name)
    i += 1

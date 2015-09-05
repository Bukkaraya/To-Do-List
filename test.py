from models import models

boards = models.Board.select()
print boards

for b in boards:
    print b.board_name
    print b.created_at
    print b.board_color
    print b.is_starred

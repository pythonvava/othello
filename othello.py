import numpy as np

EMPTY = 0
BLACK = 1
WHITE = -1
WALL = 2

BOARD_SIZE = 8


class Board:

    def __init__(self):

        self.RawBoard = np.zeros((BOARD_SIZE + 2, BOARD_SIZE + 2), dtype=int)

        self.RawBoard[0, :] = WALL
        self.RawBoard[:, 0] = WALL
        self.RawBoard[BOARD_SIZE + 1, :] = WALL
        self.RawBoard[:, BOARD_SIZE + 1] = WALL

        self.RawBoard[4, 4] = WHITE
        self.RawBoard[5, 5] = WHITE
        self.RawBoard[4, 5] = BLACK
        self.RawBoard[5, 4] = BLACK

        self.Turns = 0

        self.CurrentColor = BLACK


    def move(self, x: int, y: int):
        if x < 1 or BOARD_SIZE < x:
            raise Exception('x is less 1 or over BOARD_SIZE')
        if y < 1 or BOARD_SIZE < y:
            raise Exception('y is less 1 or over BOARD_SIZE')
        if self.MovablePos[x, y] == 0:
            raise Exception('Dont put the same position')


        # 石を裏返す
        self.flipDiscs(x, y)

        # 手番を進める
        self.Turns += 1

        # 手番を交代する
        self.CurrentColor = - self.CurrentColor
        
        # MovablePosとMovableDirの更新
        self.initMovable()

        return True


board = Board()
print(board.RawBoard)
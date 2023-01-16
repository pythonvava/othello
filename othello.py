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


    def flipDiscs(self, y: int, x:int):
        self.RawBoard[y, x] = self.CurrentColor


    def move(self, x: int, y: int):
        if x < 1 or BOARD_SIZE < x:
            raise Exception('x is less 1 or over BOARD_SIZE')
        if y < 1 or BOARD_SIZE < y:
            raise Exception('y is less 1 or over BOARD_SIZE')
        # if self.MovablePos[x, y] == 0:
        #     raise Exception('Dont put the same position')


        # 石を裏返す
        self.flipDiscs(x, y)

        # 手番を進める
        self.Turns += 1

        # 手番を交代する
        self.CurrentColor = - self.CurrentColor
        
        # MovablePosとMovableDirの更新
        #self.initMovable()

        return True


        """
    どの方向に石が裏返るかをチェック
    """
    def checkMobility(self, x, y, color):

        # 注目しているマスの裏返せる方向の情報が入る
        dir = 0

        # 既に石がある場合はダメ
        if(self.RawBoard[x, y] != EMPTY):
            return dir

        ## 左
        if(self.RawBoard[x - 1, y] == - color): # 直上に相手の石があるか
            
            x_tmp = x - 2
            y_tmp = y

            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LEFT

        ## 左上
        if(self.RawBoard[x - 1, y - 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x - 2
            y_tmp = y - 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
                y_tmp -= 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER_LEFT

        ## 上
        if(self.RawBoard[x, y - 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x
            y_tmp = y - 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                y_tmp -= 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER

        ## 右上
        if(self.RawBoard[x + 1, y - 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x + 2
            y_tmp = y - 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
                y_tmp -= 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | UPPER_RIGHT

        ## 右
        if(self.RawBoard[x + 1, y] == - color): # 直上に相手の石があるか

            x_tmp = x + 2
            y_tmp = y
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | RIGHT

        ## 右下
        if(self.RawBoard[x + 1, y + 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x + 2
            y_tmp = y + 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp += 1
                y_tmp += 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER_RIGHT

        ## 下
        if(self.RawBoard[x, y + 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x
            y_tmp = y + 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                y_tmp += 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER

        ## 左下
        if(self.RawBoard[x - 1, y + 1] == - color): # 直上に相手の石があるか
            
            x_tmp = x - 2
            y_tmp = y + 2
            
            # 相手の石が続いているだけループ
            while self.RawBoard[x_tmp, y_tmp] == - color:
                x_tmp -= 1
                y_tmp += 1
            
            # 相手の石を挟んで自分の石があればdirを更新
            if self.RawBoard[x_tmp, y_tmp] == color:
                dir = dir | LOWER_LEFT

        return dir


    """
    MovablePosとMovableDirの更新
    """
    def initMovable(self):

        # すべてのマス（壁を除く）に対してループ
        for x in range(1, BOARD_SIZE + 1):
            for y in range(1, BOARD_SIZE + 1):

                # checkMobility関数の実行
                dir = self.checkMobility(x, y, self.CurrentColor)
    
                # 各マスのMovableDirにそれぞれのdirを代入
                self.MovableDir[x, y] = dir
    


board = Board()
print(board.move(3, 7))

for y in range(10):
    for x in range(10):
        print('{:^3}'.format(board.RawBoard[x, y]), end = '')
    print()
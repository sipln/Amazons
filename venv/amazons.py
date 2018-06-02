import random
# ======================== Class Player =======================================


class Player:

    # student do not allow to change two first functions
    def __init__(self, str_name):
        self.str = str_name

    def __str__(self):
        return self.str

    # Student MUST implement this function
    # The return value should be a move that is denoted by a list of tuples:
    # [(row1, col1), (row2, col2), (row3, col3)] with:
        # (row1, col1): current position of selected amazon
        # (row2, col2): new position of selected amazon
        # (row3, col3): position of the square is shot

    Initial_Board = [
        ['.', '.', '.', '_w_', '.', '.', '_w_', '.', '.', '.'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['_w_', '.', '.', '.', '.', '.', '.', '.', '.', '_w_'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['_b_', '.', '.', '.', '.', '.', '.', '.', '.', '_b_'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
        ['.', '.', '.', '_b_', '.', '.', '_b_', '.', '.', '.'], \
        ]

    def nextMove(self, state):
        result = [
                    # (random.randint(0,9), random.randint(0,9)),
                    # (random.randint(0,9), random.randint(0,9)),
                    # (random.randint(0,9), random.randint(0,9))
            # [(0, 3), (5, 3), (8, 6)]
                 ]
        return result

    def move_left(x, y, state):
        nextY = y
        if y == 0:
            None
        else:
            for i in range(y - 1, -1, -1):
                if state[x][i] != '.':
                    nextY = random.randint(i + 1, y - 1)
                    break
        return nextY

    def move_up(x, y, state):
        nextX = x
        if x == 0:
            None
        else:
            for i in range(x, -1, -1):
                if state[i][y] != '.':
                    nextX = random.randint(i + 1, x - 1)
                    break
        return nextX

    def move_right(x, y, state):
        nextY = y
        if y == 9:
            None
        else:
            for i in range(y + 1, 10, 1):
                if state[x][i] != '.':
                    nextY = random.randint(y + 1, i - 1)
                    break
        return nextY

    def move_down(x, y, state):
        nextX = x
        return nextX

    def move_left_up(x, y, state):
        nextX = x
        nextY = y
        found = False
        if x == 0 or y == 0:
            None
        else:
            smaller = min(x, y)
            tempX = x
            tempY = y
            print(smaller)
            for i in range(smaller - 1, -1, -1):
                if smaller == x:
                    if state[i][tempY - 1] != '.':
                        nextX = random.randint(i + 1, x -1)
                        nextY = y - abs(x - nextX)
                        found = True
                        print("Done x")
                        break
                    tempY -= 1
                elif smaller == y:
                    if state[tempX - 1][i] != '.':
                        nextY = random.randint(i+ 1, y-1)
                        nextX = x - abs(y - nextY)
                        found = True
                        print("Done y")
                        break
                    tempX -= 1

            if found == False:
                if smaller == x:
                    nextX = random.randint(0, smaller - 1)
                    nextY = random.randint(y - smaller, y - 1)
                else:
                    nextX = random.randint(x - smaller, x - 1)
                    nextY = random.randint(0, smaller - 1)
        return [nextX, nextY]

    def move_left_down(x, y, state):
        nextX = x
        nextY = y
        return [nextX, nextY]


    def move_right_up(x, y, state):
        nextX = x
        nextY = y
        return [nextX, nextY]


    def getQueens(name, state):
        queens =[]
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == name:
                   queens.append((i, j))
        return queens


    queens = getQueens("_w_",Initial_Board)
    print(queens)

    print(move_left_up(1, 6, Initial_Board))



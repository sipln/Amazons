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


def get_queens(name, state):
    queens =[]
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == name:
                queens.append((i, j))
    return queens


def move_left(x, y, state):
    next_y = y
    if y == 0:
        None
    else:
        for i in range(y - 1, -1, -1):
            if state[x][i] != '.':
                next_y = random.randint(i + 1, y - 1)
                break
    return next_y


def move_up(x, y, state):
    next_x = x
    if x == 0:
        None
    else:
        for i in range(x, -1, -1):
            if state[i][y] != '.':
                next_x = random.randint(i + 1, x - 1)
                break
    return next_x


def move_right(x, y, state):
    next_y = y
    if y == 9:
        None
    else:
        for i in range(y + 1, 10, 1):
            if state[x][i] != '.':
                next_y = random.randint(y + 1, i - 1)
                break
    return next_y


def move_down(x, y, state):
    next_x = x
    return next_x


def move_left_up(x, y, state):
    next_x = x
    next_y = y

    if x == 0 or y == 0:
        None
    else:
        found = False
        temp_x = x
        temp_y = y
        smaller = min(x, y)

        # for i in range(smaller - 1, -1, -1):
        #     if smaller == x:
        #         if state[i][temp_y - 1] != '.':
        #             next_x = random.randint(i + 1, x -1)
        #             next_y = y - abs(x - next_x)
        #             found = True
        #             break
        #         temp_y -= 1
        #     else:
        #         if state[temp_x - 1][i] != '.':
        #             next_y = random.randint(i+ 1, y-1)
        #             next_x = x - abs(y - next_y)
        #             found = True
        #             break
        #         temp_x -= 1

        if smaller == x:
            for i in range(smaller - 1, -1, -1):
                if state[i][temp_y - 1] != '.':
                    try:
                        next_x = random.randint(i + 1, smaller - 1)
                    except ValueError:
                        next_x = x
                    next_y = y - abs(x - next_x)
                    found = True
                    break
                temp_y -= 1
        else:
            for i in range(smaller - 1, -1, -1):
                if state[temp_x - 1][i] != '.':
                    try:
                        next_y = random.randint(i + 1, smaller - 1)
                    except ValueError:
                        next_y = y
                    next_x = x - abs(y - next_y)
                    found = True
                    break
                temp_x -= 1

        if found is False:
            if smaller == x:
                next_x = random.randint(0, smaller - 1)
                next_y = y - abs(x - next_x)
            else:
                next_y = random.randint(0, smaller - 1)
                next_x = x - abs(y - next_y)
    return [next_x, next_y]


def move_left_down(x, y, state):
    next_x = x
    next_y = y

    if x == 9 or y == 0:
        None
    else:
        found = False
        temp_x = x
        temp_y = y
        smaller = min(9 - x, y)

        if smaller == (9 - x):
            for i in range(x + 1, 10, 1):
                if state[i][temp_y - 1] != '.':
                    try:
                        next_x = random.randint(x + 1, i - 1)
                    except ValueError:
                        next_x = x
                    next_y = y - abs(x - next_x)
                    found = True
                    break
                temp_y -= 1
        else:
            for i in range(smaller - 1, -1, -1):
                if state[temp_x + 1][i] != '.':
                    try:
                        next_y = random.randint(i + 1, smaller - 1)
                    except ValueError:
                        next_y = y
                    next_x = x + abs(y - next_y)
                    found = True
                    break
                temp_x += 1

        if found is False:
            if smaller == (9 - x):
                next_x = random.randint(x + 1, 9)
                next_y = y - abs(x - next_x)
            else:
                next_y = random.randint(0, smaller - 1)
                next_x = x + abs(y - next_y)
    return [next_x, next_y]


def move_right_up(x, y, state):
    next_x = x
    next_y = y

    if x == 0 or y == 9:
        None
    else:
        found = False
        temp_x = x
        temp_y = y
        smaller = min(x, 9 - y)

        if smaller == x:
            for i in range(smaller - 1, -1, -1):
                if state[i][temp_y + 1] != '.':
                    try:
                        next_x = random.randint(i + 1, smaller - 1)
                    except ValueError:
                        next_x = x
                    next_y = y + abs(x - next_x)
                    found = True
                    break
                temp_y += 1
        else:
            for i in range(y + 1, 10, 1):
                if state[temp_x - 1][i] != '.':
                    try:
                        next_y = random.randint(y + 1, i - 1)
                    except ValueError:
                        next_y = y
                    next_x = x - abs(y - next_y)
                    found = True

                    break
                temp_x -= 1

        if found is False:
            if smaller == x:
                next_x = random.randint(0, smaller - 1)
                next_y = y + abs(x - next_x)
            else:
                next_y = random.randint(y + 1, 9)
                next_x = x - abs(y - next_y)
    return [next_x, next_y]


def move_right_down(x, y, state):
    next_x = x
    next_y = y

    if x == 0 or y == 9:
        None
    else:
        found = False
        temp_x = x
        temp_y = y
        smaller = min(9 - x, 9 - y)

        if smaller == (9 - x):
            for i in range(x + 1, 10, 1):
                if state[i][temp_y + 1] != '.':
                    try:
                        next_x = random.randint(i + 1, smaller - 1)
                    except ValueError:
                        next_x = x
                    next_y = y + abs(x - next_x)
                    found = True
                    break
                temp_y += 1
        else:
            for i in range(y + 1, 10, 1):
                if state[temp_x + 1][i] != '.':
                    try:
                        next_y = random.randint(y + 1, i - 1)
                    except ValueError:
                        next_y = y
                    next_x = x - abs(y - next_y)
                    found = True
                    print("Done y")
                    break
                temp_x -= 1

        if found is False:
            if smaller == x:
                next_x = random.randint(0, smaller - 1)
                next_y = y + abs(x - next_x)
            else:
                next_y = random.randint(y + 1, 9)
                next_x = x - abs(y - next_y)
    return [next_x, next_y]


Initial_Board = [
                  ['.', '.', '.', 'w', '.', '.', 'w', '.', '.', '.'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['w', '.', '.', '.', '.', '.', '.', '.', '.', 'w'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['b', '.', '.', '.', '.', '.', '.', '.', '.', 'b'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
                  ['.', '.', '.', 'b', '.', '.', 'b', '.', '.', '.'], \
                ]

print(get_queens("w", Initial_Board))

print(move_right_up(4, 8, Initial_Board))



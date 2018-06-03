import random
import copy
# ======================== Class Player =======================================

DIRECT = [
            'LEFT',
            'UP',
            'RIGHT',
            'DOWN'
            'LEFT_UP',
            'RIGHT_UP',
            'LEFT_DOWN',
            'RIGHT_DOWN',
    ]


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


    def nextMove(self, state):

        copy_state = copy.deepcopy(state)
        my_queens = get_queens(self.str, state)

        # your_queens =  []
        # if self.str == 'w':
        #     your_queens = get_queens('b', state)
        # else:
        #     your_queens = get_queens('w', state)

        picked_queen = random.choice(my_queens)

        next_move_direct = random.choice(DIRECT)

        next_move = []
        if next_move_direct == 'LEFT':
            next_move = move_left(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'UP':
            next_move = move_up(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'RIGHT':
            next_move = move_right(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'DOWN':
            next_move = move_down(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'LEFT_UP':
            next_move = move_left_up(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'RIGHT_UP':
            next_move = move_right_up(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'LEFT_DOWN':
            next_move = move_left_down(picked_queen[0], picked_queen[1], copy_state)
        elif next_move_direct == 'RIGHT_DOWN':
            next_move = move_right_down(picked_queen[0], picked_queen[1], copy_state)

        if next_move == picked_queen:
            next_move = [None, None]

        if next_move != [None, None]:
            arrow_state = copy.deepcopy(state)
            arrow_state[picked_queen[0]][picked_queen[1]] = "."
            arrow_state[next_move[0]][next_move[1]] = self.str

            throw_arrow_direct = random.choice(DIRECT)
            arrow = []
            if next_move_direct == 'LEFT':
                arrow = move_left(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'UP':
                arrow = move_up(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'RIGHT':
                arrow = move_right(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'DOWN':
                arrow = move_down(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'LEFT_UP':
                arrow = move_left_up(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'RIGHT_UP':
                arrow = move_right_up(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'LEFT_DOWN':
                arrow = move_left_down(next_move[0], next_move[1], arrow_state)
            elif next_move_direct == 'RIGHT_DOWN':
                arrow = move_right_down(next_move[0], next_move[1], arrow_state)

            if arrow == next_move:
                arrow = [None, None]
        else:
            arrow = [None, None]

        result = [
                    picked_queen,
                    next_move,
                    arrow
                 ]
        return result


def get_queens(name, state):
    queens =[]
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == name:
                queens.append((i, j))
    return queens


def get_valid_queen(queens, state):
    pass



def move_left(x, y, state):
    next_x = x
    next_y = y

    if y == 0:
        None
    else:
        found = False
        for i in range(y - 1, -1, -1):
            if state[x][i] != '.':
                try:
                    next_y = random.randint(i + 1, y - 1)
                except ValueError:
                    next_y = y
                found = True
                break

        if found is False:
            next_y = random.randint(0, y - 1)
    return [next_x, next_y]


def move_up(x, y, state):
    next_x = x
    next_y = y

    if x == 0:
        None
    else:
        found = False
        for i in range(x - 1, -1, -1):
            if state[i][y] != '.':
                try:
                    next_x = random.randint(i + 1, x - 1)
                except ValueError:
                    next_x = x
                found = True
                break

        if found is False:
            next_x = random.randint(0, x - 1)
    return [next_x, next_y]


def move_right(x, y, state):
    next_x = x
    next_y = y
    if y == 9:
        None
    else:
        found = False
        for i in range(y + 1, 10, 1):
            if state[x][i] != '.':
                try:
                    next_y = random.randint(y + 1, i - 1)
                except ValueError:
                    next_y = y
                found = True
                break

        if found is False:
            next_y = random.randint(y + 1, 9)
    return [next_x, next_y]


def move_down(x, y, state):
    next_x = x
    next_y = y
    if x == 9:
        None
    else:
        found = False
        for i in range(x + 1, 10, 1):
            if state[x][i] != '.':
                try:
                    next_x = random.randint(x + 1, i - 1)
                except ValueError:
                    next_x = y
                found = True
                break

        if found is False:
            next_x = random.randint(x + 1, 9)
    return [next_x, next_y]


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
                        next_x = random.randint(x + 1, i - 1)
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
                    next_x = x + abs(y - next_y)
                    found = True
                    break
                temp_x += 1

        if found is False:
            if smaller == (9 - x):
                next_x = random.randint(x + 1, 9)
                next_y = y + abs(x - next_x)
            else:
                next_y = random.randint(y + 1, 9)
                next_x = x + abs(y - next_y)
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



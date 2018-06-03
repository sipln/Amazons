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

        moves = [
            move_left,
            move_up,
            move_right,
            move_down,
            move_left_up,
            move_right_up,
            move_left_down,
            move_right_down
        ]

        move_check_list = []
        for queen in my_queens:
            move_check =[]
            for move in moves:
                move_check.append(move(queen[0], queen[1], copy_state))
            move_check_list.append(move_check)

        pick_queen = None
        next_move = []
        index = 0
        for queen in my_queens:
            queen_moves = move_check_list[index]
            if queen_moves != [[queen[0], queen[1]]*8 ]:
                pick_queen = queen
                for move in queen_moves:
                    if move != [queen[0], queen[1]]:
                        next_move = move
                        break
            index += 1

        arrows = []
        arrow_state = copy.deepcopy(copy_state)
        arrow_state[pick_queen[0]][pick_queen[1]] = '.'
        arrow_state[next_move[0]][next_move[1]] = self.str

        throw_arrow = []

        for move in moves:
            arrows.append(move(next_move[0], next_move[1], arrow_state))
            for arrow in arrows:
                if arrow != [next_move[0], next_move[1]]:
                    throw_arrow = arrow
                    break

        result = [
            pick_queen,
            next_move,
            throw_arrow
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
            try:
                next_y = random.randint(0, y - 1)
            except ValueError:
                next_y = y
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
            try:
                next_x = random.randint(0, x - 1)
            except ValueError:
                next_x = x
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
            try:
                next_y = random.randint(y + 1, 9)
            except ValueError:
                next_y = y
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
            try:
                next_x = random.randint(x + 1, 9)
            except ValueError:
                next_x = x
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
                try:
                    next_x = random.randint(0, smaller - 1)
                except ValueError:
                    next_x = x
                next_y = y - abs(x - next_x)
            else:
                try:
                    next_y = random.randint(0, smaller - 1)
                except ValueError:
                    next_y = y
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
                try:
                    next_x = random.randint(x + 1, 9)
                except ValueError:
                    next_x = x
                next_y = y - abs(x - next_x)
            else:
                try:
                    next_y = random.randint(0, smaller - 1)
                except ValueError:
                    next_y = y
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
                try:
                    next_x = random.randint(0, smaller - 1)
                except ValueError:
                    next_x = x
                next_y = y + abs(x - next_x)
            else:
                try:
                    next_y = random.randint(y + 1, 9)
                except ValueError:
                    next_y = y
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
                try:
                    next_x = random.randint(x + 1, 9)
                except ValueError:
                    next_x = x
                next_y = y + abs(x - next_x)
            else:
                try:
                    next_y = random.randint(y + 1, 9)
                except ValueError:
                    next_y = y
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



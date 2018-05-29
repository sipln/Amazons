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
        ['___', '___', '___', '_w_', '___', '___', '_w_', '___', '___', '___'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['_w_', '___', '___', '___', '___', '___', '___', '___', '___', '_w_'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['_b_', '___', '___', '___', '___', '___', '___', '___', '___', '_b_'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['___', '___', '___', '___', '___', '___', '___', '___', '___', '___'], \
        ['___', '___', '___', '_b_', '___', '___', '_b_', '___', '___', '___'], \
        ]

    def nextMove(self, state):


        result = [
                    # (random.randint(0,9), random.randint(0,9)),
                    # (random.randint(0,9), random.randint(0,9)),
                    # (random.randint(0,9), random.randint(0,9))
            # [(0, 3), (5, 3), (8, 6)]
                 ]

        return result


    def getQueens(name, state):
        queens =[]
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == name:
                   queens.append((i, j))
        return queens


    queens = getQueens("_w_",Initial_Board)
    print(queens)


"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X, count_O = 0, 0
    for row in board:
        count_X += row.count(X)
        count_O += row.count(O)

    if count_X > count_O:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or j < 0:
        raise IndexError("action({i}, {j}) out of board")
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")

    move = player(board)
    new_board = [row.copy() for row in board]
    new_board[i][j] = move
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    horizontally = set()
    vertically = []
    diagonally = [set(), set()]

    for i in range(len(board)):
        row = board[i]

        # check if horizontally has a winner
        horizontally.update(row)
        if len(horizontally) == 1 and EMPTY not in horizontally:
            return horizontally.pop()
        horizontally.clear()

        # maintain vertically status
        if len(vertically) == 0:
            vertically = [set((piece,)) for piece in row]
        else:
            for j in range(len(row)):
                vertically[j].add(row[j])

        ## maintain diagonally status
        # main diagonal
        check_diagonal_0 = diagonally[0]
        check_diagonal_0.add(row[i])

        # anti-diagonal
        check_diagonal_1 = diagonally[1]
        check_diagonal_1.add(row[len(row)-1-i])

    # Check if vertically has a winner
    for col in vertically:
        if len(col) == 1 and EMPTY not in col:
            return col.pop()

    # Check if diagonally has a winner
    for diagonal in diagonally:
        if len(diagonal) == 1 and EMPTY not in diagonal:
            return diagonal.pop()

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        return False if actions(board) else True
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        return max(actions(board), key=lambda action: min_value(result(board, action)))
    return min(actions(board), key=lambda action: max_value(result(board, action)))


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


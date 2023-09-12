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
    return [[X, X, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numofX = sum(x.count(X) for x in board)
    numofO = sum(x.count(O) for x in board)
    return X if numofX <= numofO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j)
            for i in range(len(board))
                for j in range(len(board[i]))
                    if board[i][j] == EMPTY }

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if (board[i][j] == EMPTY):
        board[i][j] = player(board)
    
    return board
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontally
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O
                    
    # Vertically
    for col in range(3):
        if (row[col] == X for row in board):
            return X
        elif (row[col] == O for row in board):
            return O
    
    # Diagional
    if all(board[i][i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)):
        return O
    
    if all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][2 - i] == O for i in range(3)):
        return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


def test():
    board = initial_state()
    # for i in range(3):
    #     for j in range(3):
    #         print(result(board, (i, j)))
    print(winner(board))
    
test()
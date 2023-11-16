"""
Tic Tac Toe Player
"""

import math
import copy

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
    numofX = sum(x.count(X) for x in board)
    numofO = sum(x.count(O) for x in board)
    return X if numofX <= numofO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleactions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possibleactions.add((i, j))
    return possibleactions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    copyboard = copy.deepcopy(board)
    copyboard[action[0]][action[1]] = player(copyboard)

    return copyboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [[(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]]

    for win in wins:
        numOfX = 0
        numOfO = 0
        for i, j in win:
            if board[i][j] == X:
                numOfX += 1
            if board[i][j] == O:
                numOfO += 1
        if numOfX == 3:
            return X
        if numOfO == 3:
            return O

    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winnerplayer = winner(board)
    
    if winnerplayer == X:
        return 1
    elif winnerplayer == O:
        return -1
    else:
        return 0


def minimax(board, depth=5, alpha=-math.inf, beta=math.inf):
    """
    Returns the optimal action for the current player on the board.
    """ 
    
    if terminal(board):
        return None
    
    
    if player(board) == X:
        v = -math.inf
        
        for action in actions(board):
            minval = minvalue(result(board, action))
            if minval > v:
                v = minval
                bestaction = action

    elif player(board) == O:
        v = math.inf

        for action in actions(board):
            maxval = maxvalue(result(board, action))
            if maxval < v:
                v = maxval
                bestaction = action
        
        return bestaction
    
    
def maxvalue(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
        
    return v
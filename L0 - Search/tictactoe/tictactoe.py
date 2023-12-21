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
    # if # X > # of O: return O
    # else if equal: return X
    x_count = 0
    o_count = 0
    for row in board:
        for piece in row:
            if piece == X:
                x_count+=1
                continue

            if piece == O:
                o_count+=1
                continue

    return O if x_count > o_count else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: moves.add((i,j))
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i,j = action
    if new_board[i][j] != EMPTY:
        raise ValueError('Invalid Action')
    
    new_board[i][j] = player(new_board)

    return new_board

def check_rows(board, piece): 
    for row in board:
        if row == [piece,piece,piece]:
            return True
    return False
def check_cols(board,piece):
    for col in zip(*board):
        if list(col) == [piece,piece,piece]:
            return True
    return False

def check_diags(board, piece):
    if (board[0][0] == piece and board[1][1] == piece and board[2][2] == piece) or (board[0][2] == piece and board[1][1] == piece and board[2][0] == piece): return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(check_diags(board, X) or check_rows(board, X) or check_cols(board,X)): return X
    if(check_diags(board, O) or check_rows(board, O) or check_cols(board,O)): return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or next((False for row in board if EMPTY in row), True): return True
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    if winner(board) == O: return -1
    return 0 

def dfs(board):
    if terminal(board):
        return (None, utility(board))
    turn = player(board)

    max_min_util = -2 if turn == X else 2
    optimal_move = None
    for move in actions(board):
        pair = dfs(result(board,move))
        util = pair[1]
        if turn == X and util > max_min_util:
            max_min_util = util
            optimal_move = move
            if max_min_util == 1: break # AB Pruning :D

        if turn == O and util < max_min_util:
            max_min_util = util
            optimal_move = move
            if max_min_util == -1: break # AB Pruning :D
        
    return (optimal_move, max_min_util)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    return dfs(board)[0]

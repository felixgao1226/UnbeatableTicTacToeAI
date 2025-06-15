"""
Tic Tac Toe Player
"""
from __future__ import annotations

import copy
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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    i, j = action
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
    for i in range(len(board[0])):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    best_action = None
    for action in actions(board):
        max_result, _ = max_value(result(board, action))
        if max_result < v:
            v = max_result
            best_action = action
    return v, best_action


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -float('inf')
    best_action = None
    for action in actions(board):
        min_result, _ = min_value(result(board, action))
        if min_result > v:
            v = min_result
            best_action = action
    return v, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    next_player = player(board)
    if next_player == X:  # maximizing
        _, best_action = max_value(board)
    else:
        _, best_action = min_value(board)
    return best_action

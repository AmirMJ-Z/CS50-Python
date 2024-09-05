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
    x = 0
    y = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1

            elif board[i][j] == O:
                y += 1

    if x != y:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    all = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                all.append((i, j))

    return set(all)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action[0] > 2 or action[0] < 0 or action[1] < 0 or action[1] > 2:
        raise Exception('Cannot make this move')

    playing_player = player(board)

    if board[action[0]][action[1]] != EMPTY:
        raise Exception('Cannot make this move')

    new_board = board.copy()

    new_board[action[0]][action[1]] = playing_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for x in range(3):
        if board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] == X:
            return X

        if board[x][0] == board[x][1] and board[x][1] == board[x][2] and board[x][0] == O:
            return O

        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] == X:
            return X

        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] == O:
            return O

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == X:
        return X

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == O:
        return O

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == X:
        return X

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True

    if winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None

    all_actions = list(actions(board))
    results = []

    for i in range(len(all_actions)):
        results.append(None)
        new_state = result(board, all_actions[i])
        results[i] = utility(new_state)

        if results[i] == 0:
            if minimax(new_state) != None:
                results[i] = utility(result(new_state, minimax(new_state)))


    if player(board) == X:
        max = 0
        index  = 0

        for i in range(len(results)):
            if results[i] > max:
                max = results[i]
                index = i


        return(all_actions[index])


    if player(board) == O:
        min = 100
        index  = 0

        for i in range(len(results)):
            if results[i] < min:
                min = results[i]
                index = i


        return(all_actions[index])





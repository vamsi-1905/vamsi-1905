
import numpy as np
from mesa import Model
from mesa.time import BaseScheduler

ROW_COUNT, COLUMN_COUNT = 6, 7
EMPTY = 0

PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4


class Connect4Model(Model):
    def __init__(self):
        super().__init__()
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
        self.schedule = BaseScheduler(self)
        self.turn = 0  # 0 = human/player, 1 = AI
        self.game_over = False
        self.winner = None
        self.turn_count = 0

    def step(self):
        self.schedule.step()

    def is_terminal_node(self, board):
        return (winning_move(board, PLAYER_PIECE) or
                winning_move(board, AI_PIECE) or
                len(get_valid_locations(board)) == 0)



def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return None


def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]


def winning_move(board, piece):
    # horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    # vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    # positive diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    # negative diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0
    # center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    score += center_array.count(piece) * 3

    # horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # pos diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r + i][c + i]) for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # neg diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [int(board[r + 3 - i][c + i]) for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

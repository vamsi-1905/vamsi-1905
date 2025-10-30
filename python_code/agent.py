
from mesa import Agent
import random
import math
from model import (PLAYER_PIECE, AI_PIECE,
                   get_valid_locations, get_next_open_row, drop_piece,
                   is_valid_location, winning_move, score_position)

class PlayerAgent(Agent):
    """Human move"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.piece = PLAYER_PIECE

    def step(self):
        pass


class AIAgent(Agent):
    """ AI using minimax with alpha-beta pruning."""
    def __init__(self, unique_id, model, depth=4):
        super().__init__(unique_id, model)
        self.piece = AI_PIECE
        self.depth = depth

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(board)
        terminal = (winning_move(board, PLAYER_PIECE) or
                    winning_move(board, AI_PIECE) or
                    len(valid_locations) == 0)
        if depth == 0 or terminal:
            if terminal:
                if winning_move(board, AI_PIECE):
                    return None, 10**10
                elif winning_move(board, PLAYER_PIECE):
                    return None, -10**10
                else:
                    return None, 0
            else:
                return None, score_position(board, AI_PIECE)

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations) if valid_locations else None
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations) if valid_locations else None
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def choose_move(self, board):
        """
       return next best move for AI.
        """
        if random.random() < 0.1:
            valid = get_valid_locations(board)
            return random.choice(valid) if valid else None
        col, _ = self.minimax(board, self.depth, -math.inf, math.inf, True)
        return col

    def step(self):

        if self.model.game_over or self.model.turn != 1:
            return
        col = self.choose_move(self.model.board)
        if col is not None and is_valid_location(self.model.board, col):
            row = get_next_open_row(self.model.board, col)
            drop_piece(self.model.board, row, col, AI_PIECE)
            self.model.turn_count += 1
            if winning_move(self.model.board, AI_PIECE):
                self.model.game_over = True
                self.model.winner = "AI"
            else:
                self.model.turn = 0


import pygame
import sys
import math
from model import (Connect4Model, ROW_COUNT, COLUMN_COUNT,
                   PLAYER_PIECE, AI_PIECE,
                   drop_piece, get_next_open_row,
                   is_valid_location, winning_move, get_valid_locations)
from agent import AIAgent

# Pygame constants
SQUARESIZE = 80
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
LBLUE = (0, 218, 247)

pygame.init()


def draw_board(board, screen):
    # draw board frame and holes
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK,
                               (int(c * SQUARESIZE + SQUARESIZE / 2),
                                int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    # draw red and yellow pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def draw_background(screen):
    screen.fill(BLACK)


def draw_falling_token(screen, x, y, piece):
    pygame.draw.circle(screen, RED if piece == PLAYER_PIECE else YELLOW, (int(x), int(y)), RADIUS)


def draw_board_with_holes_and_tokens(screen, board):
    # draw board & already placed tokens
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK,
                               (int(c * SQUARESIZE + SQUARESIZE / 2),
                                int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)


def animate_piece_drop(screen, model, col, piece):
    """
  piece dropping animated
    """
    row = get_next_open_row(model.board, col)
    if row is None:
        return  # invalid

    x = col * SQUARESIZE + SQUARESIZE // 2
    # Compute target y (top of the slot) — note board coordinates vs screen y
    target_y = height - int(row * SQUARESIZE + SQUARESIZE / 2)
    y = 0  # start at top
    drop_speed = 4  # higher = faster; tweak for smoothness

    while y < target_y:
        draw_background(screen)
        draw_board_with_holes_and_tokens(screen, model.board)
        draw_falling_token(screen, x, y, piece)
        pygame.display.update()
        y += drop_speed
        pygame.time.wait(16)  # ~60 FPS feel

    # Final placement
    drop_piece(model.board, row, col, piece)


def play_game(model: Connect4Model, ai_agent: AIAgent):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect4 — Human vs AI (Mesa + Pygame)")
    screen.fill(BLACK)
    draw_board(model.board, screen)
    font = pygame.font.SysFont("monospace", 48)


    model.turn = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if model.game_over:
                # show result and wait to exit
                if model.winner is not None:
                    label = font.render(f"{model.winner} wins!", 1, LBLUE)
                else:
                    label = font.render("Draw!", 1, LBLUE)
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                screen.blit(label, (40, 10))
                pygame.display.update()
                continue

            if event.type == pygame.MOUSEMOTION and model.turn == 0:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN and model.turn == 0 and not model.game_over:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_valid_location(model.board, col):
                    # animate player's drop
                    animate_piece_drop(screen, model, col, PLAYER_PIECE)
                    model.turn_count += 1
                    # draw after placement
                    draw_board(model.board, screen)

                    if winning_move(model.board, PLAYER_PIECE):
                        model.game_over = True
                        model.winner = "Human"
                    else:
                        # set to AI turn and run AI move
                        model.turn = 1



        # ai turn and game not over, calculate ai move, animate then place it.
        if not model.game_over and model.turn == 1:
            # get column from ai_agent without modifying board
            col = ai_agent.choose_move(model.board)
            if col is not None:
                pygame.time.wait(300)  # small pause before AI starts dropping
                animate_piece_drop(screen, model, col, AI_PIECE)
                model.turn_count += 1
                draw_board(model.board, screen)

                if winning_move(model.board, AI_PIECE):
                    model.game_over = True
                    model.winner = "AI"
                elif len(get_valid_locations(model.board)) == 0:
                    model.game_over = True
                    model.winner = None
                else:
                    model.turn = 0

        pygame.time.wait(10)

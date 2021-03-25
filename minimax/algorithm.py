import random
from typing import List, Tuple
from copy import deepcopy

import pygame

from checkers.board import Board
from checkers.piece import Piece
from checkers.game import Game

RED = (255, 0, 0)
WHITE = (255, 255, 255)

# maxEval = float('-inf')
# best_board = None
# for possible_board in get_all_moves(board, WHITE, game):
#     evaluation = minimax(possible_board, depth-1, False, game)[0]
#     maxEval = max(maxEval, evaluation)
#     if maxEval == evaluation:
#         best_board = possible_board

# return maxEval, best_board

def minimax(board: Board, depth: int, max_player: bool, game) -> Tuple[float, Board]:
    if depth == 0 or board.winner() != None:
        if not isinstance(board, Board):
            print(board)
        return board.evaluate(), board

    if max_player:
        maxEval = float('-inf')
        best_board = []
        for possible_board in get_all_moves(board, WHITE, game):
            evaluation = minimax(possible_board, depth-1, False, game)[0]
            
            if maxEval == evaluation:
                best_board.append(possible_board)
            elif max(maxEval, evaluation) == evaluation:
                maxEval = evaluation
                best_board = []
                best_board.append(possible_board)

        return maxEval, random.choice(best_board)
    else:
        minEval = float('inf')
        best_board = []
        for possible_board in get_all_moves(board, RED, game):
            evaluation = minimax(possible_board, depth-1, True, game)[0]

            if minEval == evaluation:
                best_board.append(possible_board)
            elif min(minEval, evaluation) == evaluation:
                minEval = evaluation
                best_board = []
                best_board.append(possible_board)

        return minEval, random.choice(best_board)


def simulate_move(piece: Piece, move: tuple, board: Board, game: Game, skip: list):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board: Board, color: tuple, game: Game):
    moves: List[Board] = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())

    pygame.display.update()
    # pygame.time.delay(100)
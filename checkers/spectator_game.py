from copy import deepcopy

from .game import Game

class SpectatorGame():

    def __init__(self, game: Game):
        self.game = game

    def set_original_board(self):
        self.original_board = deepcopy(self.game.board)

    def action(self):
        print(
            "\n" + "-"*13 + "SPECTATOR GAME" + "-"*13 + "\n\n\n\n\n\n\n" +
            f"Total moves: {len(self.game.board_history)}"
        )
        return int(input(f"-> Number between 1 - {len(self.game.board_history)}: "))
    
    def view_board(self, index):
        try:
            self.game.board = self.game.board_history[index-1]
        except IndexError:
            print("Select a valid number!")
            self.game.board = self.original_board


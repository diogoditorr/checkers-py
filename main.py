import pygame
 
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from checkers.spectator_game import SpectatorGame
from minimax.algorithm import minimax

options = {
    'spectator_mode': False,
}

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    spectator_game = SpectatorGame(game)

    while run:
        clock.tick(FPS)

        if not options['spectator_mode']:
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 3, WHITE, game)
                print('1 - ' + str(value))
                game.ai_move(new_board)
                pygame.time.delay(800)

            else:
                value, new_board = minimax(game.get_board(), 3, False, game)
                print('2 - ' + str(value))
                game.ai_move(new_board)
                pygame.time.delay(800)
            
            if game.winner() != None:
                print(f'Winner! {game.winner()}')
                run = False

        else:
            if spectator_game.enter_command:
                spectator_game.enter_command = False

                result = spectator_game.action()
                if result:
                    spectator_game.view_board(result)
                print("\nPress 's' again!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if hasattr(event, 'key'):
                if event.key == pygame.K_s and event.type == 768:
                    print('pressing \'s\'')
                    spectator_game.enter_command = True

                    if not options['spectator_mode']:
                        options['spectator_mode'] = True
                        spectator_game.set_original_board()

            if not options['spectator_mode']:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)


        game.update()

    pygame.time.wait(10000)
    pygame.quit()

main()
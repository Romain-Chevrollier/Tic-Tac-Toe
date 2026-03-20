import pygame
# TODO save score 
# TODO random player start
# TODO play against AI ?
# TODO player turn avec la forme en dessous

class Player():
    def __init__(self, shape):
        self.type = 'Human'
        self.shape = shape

    def draw_shape(self, screen, rect):
        if self.shape == "circle":
            pygame.draw.circle(screen, "black", rect.center, 70)
            pygame.draw.circle(screen, "white", rect.center, 60)
        else: 
            pygame.draw.line(screen, 'black', rect.topleft, rect.bottomright, 10)
            pygame.draw.line(screen, 'black', rect.topright, rect.bottomleft, 10)

    def display_player_turn(self, screen):
        display_player_surface = test_font.render(f'Player turn : {self.shape}', False, (0,0,0))
        display_player_rectangle = display_player_surface.get_rect(center=(400,50))
        padding = 10
        bg_rect = display_player_rectangle.inflate(padding * 2, padding * 2)
        pygame.draw.rect(screen, (255,255,255), bg_rect)
        screen.blit(display_player_surface, display_player_rectangle)

class Game():
    def __init__(self):
        self.player_turn = None
        self.game_active = True
        self.game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]

    def draw(self, screen): 
        screen.fill((255,255,255))
        pygame.draw.line(screen, 'black', (315,150), (315,650), 5)
        pygame.draw.line(screen, 'black', (480,150), (480,650), 5)
        pygame.draw.line(screen, 'black', (150,315), (650,315), 5)
        pygame.draw.line(screen, 'black', (150,480), (650,480), 5)

    def is_possible_move(self, coord):
        try :
            if self.game_board[coord[0]][coord[1]] == 0: return True
            else: return False
        except: pass
    
    def game_end(self):
        winning_combos = [
            # Lignes
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # Colonnes
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # Diagonales
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)],
        ]
        for combo in winning_combos:
            symbols = [self.game_board[r][c] for r, c in combo]
            if symbols[0] != 0 and len(set(symbols)) == 1:
                return symbols[0]  # gagnant trouvé
        if all(self.game_board[r][c] != 0 for r in range(3) for c in range(3)):
            return 3
        
    def game_reset(self, screen):
        self.game_active = True
        self.draw(screen)
        self.game_board = [[0]*3 for _ in range(3)]



def run_game():
    global test_font
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Tic-Tac-Toe')
    game_active = False
    test_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

    rect1 = pygame.draw.rect(screen, [255, 0, 0], [160, 160, 145, 145])
    rect2 = pygame.draw.rect(screen, [255, 0, 0], [325, 160, 145, 145])
    rect3 = pygame.draw.rect(screen, [255, 0, 0], [490, 160, 145, 145])
    rect4 = pygame.draw.rect(screen, [255, 0, 0], [160, 325, 145, 145])
    rect5 = pygame.draw.rect(screen, [255, 0, 0], [325, 325, 145, 145])
    rect6 = pygame.draw.rect(screen, [255, 0, 0], [490, 325, 145, 145])
    rect7 = pygame.draw.rect(screen, [255, 0, 0], [160, 490, 145, 145])
    rect8 = pygame.draw.rect(screen, [255, 0, 0], [325, 490, 145, 145])
    rect9 = pygame.draw.rect(screen, [255, 0, 0], [490, 490, 145, 145])
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]

    game=Game()
    player1 = Player('cross')
    player2 = Player('circle')

    game.draw(screen)
    game.player_turn = player1
    # game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game.game_active:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    clicked = next((r for r in rects if r.collidepoint(pos)), None)
                    y = (pos[0] + 50) // 165 - 1
                    x = (pos[1] + 50) // 165 - 1
                    if clicked and game.is_possible_move((x,y)):
                        game.player_turn.draw_shape(screen, clicked)
                        if game.player_turn == player1: 
                            game.game_board[x][y] = 1
                            game.player_turn = player2
                        else : 
                            game.game_board[x][y] = 2
                            game.player_turn = player1

                        if game.game_end():
                            game.game_active=False

            if not game.game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    game.game_reset(screen)

        if not game.game_active:
            if game.game_end() == 1:  winner = "Croix"
            elif game.game_end() == 2: winner = "Cercle"
            else: winner = "None"
            # screen.fill("white")
            display_winner_surface = test_font.render(f'The winner is : {winner}', False, (39, 197, 58))
            display_winner_rectangle = display_winner_surface.get_rect(center=(400,50))
            padding = 10
            bg_rect = display_winner_rectangle.inflate(padding * 2, padding * 2)
            pygame.draw.rect(screen, (255,255,255), bg_rect)
            screen.blit(display_winner_surface, display_winner_rectangle)

            display_restart_surface = test_font.render(f'Press space to restart', False, (210, 2, 0))
            display_restart_rectangle = display_restart_surface.get_rect(center=(400,730))
            screen.blit(display_restart_surface, display_restart_rectangle)


            

        else:
            game.player_turn.display_player_turn(screen)

        pygame.display.update()

def main():
    run_game()

if __name__ == "__main__":
    main()
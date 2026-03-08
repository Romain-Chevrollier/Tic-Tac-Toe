import pygame
# TODO save score 
# TODO random player start
# TODO play against AI ?
# TODO player turn avec la forme en dessous

class Player():
    def __init__(self, shape):
        self.type = 'Human'
        self.shape = shape

        

class Game():
    def __init__(self):
        self.player_turn = None
        self.game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
        
    
    def possible_moves(self):
        pass

    def draw(self, screen): 
        screen.fill((255,255,255))
        pygame.draw.line(screen, 'black', (315,150), (315,650), 5)
        pygame.draw.line(screen, 'black', (480,150), (480,650), 5)
        pygame.draw.line(screen, 'black', (150,315), (650,315), 5)
        pygame.draw.line(screen, 'black', (150,480), (650,480), 5)




def run_game():
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
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect8, rect9]

    game=Game()
    player1 = Player('cross')
    player2 = Player('circle')




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                clicked = next((r for r in rects if r.collidepoint(pos)), None)
                if clicked:
                    print("cliqué !")

        game.draw(screen)
        pygame.draw.line(screen, 'black', (160,160), (305,305), 5)
        pygame.draw.line(screen, 'black', (305,160), (160,305), 5)
        pygame.draw.rect(screen, [255, 0, 0], [490, 490, 145, 145])
        pygame.display.update()

def main():
    run_game()

if __name__ == "__main__":
    main()
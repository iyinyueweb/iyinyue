__author__ = 'Administrator'
import pygame


class BoxesGame():
    def __init__(self):
        pygame.init()
        width, height = 1000, 550
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Boxes')
        self.clock = pygame.time.Clock()

    def update(self):
        self.clock.tick(60)

        self.screen.fill(0)
        self.draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.flip()

    def draw_board(self):
        pygame.draw.lines(self.screen, [1, 255, 1], False, [[5, 5], [70, 80]], 1)

bg = BoxesGame()
while 1:
    bg.update()

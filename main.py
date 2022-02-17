import pygame
import sys
from setup import *
from level import Level
from console import Console


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pygame.display.set_caption('RPG in need of a title')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Console test
        Console().write(str("Hello world"))
        for i in range(20):
            Console().write(str(i))
        Console().write(str("Test"))

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            Console().draw()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

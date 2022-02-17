import pygame
import sys
from setup import *
from level import Level
from console import Console


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pygame.display.set_caption("Maxime's Big Adventure")
        self.clock = pygame.time.Clock()

        Console().write("pygame-rpg by Thomas Bruninx")
        Console().write("(%s)" % sys.version)

        self.level = Level()

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        Console().toggle_visibility()

            self.screen.fill(pygame.color.Color(10, 98,150))
            self.level.run()
            Console().draw()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

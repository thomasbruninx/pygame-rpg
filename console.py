import pygame
from util import Singleton

CONSOLE_MAXLINES = 12
CONSOLE_FONTSIZE = 18
CONSOLE_FONTFILE = "assets/fonts/VT323-Regular.ttf"


class Console(metaclass=Singleton):

    def __init__(self):
        pygame.init()

        self.visible = False
        self.buffer = []
        self.bgcolor = pygame.color.Color(0, 0, 0, 200)
        self.font = pygame.font.Font(CONSOLE_FONTFILE, CONSOLE_FONTSIZE)
        self.size = (pygame.display.get_surface().get_size()[0], CONSOLE_MAXLINES * CONSOLE_FONTSIZE)
        self.surface = pygame.surface.Surface(self.size)
        self.surface = self.surface.convert_alpha()

    def write(self, text, color='White'):
        self.buffer.append((text, color))

    def toggle_visibility(self):
        self.visible = not self.visible

    def draw(self):
        if self.visible:
            display_surface = pygame.display.get_surface()

            pygame.draw.rect(self.surface, self.bgcolor, self.surface.get_rect())
            for index, line in enumerate(self.buffer[-12:]):
                line_surf = self.font.render(str(line[0]), True, line[1])
                line_rect = line_surf.get_rect(topleft=(2, CONSOLE_FONTSIZE * index))
                self.surface.blit(line_surf, line_rect)

            display_surface.blit(self.surface, self.surface.get_rect())

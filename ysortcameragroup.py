import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

    def draw(self, surface, player):
        half_width = surface.get_size()[0] // 2
        half_height = surface.get_size()[1] // 2

        self.offset.x = player.rect.centerx - half_width
        self.offset.y = player.rect.centery - half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_rect)

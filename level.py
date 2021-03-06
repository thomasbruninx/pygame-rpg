import pygame
from setup import *
from tile import Tile
from player import Player
from ysortcameragroup import YSortCameraGroup

class Level:
    def __init__(self):

        # Get display surface
        self.display_surface = pygame.display.get_surface()

        # Setup sprite group
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacle_sprites])

                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface, self.player)
        self.visible_sprites.update()

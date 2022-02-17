import pygame


class Tileset:

    def __init__(self, file, size=(64, 64), margin=1, space=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.space = space
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.space
        dy = self.size[1] + self.space

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

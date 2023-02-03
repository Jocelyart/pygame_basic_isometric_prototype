# IMPORT MODULE
import pygame

# PLAYER CLASS
class Tile:

    def __init__(self, x, y, tile_id, name):

        self.tile_id = tile_id

        # TILE 1 - WALLS
        if self.tile_id == 1: 

            self.name = name
            self.image = pygame.image.load("sprites/levels/level1/0.png").convert_alpha()
            self.hitbox = self.image.get_rect(midbottom = (x, y))
        
        # TILE 3 - FLOOR
        if self.tile_id == 3: 

            self.image = pygame.image.load("sprites/levels/level1/3.png").convert_alpha()
            self.hitbox = self.image.get_rect(midbottom = (x, y))

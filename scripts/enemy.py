# IMPORT MODULE
import pygame

# ENEMY1 CLASS
class Enemy1:

    def __init__(self, x, y, name, level):

        self.level = level

        self.name = name

        self.image = pygame.image.load("assets/enemies/enemy1/0.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (x, y))


    def update(self):
        pass

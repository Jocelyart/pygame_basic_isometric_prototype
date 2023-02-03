# IMPORT MODULE
import pygame

# PLAYER CLASS
class Player:

    def __init__(self, x, y, name, level):

        self.level = level

        self.display = pygame.display.get_surface()

        self.x = x
        self.y = y

        self.w = 32
        self.h = 32

        self.name = name

        self.image = pygame.image.load("sprites/player/0.png").convert_alpha()

        self.rect = self.image.get_rect(midbottom = (x, y))

        self.hitbox = self.rect.inflate(0, 0)
        self.rect = self.hitbox

        self.direction = pygame.math.Vector2()

        self.pos = pygame.math.Vector2()
        self.pos = self.hitbox

        # SPEED
        self.speed = 100
        


    def handle_control(self):
        
        # KEYBOARD INPUTS
        # PRESSED
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.direction.x = -1
                

        elif key[pygame.K_RIGHT]:
            self.direction.x = 1

        else:
            self.direction.x = 0
            
        
        if key[pygame.K_UP]:
            self.direction.y = -1
               
          
        
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
            

        else:
            self.direction.y = 0
        
        # NORMALIZE VECTOR (DIAGONAL SPEED)
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

   
    def move_and_collide(self, dt):

        # player movement on X axis
        self.pos.x += round(self.direction.x * self.speed * dt)
        self.hitbox.x = self.pos.x

        for wall in self.level.wall_list:

            # display wall hitbox =======================================
            # pygame.draw.rect(self.display, "red", wall.hitbox, 1)

            if self.hitbox.colliderect(wall.hitbox):

                if self.direction.x < 0:
                    self.hitbox.left = wall.hitbox.right

                if self.direction.x > 0:
                    self.hitbox.right = wall.hitbox.left

        # player movement on Y axis
        self.pos.y += round(self.direction.y * self.speed * dt)
        self.hitbox.y = self.pos.y

        for wall in self.level.wall_list:
            
            if self.hitbox.colliderect(wall.hitbox):

                if self.direction.y < 0:
                    self.hitbox.top = wall.hitbox.bottom

                if self.direction.y > 0:
                    self.hitbox.bottom = wall.hitbox.top

        # display player hitbox ===========================================
        # pygame.draw.rect(self.display, "green", self.hitbox, 1)

    def update(self, dt):

        # updates
        self.handle_control()
        self.move_and_collide(dt)
        

    
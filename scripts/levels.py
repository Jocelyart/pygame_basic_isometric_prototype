# IMPORT MODULE
import pygame
import json

# IMPORT DATA FROM FILES
from tile import Tile
from player import Player
from enemy import Enemy1


# LEVELS CLASS
class Level1:

    def __init__(self, camera):
        
        self.camera = camera

        self.tile_width = 32
        self.tile_height = 32

        # font
        self.font = pygame.font.SysFont("Arial.ttf", 20)
        
        self.cartesian_text = self.font.render("Top-Down", 1, "green")
        self.cartesian_text_rect = self.cartesian_text.get_rect(topleft = (210, 300))

        self.isometric_text = self.font.render("Isometric", 1, "green")
        self.isometric_text_rect = self.isometric_text.get_rect(topleft = (500, 300))

        self.sprite_image_list()
        self.sprite_rect_list()

        self.handle_layer0_data()

        self.handle_layer1_data()



    def cartesian_to_isometric(self, cartX, cartY, half_width, half_height, offset_x = 0, offset_y = 0):
        
        """ ISOMETRIC FORMULA """
        # isoX = (cartX - cartY)
        # isoY = (cartX + cartY) / 2

        isoX = (cartX - cartY) / (self.tile_width / half_width) + offset_x
        isoY = ((cartX + cartY) / 2) / (self.tile_height / half_height) + offset_y

        return pygame.math.Vector2(isoX, isoY)

    
    def isometric_to_cartesian(self, isoX, isoY, offset_x = 0, offset_y = 0):

        """ BACK TO CARTESIAN FORMULA """
        # cartX = (2 * isoY + isoX) / 2
        # cartY = (2 * isoY - isoX) / 2

        cartX = ((2 * isoY + isoX) / 2) + offset_x
        cartY = ((2 * isoY - isoX) / 2) + offset_y

        return pygame.math.Vector2(cartX, cartY)

    
    def sprite_image_list(self):
        self.layer0_draw_all_sprite_list = []
        self.layer1_draw_all_sprite_list = []


    def sprite_rect_list(self):

        self.player_list = []
        self.wall_list = []
      

    def handle_layer0_data(self):

        with open("sprites/levels/json/layer0.json", "r") as data:
            
            self.layer0_data_list = json.load(data)
        
        # LAYER 0
        for row_index, row in enumerate(self.layer0_data_list):
            for col_index, tile in enumerate(row):

                x = col_index * self.tile_width 
                y = row_index * self.tile_height

                if tile == 3: # FLOOR
                    self.item3 = Tile(x + 128, y + 64, 3, "item3")
                    self.layer0_draw_all_sprite_list.append(self.item3)


    def handle_layer1_data(self):

        with open("sprites/levels/json/layer1.json", "r") as data:
            
            self.layer1_data_list = json.load(data)
        
        # LAYER 1
        for row_index, row in enumerate(self.layer1_data_list):
            for col_index, tile in enumerate(row):
                
                x = col_index * self.tile_width 
                y = row_index * self.tile_height


                if tile == 0: # PLAYER  

                    self.player = Player(x + 128, y + 64, "player", self)
                    self.layer1_draw_all_sprite_list.append(self.player)
                 
                if tile == 1: # WALLS
                    
                    self.wall = Tile(x + 128, y + 64, 1, "wall")
                    self.layer1_draw_all_sprite_list.append(self.wall)
                    self.wall_list.append(self.wall)


                if tile == 2: # ENEMY
                    self.enemy1 = Enemy1(x, y, "enemy1", self) 
                   

                

    def update(self, dt):
        # update in cartesian
        self.player.update(dt)


    def draw(self):

        # LAYER 0 =================================================================
        # draw in cartesian
        for sprite in self.layer0_draw_all_sprite_list:

            sprite.image.set_alpha(50)
            self.camera.blit(sprite.image, (sprite.hitbox.x, sprite.hitbox.y))

        # draw in isometric
        for sprite in self.layer0_draw_all_sprite_list:
            
            # APPLY THE CONVERSION HERE CARTESIAN TO ISOMETRIC
            iso = self.cartesian_to_isometric(sprite.hitbox.x, sprite.hitbox.y, self.tile_width/2, self.tile_height/2)

            self.camera.blit(sprite.image, (iso.x + 450, iso.y + 50))

        # LAYER 1 =================================================================
        # draw in cartesian
        for sprite in self.layer1_draw_all_sprite_list:

            self.camera.blit(sprite.image, (sprite.hitbox.x, sprite.hitbox.y))

        # draw in isometric
        for sprite in self.layer1_draw_all_sprite_list:
            
            # APPLY THE CONVERSION HERE CARTESIAN TO ISOMETRIC
            iso = self.cartesian_to_isometric(sprite.hitbox.x, sprite.hitbox.y, self.tile_width/2, self.tile_height/2)

            self.camera.blit(sprite.image, (iso.x + 450, iso.y + 50))
        

        # DRAW TEXT
        # cartesian
        self.camera.blit(self.cartesian_text, self.cartesian_text_rect)

        # isometric
        self.camera.blit(self.isometric_text, self.isometric_text_rect)
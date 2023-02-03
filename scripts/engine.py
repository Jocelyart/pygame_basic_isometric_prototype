# IMPORT MODULE
import pygame
import sys

# IMPORT DATA FROM FILES
from settings import *
from levels import Level1

# INITIALIZE PYGAME
pygame.init()

# ENGINE CLASS
class Engine:

    def __init__(self):

        # MAIN SCREEN 
        self.main_screen = pygame.display.set_mode((screen_width, screen_height), flags)

        # ENGINE CLOCK
        self.clock = pygame.time.Clock()

        # VARIABLES
        self.start = True
        self.level1 = Level1(self.main_screen)
        
    
    def start_program(self):

        """ START THE ENGINE """
        while self.start:

            # FRAMERATE
            dt = self.clock.tick(fps) / 1000

            # DISPLAY THE GAME'S NAME AND FPS
            pygame.display.set_caption(f"Engine | {round(self.clock.get_fps())}")
            
            # GO THROUGH EVENTS
            for event in pygame.event.get():
                self.handle_event(event)
            
            # FILL SCREEN
            self.main_screen.fill((0, 0, 0))
            
            # UPDATE
            self.update(dt)

            # DRAW
            self.draw()

            # UPDATE DISPLAY
            pygame.display.update()
    
    def handle_event(self, event):

        """ HANDLE EVENT """
        if event.type == pygame.QUIT:
            self.start = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.start = False
                pygame.quit()
                sys.exit()

    
    def update(self, dt):
        self.level1.update(dt)

    def draw(self):
        self.level1.draw()
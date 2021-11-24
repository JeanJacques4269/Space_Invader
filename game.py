import pygame.sprite

from spaceship import Spaceship
from ennemy import Ennemy, create_ennemy
from constants import *


class Game:
    def __init__(self, win):  # Here I put parameters related to when you generate the game, for example the map
        # default
        self.win = win  # that is a pygame thing that you need to use as a parametre when you blit stuff on the screen
        self.game_is_on = True

        # instanciating objects
        self.spaceship = Spaceship()
        self.all_ennemies = pygame.sprite.Group()  # list of all ennemies

    def run(self):
        # default
        clock = pygame.time.Clock()  # creating the clock that will help us force Frame rate
        time_elapsed_since_last_action = 0
        while self.game_is_on:
            dt = clock.tick(FPS)  # Slows down the loop so it refreshes 60 times per second
            time_elapsed_since_last_action += dt
            self.win.fill(BLACK)  # fill background

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if you push the red cross, it close the game
                    self.game_is_on = False
            # end of default code

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.spaceship.move("left")
            if keys[pygame.K_RIGHT]:
                self.spaceship.move("right")

            if time_elapsed_since_last_action > 1000:  # in milliseconds
                self.all_ennemies.add(create_ennemy())
                time_elapsed_since_last_action = 0

            self.update_everything()
            self.draw_everything()
            self.check()

    def update_everything(self):
        self.spaceship.update_pos()
        for ennemy in self.all_ennemies:
            ennemy.update_pos()

    def draw_everything(self):
        self.win.blit(self.spaceship.surface, self.spaceship.rect)
        for sprite in self.all_ennemies:
            self.win.blit(sprite.surface, sprite.rect)
        pygame.display.flip()  # I usually forget this line which makes me get angry for no reason
        # beacause without it you only see a black screen

    def check(self):
        """ we check for loses"""


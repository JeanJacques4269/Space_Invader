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
        time_elapsed_since_last_ennemy_spawn = 0
        time_elapsed_since_last_bullet_fired = 0
        while self.game_is_on:
            dt = clock.tick(FPS)  # Slows down the loop so it refreshes 60 times per second
            time_elapsed_since_last_ennemy_spawn += dt
            time_elapsed_since_last_bullet_fired += dt
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
            if keys[pygame.K_SPACE] and time_elapsed_since_last_bullet_fired > 1000:
                time_elapsed_since_last_bullet_fired = 0
                self.spaceship.move("fire")

            if time_elapsed_since_last_ennemy_spawn > 1000:  # in milliseconds
                self.all_ennemies.add(create_ennemy())
                time_elapsed_since_last_ennemy_spawn = 0

            self.update_everything()
            self.draw_everything()
            self.check_bullet_collision()
            self.check_lose()

    def update_everything(self):
        all = pygame.sprite.Group(*self.all_ennemies, self.spaceship, *self.spaceship.fired_missiles)
        for sprite in all:
            sprite.update_pos()

    def draw_everything(self):
        all = pygame.sprite.Group(*self.all_ennemies, self.spaceship, *self.spaceship.fired_missiles)
        for sprite in all:
            self.win.blit(sprite.surface, sprite.rect)
        pygame.display.flip()  # I usually forget this line which makes me get angry for no reason
        # beacause without it you only see a black screen

    def check_bullet_collision(self):
        for bullet in self.spaceship.fired_missiles:
            hits = pygame.sprite.spritecollide(bullet, self.all_ennemies, True)
            if hits:
                bullet.kill()

    def check_lose(self):
        """ we check for ennemies being arrived at the bottom"""
        for ennemy in self.all_ennemies:
            if ennemy.pos.y > HEIGHT - img_spaceship.get_size()[0]:
                self.lose()
            return False

    def lose(self):
        self.game_is_on = False

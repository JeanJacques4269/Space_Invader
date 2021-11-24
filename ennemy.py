import random

from constants import *


class Ennemy(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.surface = img_ennemy  # instantiate image to display
        self.rect = self.surface.get_rect()  # instantiate position

        self.speed = 1
        self.pos = vec(x, 0)  # spawns on top somewhere on the x axis
        self.vel = (0, self.speed)

    def update_pos(self):
        self.pos += self.vel
        self.rect.midbottom = self.pos


def create_ennemy(x=0):
    if x == 0:
        return Ennemy(random.randint(0, WIDTH))
    else:
        return Ennemy(x)
